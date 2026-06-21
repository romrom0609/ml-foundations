# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 13:41:02 2026

@author: roman
"""

from math import *

def numerical_derivative(f,x,h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)


def sigma(x):
    return 1/(1+exp(-x))

def derivee_sigma(x):
    return sigma(x)*(1-sigma(x))

# Constantes pour les exos 7-8 (choisis-les toi-même, mais garde-les fixes)
w, b = 0.7, -0.3
w1, b1, w2, b2 = 0.5, 0.1, -1.2, 0.4


exercices = [
    #(nom, fonction f, dérivée f'calculée par moi en Leibniz, point x)
    ("(3*x+1)**5",     lambda x: (3*x+1)**5,      lambda x: 15*(3*x+1)**4, 0.5),
    ("exp(x**2)",      lambda x: exp(x**2),       lambda x: 2*x*exp(x**2), 0.5),
    ("sin(ln(x² + 1))",  lambda x: sin(log(x**2+1)),   lambda x: 2*x/(x**2+1)*cos(log(x**2+1)), 0.5),
    ("exp(cos(3*x))",  lambda x: exp(cos(3*x)),   lambda x: -3*sin(3*x)*exp(cos(3*x)), 0.5),
    ("(1+exp(2*x))**0.5", lambda x:(1+exp(2*x))**0.5,   lambda x: exp(2*x)/(1+exp(2*x))**0.5, 0.5),
    ("ln(1+exp(x))",   lambda x: log(1+exp(x)),   lambda x: sigma(x), 0.5),
    ("σ(wx + b) ",      lambda x: sigma(w*x+b),   lambda x: w*sigma(w*x+b)*(1-sigma(w*x+b)),  0.5),
    ("σ(w₂ · σ(w₁ · x + b₁) + b₂) ",   lambda x: sigma(w2*sigma(w1*x+b1)+b2),    lambda x: w1*w2*derivee_sigma(w1*x+b1)*derivee_sigma(w2*sigma(w1*x+b1)+b2), 0.5)]


def main ():
    tolerance=1e-4
    n_ok=0
    for nom , f , df_papier , x in exercices:
        num=numerical_derivative(f, x)
        pap=df_papier(x)
        ecart = abs(num-pap)
        if ecart < tolerance:
            verdict, n_ok = "OK   ", n_ok + 1
        else:
            verdict = "FAUX "
        print(f"{verdict}  f(x) = {nom:25s}  papier={pap:+.6f}  num={num:+.6f}  ecart={ecart:.2e}")
    print(f"\nScore : {n_ok}/{len(exercices)}")


if __name__ == "__main__":
    main()

