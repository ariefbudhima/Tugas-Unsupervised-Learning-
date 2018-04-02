import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

df = pd.read_csv('TrainsetTugas2.csv', sep='\t')

arr = np.array(df)

#cari koordinat maksimal
maxi = max(arr[:,0])
if maxi<max(arr[:,1]):
    maxi = max(arr[:,1])
print(maxi)

color = ["r.", "g.", "b.", "c.", "y."]
label = []
centroids = []

#random centroid
for x in range(5):
    centroids.append([random.uniform(0,maxi),random.uniform(0,maxi)])


def penentuan():
    for j in range(len(arr)):
        z = 0
        for i in range(0,len(centroids)-1):
            x = float((arr[j][0]-centroids[i][0])**2 + (arr[j][1]-centroids[i][1])**2)
            y = float((arr[j][0]-centroids[i+1][0])**2 + (arr[j][1]-centroids[i+1][1])**2)
            if x > y:
                x = y
                z = i
            print(z)
        label.append(z)

penentuan()

for i in range(len(arr)):
    plt.plot(arr[i][0], arr[i][1], color[label[i]])


#masukkan centroid ke dalam pyplot
for i in range(len(centroids)):
    plt.scatter(centroids[i][0], centroids[i][1], marker = "x", s=150)
plt.show()



# print(arr[])
