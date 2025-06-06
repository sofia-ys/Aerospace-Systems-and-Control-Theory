import control.matlab as c

s = c.tf([1,0], [1])
h = 1/(2*s + 1)