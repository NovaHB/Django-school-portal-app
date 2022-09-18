
from django.db import models

# Create your models here.
class Students(models.Model):
    email=models.EmailField(blank=True,null=True)
    full_name=models.CharField(blank=True,null=True,max_length=100)
    first_name=models.CharField(blank=True,null=True,max_length=100)
    matric=models.CharField(blank=True,null=True,max_length=100)
    admission_status=models.CharField(blank=True,null=True,max_length=100)
    level=models.CharField(blank=True,null=True,max_length=100)
    grad_year=models.CharField(blank=True,null=True,max_length=100)
    faculty=models.CharField(blank=True,null=True,max_length=100)
    department=models.CharField(blank=True,null=True,max_length=100)
    passport=models.ImageField(blank=True, upload_to='stud_images')
    class Meta:
        db_table="students"