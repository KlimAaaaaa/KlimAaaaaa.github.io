# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 19:36:36 2025

@author: Анна
"""


def calculate4():
    genomMaxName = " "
    maxProcent = 0
    
    for i in range(3):
        name = input("Введите имя:")
        genom = input("Введите строку:")
        nucleotids = {'G', 'C'}  # Множество символов для сравнения
        n = 0
        for char in genom:
            if char in nucleotids:
                n = n+1
        
        b = len(genom)
        procent = n/b*100  
        print(procent)    
        if procent > maxProcent:
            maxProcent = procent
            maxGenom = genom
            genomMaxName = name
    print(genomMaxName)
    print(maxProcent)
    
calculate4()







        
