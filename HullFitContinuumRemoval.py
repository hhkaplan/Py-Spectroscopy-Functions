#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:26:30 2017

@author: hannahkaplan
"""

import numpy as np
import scipy.spatial as sp
import matplotlib.pyplot as plt
##Inputs
#Data = np.load('/Users/hannahkaplan/Desktop/GR.npy')
#lwav = 2
#rwav = 4

def HullFitContinuumRemoval(Data, lwav, rwav):

    #Find indeces of wavelengths to be used in continuum removal and subset data
    i1 = np.where(Data[:,0] >= lwav)[0]
    i2 = np.where(Data[:,0] >= rwav)[0]
    if i1.size == 0 or i2.size == 0:
        print("Error")
        
    Data_sub = Data[i1[0]:i2[0],:]
    
    
    #Initialize matrices with size of data, and first column of wavelengths
    Cont_Fit = np.empty(np.shape(Data_sub))
    Cont_Fit[:,0] = Data_sub[:,0]
    Cont_Rem = np.empty(np.shape(Data_sub))
    Cont_Rem[:,0] = Data_sub[:,0]
    
    #iterate through all spectra
    for col in range(1,np.shape(Data)[1]): #this is "not pythonic" but whatever...
    
        #Compute convex hull
        new_spec = np.column_stack((Data_sub[:,0], Data_sub[:,col]))
        hull = sp.ConvexHull(new_spec)
        
        #Find only the upper hull
        zeroind = np.where(hull.vertices == 0) #find where the shortest wavelength position is within the convex hull
        upperhull = np.less(np.diff(hull.vertices), 0)
        upperhull = np.insert(upperhull, zeroind[0][0], 'true') #make sure the first point is included
        upperhull_pts = new_spec[hull.vertices[upperhull],:]
        upperhull_pts = upperhull_pts[upperhull_pts[:,0].argsort(),:] #sort data in ascending order
        
        #Linear nterpolate to all wavelengths
        Cont_Fit[:,col] = np.interp(new_spec[:,0], upperhull_pts[:,0], upperhull_pts[:,1])
        
        #Remove the continuum
        Cont_Rem[:,col] = np.divide(new_spec[:,1], Cont_Fit[:,col])
        
        #Plot the results
        fig1 = plt.figure()
        plt.plot(new_spec[:,0], new_spec[:,1], 'b-', lw=1)
        plt.plot(upperhull_pts[:,0], upperhull_pts[:,1], 'ro')
        plt.plot(new_spec[:,0], Cont_Fit[:,col], 'r-',lw =1)
        plt.title("Sample "+ str(col))
        #plt.show()
        
        fig2 = plt.figure()
        plt.plot(Cont_Rem[:,col], 'b-',lw =1)
        plt.title("Sample "+ str(col))
    
    #returns   
    return(Cont_Fit, Cont_Rem)
    return(fig1)
    return(fig2)