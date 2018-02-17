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
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from itertools import cycle
from scipy import interp



counter=0
chunks=1
i=1
value=19/chunks
value_train=69/chunks
print(value)
for l in range(1,2):
    counter = 0
    mean_chunk_arr = []
    print('#####################################################################IN L=', l,
          '###############################')
    for inner in range(1,l+1):


        print('In chunk:',inner)

        value = int(19 / l)
        value_train=int(69/l)

        counter+=1

        start=int((value*counter)-value)
        end=int((value*counter))

        start_train=int((value_train*counter)-value_train)
        end_train=((value_train*counter))

        dataframe_test=pd.read_csv('C:/Users/Shanu/PycharmProjects/Arem/AReM/my_normalized_dataset_test_multiclass.csv')
        dataframe_train = pd.read_csv(
            'C:/Users/Shanu/PycharmProjects/Arem/AReM/my_normalized_dataset_multiclass.csv')
        # dataframe.iloc[np.random.permutation(len(dataframe))]
        # dataframe.reindex(np.random.permutation(dataframe.index))
        # dataframe.sample(frac=1)
        # dataframe=datafram1.values[:,:16]
        #
        # df_norm = (dataframe - dataframe.mean()) / (dataframe.max() - dataframe.min())
        # # scaler = preprocessing.StandardScaler()
        # # df_norm = scaler.fit_transform(dataframe)
        # # df_norm = pd.DataFrame.as_matrix().astype(np.float)
        # # df_norm = df_norm[np.isfinite(df_norm['FeatureColumn'])]
        # df_norm.drop(['s2min', 's4min','s6min','target'], axis=1, inplace=True)
        # # print(dataset.shape)
        # df_norm['target']=dataframe['target']
        # pd.DataFrame.to_csv(df_norm, path_or_buf='C:/Users/Shanu/PycharmProjects/Arem/AReM/my_normalized_dataset_test_multiclass.csv',
        #                     index=False)
        # # s2min and s4 min are useless

        dataset_test=dataframe_test.values
        dataset_train=dataframe_train.values

        x_shuf=dataset_train[:,0:15]
        y_shuf=dataset_train[:,15:]


        x_shuf_test=dataset_test[:,0:15]
        y_shuf_test=dataset_test[:,15:]

        # print(x_train.shape)
        # print(y_train.shape)

        # x_train_prime, y_train_prime = shuffle(x_shuf,y_shuf ,random_state=0)
        # x_test_prime, y_test_prime = shuffle(x_shuf_test,y_shuf_test ,random_state=0)

        x_test_prime, y_test_prime = x_shuf_test,y_shuf_test
        x_train_prime, y_train_prime = x_shuf,y_shuf

        print('starting:',start)
        print('ending',end)

        x_train=x_train_prime[start_train:end_train,0:15]
        y_train=y_train_prime[start_train:end_train,0:15]

        x_test=x_test_prime[start:end,0:15]
        y_test=y_test_prime[start:end,0:15]


        ######################cross validation

        # kf = KFold(n_splits=5) # Define the split - into 2 folds
        # kf.get_n_splits(x_train) # returns the number of splitting iterations in the cross-validator
        # print(kf)
        # KFold(n_splits=2, random_state=None, shuffle=True)
        y=[]
        my_score_arr=[]
        # for k,(train_index, test_index) in enumerate(kf.split(x_train,y_train)):
        # print('TRAIN:', train_index)
        # print('TEST:', test_index,'\n')
        # X_train_K, X_test_K = x_train[train_index], x_train[test_index]
        # y_train_K, y_test_K = y_train[train_index], y_train[test_index]

        # X_train_K, X_test_K , y_train_K, y_test_K = train_test_split(x_train, y_train, test_size=0.3, random_state=0)

        model = LogisticRegression(penalty='l1',solver='saga',multi_class='multinomial')
        model.fit(x_train,y_train )
        preds = model.predict(x_test)
        print(preds)
        # model.fit(x_train[train_index], y_train[train_index])
        my_score=model.score(x_test, y_test)
        my_score_arr.append(my_score)
        print('score',my_score)
        print('regression coef-values ')
        print(model.coef_)

        mean_chunk=np.mean(my_score_arr)
        mean_chunk_arr.append(mean_chunk)


        conf_matrix = confusion_matrix(y_test, preds)
        print(type(conf_matrix))
        # plot_matrix_consuion(conf_matrix)
        sns.set()
        ax = sns.heatmap(conf_matrix, annot=True, cmap="YlGnBu")
        plt.show()
        error=mean_squared_error(y_test,preds)

    print(np.mean(mean_chunk_arr))

