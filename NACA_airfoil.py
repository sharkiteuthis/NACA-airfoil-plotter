# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 19:10:19 2016

@author: tcdod
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['svg.fonttype'] = 'none'

def symmetrical_4_digit_airfoil(t,c=1.0,N=300):
    x = np.linspace(0,c,N)
    x_t = x/c

    #set zero thickness at end
    C4 = 0.1036

    #C4 = 0.1015

    y= (5* t/c) * ((0.2969 * np.sqrt(x_t)) - (0.1260 * x_t) - (0.3516 * x_t**2) + \
                    (0.2843 * x_t**3) - (C4 * x_t**4))

    return x,y

x,y = symmetrical_4_digit_airfoil(0.15);

plt.figure()
plt.plot(x,y)
plt.plot(x,-1*y)
plt.show()

def cambered_4_digit_airfoil(m,p,t,c=1.0,N=300):
    x,y = symmetrical_4_digit_airfoil(t,c,N)

    y_c = np.zeros(x.shape)
    cutoff = int(np.ceil((p * c) / x[1]))
    y_c[0:cutoff] = m * x[0:cutoff] / p**2 *(2 * p - x[0:cutoff] / c)
    y_c[cutoff:] = m * (c - x[cutoff:]) / (1 - p)**2 * (1 + x[cutoff:] / c - 2 * p)

    theta = np.zeros(x.shape)
    theta[0:cutoff] = np.arctan(2 * m / p**2 * (p - x[0:cutoff] / c))
    theta[cutoff:] = np.arctan(2 * m / (1 - p)**2 * (p - x[cutoff:] / c))

    x_u = x - y * np.sin(theta)
    x_l = x + y * np.sin(theta)
    y_u = y_c + y * np.cos(theta)
    y_l = y_c - y * np.cos(theta)

    return x,y_c,x_u,x_l,y_u,y_l,theta

x,y_c,x_u,x_l,y_u,y_l,theta = cambered_4_digit_airfoil(0.06,0.4,0.09)

plt.figure()
plt.plot(x,y_c)
plt.show()

plt.figure()
plt.plot(x_u,y_u)
plt.plot(x_l,y_l)
plt.plot(x,y_c,'r')
plt.show()

