
from django.db import models
import uuid 

class Student(models.Model):
    unique_identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    age = models.IntegerField()
    level = models.IntegerField()
    contact_info = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)
    matric_number = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    cgpa = models.FloatField()
    admission_type = models.CharField(max_length=20)
    scholarship_info = models.CharField(max_length=50)
    address = models.TextField()
    passport_photograph = models.ImageField(upload_to='passport_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.unique_identifier} - {self.name}"
