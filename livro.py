#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:18:48 2022

@author: davideteixeira
"""
import datetime as dt

class Livro:
    
    def __init__(self, titulo, autor, datapub, numex, prazo):
        self._titulo = titulo
        self._autor = autor
        self._datapub = datapub
        self._numex =  int(numex)
        self._prazo = int(prazo)
        self._requisicoes = dict()
    
    def requisitar(self, pessoa):
        if (self._numex >= 1):
            today = dt.date.today()
            self._requisicoes[pessoa] = today
            self._numex -= 1
        else:
            print('Não existem exemplares!')
    
    def devolver (self, pessoa):
        if pessoa in self._requisicoes.keys():      
            self._requisicoes.pop(pessoa)
            self._numex += 1
        else:
            print('O livro não foi requisitado!')
    
    def expirar(self, pessoa):
        if pessoa in self._requisicoes.keys():
            today = dt.date.today()
            requisicao = self._requisicoes[pessoa]
            dias = str(today - requisicao)
            temp = dias.split()
            k = temp[0]
            if k == '0:00:00':
                k = 0
            if k > self._prazo:
                return 'Prazo Excedido!'
            else:
                return 'Ainda há tempo!'
        else:
            return 'O livro não fo requisitado'

    def __str__(self):
        return f'\nTítulo: {self._titulo}\nAutor: {self._autor}\nData de Publicação: {self._datapub}\nNúmero de Exemplares Disponíveis: {self._numex}\nPrazo Limite de Entrega: {self._prazo}\n'