#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:23:21 2022

@author: davideteixeira
"""
# Importar myMath
from mymath import myMath

# Apresentação do programa
m = 62
print("="*m)
print("Vamos dar Início à Resolução do Sistema de Equações Lineares")
print("="*m)

# Input do número de equações e incógnitas
n = int(input("Primeiro, qual o número de equações e incógnitas? "))

# Criação da matriz e do vetor genéricos
matriz = [[0]*n for i in range(n)]
vetor = [0] * n

# Input dos coeficientes da equação, assim como os termos independentes
for i in range(n):
    for j in range(n):
        matriz[i][j] = float(input(f'a({i+1},{j+1}): '))
    vetor[i] = float(input(f'b{i+1}: '))
    
# Criação da solução, utilizando a biblioteca myMAth
solucao = myMath.AXB(matriz, vetor)

# Apresentação da solução do sistema
print("")
print("="*m)
print("Passarei a dar a solução do sistema")
print("="*m)
print("")
for i in range(n):
    print(f'x{i+1} = {solucao[i]}')