#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:35:33 2022

@author: davideteixeira
"""

def newton(x0, tol, maxiter):
    k = 0
    erro = tol + 1
    while k < maxiter and erro > tol:
        k = k + 1
        x = x0 - (f(x0) / flinha(x0))
        erro = abs(x-x0)
        x0 = x
    return (x,erro)

def f(x):
    y = x**2 - 2
    return y

def flinha(x):
    y = 2*x
    return y
