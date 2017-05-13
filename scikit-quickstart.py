from sklearn import datasets
import scipy

iris = datasets.load_iris()
digits = datasets.load_digits()

print digits.data

print digits.target