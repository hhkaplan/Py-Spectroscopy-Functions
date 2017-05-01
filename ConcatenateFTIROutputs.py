#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:08:43 2017

@author: hannahkaplan
"""
import glob
import numpy as np

#directory = '/Users/hannahkaplan/Desktop/GR2_FTIR/'

def ConcatenateFTIROutputs(directory):

    #Define the file type and where data will be stored
    ndir = directory + '*.CSV'
    newData = []
    
    #Import files
    files = glob.glob(ndir)
    
    #Run through each file and import the wavelength/reflectance data
    for i, file in enumerate(files):
        if i == 0:  
            lines = np.loadtxt(file, comments="#", delimiter=",", unpack=False)
            newData.append(lines[:,0])
            newData.append(lines[:,1])
        else:
            lines = np.loadtxt(file, comments="#", delimiter=",", unpack=False)
            newData.append(lines[:,1])
    
    #Convert from list to array          
    newData = np.array(newData)
    newData = np.transpose(newData)
    
    #Convert to appropriate wavelength/reflectance scales
    newData[:,1:-1] = newData[:,1:-1]/100
    newData[:,0] = 10000/newData[:,0]
    
    #Sort data and return
    n = newData[newData[:,0].argsort(),:]
    return(n)