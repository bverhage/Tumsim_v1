# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:14 2019

@author: billy
"""
import numpy as np

if __name__ == "__main__":    
    print("This is the Differential equation.")
    print("To run the programm run Excecution.py")


## constants
## the Inetria matrix
    
global I
I=np.array([[5,0,0],
            [0,5,0],
            [0,0,1]])
    
# the mass
global Mass
M=1


  
## ------------ the differential eq --------------    
def f(t,w):
    ''' The differential equation that has to be solved.
        imputs: t is time array
                w matrix consisting of w=[w0,w1,w2,...,wn]
                with wi=[u1(i),u2(i),u3(i),...,um(i)]^T
                
        Returns:The next numerical approximation of the solution.
                wn+1=[u1(n+1),u2(n+1),...,un(n+1)]^T'''
    
    ## this is the linear part of the differential equation
    ## Little is linair so this matrix A is moslty filled with 0
    ## the dimentions of A are 13x13
    
    A1=np.block([
                [np.zeros((3,3)),np.identity(3)],
                [np.zeros((3,3)),np.zeros((3,3))]
                ])
    
    A2=np.block([
                [np.zeros((4,4)),np.zeros((4,3))],
                [np.zeros((3,4)),np.zeros((3,3))]
                ])
    
    A=np.block([
                [A1,np.zeros((6,7))],
                [np.zeros((7,6)),A2]
                ])
    
    # this is purly for comsetical reasons.
    #extracting a place matrix
    x=w[0:3]
    
    #exctracting a speed matrix
    x_dot=w[3:6]

    #exctrating a quaturnion matrix
    q=w[6:10]

    #exctracting a angular velocity matrix
    q_dot=w[10:13]
    


    ### quaturnion shit
    
    ## quaturnion multiplication matrix
    ## https://arxiv.org/pdf/0811.2889.pdf
    
    G_quat=1/2*np.array([
                         [-q[1,-1],q[0,-1],q[3,-1],-q[2,-1]],
                         [-q[2,-1],-q[3,-1],q[0,-1],q[1,-1]],
                         [-q[3,-1],q[2,-1],-q[1,-1],q[0,-1]]
                         ])
    
    quaturn_time_depententy=np.block([
                                     [np.zeros((6,1))],
                                     [1/2*np.transpose(G_quat).dot(q_dot)],
                                     [np.zeros((3,1))]
                                     ])
    

    
    ##The total differential equation.
    
    #Linear part
    ans=A.dot(w)
    
    #the quaturnions 
    ans=ans+quaturn_time_depententy
    
    #the Internal rotational torques
    ans=ans+Rot_Internal(q_dot)
    
    #the External rotatinal torques
    ans=ans+Rot_External(G_quat,x_dot)
    
    #Lagitudial grafitatinal acceleration
    ans=ans+Lat_Fg()/M
    
    #Lagitudial Drag acceleration
    ans=ans+Lat_Fwl(x_dot)/M
    
    ## The same but less dramatic
    #ans=A.dot(w)+quaturn_time_depententy+Rot_Internal(q_dot,I)+Rot_External(I,G_quat,x_dot)+Lat_Fg()+Lat_Fwl(x_dot)

    return(ans)    




## ----------------torques-------------------
def Rot_Internal(q_dot):

    
    #linear part of the rotional acceleration
    Internal=-1*np.linalg.inv(I).dot(np.transpose(np.cross(np.transpose(I.dot(q_dot)),np.transpose(q_dot))))

    ans=np.block([
                [np.zeros((10,1))],
                [Internal]
                ])
    return(ans)
    
def Rot_External(G_quat,x_dot):


    #M=np.transpose(np.cross(np.transpose(Lat_Fwl(x_dot)[3:6]),rcmcp))
    
    #M=1/2*np.linalg.inv(np.transpose(G_quat)).dot(Lat_Fwl(x_dot)[3:6])
    M=np.zeros((3,1))
    
    #This is underconstruction
    
    ans=np.block([
                [np.zeros((10,1))],
                [np.linalg.inv(I).dot(M)]
                ])
    return(ans)


## --------------- Forces on CM ----------------
    
def Lat_Fg():
    graf=9.81
    #Gravity
    ans=np.zeros([13,1])
    ans[5]=-graf
    return(ans)
    
    
def Lat_Fwl(v):
    #air resitance
    Cw=float(0.75)
    Area=float(0.04)
    Rho=float(1.225)
    ans=-Cw*Area*Rho*v[:,-1:]*np.linalg.norm(v[:,-1:])
    ans = np.block([
                [np.zeros((3,1))],
                [ans],
                [np.zeros((7,1))]
                ])
    return(ans)