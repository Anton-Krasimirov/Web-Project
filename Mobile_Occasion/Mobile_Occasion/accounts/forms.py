from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Mobile_Occasion.accounts.helpers import BootstrapFormMixin


class RegistrationProfileForm(UserCreationForm, BootstrapFormMixin):
    email = forms.EmailField(max_length=254, )

    region = forms.CharField(max_length=30, )

    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), )

    phone = forms.CharField(max_length=10, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #
    #     profile = UserProfile(
    #         email=self.cleaned_data['email'],
    #         phone=self.cleaned_data['phone'],
    #         region=self.cleaned_data['region'],
    #         user=user,
    #     )
    #
    #     if commit:
    #         profile.save()
    #     return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone', 'region', 'address')
        # fields = '__all__'


class EditUserProfileForm(UserCreationForm, BootstrapFormMixin):
    pass


class DeleteUserForm(forms.ModelForm):
    pass
