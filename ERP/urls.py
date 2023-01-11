from django.urls import path
from .views import add_vehical , edit_vehical , info_vehical , add_service , customer_services , approve_service
urlpatterns = [
    path('vehical/add/', add_vehical ,name='add_vehical_page'),
    path('vehical/edit/', edit_vehical ,name='edit_vehical_page'),
    path('vehical/', info_vehical ,name='info_vehical_page'),
    path('service/add', add_service ,name='add_service_page'),
    path('services', customer_services ,name='customer_service_page'),
    path('services/approve/<str:pk>', approve_service),
    
    ]
