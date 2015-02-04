# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from polls import views

    # Quando é feita a chamativa de "/pools/34" Django irá carregar o mysite.urls, por que módulo do 
    # Paython irá apontar para a confguração do ROOT_URLCONF

    # Quando as variáveis forem o urlpattern será transcrito para expressão regulares em ordem.

    # As funções de include () são simples referencias de URLS

    # View Genérica
    # Each generic view needs to know what model it will be acting upon. This is provided using the model attribute.
    # The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed 
    # question_id to pk for the generic views.

urlpatterns = patterns('',
    # Ex: /polls/
    # url(r'^$', views.index, name='index'),
    #<!-- 2 View Genérica
    url(r'^$', views.IndexView.as_view(), name ='index'),
    #Ex: /polls/5/
    #<-- 1 url(r'^(?P<question_id>\d+)/$', views.detail,name='detail'),
    
    # Este specifics faz referência ao details passando o número da question.id para o tratativa 
    # pelo jinja incorporado no html
    
    # url(r'^specifics/(?P<question_id>\d+)/$', views.detail,name='detail'),
    # <!-- 2 View Genérica
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

    # Ex: /polls/5/results/
    # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # <!-- 2 View Genérica
    url(r'^(?P<pk>\d+)/results/$'), views.ResultsView.as_view(), name='results'),

    # Ex: /polls/5/vote/
    # <!-- 2 View Genérica
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

    # ?P<question_id> --> Define o nome que será usado para identificar o padrão correspondido.
    # \d+ --> É a expressão regular que corresponde a sequência de dígitos. 
)