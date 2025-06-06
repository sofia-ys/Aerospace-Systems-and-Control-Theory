import numpy as np
import scipy.linalg as la
import numpy.random as rnd
'''question 6'''
a = np.zeros((3,4))
# print(np.size(a))
# print(dir(a))
print(locals())

'''question 5'''
# rnd.seed(5)
# a = np.transpose(rnd.rand(5,5))  # 5x5 random num matrix with uniform dist (transposed)
# t = np.transpose(la.toeplitz(np.arange(1, 6)))  # creating a toeplitz matrix (transposed)
# final = np.vstack((a, t))
# final_sum = np.sum(final[:,0])  # takes first element of every row (aka first column)
# print(final_sum)

'''question 4'''
# rnd.seed(6)
# a = np.matrix.round(rnd.randn(5,5))  # random matrix 5x5, then everythign rounded to integers
# rowvector = np.arange(-2,3).reshape((1,5))
# columnvector = np.arange(0,6).reshape((6, 1))
# a = np.vstack((a, rowvector))  # adding the rowvector "vertically" aka stacking it beneath
# a = np.hstack((a, columnvector))  # adding horizontally -- stacking it to the side
# nonzero = np.count_nonzero(a)
# print(nonzero)

'''question 3'''
# rnd.seed(4)
# a = rnd.rand(6,6)  # uniformly distributed random number matrix of 6 rows, 6 columns
# v = np.array([2, 3, 4, 5, 6, 7])
# a[4, :] = v  # replacing 5th row with this vector we made
# sum_elements = np.sum(a)
# print(sum_elements)

'''question 2'''
# size = 21
# identity = np.identity(size)  # making an identity matrix of size 21
# trace = np.trace(identity)  # haha funny fast way
# print(trace)

# # manual way alhamdullilah 
# trace = 0
# for i in range(size):
#     trace += identity[i, i]  # only diagonal positions aka where i = i
# print(trace)

'''question 1'''
# rnd.seed(3)  # setting the seed to 3
# a = rnd.rand(15, 7)  # rand(rows, columns)
# b = np.sum(a[:,5])  # slicing to get all the numbers in the 6th column and then summing them
# print(b)