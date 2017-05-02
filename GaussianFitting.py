#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:17:45 2017

@author: hannahkaplan
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Inputs
Data = np.load('/Users/hannahkaplan/Desktop/GR_ContRem.npy')
Wavelengths = [3.31, 3.38, 3.42, 3.46, 3.50]
maxWidth = 0.03
maxShift = 0.001

#Define the data columns
xdata = Data[:,0]
ydata = Data[:,1]

#Define parameters
a0 = []
Amplitudes = np.repeat(-0.5, len(Wavelengths))
Widths = maxWidth*np.repeat(1, len(Wavelengths)) 
a0 = np.concatenate((Wavelengths,Amplitudes,Widths),axis = 0)

#define constraints
lb = np.concatenate((np.subtract(Wavelengths,maxShift), -1*np.repeat(1,len(Wavelengths)), np.repeat(0,len(Wavelengths))))
ub = np.concatenate((np.add(Wavelengths,maxShift), np.repeat(0,len(Wavelengths)), maxWidth*np.repeat(1,len(Wavelengths))))
const = (lb,ub)

#define functions
def GaussianFunction(x,*a):
    
    g_add = 1
    a = np.array(a)
    a = a.flatten()
    a = np.reshape(a, (3, len(a)//3))
    for i in range(0,np.shape(a)[1]):
        #add the Gaussian equations
        g = a[1,i]*np.exp(-np.power((x-a[0,i]),2)/(2*np.power(a[2,i],2)))
        g_add = g_add + g
    #return array to original shape unneccessary?
    a = a.flatten()
    return(g_add)


#Fit the data using curve fit  
func = GaussianFunction      
popt,pcov = curve_fit(func, xdata, ydata, a0, bounds = const)

#return array to original shape unneccessary?
popt = popt.flatten()

#Plot the results
plt.plot(xdata,ydata,'k-',lw=2)
plt.plot(xdata,GaussianFunction(xdata,popt),'b-',lw=1)
plt.show()