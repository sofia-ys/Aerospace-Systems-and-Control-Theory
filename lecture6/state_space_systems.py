import numpy as np
from control.matlab import *

'''entering state-space systems'''
# state equation: x.(t) = Ax(t) + Bu(t)
# output equation: y(t) = Cx(t) + Du(t)

# creating the abcd matrices for the equations
# state matrix 
# a = np.array(([0, 1, 0], 
#               [-0.0071, -0.111, 0.12], 
#               [0, 0.07, -0.3]))
# # input matrix
# b = np.array(([0], 
#               [-0.095], 
#               [0.072]))
# # output matrix
# c = np.array(([1, 0, 0]))
# # feedforward matrix
# d = np.array(([0]))

# # state vector is x = [theta, q, alpha] (stacked vertically)
# # theta: pitch attidue, q: pitch rate, alpha: angle of attack
# # input vector is u = [delta_e] the elevator deflection

# sys = ss(a, b, c, d)  # state-space system ss(matrices, time-step)
# # rows(b) = rows(a), a must be square, cols(c) = cols(a), cols(d) = cols(b) and rows(d) = rows(c)
# # ^^ otherwise error since not compatible matrix sizes

# # output vector y = [theta, q, alpha, gamma] with descent angle gamma now too
# # gamma = theta - alpha so we use this relationship to define gamma with the state vector

# newc = np.array(([1, 0, 0],  # theta
#                  [0, 1, 0],  # q
#                  [0, 0, 1],  # alpha
#                  [1, 0, -1]))  # gamma = theta - alpha
# newd = np.zeros((4,1))  # making sure shape of d matches
# sys2 = ss(a, b, newc, newd)

# print(sys2)

'''question 1'''
# constants
m = 3  # mass [kg]
b = 9  # damping coef [Ns/m]
k = 60  # spring coef [N/m]

# DE: my.. + by. + ky = F
# input: u = [F]
# output: y = [y, dy/dt, d^2 y/dt^2]
# 2nd order DE so 2 state variables -- x(t) = [y, ydot]

A = np.array(([0, 1],
              [-k/m, -b/m]))
B = np.array(([0],
              [1/m]))
# C and D can be trimmed to fit how many outputs we want
# C = np.array(([1,0], 
#               [0,1],
#               [-k/m, -b/m]))
# D = np.array(([0],
#               [0],
#               [1/m]))

# sys = ss(A, B, C, D)

'''question 2'''
# now only position as output
C = np.array(([0,1]))
D = np.array(([0]))
sys = ss(A, B, C, D)

print(sys)