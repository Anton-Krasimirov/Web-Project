from django.urls import path

from Mobile_Occasion.autos.views.cars_views import CreateCarView
from Mobile_Occasion.autos.views.trucks_views import CreateTruckView

urlpatterns = (
    path('create/car/', CreateCarView.as_view(), name='create car'),
    # path('edit/car/<int:pk>/', EditCarView.as_view(), name='edit car'),
    # path('car/details/<int:pk>/', CarDetailsView.as_view(), name='car details'),
    # path('car/all_cars/', AllCarsView.as_view(), name='all cars'),
    # path('car/delete/<int:pk>/', DeleteCarView.as_view(), name='delete car'),

    path('create/truck/', CreateTruckView.as_view(), name='create truck')
)