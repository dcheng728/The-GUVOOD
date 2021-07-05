# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 03:35:43 2021

@author: dchen
"""

import numpy as np
import json
import matplotlib.pyplot as plt
import math
import numpy as np
import json
from meta_data import rotationMatrixToEulerAnglesXYZ,rotationMatrixToEulerAnglesXZY


#Loading a dictionary containing the labels, keys: [subject][item]
with open('labels.json','r',encoding='utf8')as fp:
    labels = json.load(fp)

#Loading a numpy array containing all the wrist transformations
transformations = np.load("transformations_array.npy")
right_trans = transformations[:10080].copy()
left_trans = transformations[10080:].copy()

#Loading the labels in numpy array format, this contains the same 
#informaiton as the dicitonary loaded from .json, but its order 
#matches that of the transformation array
labels_array = np.load("labels_array.npy")
right_lbls = labels_array[:10080].copy()
left_lbls = labels_array[10080:].copy()


#############Reading Data####################

#Keeping track of positional data
left_xs = []
left_ys = []
left_zs = []
left_phis = []
left_thetas = []
left_rs = []

right_xs = []
right_ys = []
right_zs = []
right_phis = []
right_thetas = []
right_rs = []

#Keeping track of rotational data
left_rxs = []
left_rys = []
left_rzs = []

right_rxs = []
right_rys = []
right_rzs = []
#Read the data for left dominant subjects
for n in range(len(left_trans)):
     
    
    t = left_trans[n]
    x = t[0,3]
    y = t[1,3]
    z = t[2,3]
    if (x != 0 and y != 0 and z !=0):
        left_xs.append(x)
        left_ys.append(y)
        left_zs.append(z)
        if (y > 0 and z > 0):
            phi = math.atan(z/y)
        elif (y > 0 and z < 0):
            phi = (2*math.pi + math.atan(z/y))-2*math.pi
        elif (y < 0 and z > 0):
            phi = math.pi + math.atan(z/y)
        else:
            phi = math.pi + math.atan(z/y) - 2*math.pi
        if(phi > 0 or phi < 0 or phi == 0):
            left_phis.append(phi*180/math.pi)
            theta = math.atan(x/math.sqrt(y*y+z*z))
            left_thetas.append(90-theta*180/math.pi)
            r = math.sqrt(x**2+y**2+z**2)
            left_rs.append(r)
             
    currMat = left_trans[n]
    rotation = left_trans[n,0:3,0:3]
    currMat = np.matmul(np.array([[1,0,0,0],[0,0,-1,0],[0,1,0,0],[0,0,0,1]]),currMat)
    rotation[0:3,0:3] = np.matmul(currMat[0:3,0:3],np.array([[1,0,0],[0,0,-1],[0,1,0]]))
    [rx,ry,rz] = rotationMatrixToEulerAnglesXZY(rotation)
    if (rx!=0 and ry!=0 and rz!= 0):
        left_rxs.append(rx*180/math.pi)
        left_rys.append(ry*180/math.pi)
        left_rzs.append(rz*180/math.pi)

left_phis = np.array(left_phis)
left_thetas = np.array(left_thetas)
left_rs = np.array(left_rs)

#Read the data for right dominant subjects
for n in range(len(right_trans)):
    t = right_trans[n]
    x = t[0,3]
    y = t[1,3]
    z = t[2,3]
    if (x != 0 and y != 0 and z !=0):
        right_xs.append(x)
        right_ys.append(y)
        right_zs.append(z)
        if (y > 0 and z > 0):
            phi = math.atan(z/y)
        elif (y > 0 and z < 0):
            phi = (2*math.pi + math.atan(z/y))-2*math.pi
        elif (y < 0 and z > 0):
            phi = math.pi + math.atan(z/y)
        else:
            phi = math.pi + math.atan(z/y) - 2*math.pi
        if(phi > 0 or phi < 0 or phi == 0):
            right_phis.append(phi*180/math.pi)
            theta = math.atan(x/math.sqrt(y*y+z*z))
            right_thetas.append(90-theta*180/math.pi)
            r = math.sqrt(x**2+y**2+z**2)
            right_rs.append(r)
             
    currMat = right_trans[n]
    rotation = right_trans[n,0:3,0:3]
    [rx,ry,rz] = rotationMatrixToEulerAnglesXYZ(rotation)
    if (rx!=0 and ry!=0 and rz!= 0):
        right_rxs.append(rx*180/math.pi)
        right_rys.append(ry*180/math.pi)
        right_rzs.append(rz*180/math.pi)

right_phis = np.array(right_phis)
right_thetas = np.array(right_thetas)
right_rs = np.array(right_rs)

###############Plotting#################

#Create subplots
fig,axes = plt.subplots(6,2,figsize=(11.5, 9.3))
plt.rcParams["font.family"] = "serif"

font = {'size'   : 13, 'weight' : 'bold'}

#Configure the subplots
axes[0,0].set_xlabel(r'$\phi$', **font)
axes[0,0].set_ylim(0,0.05)
axes[0,1].set_yticks([0,0.05])
axes[0,0].set_xlim(-180,180)
axes[0,0].set_xticks([-180,-120,-60,0,60,120,180])

axes[0,1].set_xlabel(r'$\phi$', **font)
axes[0,1].set_ylim(0,0.05)
axes[0,1].set_xlim(-180,180)
axes[0,1].set_yticks([0,0.05])
axes[0,1].set_xticks([-180,-120,-60,0,60,120,180])

axes[1,0].set_xlabel(r'$\theta$', **font)
axes[1,0].set_ylim(0,0.05)
axes[1,0].set_xlim(0,90)
axes[1,0].set_yticks([0,0.05])
axes[1,0].set_xticks([0,30,60,90])

axes[1,1].set_xlabel(r'$\theta$', **font)
axes[1,1].set_ylim(0,0.05)
axes[1,1].set_xlim(0,90)
axes[1,1].set_yticks([0,0.05])
axes[1,1].set_xticks([0,30,60,90])

axes[2,0].set_xlabel(r'$r$', **font)
axes[2,0].set_ylim(0,0.05)
axes[2,0].set_xlim(0,250)
axes[2,0].set_yticks([0,0.05])
axes[2,0].set_xticks([0,50,100,150,200,250])

axes[2,1].set_xlabel(r'$r$', **font)
axes[2,1].set_ylim(0,0.05)
axes[2,1].set_xlim(0,250)
axes[2,1].set_yticks([0,0.05])
axes[2,1].set_xticks([0,50,100,150,200,250])


titles = [r'$Rx$',r'$Rx$',r'$Rz$',r'$Ry$',r'$Ry$',r'$Rz$']
for n in range(6,12):
    row, col = divmod(n,2)
    axes[row,col].set_xlabel(titles[n-6], **font)
    axes[row,col].set_ylim(0,0.05)
    axes[row,col].set_xlim(-180,180)
    axes[row,col].set_yticks([0,0.05])
    axes[row,col].set_xticks([-180,-120,-60,0,60,120,180])


#Plotting the histograms along with normal PDF
def normFunc(std,mean,x):
    return (1/(std*(math.sqrt(2*math.pi))))*math.exp(-(x-mean)*(x-mean)/(2*std*std))

def plotNormPDF(axes,n,bins,data):
    xs = [(bins[n]+bins[n+1])/2 for n in range(0,len(bins)-1)]
    std = np.std(data)
    mean = np.mean(data)
    yfuncs = [normFunc(std,mean,xs[n]) for n in range(len(xs))]
    axes.plot(xs,yfuncs, color = (0.57,0.73,0.23),linewidth = 2)

n, bins, patches = axes[0,0].hist(left_phis, 180, density=True, facecolor=(0,0.5469,0.5469), alpha=1)
plotNormPDF(axes[0,0],n,bins,left_phis)

n, bins, patches = axes[0,1].hist(right_phis, 180, density=True, facecolor=(0.902,0.50196,0.10196), alpha=1)
plotNormPDF(axes[0,1],n,bins,right_phis)

n, bins, patches = axes[1,0].hist(left_thetas, 180, density=True, facecolor=(0,0.5469,0.5469), alpha=1)
plotNormPDF(axes[1,0],n,bins,left_thetas)

n, bins, patches = axes[1,1].hist(right_thetas, 180, density=True, facecolor=(0.902,0.50196,0.10196), alpha=1)
plotNormPDF(axes[1,1],n,bins,right_thetas)

n, bins, patches = axes[2,0].hist(left_rs, 180, density=True, facecolor=(0,0.5469,0.5469), alpha=1)
plotNormPDF(axes[2,0],n,bins,left_rs)

n, bins, patches = axes[2,1].hist(right_rs, 180, density=True, facecolor=(0.902,0.50196,0.10196), alpha=1)
plotNormPDF(axes[2,1],n,bins,right_rs)

n, bins, patches = axes[3,0].hist(left_rxs, 180, density=True, facecolor=(0,0.5469,0.5469), alpha=1)
plotNormPDF(axes[3,0],n,bins,left_rxs)

n, bins, patches = axes[3,1].hist(right_rxs, 180, density=True, facecolor=(0.902,0.50196,0.10196), alpha=1)
plotNormPDF(axes[3,1],n,bins,right_rxs)

n, bins, patches = axes[4,0].hist(left_rzs, 180, density=True, facecolor=(0,0.5469,0.5469), alpha=1)
plotNormPDF(axes[4,0],n,bins,left_rzs)

n, bins, patches = axes[4,1].hist(right_rys, 180, density=True, facecolor=(0.902,0.50196,0.10196), alpha=1)
plotNormPDF(axes[4,1],n,bins,right_rys)

n, bins, patches = axes[5,0].hist(left_rys, 180, density=True, facecolor=(0,0.5469,0.5469), alpha=1)
plotNormPDF(axes[5,0],n,bins,left_rys)

n, bins, patches = axes[5,1].hist(right_rzs, 180, density=True, facecolor=(0.902,0.50196,0.10196), alpha=1)
plotNormPDF(axes[5,1],n,bins,right_rzs)

fig.subplots_adjust(left=0.05,bottom=0.1,top=0.95,right=0.95,hspace=0.7,wspace=0.18)

fig.show()




