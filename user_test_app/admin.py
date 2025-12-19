from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import TestUserCreationForm, TestUserChangeForm
from .models import TestUser



class TestUserAdmin(UserAdmin):
    add_form = TestUserCreationForm
    form = TestUserChangeForm

    list_display = [
        'username',
        'email',
        'age'
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)



# Register your models here.
admin.site.register(TestUser)
