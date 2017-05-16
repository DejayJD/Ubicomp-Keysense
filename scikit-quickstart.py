from sklearn import datasets, metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import scipy
from collections import namedtuple
import numpy as np
SensorData = namedtuple("SensorData", "data targets")
data = {}

stressedFile = 'JDstressed.npy'
unstressedFile = 'JDUnstressed.npy'
def loadData():
    loadNpData(unstressedFile)
    loadNpData(stressedFile)

def loadNpData(file):
    global data
    loaded_data = np.load(file)
    loaded_data = loaded_data.astype(np.int)
    size = loaded_data.shape[0]
    if (file == stressedFile):
        targets = np.ones(size)
    else:
        targets = np.zeros(size)
    # print (bool(data["data"]))
    if data:
        data["data"] = np.concatenate([data["data"], loaded_data])
        data["targets"] = np.concatenate([data["targets"], targets])
    else:
        data["data"] = loaded_data
        data["targets"] = targets

loadData()
knn = LogisticRegression()

train_percentage = 0.8
length = data['data'].shape[0]
num_values = int(length*train_percentage)
median = length/2

train_min = 0
train_max = num_values

knn.fit(data['data'][train_min:train_max], data['targets'][train_min:train_max])


predict_min = num_values
predict_max = length

print "Training : " + str(train_percentage*100) + "%"
print "Training values : " + str(train_min) + " - " + str(train_max)
print "Using prediction values : " + str(predict_min) + " - " + str(predict_max)
prediction_values = data['targets'][predict_min:predict_max]
data['targets'][predict_min:predict_max]
prediction = knn.predict(data['data'][predict_min:predict_max])

print prediction

acc = metrics.accuracy_score(prediction, prediction_values)
print "Accuracy = " + str(acc)




