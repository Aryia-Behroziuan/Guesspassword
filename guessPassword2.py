# -*- coding: utf-8 -*-
"""
Created on Wed May  1 00:57:18 2019

@author: Faradars-pc2
"""

import datetime
import genetic

def test_Hello_World():
    target = "Hello World!"
    guess_password(target)
    
def guess_password(target):
    geneset =" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()
    
    def fnGetFitness(genes):
        return get_fitness(genes, target)
    
    def fnDisplay(genes):
        display(genes, target, startTime)
        
    optimalFitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimalFitness, geneset, fnDisplay)
    
def display(genes, target, startTime):
    timeD = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target) 
    print("{0}\t{1}\t{2}".format(genes, fitness, str(timeD)))  
    
def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
               if expected == actual)    
    
    
    
    
    
    
    
    
    
    
    
    
    

    