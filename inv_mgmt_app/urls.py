from django.urls import path
from . import views

app_name = 'inv_mgmt_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_box/', views.generate_box, name='generate_box'),
    path('create_shipment/', views.create_shipment, name='create_shipment'),
]

