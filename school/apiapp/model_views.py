from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from apiapp.models import Student
from apiapp.serializers import StudentSerializer
from rest_framework import viewsets




class StudentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #authentication_classes = [BaseAuthentication]
    

