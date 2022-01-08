"""flightServices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from flightApp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # esta vista elusuario pasará su user y pass,y recibirá su token

router = DefaultRouter()   # Router is for viewsets
router.register('flights', views.FlightViewSet)
router.register('passengers', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('flightServices/', include(router.urls)),
    # path('flightServices/findFlights/', views.find_flights),  # for custom functions use the path, no routers
    # path('flightServices/saveReservation/', views.save_reservation),
    path('api.token.auth/', obtain_auth_token, name='api_token_auth')
]
