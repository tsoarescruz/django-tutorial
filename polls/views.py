# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question_text for p in latest_question_list])
    template = loader.get_template('polls/index.html')
    # Cria um objeto contexto sendo um dicionário de dados, funciona como se fosse um vetor com 
    # a chave (index --> 'latest_question_list') e os valores indexados a chave :latest_question_list
    # O código carrega o template chamado polls/index.html e passa o context; o contecto é um dicionário
    # de dados mapeando as variáveis d template para os objetos do Phyton.

    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
        })

    # Esse output na saída está referenciado ao valor de output que foi indexado a p e que está em comentário
    # Conforme fui avançando do tutorial, foi feito outro valor de output
    # return HttpResponse(output)

    return HttpResponse(template.render(context))


    # return HttpResponse("Hello, World. You're at the polls Index.")

# As funões abaixo recebem valores passados pelos parâmetros e fazem o HttpResponse
# Mostrando os títulos das funções atribuídas a elas

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response="You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# Todo o trecho que está em comentário foi exemplos que o Kibe fez para me passar 
# informações de como poderia ser feita a orientação objeto no python e como que
# era definida as funções - def

# def teste(msg):
    # print msg


# class Pessoa(object):

    # def __init__(self):
        # pass

        #  metodo construtor precisa da passagem de parametro do self
        #  o pass faz a passagem do método, como não foi 
        #  implementado codigo nenhum neste método ele ignora e passa. 


    # def msg(self):
        # return "teste"



# class Pessoa(object):

#   def __init__(self):
#       pass


#   def msg(self):
#       pass



# In [1]: from polls.views import Pessoa

# fez o import da classe pessoa

# In [2]: pp = Pessoa() 

# kibe fez a instancia de pp para a classe pessoa


# In [3]: pp.msg()
# Out[3]: 'teste'

#  Fez a chamado do metodo msg instanciado em pp no input e out 4

# In [4]: pp.msg()

# Out[4]: 'teste'

# In [5]: Pessoa.msg
# Out[5]: <unbound method Pessoa.msg>

# In [6]: Pessoa
# Out[6]: polls.views.Pessoa


# 
# 

# In [7]: Pessoa.msg(pp)
# Out[7]: 'teste'

# In [8]: Pessoa.msg(pp)
# Out[8]: 'teste'

#  No input e out 7 e 8 o kibe fez a chamada da classe pessoa e passa a 
#  propria instancia do metodo como parametro.
#  implementacao  do parametro self, o python permite que se possa passar 
#  a propria instancia como parametro do metodo chamador. 


# In [9]: pp.msg()
# Out[9]: 'teste'

# In [10]: renato = Pessoa()

# In [11]: Pessoa.msg(renato)
# Out[11]: 'teste'

# In [12]: renato.msg()
# Out[12]: 'teste'

# In [13]: renato = Pessoa()

# In [14]: renato
# Out[14]: <polls.views.Pessoa at 0x109dc6b10>

# In [15]: renato.msg()
# Out[15]: 'teste'

# In [16]: exit()