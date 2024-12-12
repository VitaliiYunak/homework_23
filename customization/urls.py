from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.upper_text, name='upper_text'),
    path('register/', views.register, name='register'),
]