from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    date_time = models.DateTimeField("data published")

class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    