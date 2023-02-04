from django.urls import path
from .views import (add_vehical , edit_vehical , info_vehical , add_service , customer_services , approve_service, 
 service_updates , employee_service_updates , employee_service_list , update_progress , dashboard , genrate_estimate,
 estimates
 )
urlpatterns = [
    # Vehical Paths
    path('vehical/add/', add_vehical ,name='add_vehical_page'),
    path('vehical/edit/<str:pk>', edit_vehical ,name='edit_vehical_page'),
    path('vehical/', info_vehical ,name='info_vehical_page'),
    #Service Paths
    path('service/add/', add_service ,name='add_service_page'),
    path('services', customer_services ,name='customer_service_page'),
    path('services/view/update/<str:pk>', service_updates , name ='customer_service_updates_page'),
    path('services/approve/<str:pk>', approve_service),
    path('services/update/<str:pk>', employee_service_updates , name ='employee_service_update_page'),
    path('services/list', employee_service_list ,name='employee_service_list'),
    path('services/update/progress/<str:pk>', update_progress , name ='progress_update_page'),
    path('dashboard/', dashboard , name ='dashboard'),
    # Estimate Paths
    path('estimate/gen/<str:pk>', genrate_estimate , name ='genrate_estimate'),
    path('estimates/', estimates , name ='estimates'),
    ]
