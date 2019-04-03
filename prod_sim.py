import numpy
import math
import calc_q

def findSim(m1,m2):
	q = calc_q.q
	result = 0
	den1 = 0
	den2 = 0
	den = 1
	m1 = int(m1)-1
	m2 = int(m2)-1

	for i in range(len(q[0])):
		if q[m1][len(q[0])-1]==1:
			q[m1][len(q[0])-1]=0

		if q[m2][len(q[0])-1]==1:
			q[m2][len(q[0])-1]=0
		if q[m1][i]!=0 and q[m2][i]!= 0:
			result = result + ((q[m1][i]-q[m1][len(q[0])-1]) * (q[m2][i]-q[m2][len(q[0])-1]))
		if q[m1][i]!=0:
			den1 = den1 + ((q[m1][i]-q[m1][len(q[0])-1]) * (q[m1][i]-q[m1][len(q[0])-1]))
		if q[m2][i]!=0:
			den2 = den2 + ((q[m2][i]-q[m2][len(q[0])-1]) * (q[m2][i]-q[m2][len(q[0])-1]))
	den = math.sqrt(den1*den2)
	if den==0:
		den = 1
	result = float(result)/float(den)
	if result == 0:
		result = -1
	# print result
	# print q[m1]
	# print q[m2]
	return result

# print "enter movie1"
# m1 = int(input())
# print "enter movie2"
# m2 = int(input())
# findSim(m1,m2)
 # time python prod_sim.py