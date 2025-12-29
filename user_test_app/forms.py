from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import TestUser, UserActivity



class TestUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Override the help text for the 'username' field
        self.fields['username'].help_text = None

        # Override the help text for the 'password' fields
        # Note: UserCreationForm renders 'password' and 'password2'
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta(UserCreationForm):
        model = TestUser
        fields = UserCreationForm.Meta.fields# + ('password',)


class TestUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = TestUser
        fields = UserChangeForm.Meta.fields


class UserActivityForm(forms.ModelForm):
    class Meta:
        model = UserActivity
        fields = ['content']