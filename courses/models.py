from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    maximum_capacity = models.PositiveIntegerField()
    current_enrolled = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    enrolled_courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    