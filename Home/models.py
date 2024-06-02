from django.db import models
       

class Doctor(models.Model):
     
    name = models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('Dr', 'Doctor'),
        ('Sp', 'specialist'),]
    specialty = models.CharField(max_length=2, choices=STATUS_CHOICES, default='Dr')
    def __str__(self):
         return self.name
        # return self.specialty 
    
class Training(models.Model):
    name_of_traninig = models.CharField(max_length=50,null=True, blank=True)
    image_of_training = models.ImageField(upload_to='trainings/', null=True, blank=True)
    voice=models.FileField(upload_to='audio_files/',null=True, blank=True)
    def __str__(self):
         return self.name_of_traninig

class Patient(models.Model):
    name_of_doctor = models.ForeignKey(Doctor, related_name='patients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    diagnosis = models.TextField()
    recommendations = models.TextField()
    treatment_plan = models.ManyToManyField(Training,default='طماطم',related_name='patients',null=True, blank=True)
    comments = models.TextField(blank=True,null=True,default='No connents yet')
    def __str__(self):
        return self.name





