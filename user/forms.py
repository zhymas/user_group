from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'group', 'date_created']
        exclude = ['date_created']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['username', 'group', 'date_update']
        exclude = ['date_update']
