import numpy
import math
# from joblib import Parallel, delayed
# from multiprocessing import Pool

def findSim(m1,m2):
	result = 0
	den1 = 0
	den2 = 0
	den = 1
	m1 = int(m1)-1
	m2 = int(m2)-1
	for i in range(len(q[0])):
		# if q[m1][i]!=0 and q[m2][i]!= 0:
			result = result + ((q[m1][i]-q[m1][len(q[0])-1]) * (q[m2][i]-q[m2][len(q[0])-1]))
		# if q[m1][i]!=0:
			den1 = den1 + ((q[m1][i]-q[m1][len(q[0])-1]) * (q[m1][i]-q[m1][len(q[0])-1]))
		# if q[m2][i]!=0:
			den2 = den2 + ((q[m2][i]-q[m2][len(q[0])-1]) * (q[m2][i]-q[m2][len(q[0])-1]))
	den = math.sqrt(den1*den2)
	if den==0:
		den = 1
	result = result/den
	return result	


movieList = [i.strip().split('::') for i in open("movies.dat").readlines()]
userList = [i.strip().split('::') for i in open("users.dat").readlines()]
ratingList = [i.strip().split('::') for i in open("ratings.dat").readlines()]

for u in ratingList :
	movieID = int(u[1])
	genre = movieList[movieID-1][2]
	del u[3]
	u.append(genre)

c, r = 18, 6040
p = [[0 for x in range(c)] for y in range(r)] 

movies = [movieList[i][0] for i in range(len(movieList))]
users = [userList[i][0] for i in range(len(userList))]
genres= [ 'Action','Adventure','Animation','Children','Comedy', 'Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War','Western']


#################################FIND IDF##########################
IDF = [0 for x in range(c)]
movieLen = len(movies)
count = 0

for g in range(c) :
    for m in movieList :
        if genres[g] in m[2] :
            count+=1
    IDF[g] = math.log10(movieLen/count)
    count = 0
# print IDF

############################FIND P####################3
total_genres = [0 for y in range(r)]
for rating in ratingList:
	user = int(rating[0])-1
	row_genre = rating[3].split('|')
############################FIND NUME####################3
	for genre in row_genre:
		genre_index= int(genres.index(genre))
		p[user][genre_index] += int(rating[2])
###########################FIND DENO##########
	total_genres[user] += len(row_genre)*int(rating[2])
############################p = (num/den)*idf
for i in range(r):
	for j in range(c):
		p[i][j] = (float(p[i][j])/float(total_genres[i]))*IDF[j]
 
sum = 0
for i in range(r):
	for j in range(c):
		sum += float(p[i][j])
	# print sum
	for j in range(c):
		# print j
		if sum!= 0:
			p[i][j] = p[i][j]/sum
		# print j
	p[i].append(float(sum)/float(c))
	sum=0 

# for u in p:
# 	print u

r_m = 3952 
q = [[0 for x in range(c)] for y in range(r_m)] 
user_unique_genres = [0 for x in range(r)]

for i in range(r):
	for j in range(c):
		if p[i][j]!=0 :
			user_unique_genres[i] += 1

denom = [0 for x in range(r_m)]

for rating in ratingList:
	movie = int(rating[1])-1
	user = int(rating[0])-1
	row_genre = rating[3].split('|')	
	denom[movie] += user_unique_genres[user] 
	for gen in row_genre: 
		g = genres.index(gen)
		q[movie][g] += float(rating[2])*p[user][g]
		# denom[movie]+= float(rating[2])*p

# print denom

for i in range(r_m):
	for j in range(c):
		if denom[i] != 0:
			q[i][j] = (float(q[i][j])/float(denom[i]))*IDF[j]
		else :
			q[i][j] = 0	


print q[0]

sum = 0
for i in range(r_m):
	for j in range(c):
		sum += float(q[i][j])
	# print sum
	for j in range(c):
		# print j
		if sum!= 0:
			q[i][j] = q[i][j]/sum
		# print j
	q[i].append(float(sum)/float(c))
	sum=0 

# item based . let target be user 4
# rated is unsorted set of movies watched by target
rated = []
for i in range(len(ratingList)) :
	if ratingList[i][0] == '4':
		rated.append(ratingList[i][1])

enemy1 = []
# boo = []
# dict = []

for i in rated :
	for j in movies :
		# boo.append(i)
		# boo.append(j)
		# dict.append(boo)
		# boo = []
		if j not in enemy1 and j!=i:
			k = findSim(i,j)
			print k
			if k!=0 and k <= -0.4 :
				enemy1.append(j)

print "#############",len(enemy1)

# print len(dict)
# p = Pool(10)
# p.map(findSim,dict)

enemy2 = []
# boo = []
# dict = []
movieslevel1 = []
for m in movies:
	if m not in enemy1:
		movieslevel1.append(m)

for i in enemy1 :
	for j in movieslevel1 :
		# boo.append(i)
		# boo.append(j)
		# dict.append(boo)
		# boo = []
		if j not in enemy2:
			k = findSim(i,j)
			if k!=0 and k > 0.5 :
				enemy2.append(j)

# # print len(dict)
# # p = Pool(10)
# # p.map(findSim,dict)

print "&&&&&&&&&",len(enemy2)

enemy1 = enemy1 + enemy2

recSet = []
# boo = []
remmovies = []
for m in movies:
	if m not in enemy1:
		remmovies.append(m)

for i in enemy1 :
	for j in remmovies :
		# boo.append(i)
		# boo.append(j)
		# dict.append(boo)
		# boo = []
		if j not in recSet:
			k = findSim(i,j)
			if k!=0 and k <= -0.5 :
				recSet.append(j)

# # print len(dict)
# # p = Pool(10)
# # p.map(findSim,dict)

print len(recSet), recSet


