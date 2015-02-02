# -*- coding: utf-8 -*-

from django.shortcuts import render
from polls.models import Question

    #<!--2 Esses imports fazem parte da 2 opção de saída da views.

from django.http import HttpResponse
from django.template import RequestContext, loader

    # <!-- 3 Reporte de 404 erro

from django.http import Http404    

    # Essa função de index faz o retorno do objeto com o HttpResponse
    # Está atrelada com a programação do script feito no index.html
    # Essa foi a segunda opção de response do template apresentada no Tutorial
    # A primeira opção está contida na segunda e está em comentário somente com a modificação da saída do output
    # Irei deixar a segunda opção toda em comentário e gerar o código de saída da função index separado para a terceira opção.


    # 2 opção de saída da view. Utilizando o método do HttpResponse

# <!--2 def index(request):

    # Latest_question faz o carregamento dos objetos ordenando pela variável de pub_date (data de publicação).
    # o número em colchete, deve fazer referência ao número total de ordenações.

    # <!--2 latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question_text for p in latest_question_list])
    
    # Acredito que esse método faça o loader do template indicando o ponteiro para onde a página html se encontra
    # Acredito que ele já esteja direcionado para a página template criada diretamente n projeto.

    # <!-- Fazer pergunta a equipe se ao criar o diretório template se já fica um ponteiro para o caminho template
    # devido a ser suprimido o restante da string do caminho. --!>

    # <!--2 template = loader.get_template('polls/index.html')
    
    # Cria um objeto contexto sendo um dicionário de dados, funciona como se fosse um vetor com 
    # a chave (index --> 'latest_question_list') e os valores indexados a chave :latest_question_list
    # O código carrega o template chamado polls/index.html e passa o context; o contecto é um dicionário
    # de dados mapeando as variáveis d template para os objetos do Phyton.

    # <!--2 context = RequestContext(request, {
        # <!--2 'latest_question_list': latest_question_list,
      # <!--2  })

    # Esse output na saída está referenciado ao valor de output que foi indexado a p e que está em comentário
    # Conforme fui avançando do tutorial, foi feito outro valor de output
   
    # <!--1 return HttpResponse(output)

    # <!--2 return HttpResponse(template.render(context))

    # Término da 2 opção

    # Este return não foi da primeira opção de saída da view e sim para a primeira manipulação do index.
    # Somente para ter alguma saída na chamativa da página.

    # <!-- 0  return HttpResponse("Hello, World. You're at the polls Index.")

    # Término da 1 opção <!-- somente incluía a saída do return HttpResponse(output) para para a saída da view.

# As funões abaixo recebem valores passados pelos parâmetros e fazem o HttpResponse
# Mostrando os títulos das funções atribuídas a elas.


    # 3 opção de saída da view. Utilizando o atalho na renderização
    # o que muda nessa opção de renderizar é a retirada da linha template = loader.get_template('polls/index.html')
    # Essa opção de informar o template que vai ser renderizado na página, vai junto com o return do na função render, 
    # na passagem de parâmetro requer o request como primeiro argumento, caminho (template) como segundo argumento 
    # e o dicionário de dados, utilizado como terceiro argumento.
    # Equivale ao HttpResponse anterior só que de outra forma --> return HttpResponse (template.render(context)).

def index(request):

    latest_question_list = Question.objects.order_by('pub_date') [:5]
    context = {'latest_question_list': latest_question_list}
    return render (request, 'polls/index.html', context)


def detail(request, question_id):
    # <!--1 return HttpResponse("You're looking at question %s." % question_id)
 
# Excessão para o erro 404 --> Caso o question_id não exista ele cai nessa excessão.

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    return render(request, 'polls/detail.html', {'question': question })

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