from dataclasses import fields
from rest_framework import serializers

from apiapp.admin import StudentAdmin
from .models import Student
from rest_framework.authentication import BaseAuthentication

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'course', 'roll_no']





