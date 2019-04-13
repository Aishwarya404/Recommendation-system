import numpy
import math
import random

movie_max_id = 1000
user_max_id = 200
target_user = 199
movieList_test = []
userList_test = []
ratingList_test = []

movieList = [i.strip().split('::') for i in open("movies.dat").readlines()]

for i in movieList:
	if int(i[0]) <= movie_max_id:
		movieList_test.append(i) 

userList = [i.strip().split('::') for i in open("users.dat").readlines()]

for i in userList:
	if int(i[0])<=user_max_id:
		userList_test.append(i)

ratingList0 = [i.strip().split('::') for i in open("ratings.dat").readlines()]

#filtering users from rating list
ratingList1 = []
for r in ratingList0:	
	if int(r[0]) <= user_max_id:
		ratingList1.append(r)
	else: break

#filtering movies from rating list 1
for r in ratingList1:
	if int(r[1]) <= movie_max_id:
		ratingList_test.append(r)

with open('rating_testdata.dat', 'w') as f:
    for item in ratingList_test:
        f.write("%s::" % item[0])
        f.write("%s::" % item[1])
        f.write("%s::" % item[2])
        f.write("%s\n" % item[3])

