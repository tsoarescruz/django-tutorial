# -*- coding: utf-8 -*-

from django.shortcuts import render
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

# 	def __init__(self):
# 		pass


# 	def msg(self):
# 		pass



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