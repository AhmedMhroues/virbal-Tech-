
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Doctor, Patient, Training
from .serializers import DoctorSerializer, PatientSerializer, TrainingSerializer
from .models import Doctor, Patient
from django.shortcuts import render


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    patients = Patient.objects.all()
    serializer = PatientSerializer  (patients, many=True)
     

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer




