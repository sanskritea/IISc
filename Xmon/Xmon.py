import numpy as np
from matplotlib import pyplot as plt

pi = np.pi
GHz = 1e9

# import .txt files data into np array
y_data = np.loadtxt(fname ="/home/sans/y_data2.txt")
n = 101                                     # numbers of points

freq = 2 * pi * y_data[:n , 0] * GHz        # frequency range
y_imag = y_data[:n, 1] # imag(Y11)
y_real = y_data[:n, 2] # reak(Y11)

R_eff = 1 / y_real[:n]                      # Resistance
C_eff = 0.5 / ((freq[:n] ** 2) * 8.89e-9)   # Capacitance
Q = freq[:n] * R_eff[:n] * C_eff[:n]        # Quality factor
T_1 = R_eff[:n] * C_eff[:n]                 # Qubit lifetime

print(R_eff[50])
print(C_eff[50])
print(T_1[50])
print(Q[50])
print(y_data[50, 0])
                    
