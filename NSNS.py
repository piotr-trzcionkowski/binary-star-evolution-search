#!/usr/bin/env python3

import numpy as np
import sys
import subprocess

#f = open("collected.data", 'w')
#f.write("#      Tmax       M1       M2 log10(P)   e\n")
#f.close()

M1 = np.linspace(1, 20, 20)
M2 = np.linspace(10, 20, 11)
T = [10000]
P = np.linspace(1, 300, num=100)

def calc(M1, M2, T, p):
	breaker = False
	g=open("wyniki.dat", 'w')
	for t in T:
		for p in P:
			for m1 in M1:
				for m2 in M2:
					b = open("binary.in", 'w')
					b.write("%f %f %f %f 1 1 0.001 0.0\n" % (m1, m2, t, p))
					b.write("0.5 0.0 1.0 3.0 0.5\n")
					b.write("0 1 0 1 0 1 3.0 29769\n")
					b.write("0.05 0.01 0.02\n")
					b.write("190.0 0.125 1.0 1.5 0.001 10.0 -1.0\n")
					b.close()
					f=open("bevo.dat", 'w')
					subprocess.call("./bse", stdout=f)
					f.close()

					TMax, k1, k2, m_1, m_2, per, SEP = np.genfromtxt("binary.dat", usecols=(0, 1, 2, 3, 4, 16, 17), skip_footer=2, unpack=True)
					#print(TMax[d], T[i])
					d=-1
					while (TMax[d] != TMax[0]):
						if (k1[d] == 13) and (k2[d] ==13) and (per[d] < 0.000913242) and (per[d] > 0.000001) and (SEP[d] > 0):
							g.write("%f %f %f %f %f %f %f %f %f %f\n" %(TMax[d], p, m1, m2, k1[d], k2[d], m_1[d], m_2[d], m_1[d]+m_2[d], per[d]))
							subprocess.call('cp -r ./bevo.dat ./outputs/%i-%i-%f.dat' %(m1, m2, p), shell=True)
#							print("%f %f %i %i %i %i %f %f\n" %(TMax[d], p, m1, m2, k1[d], k2[d], per[d], SEP[d]))
#							breaker = True
							break
						d=d-1
					if (breaker == True):
						break
				if (breaker == True):
					break
			if (breaker == True):
				break
		if (breaker == True):
			break
	g.close()


calc(M1, M2, T, P)