import numpy.random as rnd

'''state'''
# so our number random generator generates numbers in a sequence
# this sequence is defined by the state we're currently in
xr = rnd.get_state()  # here we're saving this start point of random numbers as the variable xr
# if we later want to return to this same sequence of random numbers we can simply say rnd.set_state(xr)

'''rand'''
# rnd.rand() will create random numbers via a uniform distribution on [0,1) where each number has an equal probability
# rnd.rand(3) can output [0.42, 0.92, 0.13] which is 3 random numbers on via a uniform distribution

'''randn'''
# rnd.randn() will create numbers on a normal (also called gaussian) distribution which has a mean of 0 and a stdev of 1
# most random numbers will be close to 0 with extreme values being less and less likely 
# rnd.randn(3) can output [0.3, -1.2, 0.8]

'''randint'''
# rnd.randint(low, high) will create random numbers based on a uniform distribution between the specified low and high values [low, high)
# rnd.randint(1, 5, size=3) can output [1, 4, 2]