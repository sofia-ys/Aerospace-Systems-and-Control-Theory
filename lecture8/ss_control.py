from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

'''systems in series'''
# two ss sytems can be connected in series if number of outputs of 1st matches number of inputs of second

# create two random systems: s1 --> 1 output --> 1 input --> s2
# s1 = rss(3, 1, 2)  # 1 output, 2 inputs
# s2 = rss(2, 3, 1)  # 3 outputs, 1 input
# # rss(states, outputs, inputs) --> states is how many state variables it has

# # and put them in series
# stotal = s2 * s1
# # stotal = s1 --> s2 so it has 2 inputs like s1, and 3 outputs like s2
# # stotal will need all 3 + 2 = 5 state variables to be able to have s2 and s1 work
# print(stotal)

'''systems in parallel'''
# systems in parallel can be connected by adding them
# s1 = rss(3, 1, 2)
# s2 = rss(2, 1, 2)
# # number of inputs and outputs for both must be equal

# stotal = s1 + s2

# print(stotal)

# matrix A (the state matrix) shows that the 4th and 5th states are not connected to the first 3
# we have the same number of inputs going in, but then what the system does with it is independent on each branch

'''feedback loops'''
a = np.array(([0, 1, 0],
              [-0.0071, -0.111, 0.12],
              [0, 0.07, -0.3]))
b = np.array(([0],
              [-0.095],
              [0.072]))
c = np.array(([1, 0, 0],
              [0, 1, 0],
              [0, 0, 1],
              [1, 0, -1]))
d = np.zeros((4, 1))

sys2 = ss(a, b, c, d)  
# this is a system with 1 input and 4 outputs:
    # state variables: theta, q, alpha
    # outputs: theta, q, alpha, gamma
# print(sys2)

# we can improve the performance by introducing a feedback loop
# feedback pitch rate, q, with a gain factor
# create a feedback matrix to relate how the different outputs must be fed back

k = np.array(([0, -0.67, 0, 0]))  # only feeding back q * -0.67 (gain factor)
sysclosed = sys2.feedback(k)
# print(sysclosed)

'''inspecting the system'''
# analysing tf -- look at poles (roots of denominator)
# analysis ss -- eigenvalues of A matrix = poles of equivalent tf
# if all poles have negative real values, we can analyse stability from eigenvalues of A

print(la.eig(sysclosed.A)[0])
print(la.eig(sys2.A)[0])
# the real eigenvalues are pretty close, but the complex conjugate eigenvalues changed quite a lot!


'''question 1'''
# matrices
a = np.array(([-0.2, 0.06, 0, -1],
              [0, 0, 1, 0],
              [-17, 0, -3.8, 1],
              [9.4, 0, -0.4, -0.6]))
b = np.array(([-0.01, 0.06],
              [0, 0],
              [-32, 5.4],
              [2.6, -7]))
# output: y = r
c = np.array(([0, 0, 0, 1]))
d = np.array(([0, 0]))

sys = ss(a, b, c, d)
h = tf(sys)
hr = h[0,1]  # this is for input 2 aka the rudder 

t = np.arange(0, 20.01, 0.01)

y1 = step(hr, t)

plt.plot(t, y1[0])
plt.show()

print(np.min(y1))





