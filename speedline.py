from matplotlib.pylab import *
from numpy import *


PR = array([1.20054, 1.23887, 1.277761, 1.292773, 1.308857, 1.3187])
mdot = array([62.67, 61.45, 59.77, 58.91, 57.668, 56.19])
eff = array([80.8, 83.96, 86.11, 86.7, 86.96, 86.73]) 

fig = 1
figure(fig, figsize=(10, 6))
fig1 = plot(mdot,PR,"-o")
xlabel("Inlet Mass Flow Rate(kg/s)")
ylabel("Pressure Ratio") 
title("PR vs Mass Flow")
fig += 1
figure(fig, figsize=(10, 6))
fig2 = plot(mdot,eff,"-o")
xlabel("Inlet Mass Flow Rate(kg/s)")
ylabel("Efficiency")
title("Efficiency vs Mass Flow")

show()