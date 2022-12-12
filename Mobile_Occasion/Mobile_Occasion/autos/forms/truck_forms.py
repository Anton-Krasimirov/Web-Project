from Mobile_Occasion.accounts.helpers import BootstrapFormMixin
from django import forms

from Mobile_Occasion.autos.models import Truck


class CreatTruckProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        car = super().save(commit=False)

        car.user = self.user
        if commit:
            car.save()
        return car

    class Meta:
        model = Truck
        fields = (
        'brand', 'model', 'category', 'kilometers', 'first_reg_date', 'transmission', 'fuel', 'color', 'price',
        'photo1', 'photo2', 'photo3', 'photo4')
        widgets = {
            'first_reg_date': forms.TextInput(
                attrs={'placeholder': 'Fill in this format - 31/12/0000', }
            ),
            'km': forms.TextInput(attrs={'placeholder': 'Fill in format - 100 000', }),
            'price': forms.TextInput(attrs={'placeholder': 'fill in format - 10 000', }),
        }
