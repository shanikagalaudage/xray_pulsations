import numpy as np
import corner

intervals = [0.025,0.975]

# cygx2 values

print("*** CygX-2 parameters ***")

K2 = np.random.normal(86.4,0.6,1000000)
q = np.random.normal(0.34,0.01,1000000)
P = np.random.normal(9.844766*24*60*60, 0.000073*24*60*60, 1000000)
K1 = K2*q

asini = (K1/(3*10**5))*P/(2*np.pi)
qval = corner.quantile(asini, intervals)
print("asini 2 sigma interval [{},{}]".format(qval[0],qval[1]))

Porb = np.random.normal(9.844766, 0.000073, 1000000)
Porb = Porb * 24. * 60. * 60.
qval_Porb = corner.quantile(Porb, intervals)
print("Porb 2 sigma interval [{},{}]".format(qval_Porb[0],qval_Porb[1]))

T0 = np.random.normal(602668183,750,1000000)
Tasc = T0 - np.median(Porb)/4.
print(np.median(Porb)/(24*60*60))
qval = corner.quantile(Tasc, intervals)
print("Tasc 2 sigma interval [{},{}]".format(qval[0],qval[1]))
qval_T0 = corner.quantile(T0, intervals)


n0 = np.median(Tasc)

Porb_med = np.median(Porb)
T0_med = np.median(T0)

uPorb = qval_Porb[1] - Porb_med
uT0 = qval_T0[1] - T0_med

t_epochs = [551735827,974186811,976792264]
for te in t_epochs:
    t = n0
    n = 0
    if te > t:
        while t < te:
            t += Porb_med 
            n += 1
        if (t - te) > Porb_med/2:
            t -= Porb_med
            n -= 1
    else:
        while t > te:
            t -= Porb_med
            n += 1
        if (te - t) > Porb_med/2:
            t += Porb_med
            n -= 1

    te_uncertainty = np.sqrt(n**2*uPorb**2 + uT0**2 + 2*n*1.15*10**(-8))
    print("Cloest Tasc = {}".format(t))
    print("Range of Tasc is [{}, {}]".format(t-te_uncertainty,t+te_uncertainty))
    print("Uncertainty in phase = {}".format(2*np.pi*te_uncertainty*2/Porb_med))


# scox1 values

print("*** Sco X-1 parameters ***")

Porb = np.random.normal(0.7873132, 0.0000005, 1000000)
Porb = Porb * 24. * 60. * 60.
qval_Porb = corner.quantile(Porb, intervals)
print("Porb 2 sigma interval [{},{}]".format(qval_Porb[0],qval_Porb[1]))

T0 = np.random.normal(974433630,50,1000000)
Tasc = T0 - np.median(Porb)/4.
#print(np.median(Porb)/(24*60*60))
qval = corner.quantile(Tasc, intervals)
print("Tasc 2 sigma interval [{},{}]".format(qval[0],qval[1]))
qval_T0 = corner.quantile(T0, intervals)


n0 = np.median(Tasc)

Porb_med = np.median(Porb)
T0_med = np.median(T0)

uPorb = qval_Porb[1] - Porb_med
uT0 = qval_T0[1] - T0_med

t_epochs = [599635471,567787966,580523651,583396353,613041597]

for te in t_epochs:
    t = n0
    n = 0
    if te > t:
        while t < te:
            t += Porb_med
            n += 1
        if (t - te) > Porb_med/2:
            t -= Porb_med
            n -= 1
    else:
        while t > te:
            t -= Porb_med
            n += 1
        if (te - t) > Porb_med/2:
            t += Porb_med
            n -= 1

    te_uncertainty = np.sqrt(n**2*uPorb**2 + uT0**2 + 2*n*3*10**(-14))
    print("Range of Tasc is [{}, {}]".format(t-te_uncertainty,t+te_uncertainty))
    print("Uncertainty in phase = {}".format(2*np.pi*te_uncertainty*2/Porb_med))
