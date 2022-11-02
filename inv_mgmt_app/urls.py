from django.urls import path
from . import views

app_name = 'inv_mgmt_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_box/', views.generate_box, name='generate_box'),
    path('create_shipment/', views.create_shipment, name='create_shipment'),
    path('show_shipment_detail/<int:shipment_id>', views.show_shipment_detail, name='show_shipment_detail'),
    path('receive_shipment/<int:shipment_id>', views.receive_shipment, name='receive_shipment'),    
]

