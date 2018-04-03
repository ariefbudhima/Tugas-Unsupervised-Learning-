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

color = ["r.", "g.", "b.", "c.", "y.", "w.", 'm.']
color1 = ["r", "g", "b", "c", "y", "w", "m"]
label = []
centroids = []
x0 = 0
x0_j = 0

Xpindah = [0,0,0,0,0,0,0]
Ypindah = [0,0,0,0,0,0,0]
#random centroid
for x in range(7):
    centroids.append([random.uniform(0,maxi),random.uniform(0,maxi)])


def penentuan(centroids, Xpindah, Ypindah):



    #masukkan centroid ke dalam pyplot

    C_move = [0,0,0,0,0,0,0]

    for j in range(len(arr)):
        z = 0
        x = float((arr[j][0]-centroids[0][0])**2 + (arr[j][1]-centroids[0][1])**2)**1/2
        for i in range(1,len(centroids)):
            y = float((arr[j][0]-centroids[i][0])**2 + (arr[j][1]-centroids[i][1])**2)**1/2
            if x > y:
                x = y
                z = i
        for asa in range(7):
            if z == asa:
                Xpindah[asa] += arr[j][0]
                Ypindah[asa] += arr[j][1]
                C_move[asa]+=1

        label.append(z)


    for i in range(len(arr)):
        plt.plot(arr[i][0], arr[i][1], color[label[i]])

    for i in range(len(centroids)):
        plt.scatter(centroids[i][0], centroids[i][1], c=color1[i], marker = "x", s=150)
    plt.show()

    for i in range(7):
        if C_move[i]==0:
            C_move[i] = 1
        pindah(centroids, Xpindah, Ypindah, C_move,i)

    for i in range(len(arr)):
        plt.plot(arr[i][0], arr[i][1], color[label[i]])

    plt.show()

def pindah(centroids, Xpindah, Ypindah, C_move,i):
    print("xpindah ",i,"  =",Xpindah[i]/C_move[i])
    print("ypindah ",i,"  =",Ypindah[i]/C_move[i])
    print(C_move[i])
    if C_move[i] != 1:
        centroids[i] = [Xpindah[i]/C_move[i], Ypindah[i]/C_move[i]]

    plt.scatter(centroids[i][0], centroids[i][1], c=color1[i], marker = "x", s=150)

# def

#-------------------------------------------------------------utama-----------------------------------------------------------
penentuan(centroids, Xpindah, Ypindah)

# for i in range(len(arr)):
#     plt.plot(arr[i][0], arr[i][1], color[label[i]])


#masukkan centroid ke dalam pyplot
# for i in range(len(centroids)):
#     plt.scatter(centroids[i][0], centroids[i][1], c=color1[i], marker = "x", s=150)
# plt.show()
