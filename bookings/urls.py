from django.urls import path
from . import views

urlpatterns = [
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('agent-bookings/', views.agent_bookings, name='agent_bookings'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking/<int:booking_id>/update/', views.update_booking_status, name='update_booking_status'),
    path('agent-inquiries/', views.agent_inquiries, name='agent_inquiries'),
    path('inquiry/<int:inquiry_id>/read/', views.mark_inquiry_as_read, name='mark_inquiry_as_read'),
]
