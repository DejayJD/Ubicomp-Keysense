from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import scipy
from collections import namedtuple
import numpy as np
SensorData = namedtuple("SensorData", "data targets")
data = {}
def loadData():
    global data
    data['stressed'] = (loadNpData('stressed_data.npy'))
    data['unstressed'] = loadNpData('unstressed_data.npy')


def loadNpData(file):
    data = np.load(file)
    size = data.shape[0]
    if (file == 'stressed_data.npy'):
        targets = np.ones(size)
    else:
        targets = np.zeros(size)
    return SensorData(data, targets)
#

loadData()
print data
knn = KNeighborsClassifier(n_neighbors=1)

# iris = datasets.load_iris()
# digits = datasets.load_digits()



