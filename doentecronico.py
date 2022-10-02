#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 11:33:18 2022

@author: davideteixeira
"""
from doente import Doente
import datetime as dt

class Doentecronico (Doente):
    
    def __init__(self, codigo, nome, data, diasintervalo, especialidadecronica):
        super().__init__(codigo, nome, data)
        self.diasintervalo = int(diasintervalo)
        self.especialidadecronica = especialidadecronica
        self.consultas = dict()
        self.cronicas = []
    
    def gerar(self, data, n):
        data = dt.datetime(int(data[0:4]),int(data[5:7]), int(data[8:10]))
        soma = dt.timedelta(days=+n)
        datafinal = data + soma
        while(data.year, data.month, data.day) < (datafinal.year, datafinal.month, datafinal.day):
            temp = int(self.diasintervalo/2)
            temp3 = temp - 1
            tempo = dt.timedelta(days=-temp3)
            datamenos = data + tempo
            datasimpossiveis = []
            k = dt.timedelta(days=+1)
            
            for i in range(2*temp+1):
                datasimpossiveis.append(datamenos)
                datamenos = datamenos + k
            
            for consulta in self.cronicas:
                if consulta in datasimpossiveis:
                    logico = True
                    break
            else:
                logico = False
            
            if logico == True:
                pass
            else:
                self.cronicas.append(data)
            k = dt.timedelta(days =+ self.diasintervalo)
            data = data + k
    
    def listar(self, parametro):
        if parametro == 0:
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
        
        elif parametro == 1:
            lista = [self.especialidadecronica]
            k = self.cronicas
            k.sort()
            for consulta in k:
                dia = str(consulta.day)
                mes = str(consulta.month)
                ano = str(consulta.year)
                string = f'{dia}-{mes}-{ano}'
                lista.append(string)
        return lista
    
    def __str__(self):
        return f'\nCódigo: {self._codigo}\nNome: {self._nome}\nEspecialidade da Doença Crónica: {self.especialidadecronica}\n'