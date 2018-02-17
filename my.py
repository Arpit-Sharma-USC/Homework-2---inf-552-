from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from scipy import stats
import metrics
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold # import KFold
from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn.utils import shuffle
import statsmodels.formula.api as smf
from sklearn.feature_selection import f_classif
from sklearn import model_selection
import statsmodels.api as sm

counter=0
chunks=1
i=1
value=69/chunks
print(value)
for l in range(1,11):
    counter = 0
    mean_chunk_arr = []
    my_score_arr = []
    for inner in range(1,l+1):

        print('IN L=',l)
        print('In chunk:',inner)

        value = int(69 / l)
        counter+=1
        start=int((value*counter)-value)
        end=int((value*counter))

        dataframe=pd.read_csv('C:/Users/Shanu/PycharmProjects/Arem/AReM/my_dataset.csv')
        dataset=dataframe.values
        x_shuf=dataset[:,0:18]
        y_shuf=dataset[:,18:]


        # x_train_prime, y_train_prime = shuffle(x_shuf,y_shuf ,random_state=0)
        x_train_prime, y_train_prime = x_shuf, y_shuf
        print('starting:',start)
        print('ending',end)
        x_train=x_train_prime[start:end,0:18]
        y_train=y_train_prime[start:end,0:18]


        kfold = model_selection.KFold(n_splits=5, random_state=7,shuffle=True)
        modelCV = LogisticRegression()
        scoring = 'accuracy'
        X_new = SelectKBest(chi2, k=10).fit_transform(x_train, y_train)
        results = model_selection.cross_val_score(modelCV, X_new, y_train, cv=kfold, scoring=scoring)
        outcome_acc=results.mean()  
        print("5-fold cross validation average accuracy: %.3f" % (outcome_acc))
        my_score_arr.append(outcome_acc)

        # stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)
        #
        # logit_model = sm.Logit(y_train, X_new)
        # result = logit_model.fit()
        # print(result.summary())

    mean_chunk = np.mean(my_score_arr)
    mean_chunk_arr.append(mean_chunk)
    print(mean_chunk_arr)