from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'completed', 'created']
    list_filter = ['completed']
    search_fields = ['title']
    exclude = ['user']

    # ✅ Auto assign logged-in user
    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    # ✅ ADD THIS HERE 👇
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def has_change_permission(self, request, obj=None): 
        if obj is not None and obj.user != request.user:
            return False
        return super().has_change_permission(request, obj)
    
    