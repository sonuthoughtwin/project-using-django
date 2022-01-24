from functools import partial
from django.http import Http404
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.authentication import BaseAuthentication
#from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly                         





# class StudentModelViewSet(viewsets.ModelViewSet):
#     #authentication_classes = [BaseAuthentication]
#     permission_classes = [IsAdminUser]
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    



class StudentViewSet(viewsets.ViewSet):
    
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self ,pk):
        try:
            return Student.objects.get(pk = pk)
        except Student.DoesNotExist:
            raise Http404


    def retrieve(self, request, pk):
        # id = pk 
        # if id is not None:
        #     stu = Student.objects.get(id=id)
        stu = self.get_object(pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)
       
    def update(self, request, pk):
        # id = pk
        # stu = Student.objects.get(id=id)
        stu = self.get_object(pk)
        serializer =  StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        # id = pk
        # stu = Student.objects.get(id=id)
        stu = self.get_object(pk)
        serializer =  StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Partial Data Updated"})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        # id = pk
        # stu = Student.objects.get(id=id)
        stu = self.get_object(pk)
        stu.delete()
        return Response({"msg":"Data Delete"})

    
    