# -*- coding: utf -8 -*-

import sys
import time

numLados = int(input("Possuí quantos lados? "))

if numLados == 3:
  print("É um triângulo!")

  a = float(input("Insira a medida do lado A: "))
  b = float(input("Insira a medida do lado B: "))
  c = float(input("Insira a medida do lado C: "))

  P = (a + b + c) / 2
  A = (P * (P - a) * (P - b) * (P - c)) ** (1/2)

  print("A área do seu triangulo segund a Fórmula de Heron é = ", A)

elif numLados == 4:
  print("É um quadrado!")

  b = float(input("Insira a medida da base: "))
  h = float(input("Insira a medida da altura: "))

  a = b * h

  print("A área do quadrado é = ", a)
  
elif numLados == 5:
  print("É um pentágono!")

  l = float(input("Insira a medida do lado: "))
  h = float(input("Insira a medida da altura: "))
  
  a = (l * h) / 2

  print("A área do pentágono = ", a)
  
elif numLados <3:
  print("Não é um polígono!")
else:
  print("Polígono não identificado!")

time.sleep(5)
sys.exit
