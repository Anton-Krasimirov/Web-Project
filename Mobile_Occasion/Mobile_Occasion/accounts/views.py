from django.contrib.auth import views as auth_view, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic.base import ContextMixin
from django.contrib.auth import mixins as auth_mixin

from Mobile_Occasion.accounts.forms import RegistrationProfileForm
from Mobile_Occasion.autos.models import Car, Truck


class HomePageView(views.TemplateView):
    template_name = 'index.html'


class DashboardView(views.ListView):
    model = get_user_model()
    template_name = 'dashboard.html'


class UserRegisterView(views.CreateView):
    form_class = RegistrationProfileForm
    template_name = 'accounts/create_profile.html'

    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_view.LoginView, ContextMixin):
    template_name = 'accounts/login_user_page.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['checks'] = 'true'

        return context

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_view.LogoutView):
    pass

class UserDetailView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = get_user_model()
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars = list(Car.objects.filter(user_id=self.object.id))
        trucks = list(Truck.objects.filter(user_id=self.object.id))
        context.update({'cars': cars, 'trucks': trucks,})

        return context

#
# class EditProfileView(views.UpdateView):
#     model = UserProfile
#     template_name = 'accounts/edit_profile.html'
#     fields = ('first_name', 'last_name', 'email', 'phone', 'region')
#
#     def get_success_url(self):
#         return reverse_lazy('profile details', kwargs={'pk': self.object.pk})
#
#
# class DeleteUserProfileView(views.DeleteView):
#     model = get_user_model()
#     template_name = 'accounts/delete_user.html'
#     success_url = reverse_lazy('index')
