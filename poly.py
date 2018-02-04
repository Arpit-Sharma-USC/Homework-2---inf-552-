import pandas as pd
import statsmodels.formula.api as smf

dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Forest_Fire/forestfires.csv")
dataframe.month.replace(('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'),(1,2,3,4,5,6,7,8,9,10,11,12), inplace=True)
dataframe.day.replace(('mon','tue','wed','thu','fri','sat','sun'),(1,2,3,4,5,6,7), inplace=True)

mod = smf.ols(formula='area~ I(rain+rain**2+rain**3)', data=dataframe)
res = mod.fit()
print(res.summary())


