#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 18:17:40 2022

@author: davideteixeira
"""

def trapezios(a,b,n):
    h = (b-a)/n
    soma = 0
    for i in range(1,n-1):
        x = a + i * h
        soma = soma + f(x)
    
    trap = (h/2)*(f(a)+2*soma+f(b))
    return trap

def f(x):
    y = x
    return y