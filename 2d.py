import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import customFeatureLibrary as templib

# dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/test_data/sitting/dataset2.csv", skiprows=4)
#
# Alldat=dataframe
# Alldat['bending1']=""
# Alldat1 = Alldat.loc[:, (Alldat != 0).any(axis=0)]
# y = np.array(Alldat1['bending1'])
# Dat = Alldat1.iloc[:,:-1]


count=0


feature_min_folder11 = []
feature_min_folder12 = []
feature_min_folder13 = []
feature_min_folder14 = []
feature_min_folder15 = []
feature_min_folder16 = []

feature_max_folder11 = []
feature_max_folder12 = []
feature_max_folder13 = []
feature_max_folder14 = []
feature_max_folder15 = []
feature_max_folder16 = []

feature_mean_folder11 = []
feature_mean_folder12 = []
feature_mean_folder13 = []
feature_mean_folder14 = []
feature_mean_folder15 = []
feature_mean_folder16 = []

feature_min_1=[]
feature_min_2=[]
feature_min_3=[]
feature_min_4=[]
feature_min_5=[]
feature_min_6=[]

feature_max_1=[]
feature_max_2=[]
feature_max_3=[]
feature_max_4=[]
feature_max_5=[]
feature_max_6=[]

feature_mean_1=[]
feature_mean_2=[]
feature_mean_3=[]
feature_mean_4=[]
feature_mean_5=[]
feature_mean_6=[]


for i in range(3,8):

    count+=1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/bending1/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna(inplace=True)

    feature_min_folder11.append(dataframe['avg_rss12'].min())
    feature_min_folder12.append(dataframe['var_rss12'].min())
    feature_min_folder13.append(dataframe['avg_rss13'].min())
    feature_min_folder14.append(dataframe['var_rss13'].min())
    feature_min_folder15.append(dataframe['avg_rss23'].min())
    feature_min_folder16.append(dataframe['var_rss23'].min())

    feature_max_folder11.append(dataframe['avg_rss12'].max())
    feature_max_folder12.append(dataframe['var_rss12'].max())
    feature_max_folder13.append(dataframe['avg_rss13'].max())
    feature_max_folder14.append(dataframe['var_rss13'].max())
    feature_max_folder15.append(dataframe['avg_rss23'].max())
    feature_max_folder16.append(dataframe['var_rss23'].max())

    feature_mean_folder11.append(dataframe['avg_rss12'].mean())
    feature_mean_folder12.append(dataframe['var_rss12'].mean())
    feature_mean_folder13.append(dataframe['avg_rss13'].mean())
    feature_mean_folder14.append(dataframe['var_rss13'].mean())
    feature_mean_folder15.append(dataframe['avg_rss23'].mean())
    feature_mean_folder16.append(dataframe['var_rss23'].mean())

    if (i == 7):
        feature_min_1.append(feature_min_folder11)
        feature_min_2.append(feature_min_folder12)
        feature_min_3.append(feature_min_folder13)
        feature_min_4.append(feature_min_folder14)
        feature_min_5.append(feature_min_folder15)
        feature_min_6.append(feature_min_folder16)

        feature_max_1.append(feature_max_folder11)
        feature_max_2.append(feature_max_folder12)
        feature_max_3.append(feature_max_folder13)
        feature_max_4.append(feature_max_folder14)
        feature_max_5.append(feature_max_folder15)
        feature_max_6.append(feature_max_folder16)

        feature_mean_1.append(feature_mean_folder11)
        feature_mean_2.append(feature_mean_folder12)
        feature_mean_3.append(feature_mean_folder13)
        feature_mean_4.append(feature_mean_folder14)
        feature_mean_5.append(feature_mean_folder15)
        feature_mean_6.append(feature_mean_folder16)


feature_min_folder11 = []
feature_min_folder12 = []
feature_min_folder13 = []
feature_min_folder14 = []
feature_min_folder15 = []
feature_min_folder16 = []

feature_max_folder11 = []
feature_max_folder12 = []
feature_max_folder13 = []
feature_max_folder14 = []
feature_max_folder15 = []
feature_max_folder16 = []

