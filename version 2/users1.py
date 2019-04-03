import math
import numpy
movieList = [i.strip().split('::') for i in open("movies.dat").readlines()]
userList = [i.strip().split('::') for i in open("users.dat").readlines()]
ratingList = [i.strip().split('::') for i in open("ratings.dat").readlines()]


# for m in movieList :
#     print m
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

# sum = 0
# for i in p:
   
#     for j in i:
#         sum += j
   
#     for j in i:
#         if sum!= 0:
#             j = j/sum
#         else:
#             j = j/1.0
#     i.append(sum/c)
#     sum=0 
def similarity(u1,u2):
    result = 0    
    den1 = 0
    den2 = 0
    den = 1
    for i in range(len(p[0])-1):
        if p[int(u1)-1][i]!=0 and p[int(u2)-1][i]!= 0:
            result = result + ((p[int(u1)-1][i]-p[int(u1)-1][len(p[0])-1]) * (p[int(u2)-1][i]-p[int(u2)-1][len(p[0])-1]))
            #result = result + ((p[int(u1)-1][i]) * (p[int(u2)-1][i]))
        if p[int(u1)-1][i]!=0:
            den1 = den1 + ((p[int(u1)-1][i]-p[int(u1)-1][len(p[0])-1]) * (p[int(u1)-1][i]-p[int(u1)-1][len(p[0])-1]))
            #den1 = den1 + ((p[int(u1)-1][i]) * (p[int(u1)-1][i]))
        if p[int(u2)-1][i]!=0:
            den2 = den2 + ((p[int(u2)-1][i]-p[int(u2)-1][len(p[0])-1]) * (p[int(u2)-1][i]-p[int(u2)-1][len(p[0])-1]))
            #den2 = den2 + ((p[int(u2)-1][i]) * (p[int(u2)-1][i]))
    den = math.sqrt(den1*den2)
    if den==0:
        den = 1
    result = result/den
    #print "similarity:",result
    if result == 0:
        return -1
    return result
    #return (result*10)-9
        
ut = users[5771]
est = []
estsim = []
est2 = []
estsim2 = []
recprodt = [0 for x in range(len(movies)+1)]
recprodtden = [0 for x in range(len(movies)+1)]

fset=[]
fsetsim = []

for user in users:
    if user != ut:
        ans = similarity(ut,user)
        if ans < -0.5:
            est.append(user)
            # print user
            estsim.append(ans)
            # print ans
# print "............................"

print "enemy set",len(est)
userslevel1 = []
for u in users:
	if u not in est:
		userslevel1.append(u)

for user1 in est:
    for user2 in userslevel1:
    	if user2 not in est2:
            ans = similarity(user1,user2)
            if ans >= 0.5:
                ans=similarity(ut,user2)
                if ans < 0:# enenmy friend might not be enemy when sim >0
                    est2.append(user2)
                    estsim2.append(ans)
                    # print user2

# print "######################################"
print "enemies friends",len(est2)

#est=list(set().union(est,est2))
est = est + est2
estsim = estsim + estsim2
#estsim=list(set().union(estsim,estsim2))
remusers = []
for u in users:
	if u not in est:
		remusers.append(u)

print "final enemies ",len(est),"remaining users",len(remusers)
# print "---------fset-values--------------"

for user1 in est:
    for user2 in remusers:
        if user2 not in fset:
            ans = similarity(user1,user2)
            if ans < -0.5:
                fset.append(user2)
                fsetsim.append(ans*estsim[est.index(user1)])
                #print ans*estsim[est.index(user1)], ans, estsim[est.index(user1)]

        #else:
            # ans = similarity(user1,user2)
            # if ans*estsim[est.index(user1)] > fsetsim[fset.index(user2)]:
            #     fsetsim[fset.index(user2)] = ans*estsim[est.index(user1)] 
print "no of possible friends",len(fset)

avgrat = [0 for x in range(len(users)+1)]
avgratcount = [0 for x in range(len(users)+1)]
for i in range(len(ratingList)):
    avgrat[int(ratingList[i][0])] += int(ratingList[i][2])
    avgratcount[int(ratingList[i][0])] += 1
for i in range(len(users)):
    avgrat[int(users[i])] = float(avgrat[int(users[i])] / avgratcount[int(users[i])])
    #print avgrat[int(users[i])],users[i],"HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh"
for i in range(len(ratingList)):
    if ratingList[i][0] in fset and int(ratingList[i][2]) >= 4:
        rating_of_user2 = int(ratingList[i][2])
        credibility = fsetsim[fset.index(ratingList[i][0])]
        diff = (rating_of_user2 - avgrat[int(ratingList[i][0])])
        recprodt[int(ratingList[i][1])] = recprodt[int(ratingList[i][1])] + (credibility*diff)
        recprodtden[int(ratingList[i][1])] =  recprodtden[int(ratingList[i][1])] + fsetsim[fset.index(ratingList[i][0])]
        # if int(ratingList[i][1]) == 3694:
        #     print credibility,rating_of_user2,diff,"Meeeeeeeeeeeeeeeeeeeeeee"



for i in range(len(movies)+1):
    if recprodtden[i] != 0:
        recprodt[i] = float(recprodt[i]/recprodtden[i]) + avgrat[int(ut)]
        # print i, "recommended",recprodt[i],float(recprodt[i]/recprodtden[i]), avgrat[int(ut)]
        print i, "recommended",recprodt[i]
        # print "numerator:", recprodt[i]
        # print "denom", recprodtden[i]





					
			
			

	




		
			

		
				
			

			




	

		
		
		





