import numpy
import math
import calc_idf
import calc_p

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
p = calc_p.p

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
	# denom[movie] += user_unique_genres[user] 
	for gen in row_genre: 
		g = genres.index(gen)
		q[movie][g] += float(rating[2])*p[user][g]
		# denom[movie]+= float(rating[2])*p

sum = 0
for i in range(r_m):
	#find normalised values
	for j in range(c):
		sum += float(q[i][j])
	for j in range(c):
		if sum!= 0:
			q[i][j] = (q[i][j]/sum)*IDF[j]
	sum = 0

# # print denom
# for i in range(r_m):
# 	for j in range(c):
# 		if denom[i] != 0:
# 			q[i][j] = (float(q[i][j])/float(denom[i]))*IDF[j]
# 		else :
# 			q[i][j] = 0	

movie_genre_count = [0 for x in range(r_m)]

for i in range(r_m):
	for j in range(c):
		if q[i][j]!=0 :
			movie_genre_count[i] += 1

sum = 0
for i in range(r_m):
	#find normalised values
	for j in range(c):
		sum += float(q[i][j])
	for j in range(c):
		if sum!= 0:
			q[i][j] = q[i][j]/sum

	#find avg and append at last 
	v_sum=0
	for j in range(c):
		v_sum += q[i][j]
	#q[i].append(float(v_sum)/float(c))
	if movie_genre_count[i]!=0:
		q[i].append(float(v_sum)/float(movie_genre_count[i]))
	else:
		q[i].append(float(v_sum))
	sum=0 

# sum = 0
# for i in range(r_m):
# 	for j in range(c):
# 		sum += float(q[i][j])
# 	# print sum
# 	for j in range(c):
# 		# print j
# 		if sum!= 0:
# 			q[i][j] = q[i][j]/sum
# 		# print j
# 	q[i].append(float(sum)/float(c))
# 	sum=0 

# for u in q:
	# print u
print q[67]
# print q[2817]
# time python calc_q.py