#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:17:45 2017

@author: hannahkaplan
"""

import numpy as np
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Inputs
Data = np.load('/Users/hannahkaplan/Desktop/GR_ContRem.npy')
Wavelengths = [3.31, 3.42, 3.50]
maxWidth = 0.03
maxShift = 0.001

#Define the data columns
xdata = Data[:,0]
ydata = Data[:,1]

#Define parameters
Amplitudes = np.repeat(-0.5, len(Wavelengths)) 
Widths = maxWidth*np.repeat(1, len(Wavelengths)) 
a0 = np.column_stack((Wavelengths, Amplitudes, Widths))


def GaussianFunction(x,a):
    g_add = 1
    for i in range(0,np.shape(a)[1]):
        #add the Gaussian equations
        g = a[i,1]*np.exp(-np.power((x-a[i,0]),2)/(2*np.power(a[i,2],2)))
        g_add = g_add + g
        return(g_add)
    
    
func = GaussianFunction    
popt, pcov = curve_fit(func, xdata, ydata, a0)