feature_mean_folder11 = []
feature_mean_folder12 = []
feature_mean_folder13 = []
feature_mean_folder14 = []
feature_mean_folder15 = []
feature_mean_folder16 = []
for i in range(3,7):

    count+=1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/bending2/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna(inplace=True)

    feature_min_folder11.append(dataframe['avg_rss12'].min())
    feature_min_folder12.append(dataframe['var_rss12'].min())
    feature_min_folder13.append(dataframe['avg_rss13'].min())
    feature_min_folder14.append(dataframe['var_rss13'].min())
    feature_min_folder15.append(dataframe['avg_rss23'].min())
    feature_min_folder16.append(dataframe['var_rss23'].min())

    feature_max_folder11.append(dataframe['avg_rss12'].max())
    feature_max_folder12.append(dataframe['var_rss12'].max())
    feature_max_folder13.append(dataframe['avg_rss13'].max())
    feature_max_folder14.append(dataframe['var_rss13'].max())
    feature_max_folder15.append(dataframe['avg_rss23'].max())
    feature_max_folder16.append(dataframe['var_rss23'].max())

    feature_mean_folder11.append(dataframe['avg_rss12'].mean())
    feature_mean_folder12.append(dataframe['var_rss12'].mean())
    feature_mean_folder13.append(dataframe['avg_rss13'].mean())
    feature_mean_folder14.append(dataframe['var_rss13'].mean())
    feature_mean_folder15.append(dataframe['avg_rss23'].mean())
    feature_mean_folder16.append(dataframe['var_rss23'].mean())

    if (i == 6):
        feature_min_1.append(feature_min_folder11)
        feature_min_2.append(feature_min_folder12)
        feature_min_3.append(feature_min_folder13)
        feature_min_4.append(feature_min_folder14)
        feature_min_5.append(feature_min_folder15)
        feature_min_6.append(feature_min_folder16)

        feature_max_1.append(feature_max_folder11)
        feature_max_2.append(feature_max_folder12)
        feature_max_3.append(feature_max_folder13)
        feature_max_4.append(feature_max_folder14)
        feature_max_5.append(feature_max_folder15)
        feature_max_6.append(feature_max_folder16)

        feature_mean_1.append(feature_mean_folder11)
        feature_mean_2.append(feature_mean_folder12)
        feature_mean_3.append(feature_mean_folder13)
        feature_mean_4.append(feature_mean_folder14)
        feature_mean_5.append(feature_mean_folder15)
        feature_mean_6.append(feature_mean_folder16)

feature_min_folder11 = []
feature_min_folder12 = []
feature_min_folder13 = []
feature_min_folder14 = []
feature_min_folder15 = []
feature_min_folder16 = []

feature_max_folder11 = []
feature_max_folder12 = []
feature_max_folder13 = []
feature_max_folder14 = []
feature_max_folder15 = []
feature_max_folder16 = []

feature_mean_folder11 = []
feature_mean_folder12 = []
feature_mean_folder13 = []
feature_mean_folder14 = []
feature_mean_folder15 = []
feature_mean_folder16 = []
for i in range(4,16):
  count += 1
  # print('into cycling')
  print('dataset'+str(i))
  if(i==9 or i==14):
      dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/cycling/dataset"+str(i)+".csv")
  else:
      dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/cycling/dataset"+str(i)+".csv",skiprows = 4)
      dataframe.dropna(inplace=True)
      # print('into features')
  feature_min_folder11.append(dataframe['avg_rss12'].min())
  feature_min_folder12.append(dataframe['var_rss12'].min())
  feature_min_folder13.append(dataframe['avg_rss13'].min())
  feature_min_folder14.append(dataframe['var_rss13'].min())
  feature_min_folder15.append(dataframe['avg_rss23'].min())
  feature_min_folder16.append(dataframe['var_rss23'].min())

  feature_max_folder11.append(dataframe['avg_rss12'].max())
  feature_max_folder12.append(dataframe['var_rss12'].max())
  feature_max_folder13.append(dataframe['avg_rss13'].max())
  feature_max_folder14.append(dataframe['var_rss13'].max())
  feature_max_folder15.append(dataframe['avg_rss23'].max())
  feature_max_folder16.append(dataframe['var_rss23'].max())

  feature_mean_folder11.append(dataframe['avg_rss12'].mean())
  feature_mean_folder12.append(dataframe['var_rss12'].mean())
  feature_mean_folder13.append(dataframe['avg_rss13'].mean())
  feature_mean_folder14.append(dataframe['var_rss13'].mean())
  feature_mean_folder15.append(dataframe['avg_rss23'].mean())
  feature_mean_folder16.append(dataframe['var_rss23'].mean())

  if(i==15):
    feature_min_1.append(feature_min_folder11)
    feature_min_2.append(feature_min_folder12)
    feature_min_3.append(feature_min_folder13)
    feature_min_4.append(feature_min_folder14)
    feature_min_5.append(feature_min_folder15)
    feature_min_6.append(feature_min_folder16)

    feature_max_1.append(feature_max_folder11)
    feature_max_2.append(feature_max_folder12)
    feature_max_3.append(feature_max_folder13)
    feature_max_4.append(feature_max_folder14)
    feature_max_5.append(feature_max_folder15)
    feature_max_6.append(feature_max_folder16)

    feature_mean_1.append(feature_mean_folder11)
    feature_mean_2.append(feature_mean_folder12)
    feature_mean_3.append(feature_mean_folder13)
    feature_mean_4.append(feature_mean_folder14)
    feature_mean_5.append(feature_mean_folder15)
    feature_mean_6.append(feature_mean_folder16)

# print('break')

feature_min_folder11 = []
feature_min_folder12 = []
feature_min_folder13 = []
feature_min_folder14 = []
feature_min_folder15 = []
feature_min_folder16 = []

feature_max_folder11 = []
feature_max_folder12 = []
feature_max_folder13 = []
feature_max_folder14 = []
feature_max_folder15 = []
feature_max_folder16 = []

feature_mean_folder11 = []
feature_mean_folder12 = []
feature_mean_folder13 = []
feature_mean_folder14 = []
feature_mean_folder15 = []
feature_mean_folder16 = []


