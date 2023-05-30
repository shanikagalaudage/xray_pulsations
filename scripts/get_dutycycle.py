import numpy as np
import matplotlib.pyplot as plt
import astropy
from astropy.time import Time

source = 'CygX2'# X-ray object (e.g. ScoX1, CygX2)

object_file = source + '_modes.txt'

floats = np.loadtxt(object_file,dtype='float',usecols=(0,2))
strings = np.loadtxt(object_file,dtype='U',usecols=(5,6,7,8,9))

d_t      = floats[:,0]
exposure = floats[:,1]

mode1    = strings[:,0]
mode2    = strings[:,1]
mode3    = strings[:,2]
mode4    = strings[:,3]

obsID    = strings[:,4]

day = d_t/(24.*60.*60.)
exp_day = exposure/(24.*60.*60.)
 
duty = 1
start = day[0]
tspan = 0
tobs = 0


cutoff = 5
fname1 = "obsID_" + source + "dutycycle_cutoff" + str(cutoff) + ".txt"
fname2 = "amplitude" + source + "dutycycle_cutoff" + str(cutoff) + ".txt"
f1 = open(fname1,"w")
f2 = open(fname2,"w")

fraction = cutoff/100.
for i in range(len(day)):
    duty_old = duty
    tspan_old = tspan

    tspan = day[i] + exp_day[i] - start
    tobs += exp_day[i]
    
    duty = tobs/tspan
    if duty > fraction:
        print("{} \n".format(obsID[i]),file=f1)
    else:
        A = 8*(10**-4)/(duty_old*tspan_old*500)**(0.25)
        print("{}  {}  {}".format(duty_old, tspan_old, A),file=f2)
        print("dutycycle = {}, tspan = {}, amplitude = {} \n".format(duty_old, tspan_old, A),file=f1)
        start = day[i]
        tobs = 0
        duty = 1
        print("\n",file=f1)
        print("{} \n".format(obsID[i]),file=f1)
        tspan = exp_day[i] 

A = 8*(10**-4)/(duty*tspan*500)**(0.25) # estimate of sensitivity Eq3 arXiv:2105.13803 (simplified equation originally from arXiv:1412.5938)
print("{}  {}  {}".format(duty, tspan, A),file=f2)
print("dutycycle = {}, tspan = {}, amplitude = {} \n".format(duty, tspan, A),file=f1)
