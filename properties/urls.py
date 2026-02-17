from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),
    path('properties/<int:property_id>/book/', views.book_property, name='book_property'),
    path('properties/<int:property_id>/inquiry/', views.send_inquiry, name='send_inquiry'),
    path('agent/<int:agent_id>/properties/', views.agent_properties, name='agent_properties'),
]
