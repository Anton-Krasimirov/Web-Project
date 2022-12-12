from django.contrib.auth import mixins as auth_mixin
from django.views import generic as views
from django.urls import reverse_lazy


from Mobile_Occasion.autos.forms.car_forms import EditCarForm, CreatCarProfileForm
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


class CarDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    form_class = CreatCarProfileForm
    model = Car
    template_name = 'autos/car_profile_details.html'
    context_object_name = 'car'

    # def get_queryset(self):
    #     return Car.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class EditCarView(views.UpdateView):
    model = Car
    template_name = 'autos/edit_car_profile.html'
    form_class = EditCarForm

    def get_success_url(self):
        return reverse_lazy('car details', kwargs={'pk': self.object.id}, )


class AllCarsView(views.ListView):
    model = Car
    template_name = 'autos/all_cars_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_cars = context['object_list']
        context.update({'user_cars': user_cars, })
        return context


class DeleteCarView(views.DeleteView):
    model = Car
    template_name = 'autos/delete_car.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.id}, )