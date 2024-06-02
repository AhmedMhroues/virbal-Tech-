from django.urls import path , include 
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, PatientViewSet, TrainingViewSet


router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'trainings', TrainingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
