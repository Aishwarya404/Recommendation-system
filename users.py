import numpy
import math
import calc_q
import calc_p
import calc_idf
import user_sim

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

print "**********USER BASED************"
ut = users[u-1]
est = []
estsim = []
est2 = []
estsim2 = []
recprodt = [0 for x in range(r_m+1)]
recprodtden = [0 for x in range(r_m+1)]

fset=[]
fsetsim = []

for user in users:
    if user != ut and user not in est:
        ans = user_sim.similarity(ut,user)
        # print "first ", ut,user,ans
        if ans < 0.2:
            est.append(user)
            # fset.append(user)
            # print user
            estsim.append(ans)
            # fsetsim.append(ans)
            # print ans

userslevel1 = []
for u in users:
    if u not in est:
        userslevel1.append(u)

print "enemy set",len(est),"left users:",len(userslevel1)

for user1 in est:
    for user2 in userslevel1:
        if user2 not in est2:
            ans = user_sim.similarity(user1,user2)
            # print "second ", user1,user2,ans
            if ans > 0.8:
                ans = user_sim.similarity(ut,user2)
                # if ans < 0:# enenmy friend might not be enemy when sim >0
                est2.append(user2)
                estsim2.append(ans)

print "enemies friends",len(est2)

est = list(set(est) | set(est2))
estsim = list(set(estsim) | set(estsim2))
remusers = []
for u in users:
    if u not in est:
        remusers.append(u)

print "final enemies ",len(est),"remaining users",len(remusers)

for user1 in est:
    for user2 in remusers:
        if user2 not in fset:
            ans = user_sim.similarity(user1,user2)
            # print "third ",user1,user2,ans
            if ans < 0.2:
                fset.append(user2)
                fsetsim.append(ans*estsim[est.index(user1)])

print "no of possible friends",len(fset)

avgrat = [0 for x in range(r+1)]
avgratcount = [0 for x in range(r+1)]
for i in range(len(ratingList)):
    avgrat[int(ratingList[i][0])] += int(ratingList[i][2])
    avgratcount[int(ratingList[i][0])] += 1
for i in range(len(users)):
    avgrat[int(users[i])] = float(avgrat[int(users[i])] / avgratcount[int(users[i])])


for i in range(len(ratingList)):
    if ratingList[i][0] in fset and int(ratingList[i][2]) >= 4:
        credibility = fsetsim[fset.index(ratingList[i][0])]
        if credibility > 0 :
            rating_of_user2 = int(ratingList[i][2])
            diff = (rating_of_user2 - avgrat[int(ratingList[i][0])])
            recprodt[int(ratingList[i][1])] = recprodt[int(ratingList[i][1])] + (credibility*diff)
            recprodtden[int(ratingList[i][1])] =  recprodtden[int(ratingList[i][1])] + fsetsim[fset.index(ratingList[i][0])]

rec_movies = []
for i in range(r_m+1):
    if recprodtden[i] != 0:
        recprodt[i] = float(recprodt[i]/recprodtden[i]) + avgrat[int(ut)]
        # print movieList[int(i)-1], "recommended",recprodt[i]
        rec_movies.append(i)
        
print "User based: recommended movies:",len(rec_movies)
# with open('result.dat', 'w') as f:
#     for item in final:
#         for k in range(len(item)-1):
#             f.write("%s::" % item[k])
#         f.write("%s\n" % item[k+1])

print "*************************************"
