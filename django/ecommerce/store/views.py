from rest_framework.viewsets import ModelViewSet
from .models import Product, Order, Wishlist
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from .models import Review
from .serializers import ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Cart, CartItem, Order, OrderItem
from django.shortcuts import render
from .models import Product



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # 🔍 Search + Filter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name']

    # 🔒 Permissions
    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"})
    
    return Response(serializer.errors)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    return Response({
        "username": user.username,
        "email": user.email
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    user = request.user
    product_id = request.data.get('product_id')

    cart, created = Cart.objects.get_or_create(user=user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product_id=product_id
    )

    if not created:
        item.quantity += 1
        item.save()

    return Response({"message": "Added to cart"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request):
    user = request.user
    product_id = request.data.get('product_id')

    cart = Cart.objects.get(user=user)
    item = CartItem.objects.get(cart=cart, product_id=product_id)

    item.delete()

    return Response({"message": "Removed from cart"})



class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    user = request.user

    cart = Cart.objects.get(user=user)
    items = CartItem.objects.filter(cart=cart)

    total_price = 0

    order = Order.objects.create(user=user, total_price=0)

    for item in items:
        total_price += item.product.price * item.quantity

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    order.total_price = total_price
    order.save()

    items.delete()  # clear cart

    return Response({"message": "Order placed successfully"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_wishlist(request):
    Wishlist.objects.create(
        user=request.user,
        product_id=request.data.get('product_id')
    )
    return Response({"message": "Added to wishlist"})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def cart(request):
    return render(request, 'store/cart.html')