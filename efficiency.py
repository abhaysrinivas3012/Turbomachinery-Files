""" Program to calculate the efficiency of a compressor """

import sys

try:
	PR = eval(sys.argv[1])			#Pressure Ratio
	
except:
	print "You failed to provide PR value!"
	
try:
	TR = eval(sys.argv[2])			#Temperature Ratio

except:
	print "You failed to provide TR value!"
	
try:
	gamma = eval(sys.argv[3])		#gamma
	
except:
	print "You failed to provide gamma value!"
	
gam = (gamma-1.)/gamma

def efficiency(x,y):
	return (PR**gam-1)/(TR-1)

	
eff = efficiency(PR,TR)
print 'PR=',PR
print 'TR=',TR
print 'gamma=',gamma
print 'efficiency=',eff


#mass_flow = array