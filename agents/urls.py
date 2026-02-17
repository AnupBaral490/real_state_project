from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.agents_list, name='agents_list'),
    path('<int:agent_id>/', views.agent_detail, name='agent_detail'),
]
