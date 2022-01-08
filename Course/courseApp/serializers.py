from rest_framework import serializers
from .models import Courses


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['name', 'description', 'ratings']
