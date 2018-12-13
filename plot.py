# Import modules
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np

# Read in the netcdf file
cross = Dataset("/nfs/see-fs-02_users/eeaba/convection/homog_flux/homog_xz.nc", "r", format="NETCDF4")

# Pick out the variable to plot (e.g. vertical velocity)
w = cross.variables[('W')]

# Define the dimensions and resolution of the domain
xx = arange(0, 512) * 0.025
yy = arange(0, 512) * 0.025
xg, yg = np.meshgrid(xx, yy)

# Set up times and plot titles for plots
time=range(30) # my data is every minute and I wanted to plot the first 30 minutes
title_w=[]
for t in range(len(time)): 
    if t == 0:
        title_w.append(str(t+1)+' min')
    else:
         title_w.append(str(t+1)+' mins')

# Plot cross sections at each time frame using pcolor
for x, y in zip(time, title_w):

    plt.figure(figsize=(12,12))
    updraft = w[x,:,1,:]
    plt.pcolor(xg, yg, updraft, cmap='seismic')
    plt.colorbar(shrink=0.825)
    
    plt.title('Vertical velocity at '+y, fontsize=20)
    plt.xlabel('Distance (km)', fontsize=16)
    plt.ylabel('Distance (km)', fontsize=16)
    
    plt.tick_params(axis='both', labelsize=16)
    plt.xticks([0,6.4,12.8],['0','6.4','12.8'])
    plt.yticks([0,6.4,12.8],['0','6.4','12.8'])
    plt.axes().set_aspect('equal')
    plt.show()
