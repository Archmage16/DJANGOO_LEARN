from django.db import models

# Create your models here.
class BasePerson(models.Model):
    name = models.TextField()
    email = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
    def __str__(self) -> str:
        return f"{self.name}"
    


class Employee(BasePerson):
    position = models.TextField()

class Teacher(Employee):
    subject = models.TextField()
    


class Student(BasePerson):
    course_name = models.TextField()
    start_date = models.DateTimeField(auto_now=True)


class OrderedStudent(Student):
    class Meta:
        proxy = True
        verbose_name = 'Ordered_Students'
        ordering = ['-created_time']