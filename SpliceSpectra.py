#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 13:25:45 2017

@author: hannahkaplan
"""
import numpy as np
import matplotlib.pyplot as plt

short_data = 4
long_data = 10
splice_wav = 1.7

#Find the index of the splice-wavelength in both datasets
i_short = np.where(short_data[:,0] >= splice_wav)[0]
i_long = np.where(long_data[:,0] <= splice_wav)[0]

#Trim the short and long data at the index
short_data = short_data[0:i_short,:]
long_data = long_data[i_long:-1,:]

#Find scale factors in order to scale the long data to the short datas
scale_factor = np.divide(short_data[-1,1:-1],long_data[0,1:-1])
scale_factor_n = np.repeat(scale_factor, np.shape(long_data)[0])

#Scale the long data
long_data_scaled = np.multiply(long_data[:,1:-1], scale_factor_n)
long_data_scaled = np.column_stack(long_data[:,0], long_data_scaled)

#Merge the short and scaled data into a single matrix
spliced_spectra = np.vstack(short_data, long_data_scaled)

#Plot results
plt.plot(spliced_spectra[:,0], spliced_spectra[:,1],'k-',lw=2)
plt.plot(short_data[:,0], short_data[:,1],'b-',lw=1)
plt.plot(long_data[:,0], long_data[:,1],'r-',lw=1)
plt.show()