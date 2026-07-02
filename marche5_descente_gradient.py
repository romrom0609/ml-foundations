# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 07:23:23 2026

@author: roman
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:01:54 2026

@author: roman
"""

import numpy as np
import matplotlib.pyplot as plt

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


def descente_gradient(x,y,w0,b0,eta,n_max,epsilon):
    """
    retourne: w_final,b_finale,historique_Loss(liste)
    """
    w,b=w0,b0
    historique=[loss(w,b,x,y)]
    for t in range (n_max):
        dw=grad_w(w,b,x,y)
        db=grad_b(w,b,x,y)
        w= w-eta*dw
        b=b-eta*db
        historique+=[loss(w,b,x,y)]
        # print(historique)
        if abs(historique[-1]-historique[-2])<epsilon:
            break
    return w,b,historique


# Axe de gauche : les 3 courbes convergentes
eta_list=[0.1,0.01,0.5]
fig,axes=plt.subplots(1,2, figsize=(12,4))
# fig est la fenêtre, axes est un tableau [axe_gauche, axe_droite]
for eta in eta_list:
    w_final,b_final,hist=descente_gradient(x,y,w0=0,b0=0,eta=eta,n_max=1000,epsilon=1e-8)
    # print(f"w final= {w_final:.4f} (vrai: 2.5)")
    # print(f"b final = {b_final:.4f} (vrai: -1.0)")
    # print(f"nombre itérations : {len(hist)-1} ")
    # print(f"loss final : {hist[-1]:.6f}")
    axes[0].plot(hist,label=f"eta={eta}")

axes[0].set_yscale("log")
axes[0].set_xlabel("itérations")
axes[0].set_ylabel("Loss(MSE/2)")
axes[0].set_title("Convergence")
axes[0].set_xlim(0,100)
axes[0].legend()
axes[0].grid(True)

# Axe de droite : la courbe divergente
w_final,b_final,hist=descente_gradient(x,y,w0=0,b0=0,eta= 2,n_max=20,epsilon=1e-8)
axes[1].plot(hist,label="eta=2.0", color="red")
axes[1].set_yscale("log")
axes[1].set_xlabel("itérations")
axes[1].set_ylabel("Loss(MSE/2)")
axes[1].set_title("Divergence")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()  # évite que les titres se chevauchent
plt.show()

