import control.matlab as c
from sympy import Symbol, apart

s = c.tf([1,0], [1])  # laplace variable 

'''question 4'''
# since we're doing this a lot let's just a make a neat function
def num_den(h):
    print(f"num = {h.num[0][0]}")
    print(f"den = {h.den[0][0]}")
    
K1 = 1
h1 = 5 / (s**2 + 3*s + 5)
g = K1 * (1 + 0.2/s)

# 1. just changing inputs so we ignore disturbance and do normal feedback loop y/u
heq1 = ((h1*g) / (1 + h1*g)).minreal()
print("1")
num_den(heq1)

# 2. still ignore disturbance, just looking at effect of G on u (aka up until what comes out of G, we'll call it a)
# want to find transfer function for output/input = a/u
# a = e*G = (u - y) * G where y = H1*a 
# a = (u - H1*a) * G so a * (1 + H1*G) = u*G 
# a/u = G / (1 + H1*G)
print("2")
heq2 = (g / (1 + h1*g)).minreal()
num_den(heq2)

# 3. just disturbance to output so y/d
# feedforward: d to y is just H1
# feedback we go to this summation point so H1 * G
print("3")
heq3 = (h1 / (1 + h1 * g)).minreal()
num_den(heq3)

# 4. from d to result of G which we called a so a/d, we set u=0
# a/d = a/u * u/y * y/d 
#     = (g / (1 + h1*g)) * ((1 + h1*g) / (h1*g)) * (h1 / (1 + h1 * g))
#     = g * 1/(h1*g) * h1 / (1 + h1 * g)
#     = g*h1 / (h1*g * (1 + h1*g))
#     = 1 / (1 + h1*g)
print("4")
heq4 = (1 / (1 + h1 * g)).minreal()
num_den(heq4) 

'''question 3'''
# without d for y/u: feedforward = G*H1, feedback = G*H1 so y/u = (G*H1) / (1 + G*H1)
# now for the d part with d/y: feedforward = H1, feedback = H1*G so y/d = H1 / (1 + G*H1)
# y = u * ((G*H1) / (1 + G*H1)) + d * (H1 / (1 + G*H1)) = (u*G*H1 + d*H1) / (1 + G*H1)
# since we're adding we definitely have parallel branches -- 4 is correct and 5 is incorrect
# 1 gives is the same thing yay

'''question 2'''
# K1 = 0.5
# K2 = 2.1
# h1 = K1 / (2 + s)
# h2 = (1 + 0.4*s) / (s**2 + 3*s + 6)
# h3 = K2 / (9 + s)

# h = (h2 * h1 + h2 * h3).minreal()
# print(f"num = {h.num}")
# print(f"den = {h.den}")

'''question 1'''
# h1 = (1 + 0.4*s) / (s*(s**2 + 3*s + 6))
# K1 = 1
# h2 = K1 / (1 + 0.1*s)

# # feed-forward path: H1 and the feedback path: H2 
# h = h1.feedback(h2)

# print(f"num = {h.num}")
# print(f"den = {h.den}")