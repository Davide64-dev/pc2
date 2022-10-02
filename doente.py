#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 09:05:39 2022

@author: davideteixeira
"""
import datetime as dt

class Doente:
    
    def __init__(self, codigo, nome, data):
        self._codigo = codigo
        self._nome = nome
        self._data = dt.datetime(int(data[0:4]),int(data[5:7]), int(data[8:10]))
        self.consultas = dict()
        
    def marcar(self, data, hora, especialidade):
        today = dt.date.today()
        marcacao = dt.datetime(int(data[0:4]), int(data[5:7]), int(data[8:10]), int(hora[0:2]), int(hora[3:6]))
        if (marcacao.year, marcacao.month, marcacao.day) > (today.year, today.month, today.day):
            self.consultas[marcacao] = especialidade
        else:
            print('Por favor, uma data válida')
    
    def desmarcar(self, data, hora):
        today = dt.date.today()
        marcacao = dt.datetime(int(data[0:4]), int(data[5:7]), int(data[8:10]), int(hora[0:2]), int(hora[3:6]))
        if marcacao in self.consultas.keys() and (marcacao.year, marcacao.month, marcacao.day) > (today.year, today.month, today.day):
            self.consultas.pop(marcacao)
        else:
            print ('A consulta não se encontra marcada no registo ou já foi realizada')
    
    def listar(self):
        a = list(self.consultas.keys())
        b = a.copy()
        b.sort()
        indices = []
        lista = []
        for i in range (len(b)):
            k = b[i]
            indices.append(a.index(k))
        for i in range(len(self.consultas)):
            dataehora = a[indices[i]]
            especialidade = self.consultas[dataehora]
            dia = str(dataehora.day)
            mes = str(dataehora.month)
            ano = str(dataehora.year)
            hora = str(dataehora.hour)
            minuto = str(dataehora.minute)
            string = f'{dia}-{mes}-{ano}, {hora}:{minuto}, {especialidade}'
            lista.append(string)
        return lista
    
    def __str__(self):
        return f'\nCódigo: {self._codigo}\nNome: {self._nome}\n'