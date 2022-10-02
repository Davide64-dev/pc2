#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 08:33:01 2022

@author: davideteixeira
"""
from tarefa import Tarefa
from atividade import Atividade

class TarefaDependente(Tarefa):
    
    def __init__ (self, identificador, nomedatarefa):
        super().__init__(identificador, nomedatarefa)
        self.tarefas = []
    
    @property
    def taredas(self):
        return self.tarefas
    
    def adicionar (self, atividade, tarefa):
        self.atividades.append(atividade)
        self.tarefas.append(tarefa)
    
    def eliminar (self, atividade):
        for i in range(len(self.tarefas)):
            tarefa = self.tarefa[i]
            if atividade in tarefa.atividades:
                tarefa.atividades.remove(atividade)
            else:
                continue
    
    def terminar(self):
        for k in self.tarefas:
            temp = k._estado
            j = 'Terminado'
            if temp == 'Terminado':
                continue
            elif temp == 'Ativo':
                j = 'Ativo'
                break
        if temp == 'Terminado':
            self._estado = j