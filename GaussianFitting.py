#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:17:45 2017

@author: hannahkaplan
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import erf

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

def LorentzianFunction(x,*a):
    
    l_add = 1
    a = np.array(a)
    a = a.flatten()
    a = np.reshape(a, (3, len(a)//3))   
       
    for i in range(0,np.shape(a)[1]):
        #add the Lorentzian equations
        l =a[1,i]*(np.power(a[2,i],2)/(np.power((x-a[0,i]),2)+np.power(a[2,i],2)))
        l_add = l_add + l
    #return array to original shape unneccessary?
    a = a.flatten()
    return(l_add)
    
def SkewGaussFunction(x,*a):
    
    SG_add = 1
    a = np.array(a)
    a = a.flatten()
    a = np.reshape(a, (4, len(a)//4))   
       
    for i in range(0,np.shape(a)[1]):
        #add the Lorentzian equations
        pdf_g = a[1, i]*np.exp(-np.power((x-a[0,i]),2)/(2*np.power(a[2,i],2)))
        cdf_g = 0.5*(1+erf(a[3,i]*(x-a[0,i])/(np.sqrt(2)*a[2,i])))
        skew_pdf_g = 2*pdf_g*cdf_g
        SG_add = SG_add + skew_pdf_g
    #return array to original shape unneccessary?
    a = a.flatten()
    return(SG_add)

def PseudoVoigtFunction(x,*a):
    
    PV_add = 1
    a = np.array(a)
    a = a.flatten()
    a = np.reshape(a, (4, len(a)//4))   
       
    for i in range(0,np.shape(a)[1]):
        #add the Lorentzian equations
        Lorentz = a[1,i]*(np.power(a[2,i],2)/(np.power((x-a[0,i]),2)+np.power(a[2,i],2)))
        Gauss = a[1,i]*np.exp(-np.power((x-a[0,i]),2)/(2*np.power((a[2,i]/2.355),2)))
        PV = (1-a[3,i])*Gauss + a[3,i]*Lorentz
        PV_add = PV_add + PV
        
    #return array to original shape unneccessary?
    a = a.flatten()
    return(PV_add)


#Inputs
def FittingFunction(Data, Wavelengths, Func, maxWidth = 0.03, maxShift = 0.001):
#Data = np.load('/Users/hannahkaplan/Desktop/GR_ContRem.npy')
#Wavelengths = [3.31,3.35, 3.38, 3.42, 3.46, 3.50]
#maxWidth = 0.03
#maxShift = 0.001
#func = LorentzianFunction 

    #Define the data columns
    xdata = Data[:,0]
    results = dict()
    
    #Define parameters
    a0 = []
    Amplitudes = np.repeat(-0.5, len(Wavelengths))
    Widths = maxWidth*np.repeat(1, len(Wavelengths))
    Ns = np.repeat(0.5, len(Wavelengths)) 
    
    if func == GaussianFunction or func == LorentzianFunction:
        a0 = np.concatenate((Wavelengths,Amplitudes,Widths),axis = 0)
    
        #define constraints
        lb = np.concatenate((np.subtract(Wavelengths,maxShift), -1*np.repeat(1,len(Wavelengths)), np.repeat(0,len(Wavelengths))))
        ub = np.concatenate((np.add(Wavelengths,maxShift), np.repeat(0,len(Wavelengths)), maxWidth*np.repeat(1,len(Wavelengths))))
        const = (lb,ub)
        
    elif func == SkewGaussFunction or func == PseudoVoigtFunction:
        a0 = np.concatenate((Wavelengths,Amplitudes,Widths, Ns),axis = 0)
    
        #define constraints
        lb = np.concatenate((np.subtract(Wavelengths,maxShift), -1*np.repeat(1,len(Wavelengths)), np.repeat(0,len(Wavelengths)),np.repeat(0,len(Wavelengths))))
        ub = np.concatenate((np.add(Wavelengths,maxShift), np.repeat(0,len(Wavelengths)), maxWidth*np.repeat(1,len(Wavelengths)), np.repeat(1,len(Wavelengths))))
        const = (lb,ub)
    
    else:
        print("Undefined Function")
    
    for col in range(1,np.shape(Data)[1]):
        
        ydata = Data[:,col]
        
        #Fit the data using curve fit       
        popt,pcov = curve_fit(func, xdata, ydata, a0, bounds = const)
        
        #return array to original shape unneccessary?
        popt = popt.flatten()
        results[col] = [popt]
        
    
        #Plot the results
        fig = plt.figure()
        plt.plot(xdata,ydata,'k-',lw=2)
        plt.plot(xdata,func(xdata,popt),'b-',lw=1)
        plt.plot(xdata,func(xdata,popt),'b-',lw=1)
        #Do a bunch of extra work to get individual gaussians plotted
        if func == GaussianFunction or func == LorentzianFunction:
            popts = np.reshape(popt, (3, len(popt)//3))
        else:
            popts = np.reshape(popt, (4, len(popt)//4))
        for i in range(0,np.shape(popts)[1]):
            plt.plot(xdata,func(xdata,popts[:,i]), lw= 0.5)
        plt.show()