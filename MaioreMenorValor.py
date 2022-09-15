# -*- coding: utf -8 -*-8

import sys
import time

v1 = int(input("Digite o valor 1: "))
v2 = int(input("Digite o valor 2: "))
v3 = int(input("Digite o valor 3: "))
v4 = int(input("Digite o valor 4: "))
v5 = int(input("Digite o valor 5: "))

if v1 > v2:
    if v1 > v3:
        if v1 > v4:
            if v1 > v5:
                print("o valor 1 é maior = ", v1)
                
if v2 > v1:
    if v2 > v3:
        if v2 > v4:
            if v2 > v5:
                print("o valor 2 é maior = ", v2)
                
if v3 > v1:
    if v3 > v2:
        if v3 > v4:
            if v3 > v5:
                print("o valor 3 é maior = ", v3)
                
if v4 > v1:
    if v4 > v2:
        if v4 > v3:
            if v4 > v5:
                print("o valor 4 é maior = ", v4)
                
if v5 > v1:
    if v5 > v2:
        if v5 > v3:
            if v5 > v4:
                print("O valor 5 é maior = ", v5)
                

if v1 < v2:
    if v1 < v3:
        if v1 < v4:
            if v1 < v5:
                print("o valor 1 é menor = ", v1)
                
if v2 < v1:
    if v2 < v3:
        if v2 < v4:
            if v2 < v5:
                print("o valor 2 é menor = ", v2)
                
if v3 < v1:
    if v3 < v2:
        if v3 < v4:
            if v3 < v5:
                print("o valor 3 é menor = ", v3)
                
if v4 < v1:
    if v4 < v2:
        if v4 < v3:
            if v4 < v5:
                print("o valor 4 é menor = ", v4)
                
if v5 < v1:
    if v5 < v2:
        if v5 < v3:
            if v5 < v4:
                print("O valor 5 é menor = ", v5)
                
time.sleep(5)
sys.exit
