from math import sqrt
from itertools import combinations
a = [0,2,4,5,7,9,11]
b = [0,2,4,6,8,10]
def vector(pitchclasses):
    intervals = [0,0,0,0,0,0]
    for interval in combinations(sorted(pitchclasses),2):
        x = interval[1] - interval[0]
        intervals[6 - abs(x-6) - 1] += 1
    return intervals
def distance(pitchclass1, pitchclass2):
    intvect_1, intvect_2 = vector(pitchclass1),vector(pitchclass2)
    print (intvect_1)
    print (intvect_2)
    return sqrt(sum((vect1-vect2)**2 \
               for vect1,vect2 in zip(intvect_1, intvect_2)))
print (distance(a,b))
    
