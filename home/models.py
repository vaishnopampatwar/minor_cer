from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
import os

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Staff"), (3, "Hod"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    # name=models.CharField(max_length=255)
    # email=models.CharField(max_length=255)
    # password=models.CharField(max_length=255)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    # name=models.CharField(max_length=255)
    # email=models.CharField(max_length=255)
    # password=models.CharField(max_length=255)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    # course = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Hod(models.Model):
    id = models.AutoField(primary_key=True)
    # name=models.CharField(max_length=255)
    # email=models.CharField(max_length=255)
    # password=models.CharField(max_length=255)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    sem=models.CharField(max_length=255)
    academic_year=models.CharField(max_length=255)
    minor=models.CharField(max_length=255)
    credits=models.IntegerField()
    staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # staff= models.CharField(max_length=255)
    # staff=models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    prn= models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    mob=models.BigIntegerField()
    email=models.CharField(max_length=255)
    # subcode=models.CharField(max_length=255)
    sas=models.CharField(max_length=255)
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    date= models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class StudentResult(models.Model):
    id = models.AutoField(primary_key=True)
    prn=models.CharField(max_length=255)
    name= models.CharField(max_length=255)
    course_name= models.CharField(max_length=255,default='')
    grade = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class ResultAnalysis(models.Model):
    id = models.AutoField(primary_key=True)
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    result_file = models.FileField(upload_to=filepath, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Staff.objects.create(admin=instance)
        if instance.user_type == 3:
            Hod.objects.create(admin=instance)
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.staff.save()
    if instance.user_type == 3:
        instance.hod.save()
    


