import numpy as np
import mnist_loader_KNN as DS_loader
import matplotlib.pyplot as plt
import random
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from collections import defaultdict
import seaborn as sns
from struct import unpack
#!gzip -d data/*.gz


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


# plt.imshow(sample,cmap=plt.cm.gray)
# plt.show()
# print("Image Label: ", y_test[temp,])


# plt.figure(figsize=(20,4))
# for index,(image,label) in enumerate(zip(x_train[0:5,:],y_train[0:5,])):
#     plt.subplot(1,5,index+1)
#     plt.imshow(np.reshape(image,(28,28)),cmap=plt.cm.gray)
#     plt.title('Training: %i\n'%label,fontsize=20)
#plt.show()

#instantiating classifier
# knnclassifier=KNeighborsClassifier(n_neighbors=5,metric='euclidean',algorithm='ball_tree')

# print((x_train.shape))
#
# print((test.shape))

# knnclassifier.fit(x_train,y_train.ravel())

# image_indices = []
# for i in range(0,10):
#     distances, indices = knnclassifier.kneighbors(x_test[i].reshape(1,-1))
#     for test_data in indices:
#         for index in test_data:
#             image_indices.append(index)
#
# # plt.figure(figsize=(20,40))
# img_plot_index = 0
# for img_index in image_indices:
#     img = x_train[img_index,:].reshape(28,28)
#     img_plot_index = img_plot_index+1
#     plt.subplot(10, 5, img_plot_index)
#     plt.imshow(img,cmap=plt.cm.gray)
#      #plt.title('Training: %i\n'%label,fontsize=20)
# plt.show()
#
#
# prime_predictions = []
# prime_knnclassifier = KNeighborsClassifier(n_neighbors=1,algorithm='ball_tree')
index_error=1
error_score=[]
knnclassifier=KNeighborsClassifier(n_neighbors=1,algorithm='ball_tree')
x_test_subset = x_test[:600, :]
y_test_subset = y_test[:600, :]

plot_x=[]

for i in range(1, 13):
    x_temp = x_train[:(i*5000)+1, :]
    y_temp = y_train[:(i*5000)+1, :]
    # print(x_temp)
    # print(y_temp)

    knnclassifier.fit(x_temp, y_temp.ravel())# knnclassifier.predict(x_test[0].reshape(1,-1))
#predictions = knnclassifier.predict(x_test[0:10].reshape())
    predictions = knnclassifier.predict(x_test_subset)

    if i==1:
        prime_predictions = predictions
        prime_knnclassifier = knnclassifier


    score = knnclassifier.score(x_test_subset, y_test_subset)
    print(score)
    # print(predictions)
    error = metrics.mean_squared_error(y_test_subset,predictions, multioutput='raw_values')
    error_score.append(error)
    print(error)
    # plt.plot(i*5000, error,label='Error rates in Subsets of Training Set', linewidth=2)
    plot_x.append(((i-1)*5000)+5000)

    # plt.plot(i*5000, error, marker='o', linestyle='--', color='r', label='Best Error Rate')

    # plt.scatter(i*5000, error, 5, alpha=0.2)
# # i = i + 5000
# plt.plot(plot_x, error_score)
plt.plot(plot_x, error_score, marker='o', linestyle='--', color='r', label='Best Error Rate')
plt.xlabel('Subset Size of Train Samples')
plt.ylabel('Error Rate')
plt.title('Best error rate for subsets of Train Data')
plt.show()

miss_index = 0
misclassifiedIndexes = []
for label, predict in zip(y_test, prime_predictions):
    if label != predict:
        misclassifiedIndexes.append(miss_index)
    miss_index += 1

image_indices = []
for i in misclassifiedIndexes:
    distances, indices = prime_knnclassifier.kneighbors(x_test[i].reshape(1,-1))
    for test_data in indices:
        for index in test_data:
            image_indices.append(index)

plt.figure(figsize=(10,20))
img_plot_index = 0
for img_index in image_indices:
    img = x_train[img_index,:].reshape(28,28)
    img_plot_index = img_plot_index+1
    plt.subplot(10, 5, img_plot_index)
    plt.imshow(img,cmap=plt.cm.gray)
    #plt.title('Training: %i\n'%label,fontsize=20)
plt.show()



#confusion matrix
# cm = metrics.confusion_matrix(y_test, predictions)
# #using the saborn plot
# plt.figure(figsize=(9,9))
# sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r')
# plt.ylabel('Actual label')
# plt.xlabel('Predicted label')
# all_sample_title = 'Accuracy Score: {0}'.format(score)
# plt.title(all_sample_title, size = 15)
# plt.show()

#
# def euclidean_distance(img_a, img_b):
#     '''Finds the distance between 2 images: img_a, img_b'''
#     # element-wise computations are automatically handled by numpy
#     return sum((img_a - img_b) ** 2)
#
#
# def find_majority(labels):
#     '''Finds the majority class/label out of the given labels'''
#     # defaultdict(type) is to automatically add new keys without throwing error.
#     counter = defaultdict(int)
#     for label in labels:
#         counter[label] += 1
#
#     # Finding the majority class.
#     majority_count = max(counter.values())
#     for key, value in counter.items():
#         if value == majority_count:
#             return key
#
#
#
#
# # Setting up dataset as numpy array for faster mathematical operations.
# # Only 5000 for faster prediction - but this results into little inaccurate results.
# # Try to use all train data for accurate results.
# train_images = x_train
# train_labels = y_train
# test_images =  x_test
# test_labels = y_test
#
# def predict(k, train_images, train_labels, test_images):
#     '''
#     Predicts the new data-point's category/label by
#     looking at all other training labels
#     '''
#     # distances contains tuples of (distance, label)
#     distances = [(euclidean_distance(test_image, image), label)
#                     for (image, label) in zip(train_images, train_labels)]
#     # sort the distances list by distances
#     by_distances = sorted(distances, key=lambda distance : distance)
#     # extract only k closest labels
#     k_labels = [label for (_, label) in by_distances[:k]]
#     # return the majority voted label
#     return find_majority(k_labels)
#
# # Predicting and printing the accuracy
# ii = 0
# total_correct = 0
# for test_image in test_images:
#     pred = predict(5, train_images, train_labels, test_image)
#     if pred == test_labels[ii]:
#         total_correct += 1
#     acc = (total_correct / (ii+1)) * 100
#     print('test image['+str(ii)+']', '\tpred:', pred, '\torig:', test_labels[ii], '\tacc:', str(round(acc, 2))+'%')
#     ii += 1