#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:08:26 2022

@author: davideteixeira
"""

class complexo:
    
    def __init__(self, re=0, im=0):
        self.real = float(re)
        self.imag = float(im)
    
    @classmethod
    def from_string(cls, string):
        a = string.split('+')
        b = string.split('-')
        if (len(a) == 2) and (a != string):
            argre = float(a[0].strip())
            if a[1].strip() == 'i':
                argim = 1
            else:
                argim = float(a[1][0:len(a[1])-1].strip())
        elif (len(b) == 2) and (b != string) and (b[0] != ''):
            argre = float(b[0].strip())
            if b[1].strip() == 'i':
                argim = -1
            else:
                argim = float('-' + b[1][0:len(b[1])-1].strip())
        elif (len(b) == 3) and (b != string):
            argre = float('-' + b[1].strip())
            if b[2].strip() == 'i':
                argim = -1
            else:
                argim = float('-' + b[2][0:len(b[2])-1].strip())
        else:
            if string[len(string)-1] == 'i':
                argre = 0
                if string == 'i':
                    argim = 1
                elif string == '-i':
                    argim = -1
                else:
                    argim = float(string[0:(len(string))-1])
            else:
                argim = 0
                argre = float(string)
        return cls(argre, argim)

    def __add__(self, numero2):
        somareal = numero2.real + self.real
        somaimag = numero2.imag + self.imag
        return complexo(somareal, somaimag)
    
    def __sub__(self, numero2):
        subreal = self.real - numero2.real
        subimag = self.imag - numero2.imag
        return complexo(subreal, subimag)
    
    def __mul__(self, numero2):
        multre = (self.real * numero2.real) - (self.imag * numero2.imag)
        multimag = (self.real * numero2.imag) + (self.imag * numero2.real)
        return complexo(multre, multimag)
    
    def  __truediv__(self, numero2):
        den = numero2.real**2 + numero2.imag**2
        divre = (self.real * numero2.real + self.imag * numero2.imag)/den
        divimag = (self.imag * numero2.real - self.real * numero2.imag)/den
        return complexo(divre, divimag)
    
    def __str__(self):
        if self.imag > 0 and self.real !=0:
            n = f'{self.real}+{self.imag}i'
        elif self.imag > 0 and self.real ==0:
            n = f'{self.imag}i'
        elif self.imag == 0:
            n = f'{self.real}'
        elif self.imag < 0 and self.real != 0:
            n = f'{self.real}{self.imag}i'
        else:
            n = f'{self.imag}i'
        return n