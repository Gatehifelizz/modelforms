from django.db import models


# Create your models here.
class Student(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    emailaddress = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    age = models.IntegerField()

    class Meta:
        db_table = "wanafunzi"


class Staff(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    emailaddress = models.CharField(max_length=30)

    def __str__(self):
        return self.FirstName


class Department(models.Model):
    DepartmentName = models.CharField(max_length=20)
    HeadOfDepartment = models.CharField(max_length=20)
    emailaddress = models.CharField(max_length=30)

    def __str__(self):
        return self.DepartmentName


class Post(models.Model):
    Title = models.CharField(max_length=90)
    Description = models.TextField(max_length=100)
    Author = models.ForeignKey(Student, on_delete=models.CASCADE)
    CreatedAt = models.DateField()

    def __str__(self):
        return self.Title
