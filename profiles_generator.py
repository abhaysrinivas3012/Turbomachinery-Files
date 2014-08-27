import sys
from numpy import *

nthrow  = int(sys.argv[2])
nextrow = nthrow+1 

Tt0     = 288.15		#Inlet Total Temperature
Pt0     = 101325		#Inlet Total Pressure
counter = 0
name1   = 'pt_row'+ str(nthrow) +'.csv'
name2   = 'tt_row'+ str(nthrow) +'.csv'
name3   = 'xcomp_row'+ str(nthrow) +'.csv'
name4   = 'ycomp_row'+ str(nthrow) +'.csv'
name5   = 'zcomp_row'+ str(nthrow) +'.csv'
z       = open('temp1.txt','w')
p       = open('temp2.txt','w')
PT      = open(name1,'w')
TT      = open(name2,'w')
ALFA    = open(name3,'w')
BETA    = open(name4,'w')
PHI     = open(name5,'w')

nthrow  = int(sys.argv[2])
nextrow = nthrow+1 

infile = open(sys.argv[1])

with open(sys.argv[1]) as input_data:
	for line in input_data:
		if line.strip() == "Blade Row #:          " + str(nthrow):
			break
	for line in input_data:
		if line.strip() == "Blade Row #:          " + str(nextrow):
			break
		z.write(line)

z.close()
		
with open('temp1.txt','r') as input_data:
	for line in input_data:
		#counter+= 1
		if line.strip() == "Inlet Conditions":
			break
	for line in input_data:
		if line.strip() == "Exit Conditions":
			break
		p.write(line)
	
p.close()
	
infile = open('temp2.txt','r+')
infile.readline()

J = []
Xm = []
Rm = []
Pt = []
Tt = []
Ps = []
Ts = []
Mabs = []
Mrel = []
Alpha = []
Beta = []
Phi = []
Vx = []
Mfrac = []

for data in infile:
	numbers = data.split()
	counter += 1
	print "counter",counter
	if counter == 21:
		break
	j = float(numbers[0])
	r = float(numbers[2])
	p = float(numbers[3])
	t = float(numbers[4])
	a = float(numbers[9])
	b = float(numbers[10])
	i = float(numbers[11])
	Rm.append(r)
	Pt.append(p)
	Tt.append(t)
	Alpha.append(a)
	Beta.append(b)
	Phi.append(i)
	
PT.write('R	PT')
col1 = array(Rm)
col2 = array(Pt)
col2 = col2*Pt0
output = vstack((col1, col2)).T
savetxt(name1,output,fmt = '%2.3f',header = "R")

TT.write('R TT')
col1 = array(Rm)
col2 = array(Tt)
col2 = col2*Tt0	
print col2
output = vstack((col1,col2)).T
savetxt(name2,output,fmt = '%2.3f',header = "R")

Alpha = array(Alpha)		#Converting list to array
Alpha = Alpha*pi/180		#Converting from degrees to radians

Beta = array(Beta)
Beta = Beta*pi/180

Phi = array(Phi)
Phi = Phi*pi/180

ALFA.write('R	Vr')
col1 = array(Rm)
col2 = sin(Phi)*cos(Alpha)
output = vstack((col1, col2)).T
savetxt(name3,output,fmt = '%2.5f',header = "R")
			
BETA.write('R	Vt')
col1 = array(Rm)
col2 = sin(Alpha)
output = vstack((col1, col2)).T
savetxt(name4,output,fmt = '%2.5f',header = "R")

PHI.write('R	Vz')
col1 = array(Rm)
col2 = cos(Phi)*cos(Alpha)
output = vstack((col1, col2)).T
savetxt(name5,output,fmt = '%2.3f',header = "R")