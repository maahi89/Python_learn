from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, add_to_wishlist
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register, profile
from .views import add_to_cart, remove_from_cart, view_cart
from .views import checkout
from django.urls import path
from . import views


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('profile/', profile),
    path('cart/add/', add_to_cart),
    path('cart/remove/', remove_from_cart),
    path('cart/', view_cart),
    path('checkout/', checkout),
    path('wishlist/add/', add_to_wishlist),
    path('', views.product_list),
    path('cart/', views.cart),
]

