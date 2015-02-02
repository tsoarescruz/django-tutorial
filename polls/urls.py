# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from polls import views



    # Quando é feita a chamativa de "/pools/34" Django irá carregar o mysite.urls, por que módulo do 
    # Paython irá apontar para a confguração do ROOT_URLCONF

    # Quando as variáveis forem o urlpattern será transcrito para expressão regulares em ordem.

    # As funções de include () são simples referencias de URLS

urlpatterns = patterns('',
    # Ex: /polls/
    url(r'^$', views.index, name='index'),
    #Ex: /polls/5/
    # url(r'^(?P<question_id>\d+)/$', views.detail,name='detail'),
    url(r'^specifics/(?P<question_id>\d+)/$', views.detail,name='detail'),
    # Ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # Ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

    # ?P<question_id> --> Define o nome que será usado para identificar o padrão correspondido.
    # \d+ --> É a expressão regular que corresponde a sequência de dígitos. 
)