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
# # constants
# m = 3  # mass [kg]
# b = 9  # damping coef [Ns/m]
# k = 60  # spring coef [N/m]

# # DE: my.. + by. + ky = F
# # input: u = [F]
# # output: y = [y, dy/dt, d^2 y/dt^2]
# # 2nd order DE so 2 state variables -- x(t) = [y, ydot]

# A = np.array(([0, 1],
#               [-k/m, -b/m]))
# B = np.array(([0],
#               [1/m]))
# # C and D can be trimmed to fit how many outputs we want
# C = np.array(([1,0], 
#               [0,1],
#               [-k/m, -b/m]))
# D = np.array(([0],
#               [0],
#               [1/m]))

# sys = ss(A, B, C, D)

'''question 2'''
# # parameter values
# m = 3
# b = 9
# k = 60
# # matrices
# A = np.array(([-b/m, -k/m], 
#               [1, 0]))
# B = np.array(([1/m], 
#               [0]))
# C = np.array(([0, 1]))
# D = np.array(([0]))
# # system
# sys = ss(A, B, C, D)

# x0 = np.array(([0], [1]))  # initial state values
# t = np.arange(0, 20.01, 0.01)  # time vector

# y, t = initial(sys, t, x0)  # creates initial condition response of a linear system
# plt.plot(t, y)

# # find period
# trough = np.argmin(y)
# peak2 = np.argmax(y[trough:])
# period = t[peak2 + trough]
# print(period)

'''question 3'''
# w1 = 4.2130749  # [rad/s]
# w2 = 3.9370039  # [rad/s]
# u1 = np.sin(w1 * t)
# u2 = np.sin(w2 * t)

# y1, t, _ = lsim(sys, u1, t, x0)  # creates initial condition response of a linear system
# y2, t, _ = lsim(sys, u2, t, x0)
# plt.plot(t, y1, color='blue')
# plt.plot(t, y2, color='red')
# plt.show()

# # kind just eyeballing where we'd have a max and a min
# amp1 = (np.max(y1[1000:1200]) - np.min(y1[1000:1200]))/2
# amp2 = (np.max(y2[1050:1250]) - np.min(y2[1050:1250]))/2

# print(f"4.2 freq: {amp1}\n3.9 freq: {amp2}")

'''question 4'''
# # parameter values
# m = 3
# b = 9
# k = 60
# for k in range(50, 500, 200):
#     # matrices
#     A = np.array(([-b/m, -k/m], 
#                   [1, 0]))
#     B = np.array(([1/m], 
#                   [0]))
#     C = np.array(([0, 1]))
#     D = np.array(([0]))
#     # system
#     sys = ss(A, B, C, D)
    
#     x0 = np.array(([0], [1]))  # initial state values
#     t = np.arange(0, 20.01, 0.01)  # time vector
#     w1 = 4.2130749  # [rad/s]
#     w2 = 3.9370039  # [rad/s]
#     u1 = np.sin(w1 * t)
#     u2 = np.sin(w2 * t)
    
#     y1, t, _ = lsim(sys, u1, t, x0)  # creates initial condition response of a linear system
#     y2, t, _ = lsim(sys, u2, t, x0)
#     plt.plot(t, y1)
#     # plt.plot(t, y2, color='red')
# plt.show()