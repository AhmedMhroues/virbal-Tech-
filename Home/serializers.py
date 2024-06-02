from rest_framework import serializers
from .models import Doctor, Patient, Training






class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    trainings = TrainingSerializer(many=True, read_only=True)
    treatment_plans = TrainingSerializer(many=True, read_only=True)
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=True, read_only=True)
    class Meta:
        model = Doctor
        fields = '__all__'
####################################################################################