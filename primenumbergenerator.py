#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 20:57:58 2022

@author: stephencranney
"""

def pngen(startingnumber, endingnumber):
    numberprimes=0
    for i in range(startingnumber, endingnumber+1):
        dividecases=0
        for x in range(1, endingnumber+1):
            if i%x==0 and x!=1 and x!=i:
                dividecases+=1
        if dividecases==0 and i!=1:
            numberprimes+=1
    print("there are",numberprimes,"primes in between", startingnumber,"and",endingnumber)
    

    




            
            
            
            
            
            
            
                
    
