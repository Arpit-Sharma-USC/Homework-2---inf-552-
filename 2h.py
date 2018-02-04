import numpy as np
import pandas
import copy
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



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

df_sample = dataframe.sample(frac=0.7)

X_train=df_sample.iloc[:,:12]
Y_train=df_sample.iloc[:,12]

df_rest = dataframe.loc[~dataframe.index.isin(df_sample.index)]

X_test = df_rest.iloc[:, :12]
Y_test = df_rest.iloc[:, 12]
#
X_train['new_pred']=X_train['RH']*X_train['temp']+X_train['temp']*X_train['month']+X_train['RH']*X_train['month']
X_test['new_pred']=X_test['RH']*X_test['temp']+X_test['temp']*X_test['month']+X_test['RH']*X_test['month']

#
#
plot_uni_model=LinearRegression()
#
res=plot_uni_model.fit(X_train,Y_train)
predictions=plot_uni_model.predict(X_test)
score=plot_uni_model.score(X_test,Y_test)
error = mean_squared_error(predictions, Y_test)

print(error)

print(score)