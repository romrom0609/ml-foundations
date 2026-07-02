# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:01:54 2026

@author: roman
"""

import numpy as np


np.random.seed(42)
N=50
x=np.random.uniform(-3,3,N)
y_vrai_w, y_vrai_b= 2.5,-1
bruit=np.random.normal(0,0.5,N)
y= y_vrai_w*x+y_vrai_b+bruit

def loss(w,b,x,y):
    e= y-(w*x+b)
    return (0.5*np.mean(e**2))

def grad_w(w,b,x,y):
    e= y-(w*x+b)
    return -np.mean(x*e)

def grad_b(w,b,x,y):
    e= y-(w*x+b)
    return -np.mean(e)
    

def numerical_grad_w(w,b,x,y,h=1e-5):
    return (loss(w+h,b,x,y)-loss(w-h,b,x,y))/(2*h)

def numerical_grad_b(w,b,x,y,h=1e-5):
    return (loss(w,b+h,x,y)-loss(w,b-h,x,y))/(2*h)


points= [(0, 0), (1, 1), (-2, 5),(2.5,-1)]

for p in points:
    gw=grad_w(p[0],p[1],x,y)
    gb=grad_b(p[0],p[1],x,y)
    num_w=numerical_grad_w(p[0],p[1],x,y)
    num_b=numerical_grad_b(p[0],p[1],x,y)
    e1=abs(gw-num_w)
    e2=abs(gb-num_b)
    if e1<1e-4:
        print("OK")
    else:
        print("Faux")
    if e2<1e-4:
        print("OK")
    else:
        print("Faux")

