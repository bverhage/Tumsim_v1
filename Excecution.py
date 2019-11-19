# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:58 2019

@author: billy
"""

import numpy as np

import plots

from NumericalSolvers import RK,EF,TZ

from tqdm import tqdm 

### if the porces bar does not work as expected in spyder
### than use the following code in the console
### conda install -c conda-forge tqdm


print('------ begin of code ------')

print('Current assumprions:Flat earh')
print('Constant air density')

## boundry conditions

# time starting point  
t0=0

#time ending point
tE=30

#step time
dt=0.2


# inital conditions
# This has no coding purpose. 
# This is purly for clarivication

#initial place vector
x0=np.array([[0],   #x0
             [0],   #y0
             [80]]) #z0
    
#intial speed vector
x0_dot=np.array([[1],  #vx0
                 [1],  #vy0
                 [2]]) #vz0

#inital orientation vector
angle0=np.array([[np.pi], #roll0
                 [0],     #pitch0
                 [0]])    #yaw0
q0=plots.euler_to_quaternion(angle0[0,0], angle0[1,0], angle0[2,0]) 

#inital angular velocity vector
q0_dot=np.array([[1],
                 [-1],
                 [1]]) 
    

#creating the initial w matrix
# with the earlier defined inital conditions
w0=np.block([
                [x0],
                [x0_dot],
                [q0],
                [q0_dot]
                ])



## the first step 
## the starting point for the total data matrix w
w=w0

## the starting point for the time vector Time
Time=[t0]


##----------- The excecution --------------
## It uses tqdm to create a proces bar.

with tqdm(total=int(np.ceil(tE/dt))) as pbar:
    while(Time[-1]<tE):
        
        #appling the numerical method over the differnential eqation f.
        
        wn=RK(Time,w,dt)
        
        #adding the next point to the numerical matrix w
        
        w=np.append(w,wn,axis=1)
        
    
        #going to the next time step.
        
        Time.append(Time[-1]+dt)
        
        #reitterating everything until tE
        
        ## updating the proces bar
    
        pbar.update(1)
        
        #unless the z coordinate has become 0.
        if(w[2,-1]<0):
            pbar.write("!!The ground has been reached!!")
            break
      
## --------------- The plots ---------------   
        
plots.trajectory_3D_plot(w,Time)

plots.trjacetory_Z_plot(w,Time)

plots.quaturnianplot(w,Time)

plots.Eulerangleplot(w,Time)

print('------ end of code ------')