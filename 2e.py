import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
import metrics
from sklearn.feature_selection import chi2

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold # import KFold
from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn.utils import shuffle
import statsmodels.formula.api as smf
from sklearn.cross_validation import train_test_split



counter=0
chunks=1
i=1
value=69/chunks
# print(value)
for l in range(1,11):
    counter = 0
    mean_chunk_arr = []
    # print('#####################################################################IN L=', l,
    #       '###############################')
    for inner in range(1,l+1):


        # print('In chunk:',inner)

        value = int(69 / l)
        counter+=1
        start=int((value*counter)-value)
        end=int((value*counter))

        dataframe=pd.read_csv('C:/Users/Shanu/PycharmProjects/Arem/AReM/my_dataset.csv')
        # dataframe.iloc[np.random.permutation(len(dataframe))]
        # dataframe.reindex(np.random.permutation(dataframe.index))
        # dataframe.sample(frac=1)
        # dataframe=datafram1.values[:,:16]

        df_norm = (dataframe - dataframe.mean()) / (dataframe.max() - dataframe.min())
        # scaler = preprocessing.StandardScaler()
        # df_norm = scaler.fit_transform(dataframe)
        # df_norm = pd.DataFrame.as_matrix().astype(np.float)
        # df_norm = df_norm[np.isfinite(df_norm['FeatureColumn'])]
        df_norm.drop(['s2min', 's4min','target'], axis=1, inplace=True)
        # print(dataset.shape)
        df_norm['target']=dataframe['target']
        pd.DataFrame.to_csv(df_norm, path_or_buf='C:/Users/Shanu/PycharmProjects/Arem/AReM/my_normalized_dataset.csv',
                            index=False)
        # s2min and s4 min are useless

        dataset=df_norm.values

        x_shuf=dataset[:,0:16]
        y_shuf=dataset[:,16:]

        # print(x_train.shape)
        # print(y_train.shape)

        # x_train_prime, y_train_prime = shuffle(x_shuf,y_shuf ,random_state=0)
        x_train_prime, y_train_prime = x_shuf,y_shuf
        print('starting:',start)
        print('ending',end)
        x_train=x_train_prime[start:end,0:16]
        y_train=y_train_prime[start:end,0:16]


        ######################cross validation

        kf = KFold(n_splits=5) # Define the split - into 2 folds
        kf.get_n_splits(x_train) # returns the number of splitting iterations in the cross-validator
        # print(kf)
        KFold(n_splits=5, random_state=None, shuffle=True)
        y=[]
        my_score_arr=[]
        for k,(train_index, test_index) in enumerate(kf.split(x_train,y_train)):
            # print('TRAIN:', train_index)
            # print('TEST:', test_index,'\n')
            X_train_K, X_test_K = x_train[train_index], x_train[test_index]
            y_train_K, y_test_K = y_train[train_index], y_train[test_index]

            # X_train_K, X_test_K , y_train_K, y_test_K = train_test_split(x_train, y_train, test_size=0.3, random_state=0)

            model = LogisticRegressionCV(penalty='l1',Cs=10,cv=5,solver='liblinear')
            model.fit(X_train_K, y_train_K)
            preds = model.predict(X_test_K)

            # print(X_test_K)
            # model.fit(x_train[train_index], y_train[train_index])
            my_score=model.score(X_test_K, y_test_K)
            my_score_arr.append(my_score)

            # print("[fold {0}] score: {1:.5f}".format(k, my_score))
            # print('regression coef-values ')
            # print(model.coef_)
            # print('C',model.C_)
            # print('CS_',model.Cs_)

            # scores, pvalues = chi2(X_train_K, y_train_K)
            # print('###################',pvalues)
            # print('end of p vals###')

        mean_chunk=np.mean(my_score_arr)
        mean_chunk_arr.append(mean_chunk)


    print('Score for L=',l,' is',np.mean(mean_chunk_arr))
