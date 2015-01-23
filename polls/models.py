
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
# Create your models here.


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200, default='')
    name_user = models.CharField(max_length=200, default='')
    votes = models.IntegerField(default=0)