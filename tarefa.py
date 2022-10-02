#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:23:20 2022

@author: davideteixeira
"""
class Tarefa:
    
    def __init__(self, identificador, nomedatarefa):
        self._identificador = int(identificador)
        self._nomedatarefa = str(nomedatarefa)
        self._estado = 'Ativo'
        self.atividades = []
    
    @property
    def estado(self):
        return self._estado
    
    def adicionar(self, atividade):
        self.atividades.append(atividade)
    
    def eliminar(self, atividade):
        if atividade in self.atividades:
            self.atividades.remove(atividade)
        else:
            print('Não é possível realizar')
    
    def tempototal(self):
        soma = 0
        for i in range (len(self.atividades)):
            temp = int(self.atividades[i]._duracao)
            soma += temp
        return soma
    
    def terminar(self):
        self._estado = 'Terminado'
    
    def __str__(self):
        return f'\nNúmero Identificador: {self._identificador}\nNome da Tarefa: {self._nomedatarefa}\nEstado da Tarefa: {self._estado}\n'
