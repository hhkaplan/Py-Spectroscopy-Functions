#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:03:26 2017

@author: hannahkaplan
"""

import numpy as np
import scipy.optimize as sc
import matplotlib.pyplot as plt

#Function inputs
#Endmembers = np.loadtxt('/Users/hannahkaplan/Documents/Py-Spectroscopy-Functions/LinearFitting/EndmemberSSA.csv', skiprows = 1,comments="#", delimiter=",", unpack=False)
#Endmembers = np.array(Endmembers)
#Data = np.loadtxt('/Users/hannahkaplan/Documents/Py-Spectroscopy-Functions/LinearFitting/GrSSA.csv', skiprows = 1,comments="#", delimiter=",", unpack=False)
#Data = np.array(Data)
#addToOne = False
#Weights = None
def LinearLSFitting(Data, Endmembers, addToOne = True, Weights = None):

    #Seperate out the input data columns
    End_wav = Endmembers[:,0]
    End_spec = Endmembers[:,1:]
    Orig_wav = Data[:,0]
    Orig_spec = Data[:,1:]
    results = dict()
    
    #Throw a warning if the wavelengths of endmembers and spectra to be fit do
    #not match
    if not np.array_equal(End_wav, Orig_wav):
        print('Wavelengths of the datasets are not equal')
        
    # Default of weights = evenly weighted at all wavelengths
    if Weights == None:
        Weights = np.repeat(1,len(Data[:,0]))
    
    #Set initial guess
    g0 = np.repeat(0.5, len(End_spec[0,:]))
    
    def G(x):
       'Function for linear least squares' 
       return(np.sum((np.power((np.dot((End_spec.T*Weights).T,x) - Orig*Weights),2))))
       
    
    # Set inequality equation
    def ec(x):
        'fractions sum to one'
        return 1 - np.sum(x)
    
    #Loop through data and fit
    for col in range(0, np.shape(Orig_spec)[1]):
    
        Orig = Orig_spec[:,col]
        
        #Solve the least squares equation using fmin_slsqp
        if addToOne:
            res = sc.fmin_slsqp(G,g0,bounds=[(0,1)]*len(g0))
        else:
            res = sc.fmin_slsqp(G,g0,eqcons=[ec], bounds=[(0,1)]*len(g0))
        
        results[col] = res
               
        #Plot results
        fig1 = plt.figure()
        plt.plot(Orig_wav, Orig, 'k-',lw = 1.5, label = "Measured")
        plt.plot(Orig_wav, np.dot(End_spec, res),'r-',lw=1, label = "Modeled")
        plt.legend()
        plt.show()
    
    return(fig1)
    return(results)