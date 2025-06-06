import numpy as np
import matplotlib.pyplot as plt

'''question 2'''
# dt = 0.15
# t = np.arange(0.0, 30 + dt, dt)  # from 0s to 30s to 0.15s steps
# u = np.hstack((
#     np.linspace(0.0, 2.34, int(1.5/dt + 1)),  # creating array from 0 to 2.34 with 1.5/dt + 1 steps since it lasts 1.5 sec
#     np.ones(int(28.5/dt)) * 2.34  # filling in the rest of the 28.5 sec with 2.34
#     ))

# plt.plot(t, u)
# plt.show()

# print(np.sum(u))

'''question 1'''
# dt = 0.2
# t = np.arange(0, 20 + dt, dt)
# # sin(Bx) --> f = B / 2pi so B = f * 2pi
# B = 5.1 * 2 * np.pi
# u = np.sin(B * t)

# plt.plot(t, u)
# plt.show()

'''intro'''
# discretising signals by only having discrete times at which the signal is given
# vector for the times at which the signal is known
# t = np.arange(0, 10.01, 0.01)

# # vector representing the value of the signal at that time
# x = np.sin(t)

# plt.plot(t,x)
# plt.show()

'''frequency content of signals'''
# continuous and sample (discrete-time) signals are both functions of time
# signals can also be considered as the sum of a (possibly infinite) series of sine and cosine functions w dif freqencies
# x(t) = a0/2 + sum_{n=1}^{\infty}(a_n cos(2 pi n f t) + b_n sin(2 pi n f t))
# a_n = 2/T int_{-T/2}^{T/2} x(t) cos(2 pi n f t) dt for n = 0, 1, 2
# b_n = 2/T int_{-T/2}^{T/2} x(t) sin(2 pi n f t) dt for n = 0, 1, 2
# f = 1/T which is the base frequency signal 
# if for above frequency nf we get a_n = 0 and b_n = 0 then the signal is band limited
# a_n and b_n are the Fourier Series of the signal

'''sample time'''
# sample time/interval is when we have regular intervals b/w the signal points of a discrete signal
# trade off b/w short and large signals: inaccuracies, computational time, distortion
# sampling freq > 2x bandwidth of input signal for recreation
# even if bandwith infinite, at a certain point a_n and b_n --> 0 so we can consider it finite
# usually sample freq = 10x - 20x bandwidth for easier reconstruction

'''reconstructing'''
# zero-order bold is a cont time signal with the vlaue of the signal in the internal [n * Delta t, (n+1) * Delta t]
# aka from the point the signal is taken to the next point at which we have a signal
# construct piecewise function of just constant regions

'''time vectors'''
# # time vectors are evenly spaced and work for our input signals
# dt = 0.04  # sampling time
# t = np.arange(0.0, 30 + dt, dt)  # creating evenly spaced time vector for 30sec of sampling spaced by our sampling time
# # input signal
# u = np.hstack((
#     np.zeros(int(1/dt)),  # creates 1/0.04 = 25 zeros corresponding to how many 0s we need for the 1st sec
#     np.arange(0, 1+dt/4, dt/4),  # timestep is dt/4 to have a finer time resolution --> smoother ramp, value ranges from 0 to 1
#     np.ones(int(25/dt))  # value is 1 for a duration of 25/0.04 = 625 time steps (aka 25 secs)
#     ))
# u is a ramp and hold function (goes from 0, linearly to a certain value, then constant there)
# u has a ramp starting at 1 second and finishing at 5 sec going to a value of 1
# from t=0 to t=1s --> value is 0, from t=1s to t=5s --> value linearly increases from 0 to 1, from t=5s to t=30s the value stays at 1

# plt.plot(t, u)
# plt.show()