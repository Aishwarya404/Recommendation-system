# import numpy as np

# def is_float(string):
#     """ True if given string is float else False"""
#     try:
#         return float(string)
#     except ValueError:
#         return False

# data = []
# with open('ratings.dat', 'r') as f:
#     d = f.readlines()
#     for i in d:
#         k = i.rstrip().split("::")
#         data.append([float(i) if is_float(i) else i for i in k]) 

# # data = np.array(data, dtype='O')
# # print data 

# import multiprocessing as mp
# print("Number of processors: ", mp.cpu_count())

genres= [ 'Action','Adventure','Animation','Children','Comedy', 'Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War','Western']
print int(genres.index('Action'))