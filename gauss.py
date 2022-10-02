#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:10:29 2022

@author: davideteixeira
"""

def gauss(a,b):
    n = len(b)
    for k in range(0,n-1):
        temp = list()
        for i in range(k,n):
            temp.append(abs(a[i][k]))
        m = max(temp)
        p = temp.index(m)
        p = p + k
        if p != k:
            for j in range(k,n):
                aux = a[k][j]
                a[k][j] = a[p][j]
                a[p][j] = aux
            aux = b[k]
            b[k] = b[p]
            b[p] = aux
        for i in range(k+1, n):
            mult = a[i][k] / a[k][k]
            a[i][k] = 0
            for j in range(k+1, n):
                a[i][j] = a[i][j] - mult * a[k][j]
            b[i] = b[i] - mult*b[k]
    return a,b

def subst_inv(a,b):
    n = len(b)
    x = [0] * n
    x[n-1] = b[n-1] / a[n-1][n-1]
    for i in range(n-2,-1,-1):
        produto = 0
        for j in range(i, n):
            produto = produto + x[j] * a[i][j]
        x[i] = (b[i] - produto) / a[i][i]
    return x

def AXB(a,b):
    a,b = gauss(a,b)
    x = subst_inv(a,b)
    return x

def determinante(a):
    m = len(a)
    b = [0]* m
    a,b = gauss(a,b)
    produto = 1
    for i in range(m):
        produto = produto * a[i][i]
    return produto