# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""marche1_verifs.py — Marche 1 du plan : vérification numérique des 20 dérivées."""

from math import *


def numerical_derivative(f, x, h=1e-5):
    """Dérivée numérique centrée : (f(x+h) - f(x-h)) / (2h)."""
    return (f(x + h) - f(x - h)) / (2 * h)


# Format de chaque ligne :
# (nom, fonction f, dérivée f' (calculée par toi), point x où on évalue)
exercices = [
    # Bloc A — fonctions usuelles
    ("x**7",       lambda x: x**7,           lambda x: 7*x**6,  1.5),
    ("x**0.5",     lambda x: x**0.5,         lambda x: 0.5*x**(-0.5),1.5),
    ("1/x**3",     lambda x: 1/x**3,         lambda x: -3/x**4, 1.5),
    ("exp(x)",     lambda x: exp(x),         lambda x: exp(x), 1.5),
    ("log(x)",     lambda x: log(x),         lambda x: 1/x, 1.5),
    ("5x³ − 2x² + 7x − 4",   lambda x: 5*x**3-2*x**2+7*x-4,    lambda x: 15*x**2-4*x+7, 1.5),
    ("x**2*exp(x)",   lambda x: x**2*exp(x),     lambda x: exp(x)*x*(2+x), 1.5),
    ("x*log(x)",    lambda x: x*log(x),      lambda x: 1+log(x), 1.5),
    ("(x² + 1)(x³ − x)",     lambda x: (x**2+1)*(x**3-x),      lambda x: 5*x**4-1 ,1.5),
    ("x*sin(x)",   lambda x:x*sin(x),        lambda x: sin(x)+x*cos(x) , 1.5),
    ("x/(x**2+1)", lambda x:x/(x**2+1),      lambda x: (1-x**2)/((x**2+1)**2), 1.5),
    ("exp(x)/x",   lambda x: exp(x)/x,       lambda x: exp(x)*(x-1)/x**2, 1.5),
    ("sin(x)/x",   lambda x: sin(x)/x,       lambda x: (cos(x)*x-sin(x))/x**2, 1.5),
    ("(3x + 1)⁵",  lambda x: (3*x+1)**5,     lambda x: 15*(3*x+1)**4, 1.5),
    ("exp(x**2)",  lambda x: exp(x**2),      lambda x: 2*x*exp(x**2), 1.5),
    ("ln(x**2+1)", lambda x: log(x**2+1),     lambda x: 2*x/(x**2+1), 1.5),
    ("sin(x**2)",  lambda x: sin(x**2),      lambda x: 2*x*cos(x**2), 1.5 ),
    ("(x**2+1)**0.5",   lambda x: (x**2+1)**0.5,    lambda x: x/((x**2+1)**(0.5)), 1.5),
    ("1/(1+exp(-x))",   lambda x: 1/(1+exp(-x)),    lambda x: exp(-x)/(1+exp(-x))**2, 1.5)]
    
    


def main():
    tolerance = 1e-4
    n_ok = 0
    for nom, f, df_papier, x in exercices:
        num = numerical_derivative(f, x)
        pap = df_papier(x)
        ecart = abs(num - pap)
        if ecart < tolerance:
            verdict, n_ok = "OK   ", n_ok + 1
        else:
            verdict = "FAUX "
        print(f"{verdict}  f(x) = {nom:25s}  papier={pap:+.6f}  num={num:+.6f}  ecart={ecart:.2e}")
    print(f"\nScore : {n_ok}/{len(exercices)}")


if __name__ == "__main__":
    main()