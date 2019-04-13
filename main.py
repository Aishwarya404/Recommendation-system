import product
import users 
import calc_idf
import calc_q
import calc_p

movieList = calc_idf.movieList
userList = calc_idf.userList
ratingList = calc_idf.ratingList
IDF = calc_idf.IDF
c = calc_idf.c
r = calc_idf.r
r_m = calc_idf.r_m
q = calc_q.q
p = calc_p.p
u = calc_idf.user
genres = calc_idf.genres
to_pred = calc_idf.to_pred
to_pred_oldrat = calc_idf.to_pred_oldrat
rated = calc_idf.rated
avgrat = users.avgrat
orig_rated = calc_idf.orig_rated

print "target user:",u

product_based_rec = product.rec_movies
product_based_rat = product.pred_rat
print "product based recommendation size ",len(product_based_rec)

user_based_rec = users.rec_movies
user_based_rat = users.recprodt
for x in user_based_rat:
	if x>5:
		x = 5
print "user based recommendation size ",len(user_based_rec)


# combine movies from product and user based taking a,b = 0.5,0.5
rec_movies = list(set(product_based_rec) | set(user_based_rec))
rec_rating = [0 for x in range(r_m+1)]
print "final recommended rec_movies size ",len(rec_movies)

for movie in rec_movies:
	if movie in product_based_rec and movie in user_based_rec:
		rec_rating[int(movie)] = (0.8 * product_based_rat[int(movie)]) + (0.2 * user_based_rat[int(movie)])
	elif movie in product_based_rec:
		rec_rating[int(movie)] = product_based_rat[int(movie)]
	elif movie in user_based_rec:
		rec_rating[int(movie)] = user_based_rat[int(movie)]

	if rec_rating[int(movie)]>5:
		rec_rating[int(movie)] = 5
	# print movieList[int(movie)-1], rec_rating[int(movie)]

with open('result.dat', 'w') as f:
    for item in product_based_rec:
        f.write("%s " % movieList[int(item)-1])
        f.write("%s\n" % product_based_rat[int(item)])

with open('result0.dat', 'w') as f:
    for item in user_based_rec:
        f.write("%s " % movieList[int(item)-1])
        f.write("%s\n" % user_based_rat[int(item)])

with open('result_f.dat', 'w') as f:
    for item in rec_movies:
        f.write("%s " % movieList[int(item)-1])
        f.write("%s\n" % rec_rating[int(item)])

# for g in genres:
# 	genre_index= int(genres.index(g))
# 	print g," : ",p[u-1][genre_index],"\n"

# print p[u-1],"\n"
error = 0
for i in to_pred:
	print movieList[i-1], " O:", to_pred_oldrat[i], " N:", rec_rating[i]
	print "Q: ",q[i-1],"\n"
	error += abs(to_pred_oldrat[i] - rec_rating[i])

print " ERROR: ", float(error)/float(len(to_pred))


#RECALL CODE
rec_movies_for_recall = []
for i in rec_movies:
	# if rec_rating[i] >= avgrat[u]+1.0:
	# 	rec_movies_for_recall.append(i)
	rec_movies_for_recall.append(i)


# intersection_set = list(set(to_pred).intersection(set(rec_movies_for_recall)))
intersection_set = list(set(orig_rated).intersection(set(rec_movies_for_recall)))
# RECALL = float(len(intersection_set))/ float(len(to_pred))
RECALL = float(len(intersection_set))/ float(len(orig_rated))
print "RECALL: ", RECALL
# print "intersection_set:",intersection_set
# print "orig_rated:",orig_rated
# print "to_pred:",to_pred
# time python main.py