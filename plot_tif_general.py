# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:57:56 2019

@author: sballard
"""
import sys
import adore
import pdb
#from mayavi import mlab
import pylab as pl
from scipy import interpolate
from mpl_toolkits.basemap import Basemap
import numpy 
#from mayavi import mlab
import pylab as pl
import scipy.io
from scipy.io import netcdf
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import datetime 


file_name = 'ascat_20140331_031200_metopa_38635_eps_o_250_2300_ovw.l2.nc.gz.nc'
f = Dataset(file_name, mode='r')

time_ascat = f.variables['time'][:]
lat_ascat = f.variables['lat'][:]
lon_ascat = f.variables['lon'][:]-360
speed_ascat = f.variables['wind_speed'][:]
direction_ascat = f.variables['wind_dir'][:]

lon = scipy.io.loadmat('lon_HRHL.mat')
lat= scipy.io.loadmat('lat_HRHL.mat')
hei = scipy.io.loadmat('image_HRHL.mat')

lon = lon['lon']
lat = lat['lat']
hei = hei['image']


  d0,d1=numpy.meshgrid(numpy.linspace(lat.min(),lat.max(), lon.shape[1]), 
    numpy.linspace(lon.min(), lon.max(), lon.shape[0]))  
  if lat[0,0] > 0: #northern hemisphere
    if d1[0,0]<d1[-1,0]:
      d1=numpy.flipud(d1)
  
  hei_gridded = interpolate.griddata((lon.ravel(),lat.ravel()), hei.ravel(), (d1, d0), method='linear')
  
  #set-up basemap
  print ('Please wait... Generating map\n')
  m = Basemap(llcrnrlon=d0.min(), llcrnrlat=d1.min(), urcrnrlon=d0.max(), urcrnrlat=d1.max(), 
    resolution='f', area_thresh=1., projection='cyl')
  if 'complex' in ires[product]['Data_output_format']:#any(numpy.iscomplex(hei_gridded)):
    if mode=='p':
      m.imshow(numpy.angle(hei_gridded), interpolation='nearest', origin='upper')
    else:
      m.imshow(10*numpy.log10(abs(hei_gridded)), interpolation='nearest', origin='upper')
      pl.gray();
  else:
    m.imshow(hei_gridded, interpolation='nearest', origin='upper')
  m.drawcoastlines(color='w',linewidth=0.8)
  m.drawmapboundary() # draw a line around the map region
  m.drawrivers() 
  m.drawparallels(numpy.arange(int(d1.min()), int(d1.max()), 1),linewidth=0.2,labels=[1,0,0,0])  
  m.drawmeridians(numpy.arange(int(d0.min()), int(d0.max()), 1),linewidth=0.2,labels=[0,0,0,1])  