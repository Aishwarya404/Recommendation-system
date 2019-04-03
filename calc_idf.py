import numpy
import math
import random

# initialise all lists by reading dat files and their manipulation

movieList = [i.strip().split('::') for i in open("movies.dat").readlines()]
userList = [i.strip().split('::') for i in open("users.dat").readlines()]
ratingList = [i.strip().split('::') for i in open("ratings.dat").readlines()]
# ratingList2 = [i.strip().split('::') for i in open("ratings2.dat").readlines()]

# for u in ratingList :
# 	movieID = int(u[1])
# 	genre = movieList[movieID-1][2]
# 	del u[3]
# 	u.append(genre)

# with open('ratings.dat', 'w') as f:
#     for item in ratingList:
#     	for k in range(len(item)-1):
#     		f.write("%s::" % item[k])
#     	f.write("%s\n" % item[k+1])

# ratingList2.sort(key=lambda x:int(x[1]))
# with open('ratings2.dat', 'w') as f:
#     for item in ratingList2:
#     	for k in range(len(item)-1):
#     		f.write("%s::" % item[k])
#     	f.write("%s\n" % item[k+1])


c, r, r_m, user = 18, 6040, 3952, 4
movies = [movieList[i][0] for i in range(len(movieList))]
users = [userList[i][0] for i in range(len(userList))]
genres= [ 'Action','Adventure','Animation','Children','Comedy', 'Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War','Western']

# movies and ratings of those watched by our user
rated = []
rated_rat = [0 for x in range(r_m+1)]

for i in range(len(ratingList)) :
	if ratingList[i][0] == str(user):
		rated.append(int(ratingList[i][1]))
		rated_rat[int(ratingList[i][1])] = int(ratingList[i][2])

# print rated
# randomly choose 0.2% movies to predict and remove from rated
to_pred = [] 
to_pred_oldrat = [0 for x in range(r_m+1)]
for i in range(int(len(rated)*0.2)):
	x = random.choice(rated)
	rated.remove(x)
	to_pred.append(x)

print to_pred

for i in ratingList:
	if int(i[0]) == user and int(i[1]) in to_pred :
		to_pred_oldrat[int(i[1])] = int(i[2])

for i in ratingList:
	if int(i[0]) == user and int(i[1]) in to_pred :
		ratingList.remove(i)		

for x in to_pred:
	print to_pred_oldrat[x]
# for i in ratingList:
# 	if i[0] == str(user):
# 		print i

IDF = [0 for x in range(c)]
movieLen = 3883
count = 0

for g in range(c) :
    for m in movieList :
        if genres[g] in m[2] :
            count+=1
    IDF[g] = math.log10(movieLen/count)
    count = 0

print "-----------------IDF--------------"
print IDF

 # time python calc_idf.py