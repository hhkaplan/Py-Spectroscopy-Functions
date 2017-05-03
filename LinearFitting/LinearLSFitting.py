#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:03:26 2017

@author: hannahkaplan
"""

import numpy as np
import scipy.optimize.lsq_linear as ls

#Function inputs
Endmembers = np.loadtxt('/Users/hannahkaplan/Documents/Py-Spectroscopy-Functions/LinearFitting/EndmemberSSA.csv', skiprows = 1,comments="#", delimiter=",", unpack=False)
Endmembers = np.array(Endmembers)
Data = np.loadtxt('/Users/hannahkaplan/Documents/Py-Spectroscopy-Functions/LinearFitting/GrSSA.csv', skiprows = 1,comments="#", delimiter=",", unpack=False)
Data = np.array(Data)
addToOne = True
Weights = None

#Seperate out the input data columns
End_wav = Endmembers[:,0]
End_spec = Endmembers[:,1:]
Orig_wav = Data[:,0]
Orig_spec = Data[:,1:]

#Throw a warning if the wavelengths of endmembers and spectra to be fit do
#not match
if not np.array_equal(End_wav, Orig_wav):
    print('Wavelengths of the datasets are not equal')
    
# Default of weights = evenly weighted at all wavelengths
if Weights == None:
    Weights = np.repeat(1,len(Data[:,0]))

# Set bounds on endmembers
EndMin = np.repeat(0, len(End_spec[0,:]))
EndMax = np.repeat(float('inf'), len(End_spec[0,:]))

#Loop through data and fit
Orig = Orig_spec[:,0]

if addToOne:
    
else:
    res = ls(End_spec, Orig, bounds)
