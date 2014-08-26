from matplotlib.pylab import *
from numpy import *

infile = open("C:\Users\Acer\SkyDrive\eee_rotor6\outlet.txt","r")
Rm = []
PT = []
TT= []
alpha_m = []
beta_m = []
phi = []

for line in infile:
	data = line.split()
	rm = float(data[0])
	pt = float(data[1])
	tt = float(data[2])
	a = float(data[3])
	b = float(data[4])
	p = float(data[5])
	Rm.append(rm)
	PT.append(pt)
	TT.append(tt)
	alpha_m.append(a)
	beta_m.append(b)
	phi.append(p)
	
fig = 1
figure(fig, figsize=(10, 6))
fig1 = plot(Rm,PT,"-o")
xlabel("Mean Radius")
ylabel("Outlet Total Pressure") 
title("Outlet PT")
fig += 1
figure(fig, figsize=(10, 6))
fig2 = plot(Rm,TT,"-o")
xlabel("Mean Radius")
ylabel("Outlet Total Temperature")
title("Outlet TT")
fig += 1
figure(fig, figsize=(10, 6))
fig2 = plot(Rm,alpha_m,"-o")
xlabel("Mean Radius")
ylabel("Alpha_m(rad)")
title("Outlet Alpha")
fig += 1
figure(fig, figsize=(10, 6))
fig2 = plot(Rm,beta_m,"-o")
xlabel("Mean Radius")
ylabel("Beta_m(rad)")
title("Outlet Beta")
fig += 1
figure(fig, figsize=(10, 6))
fig2 = plot(Rm,phi,"-o")
xlabel("Mean Radius")
ylabel("Phi(rad)")
title("Outlet Phi")

show()