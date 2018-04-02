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
# print(maxi)

color = ["r.", "g.", "b.", "c.", "y.", "w.", 'm.']
color1 = ["r", "g", "b", "c", "y", "w", "m"]
label = []
centroids = []
x0 = 0
x0_j = 0
Xpindah = [0,0,0,0,0]
#random centroid
for x in range(7):
    centroids.append([random.uniform(0,maxi),random.uniform(0,maxi)])


def penentuan(Xpindah):
    for j in range(len(arr)):
        z = 0
        x = float((arr[j][0]-centroids[0][0])**2 + (arr[j][1]-centroids[0][1])**2)**1/2
        for i in range(1,len(centroids)):
            y = float((arr[j][0]-centroids[i][0])**2 + (arr[j][1]-centroids[i][1])**2)
            if x > y:
                x = y
                z = i
        if z == 0:
            Xpindah[0] += arr[j][0]

        elif z==1:
            Xpindah[1] += arr[j][0]

        elif z==2:
            Xpindah[2] += arr[j][0]

        elif z==3:
            Xpindah[3] += arr[j][0]

            # print(z)
        label.append(z)

    print("xpindah0  =",Xpindah[0]/maxi)
    print("xpindah1  =",Xpindah[1]/maxi)
    print("xpindah2  =",Xpindah[2]/maxi)
    print("xpindah3  =",Xpindah[3]/maxi)

def pindah(x0,y):
    for i in range(len(arr)):
        if label[i]==0:
            x0 += arr[i][0]
            y+=1
    # print('jumlah x0=',x0)
    # print(y)
    # print(x0/y)

penentuan(Xpindah)
pindah(x0,x0_j)
for i in range(len(arr)):
    plt.plot(arr[i][0], arr[i][1], color[label[i]])


#masukkan centroid ke dalam pyplot
for i in range(len(centroids)):
    plt.scatter(centroids[i][0], centroids[i][1], c=color1[i], marker = "x", s=150)
plt.show()
