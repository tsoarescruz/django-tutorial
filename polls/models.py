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
        # return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))
        
        # Alteração do método para que retorne as modficação da data para data futura e verificação da atual
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

        # Faz a interação para a chamativa do admin para fazer o filtro dos dados de 
        # acordo com a data de publicação DateTimeField
        # O Tipo de filtro depende do tipo de campo que se quer filtrar. Porque pub_date é DateTimeField,
        # Django conheçe as opões dos filtros apropriados como o 'Any date', 
        # 'Today', 'Past 7 days', 'This month' and 'This year'

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'

class Choice(models.Model):     # __unicode__ on Python 2

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200, default='')
    name_user = models.CharField(max_length=200, default='')
    votes = models.IntegerField(default=0)

    # ...
    def __str__(self):
        return self.choice_text