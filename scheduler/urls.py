from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scheduler/', views.agendar, name='agendar'),
    path('get_queue/', views.get_queue, name='get_queue'),
    path('complete_service/', views.complete_service, name='complete_service'),
]
