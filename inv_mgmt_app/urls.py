from django.urls import path
from . import views

app_name = 'inv_mgmt_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_bundles/', views.generate_bundles, name='generate_bundles'),
    
]

