from django.db import models

# Create your models here.
class Question(models.Model):
    # num = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=100, 
                                     unique=True, 
                                     unique_for_date='date_time', null=False, blank=False)
    
    date_time = models.DateTimeField("data published", auto_now_add=True)
    def __str__(self) -> str:
        return self.question_text

class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self) -> str:
        return f"{self.text_choice}, {self.question_text}"