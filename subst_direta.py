#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 18:21:23 2022

@author: davideteixeira
"""
import math

def subst_direta(x0, tol, maxiter):
    k = 0
    erro = tol + 1
    while k < maxiter and erro > tol:
        k = k + 1
        x = f(x0)
        erro = abs(x-x0)
        x0 = x
    return x, erro

def f(x):
    y = math.cos(x)
    return y
