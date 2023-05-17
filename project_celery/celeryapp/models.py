from django.db import models

# Model Tasks 1-5
#####################################
from django.db.models import CASCADE


class Classroom(models.Model):
    periodo = models.CharField(max_length=100)

    def __str__(self):
        return self.periodo


class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, related_name='classes')

    def __str__(self):
        return self.firstname


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    teacher_id = models.ForeignKey(Teacher, on_delete=CASCADE, related_name='professor')

    def __str__(self):
        return self.firstname
