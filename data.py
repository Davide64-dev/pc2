#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:56:28 2022

@author: davideteixeira
"""
import datetime as dt
import calendar

class Data:
    
    def __init__(self, dia, mes):
        l = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        self._dia = int(dia)
        if mes in l:
            self._mes = int(l.index(mes) + 1)
        else:
            self._mes = int(mes)
    
    def mesextenso(self):
        l = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        k = l[self._mes-1]
        return k
    
    def semana(self):
        dias = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
        today = dt.date.today()
        year = today.year
        temp = calendar.weekday(year, self._mes, self._dia)
        dia = dias[temp]
        return dia
    
    def __str__(self):
        today = dt.date.today()
        year = today.year
        return f'\n{self.semana()}, {self._dia} de {self.mesextenso()} de {year}'