from django.views import generic as views
from django.urls import reverse_lazy

from Mobile_Occasion.autos.forms.truck_forms import CreatTruckProfileForm
from Mobile_Occasion.autos.models import Truck


class CreateTruckView(views.CreateView):
    model = Truck
    template_name = 'autos/create_truck_profile.html'
    form_class = CreatTruckProfileForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )