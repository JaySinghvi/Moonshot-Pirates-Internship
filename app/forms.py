from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from .models import disaster


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class DisasterForm(forms.ModelForm):
    class Meta:
        model = disaster
        fields = ('disaster_name', 'location', 'status', 'details', 'resources_needed', 'tasks', 'updates', 'slug')