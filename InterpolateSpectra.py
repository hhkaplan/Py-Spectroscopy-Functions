#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:41:21 2017

@author: hannahkaplan
"""

import numpy as np
import matplotlib.pyplot as plt

#Wavelengths = np.linspace(1, 18, 300)
#Data = np.load('/Users/hannahkaplan/Desktop/GR.npy')

def InterpolateSpectra(Wavelengths, Data):
    
    #Name data columns and allocate space
    Wavin = Data[:,0]
    Wavout = Wavelengths
    Datout = np.empty((np.shape(Wavelengths)[0],np.shape(Data)[1]))
    Datout[:,0] = Wavelengths
    
    #Output a warning
    if Wavout[0] < Wavin[0] or Wavout[-1] > Wavin[-1]:
        print("Warning: Extrapolation is occuring")
    
    #Loop through columns of data
    for col in range(1,np.shape(Data)[1]): #this is "not pythonic" but whatever...
    
        #Interpolate
        Datin = Data[:,col]
        Datout[:,col] = np.interp(Wavout, Wavin, Datin)
    
   
    #Plot
    fig1 = plt.figure()
    plt.plot(Wavin, Datin, 'b-', lw = 2)
    plt.plot(Wavout, Datout[:,col], 'ro')
    plt.plot(Wavout, Datout[:,col], 'r-', lw = 0.5)
    #plt.show()
    
    return(Datout)
    return(fig1)