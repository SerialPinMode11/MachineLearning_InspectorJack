from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'address')  # Columns displayed in the admin list view
    search_fields = ('username', 'address')  # Add search functionality