for i in range(4,16):
  count += 1
  print('dataset'+str(i))
  if(i==9 or i==14):
      dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/lying/dataset"+str(i)+".csv",skiprows=4)
  else:
      dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/lying/dataset"+str(i)+".csv",skiprows = 4)
      dataframe.dropna(inplace=True)
      # print('into features')
  feature_min_folder11.append(dataframe['avg_rss12'].min())
  feature_min_folder12.append(dataframe['var_rss12'].min())
  feature_min_folder13.append(dataframe['avg_rss13'].min())
  feature_min_folder14.append(dataframe['var_rss13'].min())
  feature_min_folder15.append(dataframe['avg_rss23'].min())
  feature_min_folder16.append(dataframe['var_rss23'].min())

  feature_max_folder11.append(dataframe['avg_rss12'].max())
  feature_max_folder12.append(dataframe['var_rss12'].max())
  feature_max_folder13.append(dataframe['avg_rss13'].max())
  feature_max_folder14.append(dataframe['var_rss13'].max())
  feature_max_folder15.append(dataframe['avg_rss23'].max())
  feature_max_folder16.append(dataframe['var_rss23'].max())

  feature_mean_folder11.append(dataframe['avg_rss12'].mean())
  feature_mean_folder12.append(dataframe['var_rss12'].mean())
  feature_mean_folder13.append(dataframe['avg_rss13'].mean())
  feature_mean_folder14.append(dataframe['var_rss13'].mean())
  feature_mean_folder15.append(dataframe['avg_rss23'].mean())
  feature_mean_folder16.append(dataframe['var_rss23'].mean())

  if(i==15):
    feature_min_1.append(feature_min_folder11)
    feature_min_2.append(feature_min_folder12)
    feature_min_3.append(feature_min_folder13)
    feature_min_4.append(feature_min_folder14)
    feature_min_5.append(feature_min_folder15)
    feature_min_6.append(feature_min_folder16)

    feature_max_1.append(feature_max_folder11)
    feature_max_2.append(feature_max_folder12)
    feature_max_3.append(feature_max_folder13)
    feature_max_4.append(feature_max_folder14)
    feature_max_5.append(feature_max_folder15)
    feature_max_6.append(feature_max_folder16)

    feature_mean_1.append(feature_mean_folder11)
    feature_mean_2.append(feature_mean_folder12)
    feature_mean_3.append(feature_mean_folder13)
    feature_mean_4.append(feature_mean_folder14)
    feature_mean_5.append(feature_mean_folder15)
    feature_mean_6.append(feature_mean_folder16)
print('hi')
feature_min_folder11 = []
feature_min_folder12 = []
feature_min_folder13 = []
feature_min_folder14 = []
feature_min_folder15 = []
feature_min_folder16 = []

feature_max_folder11 = []
feature_max_folder12 = []
feature_max_folder13 = []
feature_max_folder14 = []
feature_max_folder15 = []
feature_max_folder16 = []

feature_mean_folder11 = []
feature_mean_folder12 = []
feature_mean_folder13 = []
feature_mean_folder14 = []
feature_mean_folder15 = []
feature_mean_folder16 = []

