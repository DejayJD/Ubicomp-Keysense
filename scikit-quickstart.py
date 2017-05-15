from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import scipy
from collections import namedtuple
import numpy as np
SensorData = namedtuple("SensorData", "data targets")
data = {}
def loadData():
    loadNpData('stressed_data.npy')
    loadNpData('unstressed_data.npy')


def loadNpData(file):
    global data
    loaded_data = np.load(file)
    size = loaded_data.shape[0]
    if (file == 'stressed_data.npy'):
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
knn = KNeighborsClassifier(n_neighbors=1)

train_percentage = .15
num_values = int(data['data'].shape[0]*train_percentage)
median = data['data'].shape[0]/2
train_min = median - (num_values/2)
train_max = median + (num_values/2)

knn.fit(data['data'][train_min:train_max], data['targets'][train_min:train_max])

predict_min = 0
predict_max = 5000
prediction_values = data['targets'][predict_min:predict_max]
data['targets'][predict_min:predict_max]
prediction = knn.predict(data['data'][predict_min:predict_max])

print data['targets'].shape
acc = float(np.sum(prediction == prediction_values)) / prediction.shape[0]
print "Accuracy = " + str(acc)




