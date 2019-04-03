import numpy
import math
import calc_p

def similarity(u1,u2):
    p = calc_p.p
    result = 0    
    den1 = 0
    den2 = 0
    den = 1
    u1 = int(u1)-1
    u2 = int(u2)-1

    for i in range(len(p[0])-1):
        if p[u1][i]!=0 and p[u2][i]!= 0:
            result = result + ((p[u1][i]-p[u1][len(p[0])-1]) * (p[u2][i]-p[u2][len(p[0])-1]))
            #result = result + ((p[int(u1)-1][i]) * (p[int(u2)-1][i]))
        if p[int(u1)-1][i]!=0:
            den1 = den1 + ((p[u1][i]-p[u1][len(p[0])-1]) * (p[u1][i]-p[u1][len(p[0])-1]))
            #den1 = den1 + ((p[int(u1)-1][i]) * (p[int(u1)-1][i]))
        if p[int(u2)-1][i]!=0:
            den2 = den2 + ((p[u2][i]-p[u2][len(p[0])-1]) * (p[u2][i]-p[u2][len(p[0])-1]))
            #den2 = den2 + ((p[int(u2)-1][i]) * (p[int(u2)-1][i]))
    den = math.sqrt(den1*den2)
    if den==0:
        den = 1
    result = result/den
    #print "similarity:",result
    if result == 0:
        result = -1
    # print result
    # print p[u1]
    # print p[u2]
    return result

# print "enter user1"
# u1 = int(input())
# print "enter user2"
# u2 = int(input())
# similarity(u1-1,u2-1)