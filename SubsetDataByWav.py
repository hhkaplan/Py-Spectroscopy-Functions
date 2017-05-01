#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 10:45:24 2017

@author: hannahkaplan
"""
import numpy as np

def SubsetDataByWav(Data, wav1, wav2):
    
    #Define wavelength column
    Wavelengths = Data[:,0]
    i_short = np.where(Wavelengths >= wav1)[0][0]
    i_long = np.where(Wavelengths >= wav2)[0][0]
    
    #Subset data
    Data = Data[i_short:i_long, :]
    return(Data)