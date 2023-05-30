import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

rcParams["font.serif"] = "Computer Modern"
rcParams["font.family"] = "Serif"
rcParams["text.usetex"] = False
rcParams["legend.fontsize"]=14
rcParams["legend.framealpha"]=0.5
rcParams["legend.frameon"]=True
rcParams["legend.edgecolor"]="white"
rcParams["axes.labelsize"]=14
rcParams["axes.grid"] = True
rcParams["grid.color"] = "black"
rcParams["grid.linewidth"] = 1
rcParams["grid.linestyle"] = "--"
rcParams["grid.alpha"] = 0.3

rcParams["xtick.labelsize"]=12
rcParams["ytick.labelsize"]=12
rcParams["legend.fontsize"]=12
rcParams["axes.labelsize"]=14
rcParams["axes.titlesize"]=20


colours = ["#132E91","#FFAC3B","#C7267C","#357413"]

one = np.loadtxt("amplitudeScoX1dutycycle_cutoff1.txt")
five = np.loadtxt("amplitudeScoX1dutycycle_cutoff5.txt")
ten = np.loadtxt("amplitudeScoX1dutycycle_cutoff10.txt")

# create contours
duty = np.linspace(0.000001,1,100)
tspan = np.linspace(1.00000001,1000,100)


D1 = 8./(np.sqrt(10**9)*0.005**2*500*tspan)

D2 = 8./(np.sqrt(10**9)*0.001**2*500*tspan)

D3 = 8./(np.sqrt(10**9)*0.0005**2*500*tspan)

D4 = 8./(np.sqrt(10**9)*0.002**2*500*tspan)


fig, ax = plt.subplots(figsize=(8,6))

ax.axvspan(0,10,color="k",alpha=0.05)
plt.scatter(one[:,1],one[:,0],marker=".",  s=100, color=colours[0], label='$D_\mathrm{min} = 1\%$')
plt.scatter(five[:,1],five[:,0],marker=".", s=100, color=colours[1], label='$D_\mathrm{min} = 5\%$')
plt.scatter(ten[:,1],ten[:,0],marker=".",  s=100, color=colours[2], label='$D_\mathrm{min} = 10\%$')
plt.plot(tspan,D1,color='k',linewidth=0.5)
plt.plot(tspan,D2,color='k',linewidth=0.5)
plt.plot(tspan,D3,color='k',linewidth=0.5)
plt.plot(tspan,D4,color='k',linewidth=0.5)

ax.text(240, 0.006, '0.05%',rotation=-38, fontsize=10)
ax.text(60, 0.006, '0.1%',rotation=-38,fontsize=10)
ax.text(15, 0.006, '0.2%',rotation=-38,fontsize=10)
ax.text(2.4, 0.006, '0.5%',rotation=-38,fontsize=10)



# label datasets

ax.text(6.12013,0.215,'1', fontsize=12, fontweight='medium')
ax.text(3.0979,0.0934,'3', fontsize=12, fontweight='medium')
ax.text(3.188888,0.1546,'2', fontsize=12, fontweight='medium')
ax.text(3.04,0.27,'4', fontsize=12, fontweight='medium')
plt.plot(10.71,0.152,'x',color='k',markersize=10,markeredgewidth=2)

plt.yscale('log')
plt.xscale('log')
plt.legend(loc='upper right')
plt.xlim(1,500)
plt.ylim(0.004,1)
plt.ylabel("Dutycycle")
plt.xlabel("$T_\mathrm{span}$ [days]")
plt.tight_layout()
plt.savefig("test_amp.png")

