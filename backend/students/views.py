from django.http.response import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

