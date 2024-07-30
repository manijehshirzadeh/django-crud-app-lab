from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'), # Routes will be added here
    path('about/', views.about, name='about'),
]