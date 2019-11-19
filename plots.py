# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:38:51 2019

@author: billy
"""
if __name__ == "__main__":
    print("This is the Plots program.")
    print("To run the programm run Excecution.py")
    
import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

import math

    
#Creating these matrices is purley cosmetical.

def Convertw(w):  
    global x
    global x_dot
    global q
    global q_dot
    global angle
    #creating a place matrix
    x=w[0:3]
    #creating a speed matrix
    x_dot=w[3:6]
    #creating a place matrix
    q=w[6:10]
    #creating a speed matrix
    q_dot=w[10:13]
    
    #creating the angle matrix 
    angle=quaternion_to_euler(q[1,0], q[2,0], q[3,0], q[0,0])
    
    for i in range(1, len(w[0,:])):
        
        angle=np.append(angle,quaternion_to_euler(q[1,i], q[2,i], q[3,i], q[0,i]),axis=1)
    
    
    

def euler_to_quaternion(roll, pitch, yaw):

        qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
        qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
        qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
        qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)

        return np.array([[qx],
                         [qy], 
                         [qz],
                         [qw]])
    
def quaternion_to_euler(x, y, z, w):

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll = math.atan2(t0, t1)
    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch = math.asin(t2)
    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw = math.atan2(t3, t4)
    return np.array([[yaw],
                     [pitch], 
                     [roll]])




##------------- The plots -----------------

def trajectory_3D_plot(w,Time):
    
    #converting into understandable quantities.
    Convertw(w)
    
    fig2 = plt.figure()
    ax = fig2.add_subplot(111, projection='3d')
    ax.scatter(x[0,:], x[1,:], x[2,:], c='r', marker='o')
    plt.show()
    return;

def trjacetory_Z_plot(w,Time):
    #converting into understandable quantities.
    Convertw(w)
    
    fig3 = plt.figure()
    
    ax = fig3.add_subplot(121)
    
    plt.plot(Time,x[2,:],'-')
    plt.xlabel('Time(s)')
    plt.ylabel('z')
    plt.title('z')
    
    ax = fig3.add_subplot(122)
    
    plt.plot(Time,x_dot[2,:],'-')
    plt.title('z_dot')
    plt.ylabel('z_dot(m/s)')
    plt.xlabel('Time(s)')
    plt.show()
    return;
    
def quaturnianplot(w,Time):
    #converting into understandable quantities.
    Convertw(w)
    
    fig1 = plt.figure()
    plt.subplot(211)
    plt.plot(Time,q_dot[0,:],'-',color='black')
    plt.plot(Time,q_dot[1,:],'-',color='blue')
    plt.plot(Time,q_dot[2,:],'-',color='red')
    plt.xlabel('Time(s)')
    plt.ylabel('z')
    plt.title('angular velocity')
    plt.legend(('q dot_0','q dot_1','q dot_2'))
    
    plt.subplot(212)
    plt.plot(Time,q[0,:],'-',color='black')
    plt.plot(Time,q[1,:],'-',color='blue')
    plt.plot(Time,q[2,:],'-',color='red')
    plt.plot(Time,q[3,:],'-',color='green')
    
    plt.title('orientation')
    plt.legend(('q_0','q_1','q_2','q_3'))
    plt.show()
    return;
    
def Eulerangleplot(w,Time):
    #converting into understandable quantities.
    Convertw(w)
    fig1 = plt.figure()
    plt.subplot(111)
    plt.plot(Time,angle[0,:],'-',color='black')
    plt.plot(Time,angle[1,:],'-',color='blue')
    plt.plot(Time,angle[2,:],'-',color='red')
    plt.xlabel('Time(s)')
    plt.ylabel('radiants')
    plt.title('euler angels')
    plt.legend(('yaw ','pitch','roll'))
    plt.show()
    
    

    


  