# -*- coding: utf-8 -*-

from django.contrib import admin
from polls.models import Choice
from polls.models import Question


        # Faz a adição dos campos de choice no add question de forma empilhada, ao contrário do outro  
        # código que só me permitia fazer a adição de um só campo; este tipo de código 
        # permite que eu possa fazer adições em série para o meu database;


        # Este trecho de código abaixo permite fazer a amostragem das choices - escolhas
        # de forma empilhada; a outra modificação implementada permite fazer de forma 
        # tabular 
        # class ChoiceInline(admin.StackedInline):


class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes':  ['collapse']}),
        # A classe colapse é passagem da classe em JavaScript
        # A modificação tem de ser feita no código do Java.
        # Esse tipo de classe faz o hide da informação a ela atrelada no field, nesse
        # caso ao field Date information
    ]
   
    # Faz a modifição de como é exibido a página do código de selecionar a questão
    # Exibe o template em forma de colunas com a data da publicação e se foi publicado 
    # recentemente, se for retirado essa linha ele vai exibir de forma empilhada e sem as
    # informações adicionais
   

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    inlines = [ChoiceInline]
# admin.site.register(Question)

# Está modificação foi feita para a adição das opções do Choice
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)

# Register your models here.
