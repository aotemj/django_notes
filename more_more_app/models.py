from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    friends = models.ManyToManyField("self")
    course = models.ManyToManyField("self")


class Course(models.Model):
    name = models.CharField(max_length=40)


class SchoolClass(models.Model):
    name = models.CharField(max_length=200)


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    school_class = models.ManyToManyField("self")
