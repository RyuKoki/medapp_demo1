from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from ndarraydjango.fields import NDArrayField

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}_{1}/{2}'.format(instance.first_name, instance.sure_name , filename)

# Create your models here.

class Elder(models.Model):
    first_name = models.CharField(max_length=30)
    sure_name = models.CharField(max_length=30)
    birthday = models.DateField()
    hospital_number = models.CharField(max_length=30)
    hospital_name = models.CharField(max_length=50)
    hospital_phone = models.CharField(max_length=10)
    relative_firstname = models.CharField(max_length=30)
    relative_surename = models.CharField(max_length=30)
    relative_relation = models.CharField(max_length=30)
    relative_phone = models.CharField(max_length=10)
    memory = models.JSONField()
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    face = models.JSONField()

    # def __str__(self):
    #     return "{"+"'first_name': {self.first_name}, 'sure_name': {self.sure_name}"+"}"

class Dispenser(models.Model):
    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    medicine = models.CharField(max_length=100)
    amount = models.IntegerField()
    pill_time = models.TimeField()

class TakeCare(models.Model):
    careTaker_id = models.ForeignKey(User, on_delete=models.CASCADE)
    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    # time_spend = models.TimeField()
    
    # def __str__(self):
        # return "{" + "'caretaker_id': {self.careTaker_id}, 'elder_id': {self.elder_id}, 'time_spend': {self.time_spend}}" + "}"
        # return {'caretaker_id': self.careTaker_id, 'elder_id': self.elder_id, 'time_spend': self.time_spend}

class ElderPhysical(models.Model):
    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    physical = models.JSONField()

class ElderDisease(models.Model):
    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    disease = models.JSONField()
