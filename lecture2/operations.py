import numpy as np
import numpy.random as rnd
import numpy.linalg as la
'''question 5'''
# rnd.seed(7)
# v = rnd.randn(1000)
# # setting the any number that falls outside of -2 < v < 2 to 0, then coutning how many nonzeros we have
# total = np.count_nonzero(np.where((v > -2) & (v < 2), v, v*0))
# percent = (total / 1000) * 100
# print(percent)

'''question 4'''
# rnd.seed(1)
# a = rnd.randn(20, 70)
# larger2 = np.where(a > 2, a, a*0)  # for values where a>2 we keep them, if a is not >2 then we multiply by 0 to cancel them out
# print(np.sum(larger2))

'''question 3'''
# a = np.arange(0, 5.01, 0.01)
# asum = np.sum(np.sin(a))
# print(asum)

'''question 2'''
# our complex numbers <3
# d = 6 + 3j
# e = -2 + -1j
# f = -4 + -5j

# # neat lil function to get angle since we do it twice
# def get_angle(x):
#     phi = np.degrees(np.atan2(x.imag,x.real))
#     print(phi)

# get_angle(d)  # angle of d
# get_angle(e)  # angle of e
# print(np.absolute(f))  # magnitude of f

'''question 1'''
# rnd.seed(9)
# a = rnd.randn(5,5)
# eigenvalues = la.eig(a)[0]  # eig spits out an array with eigenvalues, then one with the vectors
# eval_abs = np.absolute(eigenvalues)  # getting their magnitude cause of complex numbers
# idx_max = np.argmax(eval_abs)  # gets index of the max value in the eval_abs
# idx_min = np.argmin(eval_abs)
# # we use the index we got to then go back to our eigenvalues thing to find the real part
# print(f"max real: {eigenvalues[idx_max]}\nmin real: {eigenvalues[idx_min]}")