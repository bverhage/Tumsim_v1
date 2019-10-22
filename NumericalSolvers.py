# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:36:17 2019

@author: billy
"""

"""
This is a numeric differential equation solver
"""


## preperation


#does not work as I want it to

import numpy as np

from DiffEquation import f


if __name__ == "__main__":
    
    print("This is the Numerical Solver program.")
    print("To run the programm run Excecution.py")






##functions
## functions for numeric diff.eq solving
def EF(Time,w,dt):
    ''' Euler forward numerical integration method
        w_(n+1)=w_n+dt*f(tn,wn)
        
        Computational easiest integration method and Analysticly worst
        
        input is a w matrix consisting of w=[w0,w1,w2,...,wn]
        with wi=[u1(i),u2(i),u3(i),...,um(i)]^T
        
        Returns: wn+1=[u1(n+1),u2(n+1),...,un(n+1)]^T'''
    
    ans=w[:,-1:]+dt*f(Time[-1],w[:,-1:]);
    return(ans)

def TZ(Time,w,dt):
    ''' Trapezodial numerical integration method
        w_(n+1)=w_n+dt*(f(t_n,w_n)+f(tn+dt,w*_(n+1)))/2
        with w*_(n+1)=w_n+dt*f(tn,wn)
        
        Averge on computuational time and averge on analytics
        
        input is a w matrix consisting of w=[w0,w1,w2,...,wn]
        with wi=[u1(i),u2(i),u3(i),...,um(i)]^T
        
        Returns: wn+1=[u1(n+1),u2(n+1),...,un(n+1)]^T'''
        
        
    
    ans= w[:,-1:]+dt/2*(f(Time[-1],w[:,-1:])+f(Time[-1]+dt,w[:,-1:]+dt*f(Time[-1],w[:,-1:])));
    
    return(ans)
    
def RK(Time,w,dt):
    ''' Runge-Kutta integrtion method
        w_(n+1)=w_n+1/6(k1+2k2+2k3+k4)
        
        with    k1=dt*f(tn,wn)
                k2=dt*f(tn+dt/2,w_n+k1/2) 
                k3=dt*f(tn+dt/2,w_n+k2/2)
                k4=dt*f(t_n+dt,w_n+k3)
                
        Computationaly the hardest method but analystically the best.
        
        input is a w matrix consisting of w=[w0,w1,w2,...,wn]
        with wi=[u1(i),u2(i),u3(i),...,um(i)]^T
        
        Returns: wn+1=[u1(n+1),u2(n+1),...,un(n+1)]^T'''
    
    k1=dt*f(Time[-1],w[:,-1:])
    
    k2=dt*f(Time[-1]+dt/2,w[:,-1:]+k1/2)
    
    k3=dt*f(Time[-1]+dt/2,w[:,-1:]+k2/2)
    
    k4=dt*f(Time[-1]+dt,w[:,-1:]+k3)
    
    ans=w[:,-1:]+1/6*(k1+2*k2+2*k3+k4)
    
    return(ans)
    