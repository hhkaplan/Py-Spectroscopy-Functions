#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 11:37:07 2017

@author: hannahkaplan
"""
import numpy as np

def AbsorptionArea(Data):
    
    BD = 1-Data[:,1:]
    AUC_all = []
    #Find area using trapz 
    for col in range(0, np.shape(BD)[1]):
        AUC = np.trapz(BD[:,col], x = Data[:,0])
        AUC_all.append(AUC)
    
    return(AUC_all)