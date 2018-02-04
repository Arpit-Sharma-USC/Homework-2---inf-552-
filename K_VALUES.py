import numpy as np
import mnist_loader_KNN as DS_loader
import matplotlib.pyplot as plt
import random
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics


# URLs for the train image and label data
url_train_image = 'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz'
url_train_labels = 'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz'
num_train_samples = 60000

print("Downloading train data")

x_train = DS_loader.try_download_x(url_train_image, url_train_labels, num_train_samples)
y_train = DS_loader.try_download_y(url_train_image, url_train_labels, num_train_samples)

# URLs for the test image and label data
url_test_image = 'http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz'
url_test_labels = 'http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz'
num_test_samples = 10000

print("Downloading test data")
temp=random.randrange(9999)

x_test = DS_loader.try_download_x(url_test_image, url_test_labels, num_test_samples)
y_test = DS_loader.try_download_y(url_test_image, url_test_labels, num_test_samples)

print(y_test.shape)

sample=x_test[temp,:].reshape(28,28)

prime_predictions = []
prime_knnclassifier = KNeighborsClassifier(n_neighbors=1,algorithm='ball_tree')
index_error=1;
error_score=[]
i = 1
while(i <= 10001):
    knnclassifier=KNeighborsClassifier(n_neighbors=i,algorithm='ball_tree')
    knnclassifier.fit(x_train,y_train.ravel())
    predictions= knnclassifier.predict(x_test)

    if i==1:
        prime_predictions = predictions
        prime_knnclassifier = knnclassifier


    score=knnclassifier.score(x_test,y_test)
    print(score)
    print(predictions)
    error = metrics.mean_squared_error(y_test,predictions, multioutput='raw_values')
    error_score.append(error)
    print(error)
    plt.scatter(1/i, error, 5, alpha=0.2)
    i = i + 200

plt.show()

