# KNN classification
import cv2
import numpy as np
import matplotlib.pyplot as plt

def Plot_points ():
    pass

# Generating random training data
train_features = np.random.randint(0,100,(25,2)).astype(np.float32) # 25,2 because we need both x and y
labels = np.random.randint(0,2,(25,1))
i=0
for x,y in train_features:
    if labels[i] == 0:
        plt.scatter(x,y,c='red')
    else:
        plt.scatter(x,y,c='blue')
    i=i+1

new = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(new[:,0],new[:,1],c='green')

knn = cv2.ml.KNearest_create()
knn.train(train_features,labels)
ret , results , neighbours , dist = knn.find_nearest(new,3)
print(results)
print(neighbours)
print(dist)

plt.show()
