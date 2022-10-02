#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:43:38 2022

@author: davideteixeira
"""

def tabela_DD(x,y):
    m = len(x)
    T = [[0]*m for i in range(m)]
    for i in range(m):
        T[i][0] = y[i]
    for j in range(1,m):
        for i in range(j,m):
            T[i][j] = round((T[i][j-1] - T[i-1][j-1]) / (x[i]-x[i-j]),4)
    return T

def interpolacao(x,y,valor):
    m = len(x)
    T = tabela_DD(x,y)
    soma = T[0][0]
    for i in range(1,m):
        temp = T[i][i]
        for j in range(0,i):
            temp = temp * (valor - x[j])
        soma = soma + temp
    return soma