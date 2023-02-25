from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import UserChangeForm, UserCreationForm

from .models import Customer, Seller

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email','username','phone_number','first_name','last_name','is_customer','is_seller','is_active','is_staff', 'is_superuser', 'date_joined')
    list_filter = ('email','username','phone_number','first_name','last_name','is_customer','is_seller','is_active','is_staff')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email','username','first_name','last_name', 'phone_number', 'password')}),
        ('permissions', {'fields': ('is_staff', 'is_superuser', 'is_active','is_customer','is_seller' )}),
    )
# admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)
admin.site.register(Customer)
admin.site.register(Seller)
