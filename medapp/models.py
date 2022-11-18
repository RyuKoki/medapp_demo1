from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from ndarraydjango.fields import NDArrayField

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}_{1}/{2}'.format(instance.first_name, instance.sure_name , filename)

# Create your models here.

class Elder(models.Model):
    IDN = models.CharField(max_length=13)
    first_name = models.CharField(max_length=30)
    sure_name = models.CharField(max_length=30)
    birthday = models.DateField()
    memory = models.JSONField()
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    face = models.JSONField()

class Emergency(models.Model):
    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    hospital_number = models.CharField(max_length=30)
    hospital_name = models.CharField(max_length=50)
    hospital_phone = models.CharField(max_length=10)
    relative_firstname = models.CharField(max_length=30)
    relative_surename = models.CharField(max_length=30)
    relative_relation = models.CharField(max_length=30)
    relative_phone = models.CharField(max_length=10)

class History(models.Model):
    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    time = models.DateTimeField()
    med_picture = models.ImageField()

class Schedule(models.Model):
    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    breakfast = models.JSONField()
    # breakfast = {time: 00.00, before: {med: name, amount: 2}, after: {}}
    lunch = models.JSONField()
    dinner = models.JSONField()
    night = models.JSONField()

class TakeCare(models.Model):
    careTaker_id = models.ForeignKey(User, on_delete=models.CASCADE)
    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)

class ElderPhysical(models.Model):
    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    physical = models.JSONField()

class ElderDisease(models.Model):
    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    disease = models.JSONField()
