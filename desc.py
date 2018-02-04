import numpy as np
import pandas
import copy
from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesRegressor
from scipy import stats
from scipy import stats
from sklearn.neighbors import KNeighborsRegressor



import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
from keras.constraints import maxnorm
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LassoLarsCV



# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

# load the dataset
dataframe = pandas.read_csv("C:/Users/Shanu/PycharmProjects/Forest_Fire/forestfires.csv")
data=copy.copy(dataframe)
# Encode Data
dataframe.month.replace(('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'),(1,2,3,4,5,6,7,8,9,10,11,12), inplace=True)
dataframe.day.replace(('mon','tue','wed','thu','fri','sat','sun'),(1,2,3,4,5,6,7), inplace=True)
dataframe['area'] = np.log(dataframe['area']+1)
print("Head:")
print(dataframe.head())
print("Statistical Description:")
print(dataframe.describe())
print("Shape:")
print(dataframe.shape)
print("Data Types:")
print(dataframe.dtypes)
print("Correlation:")
print(dataframe.corr(method='pearson'))
print('Printing median')
print(dataframe.median())
#
print('Printing Range')
print(dataframe.max()-dataframe.min())

print('Printing mean')
print(dataframe.mean())
print('Inter-quartile Ranges')
print(dataframe.quantile(q=0.75, axis=0, numeric_only=True, interpolation='linear')-dataframe.quantile(q=0.25,axis=0,numeric_only=True,interpolation='linear'))