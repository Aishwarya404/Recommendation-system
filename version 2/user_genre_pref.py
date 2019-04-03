import numpy
import math

movieList = [i.strip().split('::') for i in open("movies.dat").readlines()]
userList = [i.strip().split('::') for i in open("users.dat").readlines()]
ratingList = [i.strip().split('::') for i in open("ratings.dat").readlines()]

# for m in movieList :
# 	print m
# print userList
# print ratingList
# print len(movieList)

for u in ratingList :
	movieID = int(u[1])
	# print movieID
	genre = movieList[movieID-1][2]
	del u[3]
	u.append(genre)
	# print u

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

# for u in p:
# 	print u

r_m = 3952 
q = [[0 for x in range(c)] for y in range(r_m)] 
# user_unique_genres = [0 for x in range(r)]

# for i in range(r):
# 	for j in range(c):
# 		if p[i][j]!=0 :
# 			user_unique_genres[i] += 1

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


# print q[0]

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

for u in q:
	print u