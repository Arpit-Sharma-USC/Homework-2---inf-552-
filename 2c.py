import pandas as pd
import numpy as np
import customFeatureLibrary as templib

# dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/test_data/sitting/dataset2.csv", skiprows=4)
#
# Alldat=dataframe
# Alldat['bending1']=""
# Alldat1 = Alldat.loc[:, (Alldat != 0).any(axis=0)]
# y = np.array(Alldat1['bending1'])
# Dat = Alldat1.iloc[:,:-1]


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


count=0

for i in range(1,8):

    count+=1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/bending1/dataset"+str(i)+".csv", skiprows=4)
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


    # print('break')
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

for i in range(1,7):
    count += 1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/bending2/dataset"+str(i)+".csv", skiprows=4)
    dataframe.fillna(method='ffill')

    # print('into features')
    #
    # feature_min_folder11 = []
    # feature_min_folder12 = []
    # feature_min_folder13 = []
    # feature_min_folder14 = []
    # feature_min_folder15 = []
    # feature_min_folder16 = []
    #
    # feature_max_folder11 = []
    # feature_max_folder12 = []
    # feature_max_folder13 = []
    # feature_max_folder14 = []
    # feature_max_folder15 = []
    # feature_max_folder16 = []
    #
    # feature_mean_folder11 = []
    # feature_mean_folder12 = []
    # feature_mean_folder13 = []
    # feature_mean_folder14 = []
    # feature_mean_folder15 = []
    # feature_mean_folder16 = []
    #
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


    # print('break')
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

for i in range(1,16):
  count += 1
  # print('into cycling')
  # print(i)
  if(i==9 or i==14):
      dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/cycling/dataset"+str(i)+".csv")
  else:
      dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/cycling/dataset"+str(i)+".csv",skiprows = 4)
      dataframe.dropna(inplace=True)
      # feature_min_folder11 = []
      # feature_min_folder12 = []
      # feature_min_folder13 = []
      # feature_min_folder14 = []
      # feature_min_folder15 = []
      # feature_min_folder16 = []
      #
      # feature_max_folder11 = []
      # feature_max_folder12 = []
      # feature_max_folder13 = []
      # feature_max_folder14 = []
      # feature_max_folder15 = []
      # feature_max_folder16 = []
      #
      # feature_mean_folder11 = []
      # feature_mean_folder12 = []
      # feature_mean_folder13 = []
      # feature_mean_folder14 = []
      # feature_mean_folder15 = []
      # feature_mean_folder16 = []
      #
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


      # print('break')
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

for i in range(1,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/lying/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna(inplace=True)

    # print('into features')
    #
    # feature_min_folder11 = []
    # feature_min_folder12 = []
    # feature_min_folder13 = []
    # feature_min_folder14 = []
    # feature_min_folder15 = []
    # feature_min_folder16 = []
    #
    # feature_max_folder11 = []
    # feature_max_folder12 = []
    # feature_max_folder13 = []
    # feature_max_folder14 = []
    # feature_max_folder15 = []
    # feature_max_folder16 = []
    #
    # feature_mean_folder11 = []
    # feature_mean_folder12 = []
    # feature_mean_folder13 = []
    # feature_mean_folder14 = []
    # feature_mean_folder15 = []
    # feature_mean_folder16 = []

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


    # print('break')

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

for i in range(1,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/sitting/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna(inplace=True)
    # feature_min_folder11 = []
    # feature_min_folder12 = []
    # feature_min_folder13 = []
    # feature_min_folder14 = []
    # feature_min_folder15 = []
    # feature_min_folder16 = []
    #
    # feature_max_folder11 = []
    # feature_max_folder12 = []
    # feature_max_folder13 = []
    # feature_max_folder14 = []
    # feature_max_folder15 = []
    # feature_max_folder16 = []
    #
    # feature_mean_folder11 = []
    # feature_mean_folder12 = []
    # feature_mean_folder13 = []
    # feature_mean_folder14 = []
    # feature_mean_folder15 = []
    # feature_mean_folder16 = []

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


    # print('break')
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

for i in range(1,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/standing/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna(inplace=True)
    # feature_min_folder11 = []
    # feature_min_folder12 = []
    # feature_min_folder13 = []
    # feature_min_folder14 = []
    # feature_min_folder15 = []
    # feature_min_folder16 = []
    #
    # feature_max_folder11 = []
    # feature_max_folder12 = []
    # feature_max_folder13 = []
    # feature_max_folder14 = []
    # feature_max_folder15 = []
    # feature_max_folder16 = []
    #
    # feature_mean_folder11 = []
    # feature_mean_folder12 = []
    # feature_mean_folder13 = []
    # feature_mean_folder14 = []
    # feature_mean_folder15 = []
    # feature_mean_folder16 = []

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


    # print('break')
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

for i in range(1,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/walking/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna(inplace=True)

    # print('into features')
    #
    # feature_min_folder11 = []
    # feature_min_folder12 = []
    # feature_min_folder13 = []
    # feature_min_folder14 = []
    # feature_min_folder15 = []
    # feature_min_folder16 = []
    #
    # feature_max_folder11 = []
    # feature_max_folder12 = []
    # feature_max_folder13 = []
    # feature_max_folder14 = []
    # feature_max_folder15 = []
    # feature_max_folder16 = []
    #
    # feature_mean_folder11 = []
    # feature_mean_folder12 = []
    # feature_mean_folder13 = []
    # feature_mean_folder14 = []
    # feature_mean_folder15 = []
    # feature_mean_folder16 = []

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


    # print('break')
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
#train_idx = np.random.choice(np.arange(0,len(Dat)),500)
# train_idx = np.random.rand(len(Dat)) < 0.6
# X_train = Dat[train_idx]
# y_train = y[train_idx]
# X_test = Dat.iloc[~train_idx]
# y_test = y[~train_idx]
#
# model = templib.customFeatureLibrary()
#
# model.feature_agg(Data=X_train)
# model.F_test(Data=X_train,y=y_train)
# # print(X_train)
# # print('printing y train')
# # print(y_train)
# model.fit(Data=X_train,y=y_train,size=5)
# # model.score(X_test,y_test)