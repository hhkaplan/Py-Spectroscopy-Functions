#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:54:39 2017

@author: hannahkaplan
"""

import numpy as np
import peakutils
import matplotlib.pyplot as plt

#Data = x
#minHeight = 0.01
#minDistance = 10

def PeakDetection(Data,minHeight,minDistance):
    
    results = dict()
    #Loop through all spectra
    for col in range(1, np.shape(Data)[1]):
        
        #Find minima instead of maxima
        BD = 1 - Data[:,col]
        
        #Requires peakutils (from https://bitbucket.org/lucashnegri/peakutils)
        indexes = peakutils.indexes(BD, thres=minHeight, min_dist=minDistance)
        
        #Return the results in a dictionary
        name = "Sample"+str(col)
        results[name] = [Data[indexes,0],Data[indexes,col]]
        
        
        #Plot results
        fig1 = plt.figure()
        plt.plot(Data[:,0], Data[:,col],'k-')
        plt.plot(Data[indexes,0], Data[indexes,col],'ro')
        #plt.show()
    
    return(fig1)
    return(results)