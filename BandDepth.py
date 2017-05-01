#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 11:32:27 2017

@author: hannahkaplan
"""

import numpy as np

def BandDepth(Data):
    
    BD = 1-Data[:,1:]
    BD = np.column_stack((Data[:,0], BD))
    
    return(BD)