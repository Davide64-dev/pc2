#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:28:43 2022

@author: davideteixeira
"""

import statistics as st
import math

class Estatistica:

    def __init__(self, lista=None):
        if lista == None:
            self._lista=[]
        else:
            self._lista = lista.copy()
 
    @classmethod
    def from_string(cls, lista_str):
        lista = list(map(float,lista_str.strip().split(',')))
        return cls(lista)
    
    @property
    def lista(self):
        return self._lista

    @property
    def count(self):
        return len(self.lista)
    
    @property
    def mean(self):
        soma=0
        for i in self.lista:
            soma +=i
        return soma/self.count
    
    # std 
    @property
    def std(self):
        somadif =0
        mean = self.mean
        for i in self.lista:
            somadif +=(i-mean)**2
        return math.sqrt(somadif/(self.count-1))
        
    def add(self, value):
        self.lista.append(float(value))

    # Implements the evaluation of self[key]
    def __getitem__(self, key):
        return self.lista[key]

    def remove(self, value):
        self.lista.remove(value)
    
    def correlation(self, other):
        if self.count != other.count:
            return None
        mean = self.mean
        other_mean = other.mean
        num=0
        den1=0
        den2=0
        for i in range(self.count):
            num += (self.lista[i]-mean)*(other[i]-other_mean)
            den1 += (self.lista[i]-mean)**2
            den2 += (other[i]-other_mean)**2
        return num/(math.sqrt(den1) * math.sqrt(den2))
    
    def __str__(self):
        lista_str = ','.join(list(map(str,self.lista)))
        return lista_str