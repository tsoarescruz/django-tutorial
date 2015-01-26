# -*- coding: utf-8 -*-
import datetime
# from datetetime import timedelta

from django.db import models
from django.utils import timezone

    # Função que retorna se os dados foram publicados recentemente. Não ficou muito claro
    # a utilização do método timedelta para mim. 

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):          # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))


class Choice(models.Model):     # __unicode__ on Python 2

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200, default='')
    name_user = models.CharField(max_length=200, default='')
    votes = models.IntegerField(default=0)

    # ...
    def __str__(self):
        return self.choice_text


