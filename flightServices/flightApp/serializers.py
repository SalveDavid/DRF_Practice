import re
from rest_framework import serializers
from .models import Flight, Passenger, Reservation


def isFlightNumberValid(data):
    print(data)
    print('isFlightNumberValid')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validator = [isFlightNumberValid]

    def validate_flightNumber(self, flightNumber):
        if re.match('^[a-zA-Z0-9]*$', flightNumber) is None:
            raise serializers.ValidationError('Invalid Flight Number. Make sure it is alpha numeric')
        return flightNumber

    def validate(self, data):
        print(data['flightNumber'])
        print(data)
        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
