from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

class SubjectChoice(models.TextChoices):

    CSE = 'cse', _('CSE')
    EEE = 'eee', _('EEE')
    Textile = 'textile', _('TEXTILE')
    Bba = 'bba', _('BBA')


class Student(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=20)
    batch_no = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    student_id = models.CharField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=42)
    startDate = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=16)

    def __str__(self):
        return self.code

class Faculty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=64)

    def __str__(self):
        return self.user.username



class CourseRegistration(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #approvedBy = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.student.name

class Environment(models.Model):
    key = models.CharField(max_length=128)
    value = models.CharField(max_length=128)

    def __str__(self):
        return  self.key

