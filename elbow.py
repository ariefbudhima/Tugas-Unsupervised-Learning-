from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv('TestsetTugas2.csv', sep='\t', header=0)
atrain = np.array(file)

fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
colors = ['r', 'g', 'b', 'y', 'c', 'm']

x = atrain[:,0]
y = atrain[:,1]

ax.scatter(x, y)
plt.show()

# create new plot and data
plt.plot()
X = np.array(list(zip(x, y))).reshape(len(x), 2)

# determine k
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])

# Plot elbow curve
plt.plot(K, distortions, 'bx-')
plt.xlabel('')
plt.title('Optimal K')
plt.show()
