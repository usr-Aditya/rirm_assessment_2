from collections import namedtuple
from django.db import models
from django.urls import reverse

class StudentInfo(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    klass = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.roll_no)
    
    def get_absolute_url(self):
        return reverse('academics-create')
        


class StudentAcademics(models.Model):
    roll_no = models.ForeignKey(StudentInfo, blank=True, null=True, on_delete=models.CASCADE)
    maths = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    biology = models.IntegerField(default=0)
    english = models.IntegerField(default=0)

    def get_absolute_url(self):
        # print(self.roll_no.pk)
        return reverse('student-details')

    