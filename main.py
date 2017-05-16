import numpy as np
import re

stressed = np.load("OmarStressed.npy")
unstressed = np.load("JDUnstressed.npy")

def clean_data(data):
    for row in data:
        for col in row:
            re.sub('[^0-9.]','', col)
clean_data(stressed)

stressed =  stressed.astype(np.int)
# unstressed = unstressed.astype(np.int)
# stressed_mean = np.mean(stressed, axis=0)
# unstressed_mean = np.mean(unstressed, axis=0)
#
# print stressed_mean
# print unstressed_mean
#
#
# print stressed_mean - unstressed_mean