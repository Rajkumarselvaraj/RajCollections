import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns
import warnings
from sklearn.datasets import make_blobs
from collections import defaultdict
warnings.filterwarnings('ignore')

def kmeans(k,data,itr,thres):
    # choosing k rabdom datapoints to initialize the means
    means=data.sample(k).values
    count=0
    compare=[]
    # outer while loop to control the no of iterations using count
    while count<itr:
        count+=1
        # initializing hash table to assign the cluster to each data point
        mean_dict=defaultdict(list)
        for point in data.values:
            tmp=None
            mindist=float('inf')
            for mean in means:
                # finding the distance between the point under consideration # and the centroids of previously formed clusters 
                d=dist(mean,point)
                if d<mindist:
                    # capturing the closest centroid for the given point mindist=d
                    tmp=mean
            # assiging the datapoint to the closest cluster
            mean_dict[str(tmp)].append(list(point))
        means=[]
        for mean in mean_dict:
            # optimizing the centroids by taking the mean of all the points in a particul
            means.append(list(np.array(mean_dict[mean]).mean(axis=0)))
        compare.append(np.array(means))
        # checking for convergence of centroid for early stopping
        if len(compare)>1 and dist(compare[-1],compare[-2])<thres:
            print(f'The algorithm converged in {count} iterations')
            return means
    return means

def dist(pt1,pt2):
    if type(pt1)!=type(np.array([1])) or type(pt2)!=type(np.array([1])):
        pt1,pt2=np.array(pt1),np.array(pt2)
    return np.sqrt(((pt1-pt2)**2).sum())

def coloring(point1,point2,point3):
    mindist=float('inf')
    ans=None
    point=[point1,point2,point3]
    for i,pt in enumerate(mu):
        if dist(pt,point)<mindist:
            mindist=dist(pt,point)
            ans=i
    return ans


data=make_blobs(n_samples=10000,n_features=3,centers=5)
print(data[0])
print('\n')

# the next array is an array of labels which we'll use later to compare our clusters with the actuals
print(data[1])

df=pd.DataFrame(data[0],columns=['x','y','z'])

print(df)
fig = plt.figure(dpi=100)
ax = fig.gca(projection='3d')
ax.scatter(df.x, df.y, df.z)

plt.show()

mu=kmeans(5,df,1000,10**-4)
print(f'\nThe centroids of k-clusters are {mu}')


df['color']=df.apply(lambda df: coloring(df.x,df.y,df.z),axis=1)
mu=np.array(mu)

# visualizing the given dataset based on the clusters that we created using k-means clustering algorithm
fig = plt.figure(dpi=100)
ax = fig.gca(projection='3d')
hue=('Red','Blue','Green','Purple','Orange','Pink','Yellow')
k=5
for i in range(k):
    dt=df[df.color==i]
    ax.scatter(dt.x, dt.y, dt.z, c=hue[i], label=i)
plt.legend(loc=2)

plt.show()



# visualizing the original dataset using the actual clustering as given by the make_blobs
fig = plt.figure(dpi=100)
ax = fig.gca(projection='3d')
hue=('Red','Blue','Green','Purple','Orange','Pink','Yellow')
k=5
for i in range(k):
    dt=df[data[1]==i]
    ax.scatter(dt.x, dt.y, dt.z, c=hue[i], label=i)
plt.legend(loc=2)
plt.show()