import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import KFold



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


        dataframe=pd.read_csv('C:/Users/Shanu/PycharmProjects/Arem/AReM/my_dataset.csv')
        dataset=dataframe.values
        x_shuf=dataset[:,0:18]
        y_shuf=dataset[:,18:]


        value = int(len(x_shuf) / l)
        counter+=1
        start=int((value*counter)-value)
        end=int((value*counter))

        # x_train_prime, y_train_prime = shuffle(x_shuf,y_shuf ,random_state=0)
        x_train_prime, y_train_prime = x_shuf, y_shuf
        print('starting:',start)
        print('ending',end)
        x_train=x_train_prime[start:end,0:18]
        y_train=y_train_prime[start:end,0:18]
        #

        kf = KFold(n_splits=5)  # Define the split - into 2 folds
        kf.get_n_splits(x_train)  # returns the number of splitting iterations in the cross-validator
        print(kf)
        KFold(n_splits=2, random_state=7, shuffle=True)
        y = []
        my_score_arr = []
        modelCV = LogisticRegression()
        X_new = SelectKBest(chi2, k=6).fit_transform(x_train, y_train)


        for k, (train_index, test_index) in enumerate(kf.split(X_new, y_train)):
            print('TRAIN:', train_index)
            print('TEST:', test_index, '\n')

            X_train_K, X_test_K = x_train[train_index], x_train[test_index]
            y_train_K, y_test_K = y_train[train_index], y_train[test_index]

            modelCV.fit(x_train[train_index], y_train[train_index])

            my_score = modelCV.score(x_train[test_index], y_train[test_index])

            my_score_arr.append(my_score)

            print("[fold {0}] score: {1:.5f}".format(k, my_score))

            y_pred = modelCV.predict(X_test_K)

            print('Regression Coef:\n',modelCV.coef_)

            print('\n p values for X_train_K\n')

            bogus, pvalues_whole = chi2(X_train_K, y_train_K)
            print(pvalues_whole)

        mean_chunk = np.mean(my_score_arr)
        mean_chunk_arr.append(mean_chunk)
        print(mean_chunk_arr)
    print('Final Score for L=',l,':',np.mean(mean_chunk_arr))
    print('#####################################################################')