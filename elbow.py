#Author Arief Budhiman/1301154360

from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

#baca data
df = pd.read_csv('TestsetTugas2.csv', sep='\t', header=0)
arr = np.array(df)

x = arr[:,0]
y = arr[:,1]

X = np.array(list(zip(x, y))).reshape(len(x), 2)
# determine k
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
# Plot elbow curve
plt.plot(K, distortions, 'g-X')
plt.title('K for KMeans')
plt.show()
