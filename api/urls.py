from django.urls import path
from . import views

urlpatterns  = [
    path('api/', views.get_api_url_patterns),
    path('res/', views.Reservation,name="reservation"),
    path('reservation/<str:pk>/', views.GetOneReservation, name="getoneresevation"),
    path('reservation-create/', views.ReservationCreate, name="rescreate"),
    path('reservation-delete/<str:pk>/', views.ResDelete, name="resdelete"),
    path('reservation-edit/<str:pk>/', views.ResUpdate, name="resupdate"),
    
    path('get-rooms/', views.GetRooms,name="room"),

    path('get-customer/', views.GetCustomer,name="customer"),
    path('customer-create/', views.CustomerCreate, name="custcreate"),
    path('customer-delete/<str:pk>/', views.CustDelete, name="custdelete"),

]