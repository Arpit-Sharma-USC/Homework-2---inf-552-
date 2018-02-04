import numpy as np
import pandas
import copy
from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesRegressor

dataframe = pandas.read_csv("C:/Users/Shanu/PycharmProjects/Forest_Fire/forestfires.csv")
print(list(dataframe))