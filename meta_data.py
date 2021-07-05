# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:47:34 2021

@author: dchen
"""
import math
import numpy as np

items = [["mug","apple","tape","rubik","plate","bowl","grinder","swiss knife","toothpaste","tooth brush"],
         ["jar","scissors","spoon","fork","knife","chopstick","pen","clamp","lighter","tweezers"],
         ["mouse","mineral water","screw driver","screw","marker","stapler","cigarette","cig box","banana","usb drive"],
         ["exacto knife", "stainless bot.","chess knight","shoe","majiang","drum stick","glasses","tune clip","nail clip","watch"],
         ["sprayer bot.","tea cup","toy car","blow dryer","headphone","tennis ball","wrench","ping pong pad.","pepper","light bulb"],
         ["med bottle","milk carton","shampoo bottle","brush","phone","iron","eraser","remote control","injector","bottle opener"]]

left_subjects = ['01-xcj', #22
                '09-gsb',
                '10-cz',
                '11-xzq',
                '12-lc',
                '19-rhd',
                '24-xg']

right_subjects = ['02-gmj',
                 '03-yq',
                 '04-zjn',
                 '05-yjm',
                 '06-lyz',
                 '07-lcd',
                 '08-gdc',
                 '13-zyf',
                 '14-zxn',
                 '15-gyq',
                 '16-zp',
                 '17-qg',
                 '18-syy',
                 '20-zmr',
                 '21-wsy',
                 '22-hpz',
                 '23-zkj',
                 '26-dsn',
                 '27-why',
                 '28-yxl',
                 '29-cyx'] #21

def rotationMatrixToEulerAnglesXYZ(R) :
    x = 0
    y = 0
    z = 0
    if(R[0,2] < 1):
        if(R[0,2] > -1):
            y = math.asin(R[0,2])   
            x = math.atan2(-R[1,2],R[2,2])
            z = math.atan2(-R[0,1],R[0,0])
        else:
            y = math.pi / 2
            x = - math.atan2(-R[1,0],R[1,1])
            z = 0
    else:
        y = math.pi/2
        x = math.atan2(R[1,2],R[1,1])
        z = 0
    return np.array([x, y, z])

def rotationMatrixToEulerAnglesXZY(R):
    x = 0
    y = 0
    z = 0
    if(R[0,1] < 1):
        if(R[0,1] > -1):
            z = math.asin(-R[0,1])
            x = math.atan2(R[2,1],R[1,1])
            y = math.atan2(R[0,2],R[0,0])
        else:
            z = math.pi / 2
            x = - math.atan2(-R[2,0],R[2,2])
            y = 0
    else:
        z = - math.pi/2
        x = math.atan2(R[2,0],R[2,2])
        y = 0
    return np.array([x, y, z])