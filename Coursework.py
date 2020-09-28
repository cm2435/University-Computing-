
import numpy as np

#first we will defne our known values given in 1b)

G=6.67e-11; Earth_Radius=6.371e6; Moon_radius=1.7371e6; M= 5.9722e24
m=7.3420e22; R=3.8440e8; w=2.6617e-6 


def Secant_Function (f, x0, x1, iterations: int):
    x=[x0, x1]
    
    for i in range(iterations):
        x.append(x[i+1] - f(x[i+1])*(x[i+1] - x[i]/f(x([i+1]) - f(x[i]))))
        
    return x[-1], x[-2]
    

def Lagrange (r):
     return G*M*(r**-2)- G*m*(R-r)**-2 - (w*r) 
 
n=1

#Defining our initial guesses

a=float(input("x1 value:   "))
b=float(input("x2 value:   "))

L1, lold= Secant_Function(Lagrange, a, b, n)

l1c= '{:#.5g}'.format(L1)
loldc= '{:#.5g}'.format(lold)

e= l1-lold

while l1c != loldc:
    
    n= n + 1
    
    L1, lold = Secant_Function(Lagrange, a, b, n)

l1c= '{:#.5g}'.format(L1)
loldc= '{:#.5g}'.format(lold)

print("/nL1: {:.5g}, Lold: {:#0.5g}, n: {}".format(L1, lold, n))

