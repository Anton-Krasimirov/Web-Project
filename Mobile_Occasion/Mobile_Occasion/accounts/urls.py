from django.urls import path

from Mobile_Occasion.accounts.views import UserRegisterView, DashboardView, UserLoginView, UserLogoutView, HomePageView, \
    UserDetailView, EditProfileView, DeleteUserProfileView

urlpatterns = (
    path('', HomePageView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('register/user/', UserRegisterView.as_view(), name="register user"),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='profile details'),
    path('edit/user/<int:pk>/', EditProfileView.as_view(), name='edit user'),
    path('delete/user/<int:pk>/', DeleteUserProfileView.as_view(), name='delete user'),
)