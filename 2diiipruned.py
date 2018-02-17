import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import metrics
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold # import KFold
from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn.utils import shuffle
import statsmodels.formula.api as smf


counter=0
chunks=1
i=1
value=69/chunks
print(value)
for l in range(1,11):
    counter = 0
    mean_chunk_arr = []

    for inner in range(1,l+1):

        print('IN L=',l)
        print('In chunk:',inner)

        value = int(69 / l)
        counter+=1
        start=int((value*counter)-value)
        end=int((value*counter))

        dataframe=pd.read_csv('C:/Users/Shanu/PycharmProjects/Arem/AReM/my_pruned_dataset.csv')
        # dataframe.iloc[np.random.permutation(len(dataframe))]
        # dataframe.reindex(np.random.permutation(dataframe.index))
        # dataframe.sample(frac=1)
        dataset=dataframe.values
        # print(dataset.shape)
        x_shuf=dataset[:,0:10]
        y_shuf=dataset[:,10:]

        # print(x_train.shape)
        # print(y_train.shape)

        # x_train_prime, y_train_prime = shuffle(x_shuf,y_shuf ,random_state=0)
        x_train_prime, y_train_prime = x_shuf,y_shuf
        print('starting:',start)
        print('ending',end)
        x_train=x_train_prime[start:end,0:18]
        y_train=y_train_prime[start:end,0:18]
        model=LogisticRegression()
        model.fit(x_train,y_train)
        preds=model.predict(x_train)


        ######################cross validation

        kf = KFold(n_splits=5) # Define the split - into 2 folds
        kf.get_n_splits(x_train) # returns the number of splitting iterations in the cross-validator
        print(kf)
        KFold(n_splits=2, random_state=None, shuffle=True)
        y=[]
        my_score_arr=[]
        for k,(train_index, test_index) in enumerate(kf.split(x_train,y_train)):
            print('TRAIN:', train_index)
            print('TEST:', test_index,'\n')
            X_train_K, X_test_K = x_train[train_index], x_train[test_index]
            y_train_K, y_test_K = y_train[train_index], y_train[test_index]
            # print(X_test_K)
            model.fit(x_train[train_index], y_train[train_index])
            my_score=model.score(x_train[test_index], y_train[test_index])
            my_score_arr.append(my_score)
            print("[fold {0}] score: {1:.5f}".format(k, my_score))

        mean_chunk=np.mean(my_score_arr)
        mean_chunk_arr.append(mean_chunk)

         # y=y_test_K
         #max
        # for i in range(2,7):
        #     if i==4:
        #         continue
        #     strin='s'+str(i)+'max'
        #     print('printing for ',strin)
        #     mod = smf.ols(formula='target~ I('+strin+')', data=dataframe)
        #     res = mod.fit()
        #     print(res.summary())
        #
        # for i in range(5, 6):
        #     strin = 's' + str(i) + 'min'
        #     print('printing for ', strin)
        #     mod = smf.ols(formula='target~ I(' + strin + ')', data=dataframe)
        #     res = mod.fit()
        #     print(res.summary())
        #
        # for i in range(1, 7):
        #     if i == 3:
        #         continue
        #     strin = 's' + str(i) + 'mean'
        #     print('printing for ', strin)
        #     mod = smf.ols(formula='target~ I(' + strin + ')', data=dataframe)
        #     res = mod.fit()
        #     print(res.summary())

    print(mean_chunk_arr)
 # model.fit(X_train_K,y_train_K)
 # predictions=model.predict(X_test_K)
 # error=mean_squared_error(y_test_K,predictions)
 # print(error)
 # score=model.score(X_test_K,y_test_K)
#  # print(score)
# scores = cross_val_score(model, x_train, y_train, cv=5)
# print ('Cross-validated scores:', scores)