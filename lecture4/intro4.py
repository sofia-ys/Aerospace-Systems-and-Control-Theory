import control.matlab as c
from sympy import Symbol, apart

# creates a transfer function c.tf([numerator], [denominator])
# [num] is a list of the coeffs of numerator polynom in descending powers of s
# [denom] is list of coefs for denominator polynomial 
s = c.tf([1,0], [1])  # laplace variable --> s = (1s + 0)/(1) = s/1 = s
# aka we're calling a transfer function that acts just as the laplace variable s

# building the transfer function h using our variable s
# because s is a transfer function object, we can now do algebraic operations that construct new transfer functions
h = 1/(2*s + 1)  # h: transfer function

'''combining transfer functions'''
# for the simple block diagram U --> [H1(s)] --> Y1 = U2 --> [H2(s)] --> Y
# equivalent transfer function from this block diagram is H(s) = H1(s) * H2(s)
# since U --> Y is U * H1(s) * H2(s) = Y hence the transfer function can be combined
# we can define two transfer functions h1 and h2
h1 = 1/((1 + 2*s) * (1 + 3*s))
h2 = 1 /(1 + 3*s)

# for transfer functions that add up for a final result
# U --> H1(s) --> Y1
# U --> H2(s) --> Y2
# Y = Y1 + Y2 therefore U --> Y1 + Y2 --> Y therefore U --> H1(s) + H2(s) --> Y
# the equivalent transfer function is H(s) = H1(s) + H2(s)

# print(h1 + h2)  # this will print a correct result (in terminal window it is numerator ----- denominator)
# however, it is not simplified so stuff that cancels out doesn't 
# aka (6s^2 + 8s + 2) / (18s^3 + 21s^2 + 8s + 1)  = 2(s+1) / (6s^2 + s + 1) when simplified, which the program doesn't automatically do
# ^^ since s = 1/3 is a root, (3s + 1) is a factor so we can divide the denom by (3s + 1) or multiply fraction by 1 / (1 + 3s) to get simplified version
# print((h1 + h2).minreal())  # this is a goated version which gives the simplied result 

# help function will act on the object h1 (which is a transferfunction object)
# help will show its class documentation, its attributes, and methods
# attributes are the data stored inside the object (aka variables tied to the object)
# methods are the functions that the object can perform
# help(h1)  
# attributes: h1.num gives the numerator polynomial coeefs, h1.den gives the denominator poly coeffs
# methods: h1.minreal() simplifies the tf etc

# for a closed loop H(s) = (H1(s)) / (1 + H1(s)H2(s)) 
# numerator is the feed-forward path (from Yref to Y)
# denominator is 1 + feedback path (Yref back to Yref)
# print(h1.feedback(h2))  # h1 is the feedforward path, h2 is the feedback path
# for more complex systems you have to define h2 = G2*G3 etc
# h1/(1 + h1*h2) = (h1/(1 + h1*h2)).minreal() = h1.feedback(h2)
# feedback function is more robust !

'''partial fraction expansion'''
# using sympy to solve our partial fractions
s = Symbol("s")  # defining the symbol variable s

# the step input signal
u = 1/s  # the LT of the unit step u(t) = 1 where L{1} = 1/s
# the system transfer function
h = (s+2)/(s**3 + 3*s**2 + 2*s + 5)

# the partial fraction expansion
# print(apart(h*u, s))  # apart(expression, s) 
# apart does a partial frac decomp of the rational function given in expression wrt variable s