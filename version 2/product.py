import numpy
import math
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
# item based . let target be user 4
# rated is unsorted set of movies watched by target
rated = []
for i in range(len(ratingList)) :
	if ratingList[i][0] == '4':
		rated.append(ratingList[i][1])

enemy1 = []
movieslevel1 = []
for m in movies:
	if m not in rated:
		movieslevel1.append(m)

for i in rated :
	for j in movieslevel1 :
		if j not in enemy1:
			k = prod_sim.findSim(i,j)
			print "first ",i,j,k
			if k > 0.7 :
				enemy1.append(j)

print "#############",len(enemy1)
for j in enemy1:
	print j,movieList[int(j)]

# enemy2 = []
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

# print "&&&&&&&&&",len(enemy2)


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
avg_rating_movie = [0 for x in range(r_m)]
count_users_movie = [0 for x in range(r_m)]
for rating in ratingList:
	avg_rating_movie[int(rating[1])-1]+=rating[2]
	count_users_movie[int(rating[1])-1]+=1

for i in range(len(avg_rating_movie)):
	avg_rating_movie[i] = avg_rating_movie[i]/count_users_movie[i]

sum=0
count=0
for item in enemy1:
	

# time python product.py