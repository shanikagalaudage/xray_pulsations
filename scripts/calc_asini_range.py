# Calculating the range of asini for Cyg X2 using K2

import numpy as np
import corner

K2 = np.random.normal(86.4,0.6,1000000)
q = np.random.normal(0.34,0.01,1000000)
P = np.random.normal(9.844766*24*60*60, 0.000073*24*60*60, 1000000)

K1 = K2*q

quantile = [0.05, 0.16, 0.84, 0.95]

#intervals = corner.quantile(K1, quantile)

#print(intervals)

#P = 9.844766*24*60*60

asini = (K1/(3*10**5))*P/(2*np.pi)

n = corner.quantile(asini, quantile)
print("1 sigma interval [{},{}]".format(n[1],n[2]))
print("2 sigma interval [{},{}]".format(n[0],n[3]))

K2_min = 86.4 - 0.6
K2_max = 86.4 + 0.6

q_min = 0.34 - 0.01
q_max = 0.34 + 0.01

K1_min = K2_min*q_min
K1_max = K2_max*q_max 

P_min = (9.844766 - 0.000073)*24*60*60
P_max = (9.844766 + 0.000073)*24*60*60

asini_min = (K1_min/(3*10**5))*P_min/(2*np.pi)
asini_max = (K1_max/(3*10**5))*P_max/(2*np.pi)


print("range = [{},{}]".format(asini_min,asini_max))
