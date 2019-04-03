import math
# from joblib import Parallel, delayed
from multiprocessing import Pool



def findSim(pair) :
# def findSim(movie1,movie2) :

	movie1 = pair[0]
	movie2 = pair[1]
	commonRatings = []
	movie1Ratings = []
	movie2Ratings = []
	for i in range(len(ratingList)) :
		if ratingList[i][1] == movie1:
			movie1Ratings.append(ratingList[i])
		if ratingList[i][1] == movie2:
			movie2Ratings.append(ratingList[i])

	#print len(movie1Ratings)
	#print len(movie2Ratings)

	for i in movie1Ratings :
		for j in movie2Ratings :
			if i[0] == j[0] :
				commonRatings.append(i)
				commonRatings.append(j)

	#print len(commonRatings)
	if len(movie1Ratings) == 0 or len(movie2Ratings) ==0 or len(commonRatings) ==0 :
		return 0

	avgMovie1 = 0
	for i in movie1Ratings:
		avgMovie1 += int(i[2])
	avgMovie1 = avgMovie1/len(movie1Ratings)

	avgMovie2 = 0
	for i in movie2Ratings:
		avgMovie2 += int(i[2])
	avgMovie2 = avgMovie2/len(movie2Ratings)

	i=0
	x=0
	while i < len(commonRatings):
		x += (int(commonRatings[i][2]) - avgMovie1) * (int(commonRatings[i+1][2]) - avgMovie2)
		i+=2

	i=0
	y=0
	while i < len(movie1Ratings):
		y+= (int(movie1Ratings[i][2]) - avgMovie1)* (int(movie1Ratings[i][2]) - avgMovie1)
		i+=1

	i=0
	z=0
	while i < len(movie2Ratings):
		z+= (int(movie2Ratings[i][2]) - avgMovie2)* (int(movie2Ratings[i][2]) - avgMovie2)
		i+=1

	if x!=0 and y!=0 and z!=0:
		ans = x/(math.sqrt(y)*math.sqrt(z))
	else:
		ans = 0
	
	print pair,ans

	if ans!=0 and ans < -0.1 :
		enemy1.append(j)

	return


movieList = [i.strip().split('::') for i in open("movies.dat").readlines()]
userList = [i.strip().split('::') for i in open("users.dat").readlines()]
ratingList = [i.strip().split('::') for i in open("ratings.dat").readlines()]

movies = [movieList[i][0] for i in range(len(movieList))]
users = [userList[i][0] for i in range(len(userList))]

# item based . let target be user 4
rated = []
for i in range(len(ratingList)) :
	if ratingList[i][0] == '4':
		rated.append(ratingList[i][1])

enemy1 = []
boo = []
dict = []
for i in rated :
	for j in movies :
		boo.append(i)
		boo.append(j)
		dict.append(boo)
		boo = []
		# k = findSim(i,j)
		# print i,j,k
		# if k!=0 and k < -0.5 :
		# 	enemy1.append(j)
			

print len(dict)
p = Pool(20)
p.map(findSim,dict)

# enemy2 = []
# for i in enemy1 :
# 	for j in movies :
# 		k = findSim(i,j)
# 		if k!=0 and k > 0.5 :
# 			enemy2.append(j)

# print "ool"

# enemy1.extend(enemy2)

# recSet = []
# for i in enemy1 :
# 	for j in movies :
# 		k = findSim(i,j)
# 		if k!=0 and k < -0.5 :
# 			recSet.append(j)

# print "plss"
# print recSet

