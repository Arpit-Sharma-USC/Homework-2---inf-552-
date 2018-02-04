import numpy as np
import pandas
import copy
import statsmodels.formula.api as smf



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


mod = smf.ols(formula='area~ I(ISI)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(RH)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(rain)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(wind)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(temp)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(DMC)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(DC)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(FFMC)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(day)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(month)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(Y)', data=dataframe)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula='area~ I(X)', data=dataframe)
res = mod.fit()
print(res.summary())
