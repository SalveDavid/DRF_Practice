from django.urls import path
from CustomerApp import views

urlpatterns = [
    path('customer/', views.CustomerListView.as_view()),
    path('customer/<int:pk>', views.CustomerDetailView.as_view()),
    path('order/', views.OrderListView.as_view()),
    path('order/<int:pk>', views.OrderDetailView.as_view()),
]
