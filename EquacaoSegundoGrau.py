# -*- coding: utf -8 -*-

import time
import sys

a = float(input("Digita seu coeficiente a: "))
b = float(input("DIgite seu coeficiente de b: "))
c = float(input("Digite seu coeficiente de c: "))

delta = (b ** 2 - 4*a*c)
print("O valor do delta é", delta)
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)

if delta < 0:
  print("Não há solução, pois o delta é menor que 0")
elif delta > 0:
  print("A raiz x1 = ", x1)
  print("A raiz x2 = ", x2)
else:
  print("Há apenas uma solução, x1 = ", x1, "e x2 = ", x2)

time.sleep(5)
sys.exit 
