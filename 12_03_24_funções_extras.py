# -*- coding: utf-8 -*-
"""12/03/24 - Funções Extras

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SIasMjqsPkv5OY7ba-tD3GmkU7nL71Fe

Função incursiva
"""

#funcao recursiva potencia(a, b)
# potencia(a, b) = a * potencia(a, b-1)
# caso base: potencia(a, 0) = 1

def potencia(a, b):
  if b == 0:
    return 1
  return a * potencia(a, b-1)

potencia(5, 3)

"""Função iterativa comparando com a função incursiva"""

#versao iterativa
#potencia(a, b) = a * a * ... * a, b vezes

def ponteciaI(a, b):
  pot = 1
  for i in range(b):
    pot = pot * a
  return pot

"""função lambda"""

c2f = lambda c: c * 1.8 + 32

c2f(30)

"""pitágoras"""

def raiz(N):
  """
  Calcula a raiz quadrada de N
  Usando o algoritmo>
  x_(n+1) = 1/2  * (x_n + N/x-n)
  """
  if N == 0 or N == 1:
    return N
  x, n = 1, 0
  while abs(x*x - N)> 1e-9:
    n += 1
    x = 1/2 * (x + N/x)
  return x

"""cálcule o pi"""

def pi(n):



"""função de pitagoras"""

def pitagoras(a, b):
  """ #docstring
  Calcula a hipotenusa
  de triângulo retângulo
  de catetos a e b
  """
  return raiz(a*a + b*b) # 2 ** 2 (fórmula para potência)

"""equação do 2 grau"""

def eqgrau2(a, b, c):
  """
  Resolve:
  a * x**2 + b * x + c = 0
  """
  delta = (b**2- 4 * a * c)
  if delta < 0:
    print(f'Delta {delta} é menor do que zero!')
    return None
  raiz_delta = raiz(delta)
  x1 = (-b - raiz_delta) / (2 * a)
  x2 = (-b + raiz_delta) / (2 * a)
  return x1, x2

# (x - 2) * (x - 3) = 0 tem raizes 2 e 3
# x**2 - 5 * x + 6 = 0
# a = 1, b = -5, c = 6

a, b, c = 1, -5, 6
eqgrau2(a, b, c)

"""função recursiva 2"""

def soma_recursiva(n):
  if n == 1:
    return 1
  return n + soma_recursiva(n-1)

soma_recursiva(10)

"""função iterativa 2"""

def soma_iterativa(n):
  soma = 0
  for n in range(1, n+1):
    soma += 1
  return soma

soma_iterativa(5)

"""Sequência Fibonacci (função recursiva)"""

def fibonnaci(n):
  if n == 0 or n == 1:
    return n
  return fibonnaci(n-1) + fibonnaci(n-2)

fibonnaci(10)

#Compreensão de lista da sequência fibonnaci

[fibonnaci(n) for n in range(1, 8)]