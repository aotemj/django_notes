from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=20)


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Mother(models.Model):
    name = models.CharField(max_length=200)


class Children(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)
