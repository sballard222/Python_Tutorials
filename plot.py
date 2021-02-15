# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:59:52 2019

@author: sballard
"""

import sys
#import adore
#import pdb
#from mayavi import mlab
import pylab as pl
from scipy import interpolate
#from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

#import hdf5storage
#mat = hdf5storage.loadmat('mmat2.mat')


import h5py
#with h5py.File('mmat2.mat', 'r') as f:
#   print(list (f.keys()))
   
with h5py.File('mmat2.mat', 'r') as f:
    mmat2 = list(f['mmat2'])
    
with h5py.File('roughnessz0.mat', 'r') as f:
    roughnessz0 = list(f['roughnessz0'])   
#    import h5py
#with h5py.File('test.mat', 'r') as file:
#    print(list(file.keys()))
#import h5py 
#f = h5py.File("C:\Users\sballard\OneDrive - University of Miami\Desktop\mmat2.mat",'r') 
#data = f.get('mmat2') 
#data = np.array(data)

#mmat = sio.loadmat('mmat2.mat')

plt.plot(mmat2,roughnessz0)
plt.ylim(0, 2e-3) 
plt.gca().invert_xaxis()
plt.ylabel('$z_{0}$  [m]')
plt.xlabel('Longitudinal Distance away from Tower ESS')

plt.title('SAR-derived Surface Roughness Length $z_{0}$ extract  Tower ESS')
