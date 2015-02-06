# -*- coding: utf-8 -*-



from polls.models import Question, Choice  

    #<!-- 2 Esses imports fazem parte da 2 opção de saída da views.

    # <!-- 3
# from django.http import HttpResponse
from django.template import RequestContext, loader

    #<!-- 2 Reporte de 404 erro
# from django.http import Http404    

    #<!-- 3 Faz o shortcut do erro 404
# from django.shortcuts import get_object_or_404

    #<!-- 4 Shortcut do error404
from django.shortcuts import get_object_or_404, render

    #<!-- 4 
from django.http import HttpResponseRedirect, HttpResponse

    #<!-- 4
from django.core.urlresolvers import reverse

from django.views import generic

    # Essa função de index faz o retorno do objeto com o HttpResponse
    # Está atrelada com a programação do script feito no index.html
    # Essa foi a segunda opção de response do template apresentada no Tutorial
    # A primeira opção está contida na segunda e está em comentário somente com a modificação da saída do output
    # Irei deixar a segunda opção toda em comentário e gerar o código de saída da função index separado para a terceira opção.


    # 2 opção de saída da view. Utilizando o método do HttpResponse

# <!-- 2 def index(request):

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

# import ipdb; ipdb.set_trace();
    # Faz teste 

def index(request):

    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render (request, 'polls/index.html', context)


def detail(request, question_id):
    # Esta implementação faz o retorno do question_id como parâmetro informado no endereço do 
    # página, informado pelo endereçamento da url 
    # <!--1 return HttpResponse("You're looking at question %s." % question_id)
 
# Excessão para o erro 404 --> Caso o question_id não exista ele cai nessa excessão.

    #Implementação do error 404
    #<!-- 2 try:
    #<!-- 2     question = Question.objects.get(pk=question_id)
    #<!-- 2 except Question.DoesNotExist:
    #<!-- 2     raise Http404("Question does not exists")
    #<!-- 2 return render(request, 'polls/detail.html', {'question': question })


    # <!-- 3 Implementação do shortcuts do error 404

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question })

def results(request, question_id):
    
    # <!--1
    # response="You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    
    #<!-- 1
     # return HttpResponse("You're voting on question %s." % question_id)
     
    #<!-- 2 Escrevendo um form simples 
     p = get_object_or_404(Question, pk=question_id)
     try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
     except(KeyError, Choice.DoesNotExist):
          # Redisplay the question voting form
         return render(request, 'polls/detail.html', {
             'question': polls,
             'error_message': "You didn't select a Choice."
          })
     else:
         selected_choice.votes += 1
         selected_choice.save() 

         # Ex: '/polls/3/results/'
         # A funcão reverse ajuda a evitar que se escreva a URL na função da view. 
         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # Variável de context[]\o, faz o mesmo papel da latest_questio_list instanciada. 
    # Essa variável está sobreescrevendo a variável default do
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
# Variável de contexto question e latest_question_list são geradas automaticamete de modelo Question do Django.

    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
