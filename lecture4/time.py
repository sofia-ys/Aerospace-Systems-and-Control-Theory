import control as c
import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, apart

'''time step'''
# transfer function
H = c.tf([10], [1, 2, 5]) * c.tf([1], [1, 5])  # H = 10 / (s^3 + 7s^2 + 15s + 25)

# for a time response we need a time signal
t = np.arange(0, 60.1, 0.1)

# size of time step is dependent on the system that we're calculating the response for (aka the transfer function)
# zeros are the values of s in the Laplace domain that make the numerator = 0
# zeros show frequencies where system output is suppressed/reduced (aka where H(s) = 0)
# poles are the values of s that make the denom zero
# poles determine the stability, speed and oscillations of the system (where the system repsonse grows/decays/oscillates) 
c.pzmap(H)  # generates poles and zeros map for H on a real-imaginary plane
plt.show()

# for the given H(s), the poles are at -5, at -1 -2i and -1 +2i (aka one real pole and a pair of complex conjugates)

# the impulse response of the system (aka the system is reacting to an impulse so u = dirac delta  --> U(s) = 1) hence Y(s) = H(s)
# hence for this transfer function H(s), our response is Y(s) = H(s) = 10 / (s^3 + 7s^2 + 15s + 25)
# now to solve for y(t), our time dependent output function we partial fraction it and laplace it back
# specifically for this case we get y(t) = A e^-t sin(2t) + B e^-t cos(2t) + C e^-5t
# that's a sine and cosine scaled by e^-t and then just a decay e^-5t = e^-t/0.2 (5 = 1/0.2) --> this 0.2 is the time constant (scales speed of response)

# for accurate sampling, we need to have a time step much smaller than the period of the sin/cos functions and also smaller than the time constant of the exponential
# two limiting factors: either the frequency of the sin/cos OR the time constant of the expeonential
# time constant is 1/|real pole| --> in this case 1/|-5| = 0.2

# frequency can be found from the complex poles 
# the real part gives the exp for the decay part aka e^-1 from -1 real 
# highest freq from the imaginary part so 2 rad/s angular freq

# time step from time consant is just /10 --> 0.2/20 = 0.02s
# time step from frequency is 1/f where f = angular_freq / 2pi --> time step: (1/f)/10 = (2pi / angular_freq)/10 = (2pi/2)/10 = pi/10

# you take the smallest between time_constant/10 and (1/f)/10 as the time step

'''step and impulse responses'''
# step and impulse responses are responses of a system (aka the outputs) to a step and impulse INPUT

# t, y1 = c.step_response(H,t)  # gives a response and time vector for a step input
# t, y2 = c.impulse_response(H,t)  # also gives response and time vectors but for impulse input
# plt.plot(t, y1, t, y2)
# plt.show()

'''arbitrary input response'''
u = np.minimum(0.1 * t, 1.0)
t, y1 = c.step_response(H, t)
t, y2 = c.forced_response(H, t, u)  # lsim function for an arbirtary input
plt.plot(t, u, t, y1, t, y2)
plt.show()

'''time domain response criteria'''
# time responses of a system to a test signal is how we can define the criteria for acceptance
# Tr rise time is time for wave to go from 0.1 to 0.9 of converged final value
# Tp peak time is time to reach first maxima
# %OS percent overshoot is amount overshoot from final converged value at Tp as a percentage of that steady state value
# Ts settling time is time for damped oscillations to be +/- 2% of steady state value

# for a second-order system, the system response has a lot of different possibilities
# the generalised form of a second-order transfer function is H(s) which depends on the natural freq of the system omega_n and the damping ratio zeta
# H(s) = omega_n^2 / (s^2 + 2 zeta omega_n s + omega_n^2)

# for a step response, the Laplace of the input function L{u} = 1/s 
# hence transfer function of step response is 1/s * H(s) = omega_n^2 / s (s^2 + 2 zeta omega_n s + omega_n^2)

# zeta affects the amplitude of the oscillations
# omega_n scales the response in time (aka stretches the period etc)

# y1 contains the matrix with the result:
# assume that the final value of the response is y1[0, -1]
# ALWAYS check this with a plot, or theoretically with the final value theorem!
# overshoot, in %
overshoot = (y1.max()/y1[-1] - 1) * 100
# peak time, the time when the response reaches its highest peak
# Given that the response is positive (always check with a plot),
# max(y1) is the peak value. Of course, some systems don't have a peak!
tpeak = t[y1.argmax()]
# settling time, to within 5%
# this determines all values out of +/- 5% band, last one is index of
# settling time. The logical_or figures out which values are either too
# high or too low. This returns a truth matrix, using it as index gives the
# times, and with the [-1] the last one of those times is selected
tsettling = t[np.logical_or(y1 > y1[-1]*1.05, y1 < y1[-1]*0.95)][-1]  # indexing last from t where logical condition true
# delay time, the time to reach (commonly) 10 % of the final response
tdelay = t[y1 >= 0.1*y1[-1]][0];
# rise time, 10 % to 90 %
trise = t[y1 >= 0.9 * y1[-1]][0] - tdelay

'''question 1'''
# m = 2  # mass [kg]
# k = 20  # spring coeff [N/m]
# b = 5  # damping coeff [Ns/m]
# input -- force f, output -- displacement y
# DE: mx.. + bx. + kx = f
# LT: ms^2 X + bsX + kX = F
# transfer function is output/input = X/F = ms^2 + bs + k

s = c.tf([1,0], [1])  # laplace variable
H = 1 / (2*s**2 + 5*s + 20)

'''question 2'''
poles = c.poles(H)
# poles tell us the frequency so we can get a good time step -- time = (2pi/pole)/10
dt = (2 * np.pi / poles.imag[0]) / 10000

t = np.arange(0, 10 + dt, dt)
t, y1 = c.step_response(H,t)  # getting step response from the built in function yay
# seeing the grpah to play around with the max time
plt.plot(t, y1)
plt.show()

# overshoot
peak = np.max(y1)
settled = y1[-1]
overshoot = (peak/settled - 1) * 100
print(overshoot)

# rise time
ten = np.where(y1 >= 0.1 * y1[-1])[0][0]  # first instance in y1 where the value is >= 0.1 * converging value
ninety = np.where(y1 >= 0.9 * y1[-1])[0][0]
rise = t[ninety] - t[ten]
print(rise)

# delay time
delay = t[ten]
print(delay)

# settling time
settle_range = np.where((y1 > 1.05*y1[-1]) | (y1 < 0.95*y1[-1]))[0][-1]  # last time we exit the +/- 5% band
settle = t[settle_range]
print(settle)

'''question 3'''
s = c.tf([1,0], [1])
h_rd = 9 / (s * (s + 1.4))  # roll dynamics transfer function
t = np.arange(0, 20.01, 0.01)

settling_lst = []
for k in np.arange(0.5, 3.5, 0.5):
    h_ap = k / (s + 10)  # autopilot transfer functino
    H = (h_rd * h_ap) / (1 + h_rd * h_ap)  # closed loop transfer function
    t, y = c.step_response(H, t)  # step response
    
    plt.plot(t,y)
    
    # settling time
    settle_time = t[np.where((y > 1.15*y[-1]) | (y < 0.85*y[-1]))[0][-1]]  # last time we exit the +/- 15% band
    settling_lst.append((float(k), float(settle_time)))
    
print(settling_lst)

plt.show()