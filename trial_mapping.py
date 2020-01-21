import csv
import numpy as np
with open('mesh1_b.csv', newline='') as csvfile:
    cordinates = list(csv.reader(csvfile))
    
with open('mesh1_new_a.csv', newline='') as csvfile:
    vertices = list(csv.reader(csvfile))

for n in range(len(vertices)):
    i = vertices[n+1][0]
    j = vertices[n+1][1]
    k = vertices[n+1][2]
    u = int(i)
    v = int(j)
    w = int(k)
    print(i)
    print(j)
    print(k)
    x = cordinates[u]
    y = cordinates[v]
    z = cordinates[w]
    print(x)
    print(y)
    print(z)
#import csv


#for i in range(len(vertices)):
    #for j in range(len(vertices[i])):
#x = vertices[100]
#y = np.array(x) 
#z = y[-1][3]
#print(z, end=' ')
#print()

#for n in range(1040,1):
#i = vertices[1][0]
    #j = vertices[n][1]
    #k = vertices[n][2]
#print(i)
#print(j)
#print(k)
