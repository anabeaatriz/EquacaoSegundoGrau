# -*- coding: utf -8 -*-

import time
import sys

ano = int(input("Digite o ano para analisar se ele é bissexto: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print("O ano de {} é bissexto" .format(ano))
else:
  print("O ano {} não é bissexto!" .format(ano))

time.sleep(5)
sys.exit
