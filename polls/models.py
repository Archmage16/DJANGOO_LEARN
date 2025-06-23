from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# Create your models here.
class Question(models.Model):
    # num = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=100, 
                                     unique=True, 
                                     unique_for_date='date_time', null=False, blank=False)
    
    notes = GenericRelation('Note')
    date_time = models.DateTimeField("data published", auto_now_add=True)
    def __str__(self) -> str:
        return self.question_text

class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    notes = GenericRelation('Note')
    def __str__(self) -> str:
        return f"{self.text_choice} - {self.votes} votes"


class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')
    pass