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
#
# 'temp' has the highest correlation with the area of forest fire(which is a positive correlation),
# followed by 'RH' also a positive correlation, 'Rain' has the least correlation


dataset = dataframe.values


X = dataset[:,0:12]
Y = dataset[:,12]

#linear regression model
# lin_reg_model=
#

#Feature Selection
uni_model = ExtraTreesRegressor()
rfe = RFE(uni_model, 4)
fit = rfe.fit(X, Y)

print("Number of Features: ", fit.n_features_)
print("Selected Features: ", fit.support_)
print("Feature Ranking: ", fit.ranking_)





# 'Wind', 'RH' and 'DMC' were top 3 selected features/feature combination for predicting 'Area' using Recursive Feature Elimination,
# the 2nd selected feature was atually one of the attributes with the highest correlation with the 'Area'

plt.hist((dataframe.area))
# Most of the dataset's samples fall between 0 and 200 of 'Area' output class, with majority being less than 100



dataframe.hist()

#
# 'Temp' has a near Guassian Distribution. There are a mixture of positive skews and
# negative skews among the other attributes

#density plot not needed just for reference
# dataframe.plot(kind='density', subplots=True, layout=(4,4), sharex=False, sharey=False)

# #box plot not needed just for reference
# dataframe.plot(kind='box', subplots=True, layout=(4,4), sharex=False, sharey=False)

# this plots our pairwise scatter plot
scatter_matrix(dataframe)
plt.show()


my_labels=list(dataframe[0:13])
print(my_labels)
labels=my_labels[0:12]
# print(labels.shape)
print(labels)
#2nd uni model
plot_uni_model=LinearRegression()
coef_uni_vaale=plot_uni_model.fit(X,Y).coef_

uni_pred=plot_uni_model.predict(X)
error=mean_squared_error(Y,uni_pred)
print(error)
#
#
#
#
#
#
###################CONTINUE FROM HERE#####################
#
#
#
#
#
ax = plt.gca()
plt.scatter(labels,coef_uni_vaale,16,alpha=0.5)
# plt.axvline(-np.log10(coef_uni_vaale.alpha_), linestyle='--', color='k',
#             label='alpha CV')
plt.ylabel('Regression Coefficients')
plt.xlabel('predictors')
plt.title('Regression Coefficients Progression for linear regression Paths')
plt.show()


#fitting a multiple model


pred_train, pred_test, tar_train, tar_test = train_test_split(X, Y,
                                                              test_size=.3, random_state=123)

multi_model=LassoLarsCV(cv=10, precompute=False).fit(pred_train,tar_train)
# specify the lasso regression model

# print variable names and regression coefficients
# pred_multi=LassoLarsCV.predict(pred_test)
print(dict(zip(labels[:12], multi_model.coef_)))

# plot coefficient progression
m_log_alphas = -np.log10(multi_model.alphas_)
ax = plt.gca()
plt.plot(m_log_alphas, multi_model.coef_path_.T)
plt.axvline(-np.log10(multi_model.alpha_), linestyle='--', color='k',
            label='alpha CV')
print(multi_model.coef_)
# print(multi_model.coef_path.T)
print(multi_model.coef_.shape)
# error_multi=mean_squared_error(tar_test,pred_multi)
print('Error in multivariate ')
# print(error_multi)
plt.ylabel('Regression Coefficients')
plt.xlabel('-log(alpha)')
plt.title('Regression Coefficients Progression for Lasso Paths')
plt.show()

# 2c vs 2d
ax = plt.gca()
plt.scatter(coef_uni_vaale,multi_model.coef_)
# plt.plot(coef_uni_vaale, multi_model.coef_, marker='o', linestyle='--', color='r', label='vals')

# plt.axvline(-np.log10(coef_uni_vaale.alpha_), linestyle='--', color='k',
#             label='alpha CV')
plt.ylabel('multivariate- Regression Coefficients')
plt.xlabel('univariate- Regression Coefficients')
plt.title('Regression Coefficients comparison')
plt.show()


print('in poly function now')

poly = PolynomialFeatures(degree=3)

poly_feature=dataframe['temp']
print('printing Y')
print(Y)
print('shape of Y')
print(Y.shape)

# poly_feature_prime=poly.fit_transform(poly_feature.reshape(1,-1))
# print(poly_feature_prime)
#
# lg = LinearRegression()
#
# lg.fit(poly_feature_prime,Y)
#
# print(lg.coef_)
#
#

X_Knn_train=dataset[:400,8:12]
Y_Knn_train=dataset[:400,12]

X_Knn = dataset[400:, 8:12]
Y_Knn = dataset[400:, 12]

error_arr=[]
k_arr=[]
# knn regression
for k in range(1,350):
    neigh = KNeighborsRegressor(n_neighbors=k)
    neigh.fit(X_Knn_train, Y_Knn_train)
    predictions=neigh.predict(X_Knn)

    # print(predictions)
    error= mean_squared_error(Y_Knn,predictions)
    score=neigh.score(X_Knn,Y_Knn)
    error_arr.append(error)
    k_arr.append((1/k))
    plt.plot(1/k, error, marker='o',linestyle='--', color='b')
    plt.xlabel('1/k')
    plt.ylabel('Error observed in Test Set')
    plt.title('KNN-Regression with last 4  predictors')
plt.show()

# 2g
# X_new=copy.copy(dataframe)
# print('Created new df')
# X_new['area']=dataframe['area']
# print(X_new)
# print(X.shape)
# print('dropping features')
# X_new.drop(['X', 'Y','month','day','FFMC','DMC','DC','ISI','wind','rain','area'], axis=1,inplace=True)
# print(X_new)
# print(X_new.shape)
# print('into adding new col')
# X_new['new_predictor']=X_new['temp']*X_new['RH']
# X_new['area']=dataframe['area']
# print(X_new)
# print(X_new.shape)
#
# y_inter=X_new['area']
#
# slope, intercept, r_value, p_value, std_err = stats.linregress(X_new,X_new)
# print('P-val')
# print(p_value)


# continue here with rest

