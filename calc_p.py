import numpy
import math
import calc_idf

movieList = calc_idf.movieList
userList = calc_idf.userList
ratingList = calc_idf.ratingList
movies = calc_idf.movies
users = calc_idf.users
genres= calc_idf.genres
IDF = calc_idf.IDF
c = calc_idf.c
r = calc_idf.r
u = calc_idf.user

p = [[0 for x in range(c)] for y in range(r)] 
total_genres = [0 for y in range(r)]

for rating in ratingList:
	user = int(rating[0])-1
	row_genre = rating[3].split('|')
	for genre in row_genre:
		genre_index= int(genres.index(genre))
		p[user][genre_index] += int(rating[2])

	total_genres[user] += len(row_genre)*int(rating[2])
	
for i in range(r):
	for j in range(c):
		p[i][j] = (float(p[i][j])/float(total_genres[i]))


user_unique_genres = [0 for x in range(r)]

for i in range(r):
	for j in range(c):
		if p[i][j]!=0 :
			user_unique_genres[i] += 1

sum = 0
for i in range(r):
	#find normalised values
	for j in range(c):
		sum += float(p[i][j])
	for j in range(c):
		if sum!= 0:
			p[i][j] = p[i][j]/sum
	#find avg of normalised values and append at last
	w_sum = 0
	for j in range(c):
		w_sum += p[i][j]
	# p[i].append(float(w_sum)/float(c))
	p[i].append(float(w_sum)/float(user_unique_genres[i]))
	sum=0 
# sum = 0
# for i in range(r):
# 	for j in range(c):
# 		sum += float(p[i][j])
# 	# print sum
# 	for j in range(c):
# 		# print j
# 		if sum!= 0:
# 			p[i][j] = p[i][j]/sum
# 		# print j
# 	p[i].append(float(sum)/float(c))
# 	sum=0 

# for u in p:
# 	print u
print "********** P **************"
# print p[u-1]
for g in genres:
	genre_index= int(genres.index(g))
	print g," : ",p[u-1][genre_index]
# time python calc_p.py