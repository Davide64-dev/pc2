#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 18:08:46 2022

@author: davideteixeira
"""

def simpson(a, b, n):
    h = (b-a)/n
    soma_impar = 0
    soma_par = 0
    for i in range(1,n-2,2):
        x = a + h * i
        soma_par = soma_par + f(x)
    for i in range(1,n-1,2):
        x = a + h* i
        soma_impar = soma_impar + f(x)
    simp = (h/3)*(f(a) + 4 * soma_impar + 2 * soma_par + f(b))
    return simp

def f(x):
    y = 2.7 ** x
    return y