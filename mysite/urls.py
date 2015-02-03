# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    # <!-- 1 url(r'^polls/', include('polls.urls')),
    
    # <!-- 2 Adicionando NameSpace na chamativa da App; A adição de NameSpace, faz o vinculo das Urls
    # com as aplicações, serve para quando se tem várias apps no mesmo projeto, poder fazer o vínculo
    # de quais urls estão atreladas a quais apps.
    # Fazendo o namespace eu posso acessar quaisquer def e objeto da aplicação fazendo chamada ao nome do namespace --> da app 

    url(r'^polls/', include('polls.urls', namespace="polls")),

    # Está linha está fazendo a mudança do urls do mysite para o urls do polls que foi o modificado
    # Na página 3 do tutorial. A linha url(r'^admin/', include(admin.site.urls)) já é default do Django
    # Não houve modificação nessa linha. Já estava default da página.

    url(r'^admin/', include(admin.site.urls)),

    # Expressão regulares, são os primeiros parâmetros passados dentro da URL e a view que ela 
    # está atrelada, no caso do exemplo é o polls.url
    # Podem ser requeridos --> Expressões regulares e views
    # Podem ser opionais --> Keys arguments (arqgumentos de palavras) e names.
    # Complexas expressões regulares podem ter performance pobre
    # A performance depende do poder das expressões regulares.


    # Argumentos --> Quando o Django encontra a expressão regular ele chama a funcão especificada 
    # na views.
    # Se a expressão regular usa capturas simples, valores são passados como a posição dos argumentos (passagem posicional de argumentos)
    # Se usa capturas de nomes, valores são passados com "palavras" de argumentos.

    # Key words podem ser passados como dicionário para a requisição da view

)


