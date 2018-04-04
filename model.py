class KMeans:
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import random
    import time

    df = pd.read_csv('TrainsetTugas2.csv', sep='\t')

    arr = np.array(df)

    #cari koordinat maksimal
    maxi = max(arr[:,0])
    if maxi<max(arr[:,1]):
        maxi = max(arr[:,1])

    color = ["r.", "g.", "b.", "c.", "y.", "k.", 'm.']
    color1 = ["r", "g", "b", "c", "y", "k", "m"]
    label = []
    centroids = []
    x0 = 0
    x0_j = 0

    Xpindah = [0,0,0,0,0,0,0]
    Ypindah = [0,0,0,0,0,0,0]
    C_move = [0,0,0,0,0,0,0]
    C_move1 = [0,0,0,0,0,0,0]
    penanda = False
    #random centroid
    for x in range(7):
        centroids.append([random.uniform(0,maxi),random.uniform(0,maxi)])

    # for i in range(len(centroids)):
    #     Xpindah.append(0)
    #     Ypindah.append(0)
    #     C_move.append(0)
    #     C_move1.append(0)
#-----------------------------------------------------------------------------------------------
    def penentuan(self):
        self.penanda = False
        del self.label[:]
        # for i in range(len(centroids)):
        #     self.Xpindah[i] = 0;
        #     self.Ypindah[i] = 0
        #     self.C_move[i] = 0
        self.Xpindah = [0,0,0,0,0,0,0]
        self.Ypindah = [0,0,0,0,0,0,0]
        self.C_move = [0,0,0,0,0,0,0]
        x = 0

        #masukkan centroid ke dalam pyplot


        for j in range(0,len(self.arr)):
            z = 0
            x = float((self.arr[j][0]-self.centroids[0][0])**2 + (self.arr[j][1]-self.centroids[0][1])**2)**1/2
            for i in range(0,len(self.centroids)):
                y = float((self.arr[j][0]-self.centroids[i][0])**2 + (self.arr[j][1]-self.centroids[i][1])**2)**1/2
                if x >= y:
                    x = y
                    z = i
            self.label.append(z)
            # print(self.color)
            for asa in range(0,len(self.centroids)):
                if z == asa:
                    self.Xpindah[asa] += self.arr[j][0]
                    self.Ypindah[asa] += self.arr[j][1]
                    self.C_move[asa]+=1




        # print(len(self.label ))
        for i in range(0,len(self.arr)):
            self.plt.plot(self.arr[i][0], self.arr[i][1], self.color[self.label[i]])

        for i in range(0,len(self.centroids)):
            self.plt.scatter(self.centroids[i][0], self.centroids[i][1], c=self.color1[i], marker = "x", s=150)
        self.plt.show(block=False)
        self.time.sleep(1)
        self.plt.close()

        if self.C_move != self.C_move1:
            self.penanda = True

        for i in range(0,len(self.centroids)):
            if self.C_move[i]==0:
                self.C_move[i] = 1
            self.pindah(i, self.C_move)

        for i in range(0,len(self.arr)):
            self.plt.plot(self.arr[i][0], self.arr[i][1], self.color[self.label[i]])

        if self.penanda:
            self.plt.show(block=False)
            self.time.sleep(1)
            self.plt.close()
        else:
            self.plt.show()

        if self.penanda:
            self.penentuan()

    def pindah(self, i, C_move):
        self.C_move1 = self.C_move
        if C_move[i] != 1:
            self.centroids[i] = [self.Xpindah[i]/C_move[i], self.Ypindah[i]/C_move[i]]
        else:
            C_move[i] = 0
        self.plt.scatter(self.centroids[i][0], self.centroids[i][1], c=self.color1[i], marker = "x", s=150)

#-----------------------------------------------------------main-----------------------------------------------
km = KMeans()
km.penentuan()


# print(km.label)
