from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np

'''from state-space to transfer function'''
# # can you recognise this one?
# a = np.array(([0, 1, 0],
#               [-0.0071, -0.111, 0.12],
#               [0, -0.095, 0.072]))
# b = np.array(([0],
#               [-0.095],
#               [0.072]))
# c = np.array(([1, 0, 0]))
# d = np.array(([0]))
# sys = ss(a, b, c, d)  # creating the state space of these given matrices
# h = tf(sys)  # converting that state space into a transfer function

# # a random transfer function (each time you run it, it's different !)
# sys = rss(3, 2, 3)  # random state-space function with 3 states, 2 outputs, 3 inputs
# print(sys)

# # y, t = impulse(sys)
# # plt.plot(t, y)
# # plt.show()

# h = tf(sys)
# # since sys has multiple inputs and outputs, but a tf doesn't it gives us all possibiltites for h
# # in 1 to out 1, in 1 to out 2, in 2 to out 1, in 2 to out 2, in3 to out1 etc 
# print(h)
# print(h.__class__)  # yup h is a tf

# # select one of the transfer functions
# h11 = tf(h.num[0][1], h.den[0][1])  # here we selected out 1 to in 2 -- indexing is [output - 1][input - 1]

# print(h11)

'''from tf to state-space'''
# invent a transfer function
s = tf([1, 0], [1])  # getting our laplace variable
h = (1 + 2*s)/(s*(s ** 2 + 0.5 *s + 4))  # just a random tf
# convert to state-space
sys = ss(h)

# a multi-dimensional transfer function needs to be entered with num and
# den arrays in Python
# first output is h, second output is h*s so the same input u(t) is producing two outputs via two tfs
H = tf([[h.num[0][0]], [(h*s).num[0][0]]], 
       [[h.den[0][0]], [(h*s).den[0][0]]])
# the tf function is stored as two arrays: first array for the numerator, second for the denominator
# arrays give the coeffs in descending order of degree of s
# we double index [0][0] because the information is stored as a nested list
# [[[2.0, 1.0]]] --> double index [0][0] --> [2.0, 1.0] --> 2s^1 + 1s^0 = 2s + 1
# here our transfer function H has one input and 2 outputs
# one input because one column (look at the outermost [], there's one column of the big ones), 2 rows hence two outputs
# tf function works like tf(numerators, denominators)
# here we give a list of numerators, and then our list of denominators since we're expecting two outputs
print(H)


'''question 1'''
A = np.array(([[-1.2, 0, 0],
               [0.4, -1.2, -5.0],
               [0, 1, 0]]))
B = np.array(([[0.3], 
               [0], 
               [0]]))
C = np.array(([[0, 1, 0],
               [0.1, 0, 1]]))
D = np.array(([[0], 
               [0]]))

sys = ss(A, B, C, D)  # getting the state-space system
h = tf(sys)  # converting it to a transfer function

# we can index the functions how we'd index a numpy array
# h[i, j] gives the tf from input j to output i aka h[output, input]
# print("output 1:", h[0, 0])
# print("output 2:", h[1, 0])

# since the number of coeffs in the numerator tells us the order - 1 we can find the order of num from the len of h.num
# have to double index num[0][0] because the values are stored in a list in a list in a list lol
# print("order of num 1st tf", len(h[0, 0].num[0][0]) - 1)
# print("order of num 2nd tf", len(h[1, 0].num[0][0]) - 1)

for pole in poles(h):
    if pole.imag == 0:
        print(pole.real)

'''question 2'''
# coefficients
b0 = 0.8
b1 = 0.1
b2 = 0.5
a0 = 2.3
a1 = 6.3
a2 = 3.6
a3 = 1.0

s = tf([1,0], [1])  # defining our laplace variable
h = (b0 + b1*s + b2*s**2) / (a0 + a1*s + a2*s**2 + a3*s**3)

# we want a ss with two outputs 
# output1 is the transfer function so just h
# output2 is the derivative of the first output aka h*s
H =  tf([[h], [h * s]])
# overarching list is #inputs, sublists inside that overarching list are #outputs corresponding to that input
sys = ss(H)

print(sys)