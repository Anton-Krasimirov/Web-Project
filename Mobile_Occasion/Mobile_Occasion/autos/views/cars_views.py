
from django.views import generic as views
from django.urls import reverse_lazy

from Mobile_Occasion.autos.forms import CreatCarProfileForm
from Mobile_Occasion.autos.models import Car


class CreateCarView(views.CreateView):
    model = Car
    template_name = 'autos/create_car_profile.html'
    form_class = CreatCarProfileForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )