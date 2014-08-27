from matplotlib.pylab import *
from numpy import *
#from efficiency import efficiency

gamma = 1.4
gam = (gamma-1.)/gamma
PR = array([1.202699, 1.245618, 1.286069, 1.301606, 1.318778, 1.331579])
TR = array([1.063539, 1.073113, 1.081921, 1.085347, 1.089198, 1.092167])
mdot = array([0.7848303, 0.7741172, 0.7567925, 0.7475252, 0.7353464, 0.7241184])
mdot = mdot * 80
eff = array([]) 

def efficiency(x,y):
	return (PR**gam-1)/(TR-1)

eff = efficiency(PR,TR)
print eff

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