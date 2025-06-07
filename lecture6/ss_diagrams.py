import numpy as np
from control.matlab import *

'''state-space systems from block diagrams'''
# transfer functions describe the relation b/w one input and one output
# state-space can have multiple inputs and multiple outputs -- describes entire system
# inputs go into the system with nothing before affecting them
# outputs are what comes out of each block in the diagram, not just the final output
# ss system: diagram --> individual tfs --> ss systems --> combine

# parameters
I2 = 1100  # momentum of inertia [kgm^2]
K = 1  # controller gain [1/rad]
tau = 15  # time constant of reaction wheel [s]

# for this system, inputs are theta_c the reference attidue and T_d the disturbing torque
# outputs:
    # y_cntrl = (theta_c - theta) * K(s + 0.01)/s  --> command to torque wheel
    # T_w = (y_cntrl + h_w) * 1/tau --> torque wheel
    # h_w = T_w * -1/s --> momentum stored in torque wheel
    # theta = (T_w + T_d) * 1/(I2 * s^2)  --> attiude of satellite
    # (theta_c - theta) --> error signal
    

# for the state-space system:
    # x* = Ax + Bu describes the dynamic states (not affected by algebraic stuff like scalars or offsets)
    # y = Cx + Du descibes the output (algebraic stuff will be stored in D)
    # only need to consider stuff that undergoes controls with s in our state eq
    
# for the controller:
    # tf: H_c(s) = K(s + 0.01)/s
    # order of numerator = order of denominator !! attenzione!! --> rewrite
    # H_c(s) = (Ks + 0.01K)/s = Ks/s + 0.01K/s = K + 0.01K/s --> no longer order issue
    # now our controller acts as two parallel paths, one with a tf of K, the other with K0.01/s
    # since tf of K has no s terms or integration, it will not be in the STATE eq
    # let x1 be the output of controller that affects the state (aka for only the stuff with s) --> x1 = (theta_c - theta) * K0.01/s
    # for our ss stuff we also want derivative of x1 --> x1* = 0.01K(theta_c - theta) (derivative in laplace  is multiply by s)
    
# for the reachtion wheel assembly:
    # we have a block that is -1/s so yay! state eq stuff
    # h_w = -1/s * T_w so we'll make h_w our state variable x2
    # T_w = 1/tau * (hw + y_cntrl) = 1/tau * (h_w + ((theta_c - theta) * K + (theta_c - theta) * K0.01/s))
    # from before x1 = (theta_c - theta) * K0.01/s and x2 = h_w
    # T_w = 1/tau * (x2 + ((theta_c - theta) * K + x1))
    # h_w = -1/s * T_w therefore x2 = -1/s * 1/tau * (x2 + ((theta_c - theta) * K + x1))
    # we also want x2* which is just multiply by s --> x2* = -1/tau * (x2 + (theta_c - theta) * K + x1)
    
# for the satellite attitude dynamics:
    # the controller block is 1/(I2 * s^2)
    # attenzione! the order is 2 hence we need 2 state variables for this
    # theta = (T_d + T_w) * 1/(I2 * s^2) = 1/(I2 * s^2) * (T_d +  (x2 + ((theta_c - theta) * K + x1))
    # the variable we put into the state space can't have any s's so we need the 1/s^2 to be gone once we get x3* aka --> x3 = theta*
    # x3 = theta* = 1/(I2 * s) * (T_d +  (x2 + ((theta_c - theta) * K + x1))
    # now when we take x3* we have no s!! x3* = 1/I2 * (T_d +  (x2 + ((theta_c - theta) * K + x1))
    # since theta* is a state variable, we'll also take theta as the second one we needed --> x4 = theta
    # that leaves us with x4* = theta* = x3 hence x4* = x3

# defined state variables: x1, x2, x3, x4 and their respective derivatives for the state equation
# output equation has output vector [y_cntrl, T_w, T_d + T_w, h_w, theta, theta_c - theta]

A = np.array(([0, 0, 0, -0.001*K],
              [-1/tau, -1/tau, 0, K/tau],
              [1/(tau * I2), 1/(tau * I2), 0, -K/(tau * I2)],
              [0, 0, 1, 0]))    
B = np.array(([0.01*K, 0],
              [-K/tau, 0],
              [K/(tau * I2), 1/(tau * I2)],
              [0, 0]))
C = np.array(([1, 0, 0, -K],
              [1/tau, 1/tau, 0, -K/tau],
              [1/tau, 1/tau, 0, -K/tau],
              [0, 1, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 0, -1]))
D = np.array(([K, 0],
              [K/tau, 0],
              [K/tau, 1],
              [0, 0],
              [0, 0],
              [1, 0]))
    
sys = ss(A, B, C, D)
y, t = step(sys)
    
'''question 1'''
# gain parameters
k1 = 1.2
k2 = 2.5
k3 = 2.5
k4 = 0.6

# inputs: r, d
# outputs: y
# state variable equations:
    # x1* = -k2k4x2 - k3k4x3 +k4r + d
    # x2* = x1 - x2
    # x3* = x2

a = np.array(([0, -k2*k4, -k3*k4],
              [1, -1, 0],
              [0, 1, 0]))
b = np.array(([k4, 1],
              [0, 0],
              [0, 0]))

# output variable equation:
    # y = k1x1 + x3

c = np.array(([k1, 0, 1]))
d = np.array(([0, 0]))

sys = ss(a, b, c, d)
print(sys)