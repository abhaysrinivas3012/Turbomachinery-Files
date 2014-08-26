import sys
from numpy import *

z = open('temp1.txt','r+')
p = open('temp2.txt','r+')
PT = open('pt.csv','w')
TT = open('tt.csv','w')
ALFA = open('xcomp.csv','w')
BETA = open('ycomp.csv','w')
PHI = open('zcomp.csv','w')

infile = open(sys.argv[1])

with open(sys.argv[1]) as input_data:
	for line in input_data:
		if line.strip() == "Blade Row #:          11":
			break
	for line in input_data:
		if line.strip() == "Blade Row #:          12":
			break
		z.write(line)
counter = 0		
with open('temp1.txt') as input_data:
	for line in input_data:
		#counter+= 1
		if line.strip() == "Inlet Conditions":
			break
	for line in input_data:
		if line.strip() == "Exit Conditions":
			break
		p.write(line)
		
infile = open('temp2.txt')
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
output = vstack((col1, col2)).T
savetxt('pt.csv',output,fmt = '%2.3f',header = "R")
TT.write('R TT')
col1 = array(Rm)
col2 = array(Tt)
col2 = col2*288.15
print col2
output = vstack((col1,col2)).T
savetxt('tt.csv',output,fmt = '%2.3f',header = "R")


			
