from django.urls import path
from firstApp import views

urlpatterns = [
    path('emp/', views.employeeView),
]