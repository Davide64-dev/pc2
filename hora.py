#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:30:02 2022

@author: davideteixeira
"""

class Hora:
    
    def __init__(self, horas, minutos, segundos):
        self._horas = horas
        self._minutos = minutos
        self._segundos = segundos
    
    def nsegundos(self):
        nsegundos = self._segundos
        nsegundos += self._minutos * 60
        nsegundos += self._horas * 3600
        return nsegundos
    
    def adicionar(self, outro):
        horanova = self._horas + outro._horas
        minutonovo = self._minutos + outro._minutos
        segundonovo = self._segundos + outro._segundos
        if segundonovo >= 60:
            minutonovo +=1
            segundonovo -= 60
        else:
            pass
        if minutonovo >= 60:
            horanova += 1
            minutonovo -= 60
        else:
            pass
        return Hora(horanova, minutonovo, segundonovo)
    
    def __str__(self):
        return f'\n{self._horas}:{self._minutos}:{self._segundos}\n'