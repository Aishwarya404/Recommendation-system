import numpy
import math

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

c, r, r_m = 18, 6040, 3952
movies = [movieList[i][0] for i in range(len(movieList))]
users = [userList[i][0] for i in range(len(userList))]
genres= [ 'Action','Adventure','Animation','Children','Comedy', 'Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War','Western']

IDF = [0 for x in range(c)]
movieLen = 3883
count = 0

for g in range(c) :
    for m in movieList :
        if genres[g] in m[2] :
            count+=1
    IDF[g] = math.log10(movieLen/count)
    count = 0

print "-----------------IDF--------------", IDF

 # time python calc_idf.py