for i in range(4,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/sitting/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna(inplace=True)
    feature_min_folder11.append(dataframe['avg_rss12'].min())
    feature_min_folder12.append(dataframe['var_rss12'].min())
    feature_min_folder13.append(dataframe['avg_rss13'].min())
    feature_min_folder14.append(dataframe['var_rss13'].min())
    feature_min_folder15.append(dataframe['avg_rss23'].min())
    feature_min_folder16.append(dataframe['var_rss23'].min())

    feature_max_folder11.append(dataframe['avg_rss12'].max())
    feature_max_folder12.append(dataframe['var_rss12'].max())
    feature_max_folder13.append(dataframe['avg_rss13'].max())
    feature_max_folder14.append(dataframe['var_rss13'].max())
    feature_max_folder15.append(dataframe['avg_rss23'].max())
    feature_max_folder16.append(dataframe['var_rss23'].max())

    feature_mean_folder11.append(dataframe['avg_rss12'].mean())
    feature_mean_folder12.append(dataframe['var_rss12'].mean())
    feature_mean_folder13.append(dataframe['avg_rss13'].mean())
    feature_mean_folder14.append(dataframe['var_rss13'].mean())
    feature_mean_folder15.append(dataframe['avg_rss23'].mean())
    feature_mean_folder16.append(dataframe['var_rss23'].mean())

    if (i == 15):
        feature_min_1.append(feature_min_folder11)
        feature_min_2.append(feature_min_folder12)
        feature_min_3.append(feature_min_folder13)
        feature_min_4.append(feature_min_folder14)
        feature_min_5.append(feature_min_folder15)
        feature_min_6.append(feature_min_folder16)

        feature_max_1.append(feature_max_folder11)
        feature_max_2.append(feature_max_folder12)
        feature_max_3.append(feature_max_folder13)
        feature_max_4.append(feature_max_folder14)
        feature_max_5.append(feature_max_folder15)
        feature_max_6.append(feature_max_folder16)

        feature_mean_1.append(feature_mean_folder11)
        feature_mean_2.append(feature_mean_folder12)
        feature_mean_3.append(feature_mean_folder13)
        feature_mean_4.append(feature_mean_folder14)
        feature_mean_5.append(feature_mean_folder15)
        feature_mean_6.append(feature_mean_folder16)

feature_min_folder11 = []
feature_min_folder12 = []
feature_min_folder13 = []
feature_min_folder14 = []
feature_min_folder15 = []
feature_min_folder16 = []

feature_max_folder11 = []
feature_max_folder12 = []
feature_max_folder13 = []
feature_max_folder14 = []
feature_max_folder15 = []
feature_max_folder16 = []

feature_mean_folder11 = []
feature_mean_folder12 = []
feature_mean_folder13 = []
feature_mean_folder14 = []
feature_mean_folder15 = []
feature_mean_folder16 = []

for i in range(4,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/standing/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna(inplace=True)
    feature_min_folder11.append(dataframe['avg_rss12'].min())
    feature_min_folder12.append(dataframe['var_rss12'].min())
    feature_min_folder13.append(dataframe['avg_rss13'].min())
    feature_min_folder14.append(dataframe['var_rss13'].min())
    feature_min_folder15.append(dataframe['avg_rss23'].min())
    feature_min_folder16.append(dataframe['var_rss23'].min())

    feature_max_folder11.append(dataframe['avg_rss12'].max())
    feature_max_folder12.append(dataframe['var_rss12'].max())
    feature_max_folder13.append(dataframe['avg_rss13'].max())
    feature_max_folder14.append(dataframe['var_rss13'].max())
    feature_max_folder15.append(dataframe['avg_rss23'].max())
    feature_max_folder16.append(dataframe['var_rss23'].max())

    feature_mean_folder11.append(dataframe['avg_rss12'].mean())
    feature_mean_folder12.append(dataframe['var_rss12'].mean())
    feature_mean_folder13.append(dataframe['avg_rss13'].mean())
    feature_mean_folder14.append(dataframe['var_rss13'].mean())
    feature_mean_folder15.append(dataframe['avg_rss23'].mean())
    feature_mean_folder16.append(dataframe['var_rss23'].mean())

    if (i == 15):
        feature_min_1.append(feature_min_folder11)
        feature_min_2.append(feature_min_folder12)
        feature_min_3.append(feature_min_folder13)
        feature_min_4.append(feature_min_folder14)
        feature_min_5.append(feature_min_folder15)
        feature_min_6.append(feature_min_folder16)

        feature_max_1.append(feature_max_folder11)
        feature_max_2.append(feature_max_folder12)
        feature_max_3.append(feature_max_folder13)
        feature_max_4.append(feature_max_folder14)
        feature_max_5.append(feature_max_folder15)
        feature_max_6.append(feature_max_folder16)

        feature_mean_1.append(feature_mean_folder11)
        feature_mean_2.append(feature_mean_folder12)
        feature_mean_3.append(feature_mean_folder13)
        feature_mean_4.append(feature_mean_folder14)
        feature_mean_5.append(feature_mean_folder15)
        feature_mean_6.append(feature_mean_folder16)

feature_min_folder11 = []
feature_min_folder12 = []
feature_min_folder13 = []
feature_min_folder14 = []
feature_min_folder15 = []
feature_min_folder16 = []

feature_max_folder11 = []
feature_max_folder12 = []
feature_max_folder13 = []
feature_max_folder14 = []
feature_max_folder15 = []
feature_max_folder16 = []

feature_mean_folder11 = []
feature_mean_folder12 = []
feature_mean_folder13 = []
feature_mean_folder14 = []
feature_mean_folder15 = []
feature_mean_folder16 = []

for i in range(4,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/walking/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna(inplace=True)
    feature_min_folder11.append(dataframe['avg_rss12'].min())
    feature_min_folder12.append(dataframe['var_rss12'].min())
    feature_min_folder13.append(dataframe['avg_rss13'].min())
    feature_min_folder14.append(dataframe['var_rss13'].min())
    feature_min_folder15.append(dataframe['avg_rss23'].min())
    feature_min_folder16.append(dataframe['var_rss23'].min())

    feature_max_folder11.append(dataframe['avg_rss12'].max())
    feature_max_folder12.append(dataframe['var_rss12'].max())
    feature_max_folder13.append(dataframe['avg_rss13'].max())
    feature_max_folder14.append(dataframe['var_rss13'].max())
    feature_max_folder15.append(dataframe['avg_rss23'].max())
    feature_max_folder16.append(dataframe['var_rss23'].max())

    feature_mean_folder11.append(dataframe['avg_rss12'].mean())
    feature_mean_folder12.append(dataframe['var_rss12'].mean())
    feature_mean_folder13.append(dataframe['avg_rss13'].mean())
    feature_mean_folder14.append(dataframe['var_rss13'].mean())
    feature_mean_folder15.append(dataframe['avg_rss23'].mean())
    feature_mean_folder16.append(dataframe['var_rss23'].mean())

    if (i == 15):
        feature_min_1.append(feature_min_folder11)
        feature_min_2.append(feature_min_folder12)
        feature_min_3.append(feature_min_folder13)
        feature_min_4.append(feature_min_folder14)
        feature_min_5.append(feature_min_folder15)
        feature_min_6.append(feature_min_folder16)

        feature_max_1.append(feature_max_folder11)
        feature_max_2.append(feature_max_folder12)
        feature_max_3.append(feature_max_folder13)
        feature_max_4.append(feature_max_folder14)
        feature_max_5.append(feature_max_folder15)
        feature_max_6.append(feature_max_folder16)

        feature_mean_1.append(feature_mean_folder11)
        feature_mean_2.append(feature_mean_folder12)
        feature_mean_3.append(feature_mean_folder13)
        feature_mean_4.append(feature_mean_folder14)
        feature_mean_5.append(feature_mean_folder15)
        feature_mean_6.append(feature_mean_folder16)



print(feature_min_1)
print(feature_min_2)

print(feature_min_3)
print(feature_min_4)
print(feature_min_5)
print(feature_min_6)



print('\\nnow in max')

print(feature_max_1)
print(feature_max_2)
print(feature_max_3)
print(feature_max_4)
print(feature_max_5)
print(feature_max_6)


print('now in mean')

print(feature_mean_1)
print(feature_mean_2)
print(feature_mean_3)
print(feature_mean_4)
print(feature_mean_5)
print(feature_mean_6)

print(count)
print(np.std(feature_min_1[0]))

print('################min series 1 bending')
bending_min_series_1=[]

bending_min_series_1=feature_min_1[0:2]
bending_min_single_array=np.array(bending_min_series_1)
bending_min_single_array_ravelelled=bending_min_single_array.ravel()

# print(bending_min_single_array_ravelelled)
# print(type(bending_min_single_array_ravelelled))

bending_min_single_array_ravelelled_1_split=[]
for i in range(0,len(bending_min_single_array_ravelelled)):
    temp=bending_min_single_array_ravelelled[i]
    # print(temp)
    for j in range(0,len(temp)):
        bending_min_single_array_ravelelled_1_split.append(temp[j])
# print('check')
bending_min_single_array_ravelelled_1_split_array=np.array(bending_min_single_array_ravelelled_1_split)

# print(bending_min_single_array_ravelelled_1_split_array)
# print(type(bending_min_single_array_ravelelled_1_split_array))

print('################min series 1 others')

# for other activities min
others_min_series_1=[]
others_min_series_1=feature_min_1[2:]
others_min_single_array=np.array(others_min_series_1)
others_min_single_array_ravelelled=others_min_single_array.ravel()

# print(others_min_single_array_ravelelled)
# print(type(others_min_single_array_ravelelled))

others_min_single_array_ravelelled_1_split=others_min_single_array_ravelelled



print('################max series 1 bending')
bending_max_series_1=[]

bending_max_series_1=feature_max_1[0:2]
bending_max_single_array=np.array(bending_max_series_1)
bending_max_single_array_ravelelled=bending_max_single_array.ravel()
#
# print(bending_max_single_array_ravelelled)
# print(type(bending_max_single_array_ravelelled))

bending_max_single_array_ravelelled_1_split=[]
for i in range(0,len(bending_max_single_array_ravelelled)):
    temp=bending_max_single_array_ravelelled[i]
    # print(temp)
    for j in range(0,len(temp)):
        bending_max_single_array_ravelelled_1_split.append(temp[j])
# print('check')
bending_max_single_array_ravelelled_1_split_array=np.array(bending_max_single_array_ravelelled_1_split)

# print(bending_max_single_array_ravelelled_1_split_array)
# print(type(bending_max_single_array_ravelelled_1_split_array))

print('################max series 1 others')

# for other activities max
others_max_series_1=[]
others_max_series_1=feature_max_1[2:]
others_max_single_array=np.array(others_max_series_1)
others_max_single_array_ravelelled=others_max_single_array.ravel()

# print(others_max_single_array_ravelelled)
# print(type(others_max_single_array_ravelelled))

others_max_single_array_ravelelled_1_split=others_max_single_array_ravelelled


print('################mean series 1 bending')
bending_mean_series_1=[]

bending_mean_series_1=feature_mean_1[0:2]
bending_mean_single_array=np.array(bending_mean_series_1)
bending_mean_single_array_ravelelled=bending_mean_single_array.ravel()
#
# print(bending_mean_single_array_ravelelled)
# print(type(bending_mean_single_array_ravelelled))

bending_mean_single_array_ravelelled_1_split=[]
for i in range(0,len(bending_mean_single_array_ravelelled)):
    temp=bending_mean_single_array_ravelelled[i]
    # print(temp)
    for j in range(0,len(temp)):
        bending_mean_single_array_ravelelled_1_split.append(temp[j])
# print('check')
bending_mean_single_array_ravelelled_1_split_array=np.array(bending_mean_single_array_ravelelled_1_split)

# print(bending_mean_single_array_ravelelled_1_split_array)
# print(type(bending_mean_single_array_ravelelled_1_split_array))

print('################mean series 1 others')

# for other activities mean
others_mean_series_1=[]
others_mean_series_1=feature_mean_1[2:]
others_mean_single_array=np.array(others_mean_series_1)
others_mean_single_array_ravelelled=others_mean_single_array.ravel()
#
# print(others_mean_single_array_ravelelled)
# print(type(others_mean_single_array_ravelelled))

others_mean_single_array_ravelelled_1_split=others_mean_single_array_ravelelled



print('################mean series 2 bending')
bending_mean_series_2=[]

bending_mean_series_2=feature_mean_2[0:2]
bending_mean_single_array=np.array(bending_mean_series_2)
bending_mean_single_array_ravelelled=bending_mean_single_array.ravel()

# print(bending_mean_single_array_ravelelled)
# print(type(bending_mean_single_array_ravelelled))

bending_mean_single_array_ravelelled_2_split=[]
for i in range(0,len(bending_mean_single_array_ravelelled)):
    temp=bending_mean_single_array_ravelelled[i]
    # print(temp)
    for j in range(0,len(temp)):
        bending_mean_single_array_ravelelled_2_split.append(temp[j])
# print('check')
bending_mean_single_array_ravelelled_2_split_array=np.array(bending_mean_single_array_ravelelled_2_split)

# print(bending_mean_single_array_ravelelled_2_split_array)
# print(type(bending_mean_single_array_ravelelled_2_split_array))

print('################mean series 2 others')

# for other activities mean
others_mean_series_2=[]
others_mean_series_2=feature_mean_2[2:]
others_mean_single_array=np.array(others_mean_series_2)
others_mean_single_array_ravelelled=others_mean_single_array.ravel()
#
# print(others_mean_single_array_ravelelled)
# print(type(others_mean_single_array_ravelelled))

others_mean_single_array_ravelelled_2_split=others_mean_single_array_ravelelled



print('################max series 2 bending')
bending_max_series_2=[]

bending_max_series_2=feature_max_2[0:2]
bending_max_single_array=np.array(bending_max_series_2)
bending_max_single_array_ravelelled=bending_max_single_array.ravel()
#
# print(bending_max_single_array_ravelelled)
# print(type(bending_max_single_array_ravelelled))

bending_max_single_array_ravelelled_2_split=[]
for i in range(0,len(bending_max_single_array_ravelelled)):
    temp=bending_max_single_array_ravelelled[i]
    # print(temp)
    for j in range(0,len(temp)):
        bending_max_single_array_ravelelled_2_split.append(temp[j])
# print('check')
bending_max_single_array_ravelelled_2_split_array=np.array(bending_max_single_array_ravelelled_2_split)
#
# print(bending_max_single_array_ravelelled_2_split_array)
# print(type(bending_max_single_array_ravelelled_2_split_array))

print('################max series 2 others')

# for other activities max
others_max_series_2=[]
others_max_series_2=feature_max_2[2:]
others_max_single_array=np.array(others_max_series_2)
others_max_single_array_ravelelled=others_max_single_array.ravel()
#
# print(others_max_single_array_ravelelled)
# print(type(others_max_single_array_ravelelled))

others_max_single_array_ravelelled_2_split=others_max_single_array_ravelelled


print('################min series 2 bending')
bending_min_series_2=[]

bending_min_series_2=feature_min_2[0:2]
bending_min_single_array=np.array(bending_min_series_2)
bending_min_single_array_ravelelled=bending_min_single_array.ravel()

# print(bending_min_single_array_ravelelled)
# print(type(bending_min_single_array_ravelelled))

bending_min_single_array_ravelelled_2_split=[]
for i in range(0,len(bending_min_single_array_ravelelled)):
    temp=bending_min_single_array_ravelelled[i]
    # print(temp)
    for j in range(0,len(temp)):
        bending_min_single_array_ravelelled_2_split.append(temp[j])
# print('check')
bending_min_single_array_ravelelled_2_split_array=np.array(bending_min_single_array_ravelelled_2_split)

# print(bending_min_single_array_ravelelled_2_split_array)
# print(type(bending_min_single_array_ravelelled_2_split_array))

print('################min series 2 others')

# for other activities min
others_min_series_2=[]
others_min_series_2=feature_min_2[2:]
others_min_single_array=np.array(others_min_series_2)
others_min_single_array_ravelelled=others_min_single_array.ravel()

# print(others_min_single_array_ravelelled)
# print(type(others_min_single_array_ravelelled))

others_min_single_array_ravelelled_2_split=others_min_single_array_ravelelled


print('################min series 6 bending')
bending_min_series_6=[]

bending_min_series_6=feature_min_6[0:2]
bending_min_single_array=np.array(bending_min_series_6)
bending_min_single_array_ravelelled=bending_min_single_array.ravel()


bending_min_single_array_ravelelled_6_split=[]
for i in range(0,len(bending_min_single_array_ravelelled)):
    temp=bending_min_single_array_ravelelled[i]
    for j in range(0,len(temp)):
        bending_min_single_array_ravelelled_6_split.append(temp[j])
ending_min_single_array_ravelelled_6_split_array=np.array(bending_min_single_array_ravelelled_6_split)


print('################min series 6 others')

# for other activities min
others_min_series_6=[]
others_min_series_6=feature_min_6[2:]
others_min_single_array=np.array(others_min_series_6)
others_min_single_array_ravelelled=others_min_single_array.ravel()


others_min_single_array_ravelelled_6_split=others_min_single_array_ravelelled


print('################max series 6 bending')
bending_max_series_6=[]

bending_max_series_6=feature_max_6[0:2]
bending_max_single_array=np.array(bending_max_series_6)
bending_max_single_array_ravelelled=bending_max_single_array.ravel()

bending_max_single_array_ravelelled_6_split=[]
for i in range(0,len(bending_max_single_array_ravelelled)):
    temp=bending_max_single_array_ravelelled[i]
    for j in range(0,len(temp)):
        bending_max_single_array_ravelelled_6_split.append(temp[j])
bending_max_single_array_ravelelled_6_split_array=np.array(bending_max_single_array_ravelelled_6_split)


print('################max series 6 others')

# for other activities max
others_max_series_6=[]
others_max_series_6=feature_max_6[2:]
others_max_single_array=np.array(others_max_series_6)
others_max_single_array_ravelelled=others_max_single_array.ravel()

# print(others_max_single_array_ravelelled)
# print(type(others_max_single_array_ravelelled))

others_max_single_array_ravelelled_6_split=others_max_single_array_ravelelled



print('################mean series 6 bending')
bending_mean_series_6=[]

bending_mean_series_6=feature_mean_6[0:2]
bending_mean_single_array=np.array(bending_mean_series_6)
bending_mean_single_array_ravelelled=bending_mean_single_array.ravel()
#
# print(bending_mean_single_array_ravelelled)
# print(type(bending_mean_single_array_ravelelled))

bending_mean_single_array_ravelelled_6_split=[]
for i in range(0,len(bending_mean_single_array_ravelelled)):
    temp=bending_mean_single_array_ravelelled[i]
    # print(temp)
    for j in range(0,len(temp)):
        bending_mean_single_array_ravelelled_6_split.append(temp[j])
# print('check')
bending_mean_single_array_ravelelled_6_split_array=np.array(bending_mean_single_array_ravelelled_6_split)

# print(bending_mean_single_array_ravelelled_6_split_array)
# print(type(bending_mean_single_array_ravelelled_6_split_array))

print('################mean series 6 others')

# for other activities mean
others_mean_series_6=[]
others_mean_series_6=feature_mean_6[2:]
others_mean_single_array=np.array(others_mean_series_6)
others_mean_single_array_ravelelled=others_mean_single_array.ravel()

others_mean_single_array_ravelelled_6_split=others_mean_single_array_ravelelled




#normalizing
bending_min_single_array_ravelelled_1_split_array= np.nan_to_num(bending_min_single_array_ravelelled_1_split_array)
others_min_single_array_ravelelled_1_split=np.nan_to_num(others_min_single_array_ravelelled_1_split)

bending_min_single_array_ravelelled_2_split_array=np.nan_to_num(bending_min_single_array_ravelelled_2_split_array)
others_min_single_array_ravelelled_2_split=np.nan_to_num(others_min_single_array_ravelelled_2_split)

bending_min_single_array_ravelelled_6_split_array=np.nan_to_num(bending_min_single_array_ravelelled_6_split_array)
others_min_single_array_ravelelled_6_split=np.nan_to_num(others_min_single_array_ravelelled_6_split)



#max
bending_max_single_array_ravelelled_1_split_array=np.nan_to_num(bending_max_single_array_ravelelled_1_split_array)
others_max_single_array_ravelelled_1_split=np.nan_to_num(others_max_single_array_ravelelled_1_split)

bending_max_single_array_ravelelled_2_split_array=np.nan_to_num(bending_max_single_array_ravelelled_2_split_array)
others_max_single_array_ravelelled_2_split=np.nan_to_num(others_max_single_array_ravelelled_2_split)

bending_max_single_array_ravelelled_6_split_array=np.nan_to_num(bending_max_single_array_ravelelled_6_split_array)
others_max_single_array_ravelelled_6_split=np.nan_to_num(others_max_single_array_ravelelled_6_split)


#mean

bending_mean_single_array_ravelelled_1_split_array=np.nan_to_num(bending_mean_single_array_ravelelled_1_split_array)
others_mean_single_array_ravelelled_1_split=np.nan_to_num(others_mean_single_array_ravelelled_1_split)


bending_mean_single_array_ravelelled_2_split_array=np.nan_to_num(bending_mean_single_array_ravelelled_2_split_array)
others_mean_single_array_ravelelled_2_split=np.nan_to_num(others_mean_single_array_ravelelled_2_split)

bending_mean_single_array_ravelelled_6_split_array=np.nan_to_num(bending_mean_single_array_ravelelled_6_split_array)
others_mean_single_array_ravelelled_6_split=np.nan_to_num(others_mean_single_array_ravelelled_6_split)

############################PLOTTING VARIABLES
#min
print('min series 1 ')
print(bending_min_single_array_ravelelled_1_split_array)
print(others_min_single_array_ravelelled_1_split)

print('min series 2 ')
print(bending_min_single_array_ravelelled_2_split_array)
print(others_min_single_array_ravelelled_2_split)

print('min series 6 ')
print(bending_min_single_array_ravelelled_6_split_array)
print(others_min_single_array_ravelelled_6_split)


#max
print('max series bending1')
print(bending_max_single_array_ravelelled_1_split_array)

print('max series others1')
print(others_max_single_array_ravelelled_1_split)

print('max series bending2')
print(bending_max_single_array_ravelelled_2_split_array)

print('max series others2')
print(others_max_single_array_ravelelled_2_split)

print('max series bending 6')
print(bending_max_single_array_ravelelled_6_split_array)

print('max series others 6')
print(others_max_single_array_ravelelled_6_split)


#mean
print('mean series others 1')

print(bending_mean_single_array_ravelelled_1_split_array)
print(others_mean_single_array_ravelelled_1_split)


print('mean series others 2')

print(bending_mean_single_array_ravelelled_2_split_array)
print(others_mean_single_array_ravelelled_2_split)

print('man series 6')

print(bending_mean_single_array_ravelelled_6_split_array)
print(others_mean_single_array_ravelelled_6_split)
print('#############################################################################################')

#################PLOTTING
fig, ax = plt.subplots()

plt.xlabel('Time-Series number')
plt.ylabel('Feature Value')
plt.title('Feature-Min: Series 1,2 and 6')
for i in range(0,len(bending_min_single_array_ravelelled_1_split_array)):
    ax.scatter(1,bending_min_single_array_ravelelled_1_split_array[i],  color='blue', label='$x$')
for i in range(0,len(others_min_single_array_ravelelled_1_split)):
    ax.scatter(1,others_min_single_array_ravelelled_1_split[i], 5,color='red', label='$x$')

for i in range(0, len(bending_min_single_array_ravelelled_2_split_array)):
    ax.scatter(2,bending_min_single_array_ravelelled_2_split_array[i], color='blue', label='$x$')
for i in range(0, len(others_min_single_array_ravelelled_2_split)):
    ax.scatter(2,others_min_single_array_ravelelled_2_split[i],  5,color='red', label='$x$')

for i in range(0, len(bending_min_single_array_ravelelled_6_split)):
    ax.scatter(6,bending_min_single_array_ravelelled_6_split_array[i],  color='blue', label='$x$')
for i in range(0, len(others_min_single_array_ravelelled_6_split)):
    ax.scatter(6,others_min_single_array_ravelelled_6_split[i], 5,color='red', label='$x$')

plt.show()



fig, ax = plt.subplots()

plt.xlabel('Time-Series number')
plt.ylabel('Feature Value')
plt.title('Feature-Max: Series 1,2 and 6')
for i in range(0,len(bending_max_single_array_ravelelled_1_split_array)):
    ax.scatter(1,bending_max_single_array_ravelelled_1_split_array[i],  color='blue', label='$x$')
for i in range(0,len(others_max_single_array_ravelelled_1_split)):
    ax.scatter(1,others_max_single_array_ravelelled_1_split[i], 5,color='red', label='$x$')

for i in range(0, len(bending_max_single_array_ravelelled_2_split_array)):
    ax.scatter(2,bending_max_single_array_ravelelled_2_split_array[i], color='blue', label='$x$')
for i in range(0, len(others_max_single_array_ravelelled_2_split)):
    ax.scatter(2,others_max_single_array_ravelelled_2_split[i],  5,color='red', label='$x$')

for i in range(0, len(bending_max_single_array_ravelelled_6_split)):
    ax.scatter(6,bending_max_single_array_ravelelled_6_split_array[i],  color='blue', label='$x$')
for i in range(0, len(others_max_single_array_ravelelled_6_split)):
    ax.scatter(6,others_max_single_array_ravelelled_6_split[i], 5,color='red', label='$x$')

plt.show()



fig, ax = plt.subplots()

plt.xlabel('Time-Series number')
plt.ylabel('Feature Value')
plt.title('Feature-Mean: Series 1,2 and 6')
for i in range(0,len(bending_mean_single_array_ravelelled_1_split_array)):
    ax.scatter(1,bending_mean_single_array_ravelelled_1_split_array[i],  color='blue', label='$x$')
for i in range(0,len(others_mean_single_array_ravelelled_1_split)):
    ax.scatter(1,others_mean_single_array_ravelelled_1_split[i], 5,color='red', label='$x$')

for i in range(0, len(bending_mean_single_array_ravelelled_2_split_array)):
    ax.scatter(2,bending_mean_single_array_ravelelled_2_split_array[i], color='blue', label='$x$')
for i in range(0, len(others_mean_single_array_ravelelled_2_split)):
    ax.scatter(2,others_mean_single_array_ravelelled_2_split[i],  5,color='red', label='$x$')

for i in range(0, len(bending_mean_single_array_ravelelled_6_split)):
    ax.scatter(6,bending_mean_single_array_ravelelled_6_split_array[i],  color='blue', label='$x$')
for i in range(0, len(others_mean_single_array_ravelelled_6_split)):
    ax.scatter(6,others_mean_single_array_ravelelled_6_split[i], 5,color='red', label='$x$')

plt.show()