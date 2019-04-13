import numpy
import math
import random
import calc_q
import calc_p
import calc_idf
import prod_sim

movieList = calc_idf.movieList
userList = calc_idf.userList
ratingList = calc_idf.ratingList
movies = calc_idf.movies
users = calc_idf.users
genres= calc_idf.genres
IDF = calc_idf.IDF
c = calc_idf.c
r = calc_idf.r
r_m = calc_idf.r_m
u = calc_idf.user
rated = calc_idf.rated
rated_rat = calc_idf.rated_rat

print "**********PRODUCT BASED************"

rec_movies = []
movieslevel1 = []
for m in movies:
	if int(m) not in rated:
		movieslevel1.append(int(m))

sim_ij = [[0 for x in range(r_m+1)] for y in range(r_m+1)] 

# for i in rated :
# 	for j in movieslevel1 :
# 		if j not in enemy1:
# 			k = prod_sim.findSim(i,j)
# 			print "first ",i,j,k
# 			if k > 0.7 :
# 				enemy1.append(j)
# 				sim_ij[int(i)][int(j)]=k

g = 0

for i in movieslevel1 :
	for j in rated :
		k = prod_sim.findSim(i,j)
		# print "first ",i,j,k
		if k != -1 :
			g+=1
	if g > len(rated)/2:
		rec_movies.append(i)
		sim_ij[i][j]=k
	g=0

# enemy2 = []
# enemy2_sim = []
# movieslevel2 = []
# for m in movies:
# 	if m not in enemy1:
# 		movieslevel2.append(m)

# for i in enemy1 :
# 	for j in movieslevel2 :
# 		if j not in enemy2:
# 			k = prod_sim.findSim(i,j)
# 			print "second ",i,j,k
# 			if k >= 0.5 :
# 				enemy2.append(j)
# 				enemy2_sim.append(k)

# print "&&&&&&&&&",len(rec_movies)


# enemy1 = enemy1 + enemy2
# recSet = []
# remmovies = []
# for m in movies:
# 	if m not in enemy1:
# 		remmovies.append(m)

# for i in enemy1 :
# 	for j in remmovies :
# 		if j not in recSet:
# 			k = prod_sim.findSim(i,j)
# 			print "last ",i,j,k
# 			if k < -0.5 :
# 				recSet.append(j)

# print len(recSet)
# for j in recSet:
# 	print j,movieList[int(j)]
pred_rat = [0 for x in range(r_m+1)]
deno = 0
numo = 0

avgrat = [0 for x in range(r_m+1)]
avgratcount = [0 for x in range(r_m+1)]
for i in range(len(ratingList)):
    avgrat[int(ratingList[i][1])] += int(ratingList[i][2])
    avgratcount[int(ratingList[i][1])] += 1
for i in range(len(movies)):
	if avgrat[int(movies[i])]!=0 and avgratcount[int(movies[i])]!=0:
		avgrat[int(movies[i])] = float(avgrat[int(movies[i])]) / float(avgratcount[int(movies[i])])

print "product based no of rec movies :", len(rec_movies)
# for i in rec_movies:
# 	for j in range(len(ratingList)):
# 		if ratingList[j][1] in rated and ratingList[j][0] == str(u):
# 			numo = numo + (sim_ij[i][j] * (int(ratingList[j][2]) - avgrat[j]))
# 			deno = deno + sim_ij[i][j]
# 	if deno == 0:
# 		pred_rat[i] = avgrat[i] + 0
# 	else:
# 		pred_rat[i] = avgrat[i] + float(numo)/float(deno)
# 	numo = 0
# 	deno = 0
# 	print i
	# print movieList[i-1],pred_rat[i] 


for i in rec_movies:
	for j in rated:
			numo = numo + ( sim_ij[i][j] * (rated_rat[j] - avgrat[j]) )
			deno = deno + sim_ij[i][j]
	if deno == 0:
		pred_rat[i] = avgrat[i] + 0
	else:
		pred_rat[i] = avgrat[i] + float(numo)/float(deno)
	numo = 0
	deno = 0
	# print movieList[i-1],pred_rat[i] 

# print rec_movies
# print "#############",len(enemy1)
# for j in rec_movies:
# 	print j,movieList[int(j)], pred_rat[int(j)]
# print movieList[int(38)], pred_rat[int(38)]
# time python product.py