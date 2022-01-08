from django.shortcuts import render
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departureCity=request.data['departureCity'],
                                    arrivalCity=request.data['arrivalCity'],
                                    dateOfDeparture=request.data['dateOfDeparture'])
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.middleName = request.data['middleName']
    passenger.lastName = request.data['lastName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    # Reservation.save(reservation)
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['departureCity', 'arrivalCity', 'dateOfDeparture']
    permission_classes = (IsAuthenticated,)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
