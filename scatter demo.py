# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 17:07:44 2021

@author: dchen
"""
import matplotlib.pyplot as plt
import numpy as np
import json

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

left_xs = []
left_ys = []
left_zs = []
right_xs = []
right_ys = []
right_zs = []

#Read the data for left dominant subjects
for n in range(len(left_trans)):
    t = left_trans[n]
    x = t[0,3]
    y = t[1,3]
    z = t[2,3]
    left_xs.append(x)
    left_ys.append(y)
    left_zs.append(z)

#Read the data for right dominant subjects
for n in range(len(right_trans)):
    t = right_trans[n]
    x = t[0,3]
    y = t[1,3]
    z = t[2,3]
    right_xs.append(x)
    right_ys.append(y)
    right_zs.append(z)

###############Plotting#################

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
plt.gca().view_init(30, -45)
#plt.gca().view_init(90, 0)
ax.scatter(left_ys, left_zs, left_xs, marker = ".", facecolor = (0,0.5469,0.5469),alpha = 0.1)
ax.scatter(right_ys, right_zs, right_xs, marker = ".", facecolor = (0.902,0.50196,0.10196),alpha = 0.1)

ax.set_zlim(0,200)
ax.set_ylim(-200,200)
ax.set_xlim(-200,200)

#ax.set_xlabel('Y')
#ax.set_ylabel('Z')
#ax.set_zlabel('X')

ax.grid(False)
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')
#ax.set_zticks([])
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

plt.show()