from .models import Passenger
from .serializers import PassengerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def passengers_list(request):
    if request.method == 'GET':
        passenger = Passenger.objects.all()
        serializer = PassengerSerializer(passenger, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def passengers_detail(request, pk):
    try:
        passenger = Passenger.objects.get(pk=pk)
    except Passenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PassengerSerializer(passenger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
