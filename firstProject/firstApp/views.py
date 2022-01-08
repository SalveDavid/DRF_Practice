from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee


def employeeView(request):
    emp = {
        'id': 123,
        'name': 'John',
        'sal': 10000000
    }

    data = Employee.objects.all()
    response = {'employees': list(data.values('name', 'sal'))}

    return JsonResponse(response)
    # return JsonResponse(emp)
