# Calculating Tasc uncertainties for simulated dataset (INJ 3)

import numpy as np
import corner

# mid-point of observation
t_0 = 600098990.958 

gamma = np.random.normal(1.6341, 2*0.00056939, 1000000)
omega = np.random.normal(9.2367e-05, 2*2.1276e-09, 1000000)
tasc = np.ones(len(gamma))*t_0 - gamma/omega

quantile = [0.05, 0.16, 0.5, 0.84, 0.95]

n = corner.quantile(tasc, quantile)
print("1 sigma interval [{},{}]".format(n[1],n[3]))
print("2 sigma interval [{},{}]".format(n[0],n[4]))
print("inj_tasc_std = {}, {}".format(n[2]-n[0],n[4]-n[2]))
print("inj_tasc = {}".format(n[2]))


# Recovered parameters (output from loudest_candidate_props.m)

rec_omega =  9.2368e-05
rec_gamma =  1.6350

rec_tasc = t_0 - rec_gamma/rec_omega
print("tasc = {}".format(rec_tasc))
