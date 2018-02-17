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
counter=0
chunks=1
i=1
value=480/chunks
while counter < chunks:
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
    counter+=1
    start=int((value*counter)-value)
    end=int((value*counter))
    for i in range(3,8):

        count+=1
        dataframe1 = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/bending1/dataset"+str(i)+".csv", skiprows=4)
        dataframe1.dropna(inplace=True)
        print(dataframe1.shape)
        dataframe=dataframe1[start:end]
        print(dataframe.shape)
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
        dataframe1 = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/bending2/dataset"+str(i)+".csv", skiprows=4)
        dataframe1.dropna(inplace=True)
        dataframe=dataframe1[start:end]

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
          dataframe1 = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/cycling/dataset"+str(i)+".csv")
      else:
          dataframe1 = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/cycling/dataset"+str(i)+".csv",skiprows = 4)
          dataframe1.dropna(inplace=True)
          # print('into features')
      dataframe = dataframe1[start:end]

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
          dataframe1 = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/lying/dataset"+str(i)+".csv",skiprows=4)
      else:
          dataframe1 = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/lying/dataset"+str(i)+".csv",skiprows = 4)
          dataframe1.dropna(inplace=True)
          # print('into features')
      dataframe = dataframe1[start:end]

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
        dataframe1 = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/sitting/dataset"+str(i)+".csv", skiprows=4)
        dataframe1.dropna(inplace=True)
        dataframe=dataframe1[start:end]

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
        dataframe1 = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/standing/dataset"+str(i)+".csv", skiprows=4)
        dataframe1.dropna(inplace=True)
        dataframe=dataframe1[start:end]

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
        dataframe1 = pd.read_csv("C:/Users/Shanu/PycharmProjects/Arem/AReM/walking/dataset"+str(i)+".csv", skiprows=4)
        dataframe1.dropna(inplace=True)
        dataframe=dataframe1[start:end]

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
    #
    # print(bending_min_single_array_ravelelled)
    # print(type(bending_min_single_array_ravelelled))

    bending_min_single_array_ravelelled_6_split=[]
    for i in range(0,len(bending_min_single_array_ravelelled)):
        temp=bending_min_single_array_ravelelled[i]
        # print(temp)
        for j in range(0,len(temp)):
            bending_min_single_array_ravelelled_6_split.append(temp[j])
    # print('check')
    bending_min_single_array_ravelelled_6_split_array=np.array(bending_min_single_array_ravelelled_6_split)

    # print(bending_min_single_array_ravelelled_6_split_array)
    # print(type(bending_min_single_array_ravelelled_6_split_array))

    print('################min series 6 others')

    # for other activities min
    others_min_series_6=[]
    others_min_series_6=feature_min_6[2:]
    others_min_single_array=np.array(others_min_series_6)
    others_min_single_array_ravelelled=others_min_single_array.ravel()

    # print(others_min_single_array_ravelelled)
    # print(type(others_min_single_array_ravelelled))

    others_min_single_array_ravelelled_6_split=others_min_single_array_ravelelled


    print('################max series 6 bending')
    bending_max_series_6=[]

    bending_max_series_6=feature_max_6[0:2]
    bending_max_single_array=np.array(bending_max_series_6)
    bending_max_single_array_ravelelled=bending_max_single_array.ravel()
    #
    # print(bending_max_single_array_ravelelled)
    # print(type(bending_max_single_array_ravelelled))

    bending_max_single_array_ravelelled_6_split=[]
    for i in range(0,len(bending_max_single_array_ravelelled)):
        temp=bending_max_single_array_ravelelled[i]
        # print(temp)
        for j in range(0,len(temp)):
            bending_max_single_array_ravelelled_6_split.append(temp[j])
    # print('check')
    bending_max_single_array_ravelelled_6_split_array=np.array(bending_max_single_array_ravelelled_6_split)

    # print(bending_max_single_array_ravelelled_6_split_array)
    # print(type(bending_max_single_array_ravelelled_6_split_array))

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



    #################added here for the rest of features############################

    print('################min series 3 bending')
    bending_min_series_3 = []

    bending_min_series_3 = feature_min_3[0:2]
    bending_min_single_array = np.array(bending_min_series_3)
    bending_min_single_array_ravelelled = bending_min_single_array.ravel()

    # print(bending_min_single_array_ravelelled)
    # print(type(bending_min_single_array_ravelelled))

    bending_min_single_array_ravelelled_3_split = []
    for i in range(0, len(bending_min_single_array_ravelelled)):
        temp = bending_min_single_array_ravelelled[i]
        # print(temp)
        for j in range(0, len(temp)):
            bending_min_single_array_ravelelled_3_split.append(temp[j])
    # print('check')
    bending_min_single_array_ravelelled_3_split_array = np.array(bending_min_single_array_ravelelled_3_split)

    # print(bending_min_single_array_ravelelled_3_split_array)
    # print(type(bending_min_single_array_ravelelled_3_split_array))

    print('################min series 3 others')

    # for other activities min
    others_min_series_3 = []
    others_min_series_3 = feature_min_3[2:]
    others_min_single_array = np.array(others_min_series_3)
    others_min_single_array_ravelelled = others_min_single_array.ravel()

    # print(others_min_single_array_ravelelled)
    # print(type(others_min_single_array_ravelelled))

    others_min_single_array_ravelelled_3_split = others_min_single_array_ravelelled

    print('################max series 3 bending')
    bending_max_series_3 = []

    bending_max_series_3 = feature_max_3[0:2]
    bending_max_single_array = np.array(bending_max_series_3)
    bending_max_single_array_ravelelled = bending_max_single_array.ravel()
    #
    # print(bending_max_single_array_ravelelled)
    # print(type(bending_max_single_array_ravelelled))

    bending_max_single_array_ravelelled_3_split = []
    for i in range(0, len(bending_max_single_array_ravelelled)):
        temp = bending_max_single_array_ravelelled[i]
        # print(temp)
        for j in range(0, len(temp)):
            bending_max_single_array_ravelelled_3_split.append(temp[j])
    # print('check')
    bending_max_single_array_ravelelled_3_split_array = np.array(bending_max_single_array_ravelelled_3_split)

    # print(bending_max_single_array_ravelelled_3_split_array)
    # print(type(bending_max_single_array_ravelelled_3_split_array))

    print('################max series 3 others')

    # for other activities max
    others_max_series_3 = []
    others_max_series_3 = feature_max_3[2:]
    others_max_single_array = np.array(others_max_series_3)
    others_max_single_array_ravelelled = others_max_single_array.ravel()

    # print(others_max_single_array_ravelelled)
    # print(type(others_max_single_array_ravelelled))

    others_max_single_array_ravelelled_3_split = others_max_single_array_ravelelled

    print('################mean series 3 bending')
    bending_mean_series_3 = []

    bending_mean_series_3 = feature_mean_3[0:2]
    bending_mean_single_array = np.array(bending_mean_series_3)
    bending_mean_single_array_ravelelled = bending_mean_single_array.ravel()
    #
    # print(bending_mean_single_array_ravelelled)
    # print(type(bending_mean_single_array_ravelelled))

    bending_mean_single_array_ravelelled_3_split = []
    for i in range(0, len(bending_mean_single_array_ravelelled)):
        temp = bending_mean_single_array_ravelelled[i]
        # print(temp)
        for j in range(0, len(temp)):
            bending_mean_single_array_ravelelled_3_split.append(temp[j])
    # print('check')
    bending_mean_single_array_ravelelled_3_split_array = np.array(bending_mean_single_array_ravelelled_3_split)

    # print(bending_mean_single_array_ravelelled_3_split_array)
    # print(type(bending_mean_single_array_ravelelled_3_split_array))

    print('################mean series 3 others')

    # for other activities mean
    others_mean_series_3 = []
    others_mean_series_3 = feature_mean_3[2:]
    others_mean_single_array = np.array(others_mean_series_3)
    others_mean_single_array_ravelelled = others_mean_single_array.ravel()
    #
    # print(others_mean_single_array_ravelelled)
    # print(type(others_mean_single_array_ravelelled))

    others_mean_single_array_ravelelled_3_split = others_mean_single_array_ravelelled

    print('################min series 4 bending')
    bending_min_series_4 = []

    bending_min_series_4 = feature_min_4[0:2]
    bending_min_single_array = np.array(bending_min_series_4)
    bending_min_single_array_ravelelled = bending_min_single_array.ravel()

    # print(bending_min_single_array_ravelelled)
    # print(type(bending_min_single_array_ravelelled))

    bending_min_single_array_ravelelled_4_split = []
    for i in range(0, len(bending_min_single_array_ravelelled)):
        temp = bending_min_single_array_ravelelled[i]
        # print(temp)
        for j in range(0, len(temp)):
            bending_min_single_array_ravelelled_4_split.append(temp[j])
    # print('check')
    bending_min_single_array_ravelelled_4_split_array = np.array(bending_min_single_array_ravelelled_4_split)

    # print(bending_min_single_array_ravelelled_4_split_array)
    # print(type(bending_min_single_array_ravelelled_4_split_array))

    print('################min series 4 others')

    # for other activities min
    others_min_series_4 = []
    others_min_series_4 = feature_min_4[2:]
    others_min_single_array = np.array(others_min_series_4)
    others_min_single_array_ravelelled = others_min_single_array.ravel()

    # print(others_min_single_array_ravelelled)
    # print(type(others_min_single_array_ravelelled))

    others_min_single_array_ravelelled_4_split = others_min_single_array_ravelelled

    print('################max series 4 bending')
    bending_max_series_4 = []

    bending_max_series_4 = feature_max_4[0:2]
    bending_max_single_array = np.array(bending_max_series_4)
    bending_max_single_array_ravelelled = bending_max_single_array.ravel()
    #
    # print(bending_max_single_array_ravelelled)
    # print(type(bending_max_single_array_ravelelled))

    bending_max_single_array_ravelelled_4_split = []
    for i in range(0, len(bending_max_single_array_ravelelled)):
        temp = bending_max_single_array_ravelelled[i]
        # print(temp)
        for j in range(0, len(temp)):
            bending_max_single_array_ravelelled_4_split.append(temp[j])
    # print('check')
    bending_max_single_array_ravelelled_4_split_array = np.array(bending_max_single_array_ravelelled_4_split)

    # print(bending_max_single_array_ravelelled_4_split_array)
    # print(type(bending_max_single_array_ravelelled_4_split_array))

    print('################max series 4 others')

    # for other activities max
    others_max_series_4 = []
    others_max_series_4 = feature_max_4[2:]
    others_max_single_array = np.array(others_max_series_4)
    others_max_single_array_ravelelled = others_max_single_array.ravel()

    # print(others_max_single_array_ravelelled)
    # print(type(others_max_single_array_ravelelled))

    others_max_single_array_ravelelled_4_split = others_max_single_array_ravelelled

    print('################mean series 4 bending')
    bending_mean_series_4 = []

    bending_mean_series_4 = feature_mean_4[0:2]
    bending_mean_single_array = np.array(bending_mean_series_4)
    bending_mean_single_array_ravelelled = bending_mean_single_array.ravel()
    #
    # print(bending_mean_single_array_ravelelled)
    # print(type(bending_mean_single_array_ravelelled))

    bending_mean_single_array_ravelelled_4_split = []
    for i in range(0, len(bending_mean_single_array_ravelelled)):
        temp = bending_mean_single_array_ravelelled[i]
        # print(temp)
        for j in range(0, len(temp)):
            bending_mean_single_array_ravelelled_4_split.append(temp[j])
    # print('check')
    bending_mean_single_array_ravelelled_4_split_array = np.array(bending_mean_single_array_ravelelled_4_split)

    # print(bending_mean_single_array_ravelelled_4_split_array)
    # print(type(bending_mean_single_array_ravelelled_4_split_array))

    print('################mean series 4 others')

    # for other activities mean
    others_mean_series_4 = []
    others_mean_series_4 = feature_mean_4[2:]
    others_mean_single_array = np.array(others_mean_series_4)
    others_mean_single_array_ravelelled = others_mean_single_array.ravel()
    #
    # print(others_mean_single_array_ravelelled)
    # print(type(others_mean_single_array_ravelelled))

    others_mean_single_array_ravelelled_4_split = others_mean_single_array_ravelelled

    print('################min series 5 bending')
    bending_min_series_5 = []

    bending_min_series_5 = feature_min_5[0:2]
    bending_min_single_array = np.array(bending_min_series_5)
    bending_min_single_array_ravelelled = bending_min_single_array.ravel()

    # print(bending_min_single_array_ravelelled)
    # print(type(bending_min_single_array_ravelelled))

    bending_min_single_array_ravelelled_5_split = []
    for i in range(0, len(bending_min_single_array_ravelelled)):
        temp = bending_min_single_array_ravelelled[i]
        # print(temp)
        for j in range(0, len(temp)):
            bending_min_single_array_ravelelled_5_split.append(temp[j])
    # print('check')
    bending_min_single_array_ravelelled_5_split_array = np.array(bending_min_single_array_ravelelled_5_split)

    # print(bending_min_single_array_ravelelled_5_split_array)
    # print(type(bending_min_single_array_ravelelled_5_split_array))

    print('################min series 5 others')

    # for other activities min
    others_min_series_5 = []
    others_min_series_5 = feature_min_5[2:]
    others_min_single_array = np.array(others_min_series_5)
    others_min_single_array_ravelelled = others_min_single_array.ravel()

    # print(others_min_single_array_ravelelled)
    # print(type(others_min_single_array_ravelelled))

    others_min_single_array_ravelelled_5_split = others_min_single_array_ravelelled

    print('################max series 5 bending')
    bending_max_series_5 = []

    bending_max_series_5 = feature_max_5[0:2]
    bending_max_single_array = np.array(bending_max_series_5)
    bending_max_single_array_ravelelled = bending_max_single_array.ravel()
    #
    # print(bending_max_single_array_ravelelled)
    # print(type(bending_max_single_array_ravelelled))

    bending_max_single_array_ravelelled_5_split = []
    for i in range(0, len(bending_max_single_array_ravelelled)):
        temp = bending_max_single_array_ravelelled[i]
        # print(temp)
        for j in range(0, len(temp)):
            bending_max_single_array_ravelelled_5_split.append(temp[j])
    # print('check')
    bending_max_single_array_ravelelled_5_split_array = np.array(bending_max_single_array_ravelelled_5_split)

    # print(bending_max_single_array_ravelelled_5_split_array)
    # print(type(bending_max_single_array_ravelelled_5_split_array))

    print('################max series 5 others')

    # for other activities max
    others_max_series_5 = []
    others_max_series_5 = feature_max_5[2:]
    others_max_single_array = np.array(others_max_series_5)
    others_max_single_array_ravelelled = others_max_single_array.ravel()

    # print(others_max_single_array_ravelelled)
    # print(type(others_max_single_array_ravelelled))

    others_max_single_array_ravelelled_5_split = others_max_single_array_ravelelled

    print('################mean series 5 bending')
    bending_mean_series_5 = []

    bending_mean_series_5 = feature_mean_5[0:2]
    bending_mean_single_array = np.array(bending_mean_series_5)
    bending_mean_single_array_ravelelled = bending_mean_single_array.ravel()
    #
    # print(bending_mean_single_array_ravelelled)
    # print(type(bending_mean_single_array_ravelelled))

    bending_mean_single_array_ravelelled_5_split = []
    for i in range(0, len(bending_mean_single_array_ravelelled)):
        temp = bending_mean_single_array_ravelelled[i]
        # print(temp)
        for j in range(0, len(temp)):
            bending_mean_single_array_ravelelled_5_split.append(temp[j])
    # print('check')
    bending_mean_single_array_ravelelled_5_split_array = np.array(bending_mean_single_array_ravelelled_5_split)

    # print(bending_mean_single_array_ravelelled_5_split_array)
    # print(type(bending_mean_single_array_ravelelled_5_split_array))

    print('################mean series 5 others')

    # for other activities mean
    others_mean_series_5 = []
    others_mean_series_5 = feature_mean_5[2:]
    others_mean_single_array = np.array(others_mean_series_5)
    others_mean_single_array_ravelelled = others_mean_single_array.ravel()
    #
    # print(others_mean_single_array_ravelelled)
    # print(type(others_mean_single_array_ravelelled))

    others_mean_single_array_ravelelled_5_split = others_mean_single_array_ravelelled

    #normalizing
    bending_min_single_array_ravelelled_1_split_array= np.nan_to_num(bending_min_single_array_ravelelled_1_split_array)
    others_min_single_array_ravelelled_1_split=np.nan_to_num(others_min_single_array_ravelelled_1_split)

    bending_min_single_array_ravelelled_2_split_array=np.nan_to_num(bending_min_single_array_ravelelled_2_split_array)
    others_min_single_array_ravelelled_2_split=np.nan_to_num(others_min_single_array_ravelelled_2_split)

    bending_min_single_array_ravelelled_6_split_array=np.nan_to_num(bending_min_single_array_ravelelled_6_split_array)
    others_min_single_array_ravelelled_6_split=np.nan_to_num(others_min_single_array_ravelelled_6_split)

    bending_min_single_array_ravelelled_3_split_array = np.nan_to_num(bending_min_single_array_ravelelled_3_split_array)
    others_min_single_array_ravelelled_3_split = np.nan_to_num(others_min_single_array_ravelelled_3_split)

    bending_min_single_array_ravelelled_4_split_array = np.nan_to_num(bending_min_single_array_ravelelled_4_split_array)
    others_min_single_array_ravelelled_4_split = np.nan_to_num(others_min_single_array_ravelelled_4_split)

    bending_min_single_array_ravelelled_5_split_array = np.nan_to_num(bending_min_single_array_ravelelled_5_split_array)
    others_min_single_array_ravelelled_5_split = np.nan_to_num(others_min_single_array_ravelelled_5_split)

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


    ###############adding the rest


    # max
    bending_max_single_array_ravelelled_3_split_array = np.nan_to_num(bending_max_single_array_ravelelled_3_split_array)
    others_max_single_array_ravelelled_3_split = np.nan_to_num(others_max_single_array_ravelelled_3_split)

    bending_max_single_array_ravelelled_4_split_array = np.nan_to_num(bending_max_single_array_ravelelled_4_split_array)
    others_max_single_array_ravelelled_4_split = np.nan_to_num(others_max_single_array_ravelelled_4_split)

    bending_max_single_array_ravelelled_5_split_array = np.nan_to_num(bending_max_single_array_ravelelled_5_split_array)
    others_max_single_array_ravelelled_5_split = np.nan_to_num(others_max_single_array_ravelelled_5_split)

    # mean

    bending_mean_single_array_ravelelled_3_split_array = np.nan_to_num(
        bending_mean_single_array_ravelelled_3_split_array)
    others_mean_single_array_ravelelled_3_split = np.nan_to_num(others_mean_single_array_ravelelled_3_split)

    bending_mean_single_array_ravelelled_4_split_array = np.nan_to_num(
        bending_mean_single_array_ravelelled_4_split_array)
    others_mean_single_array_ravelelled_4_split = np.nan_to_num(others_mean_single_array_ravelelled_4_split)

    bending_mean_single_array_ravelelled_5_split_array = np.nan_to_num(
        bending_mean_single_array_ravelelled_5_split_array)
    others_mean_single_array_ravelelled_5_split = np.nan_to_num(others_mean_single_array_ravelelled_5_split)

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

    c_1_min=np.hstack((bending_min_single_array_ravelelled_1_split_array, others_min_single_array_ravelelled_1_split))
    print('printing c-1 min')
    print(c_1_min)
    print('length:')
    print(len(c_1_min))



    c_2_min=np.hstack((bending_min_single_array_ravelelled_2_split_array,others_min_single_array_ravelelled_2_split))
    c_3_min = np.hstack((bending_min_single_array_ravelelled_3_split_array, others_min_single_array_ravelelled_3_split))
    c_4_min = np.hstack((bending_min_single_array_ravelelled_4_split_array, others_min_single_array_ravelelled_4_split))
    c_5_min = np.hstack((bending_min_single_array_ravelelled_5_split_array, others_min_single_array_ravelelled_5_split))
    c_6_min = np.hstack((bending_min_single_array_ravelelled_6_split_array, others_min_single_array_ravelelled_6_split))

    print('length c-2:')
    print(len(c_2_min))

    print('length:c-3')
    print(len(c_3_min))

    print('length:c-4')
    print(len(c_4_min))

    print('length:c-5')
    print(len(c_5_min))

    print('length:c-6')
    print(len(c_6_min))

    c_1_max = np.hstack((bending_max_single_array_ravelelled_1_split_array, others_max_single_array_ravelelled_1_split))
    c_2_max = np.hstack((bending_max_single_array_ravelelled_2_split_array, others_max_single_array_ravelelled_2_split))
    c_3_max = np.hstack((bending_max_single_array_ravelelled_3_split_array, others_max_single_array_ravelelled_3_split))
    c_4_max = np.hstack((bending_max_single_array_ravelelled_4_split_array, others_max_single_array_ravelelled_4_split))
    c_5_max = np.hstack((bending_max_single_array_ravelelled_5_split_array, others_max_single_array_ravelelled_5_split))
    c_6_max = np.hstack((bending_max_single_array_ravelelled_6_split_array, others_max_single_array_ravelelled_6_split))


    print('length-c1 max')
    print(len(c_1_max))

    print('length c-2:')
    print(len(c_2_max))

    print('length:c-3')
    print(len(c_3_max))

    print('length:c-4')
    print(len(c_4_max))

    print('length:c-5')
    print(len(c_5_max))

    print('length:c-6')
    print(len(c_6_max))




    c_1_mean = np.hstack((bending_mean_single_array_ravelelled_1_split_array, others_mean_single_array_ravelelled_1_split))

    c_2_mean = np.hstack((bending_mean_single_array_ravelelled_2_split_array, others_mean_single_array_ravelelled_2_split))
    c_3_mean = np.hstack((bending_mean_single_array_ravelelled_3_split_array, others_mean_single_array_ravelelled_3_split))
    c_4_mean = np.hstack((bending_mean_single_array_ravelelled_4_split_array, others_mean_single_array_ravelelled_4_split))
    c_5_mean = np.hstack((bending_mean_single_array_ravelelled_5_split_array, others_mean_single_array_ravelelled_5_split))
    c_6_mean = np.hstack((bending_mean_single_array_ravelelled_6_split_array, others_mean_single_array_ravelelled_6_split))

    print('length-c1 mean')
    print(len(c_1_mean))

    print('length c-2:')
    print(len(c_2_mean))

    print('length:c-3')
    print(len(c_3_mean))

    print('length:c-4')
    print(len(c_4_mean))

    print('length:c-5')
    print(len(c_5_mean))

    print('length:c-6')
    print(len(c_6_mean))



    ##############################POPULATING  A NEW DATAFRAME

    y = []
    for i in range(0, 69):
        if (i in range(0, 9)):
            y.append(1)
        else:
            y.append(0)

    data={'s1min':c_1_min,
    's2min':c_2_min,
    's3min':c_3_min,
    's4min':c_4_min,
    's5min':c_5_min,
    's6min':c_6_min,
    's1max':c_1_max,
    's2max':c_2_max,
    's3max':c_3_max,
    's4max':c_4_max,
    's5max':c_5_max,
    's6max':c_6_max,
    's1mean': c_1_mean,
    's2mean': c_2_mean,
    's3mean': c_3_mean,
    's4mean': c_4_mean,
    's5mean': c_5_mean,
    's6mean': c_6_mean,
    'target':y
    }

    my_dataframe=pd.DataFrame(data)
    print(my_dataframe)
    pd.DataFrame.to_csv(my_dataframe,path_or_buf='C:/Users/Shanu/PycharmProjects/Arem/AReM/my_dataset.csv',index=False)



    # print('#############################################################################################')
    #
    # #################PLOTTING
    # fig, ax = plt.subplots()
    #
    # plt.xlabel('Time-Series number')
    # plt.ylabel('Feature Value')
    # plt.title('Chunk : '+str(counter)+' Feature-Min: Series 1,2 and 6 for start'+str(start)+' and end: '+ str(end))
    # for i in range(0,len(bending_min_single_array_ravelelled_1_split_array)):
    #     ax.scatter(1,bending_min_single_array_ravelelled_1_split_array[i],  color='blue', label='$x$')
    # for i in range(0,len(others_min_single_array_ravelelled_1_split)):
    #     ax.scatter(1,others_min_single_array_ravelelled_1_split[i], 5,color='red', label='$x$')
    #
    # for i in range(0, len(bending_min_single_array_ravelelled_2_split_array)):
    #     ax.scatter(2,bending_min_single_array_ravelelled_2_split_array[i], color='blue', label='$x$')
    # for i in range(0, len(others_min_single_array_ravelelled_2_split)):
    #     ax.scatter(2,others_min_single_array_ravelelled_2_split[i],  5,color='red', label='$x$')
    #
    # for i in range(0, len(bending_min_single_array_ravelelled_6_split)):
    #     ax.scatter(6,bending_min_single_array_ravelelled_6_split_array[i],  color='blue', label='$x$')
    # for i in range(0, len(others_min_single_array_ravelelled_6_split)):
    #     ax.scatter(6,others_min_single_array_ravelelled_6_split[i], 5,color='red', label='$x$')
    #
    # plt.show()
    #
    #
    #
    # fig, ax = plt.subplots()
    #
    # plt.xlabel('Time-Series number')
    # plt.ylabel('Feature Value')
    # plt.title('Chunk : '+str(counter)+' Feature-Max: Series 1,2 and 6 for start'+str(start)+' and end: '+ str(end))
    # for i in range(0,len(bending_max_single_array_ravelelled_1_split_array)):
    #     ax.scatter(1,bending_max_single_array_ravelelled_1_split_array[i],  color='blue', label='$x$')
    # for i in range(0,len(others_max_single_array_ravelelled_1_split)):
    #     ax.scatter(1,others_max_single_array_ravelelled_1_split[i], 5,color='red', label='$x$')
    #
    # for i in range(0, len(bending_max_single_array_ravelelled_2_split_array)):
    #     ax.scatter(2,bending_max_single_array_ravelelled_2_split_array[i], color='blue', label='$x$')
    # for i in range(0, len(others_max_single_array_ravelelled_2_split)):
    #     ax.scatter(2,others_max_single_array_ravelelled_2_split[i],  5,color='red', label='$x$')
    #
    # for i in range(0, len(bending_max_single_array_ravelelled_6_split)):
    #     ax.scatter(6,bending_max_single_array_ravelelled_6_split_array[i],  color='blue', label='$x$')
    # for i in range(0, len(others_max_single_array_ravelelled_6_split)):
    #     ax.scatter(6,others_max_single_array_ravelelled_6_split[i], 5,color='red', label='$x$')
    #
    # plt.show()
    #
    #
    #
    # fig, ax = plt.subplots()
    #
    # plt.xlabel('Time-Series number')
    # plt.ylabel('Feature Value')
    # plt.title('Chunk : '+str(counter)+' Feature-Mean: Series 1,2 and 6 for start'+str(start)+' and end: '+ str(end))
    # for i in range(0,len(bending_mean_single_array_ravelelled_1_split_array)):
    #     ax.scatter(1,bending_mean_single_array_ravelelled_1_split_array[i],  color='blue', label='$x$')
    # for i in range(0,len(others_mean_single_array_ravelelled_1_split)):
    #     ax.scatter(1,others_mean_single_array_ravelelled_1_split[i], 5,color='red', label='$x$')
    #
    # for i in range(0, len(bending_mean_single_array_ravelelled_2_split_array)):
    #     ax.scatter(2,bending_mean_single_array_ravelelled_2_split_array[i], color='blue', label='$x$')
    # for i in range(0, len(others_mean_single_array_ravelelled_2_split)):
    #     ax.scatter(2,others_mean_single_array_ravelelled_2_split[i],  5,color='red', label='$x$')
    #
    # for i in range(0, len(bending_mean_single_array_ravelelled_6_split)):
    #     ax.scatter(6,bending_mean_single_array_ravelelled_6_split_array[i],  color='blue', label='$x$')
    # for i in range(0, len(others_mean_single_array_ravelelled_6_split)):
    #     ax.scatter(6,others_mean_single_array_ravelelled_6_split[i], 5,color='red', label='$x$')
    #
    # plt.show()
    # ax.plot(x, x * x, color='red', label='$x^2$')
    # ax.plot(x, x ** 3, color='blue', label='$x^3$')
    # #
    # classify_min_series_1=[]
    #
    # print('my test')
    # f_min_1_ravel_vaala=feature_min_1[2:]
    # a=np.array(f_min_1_ravel_vaala)
    # b=a.ravel()
    # print(b)
    #
    #
    # #train_idx = np.random.choice(np.arange(0,len(Dat)),500)
    # # train_idx = np.random.rand(len(Dat)) < 0.6
    # # X_train = Dat[train_idx]
    # # y_train = y[train_idx]
    # # X_test = Dat.iloc[~train_idx]
    # # y_test = y[~train_idx]
    # #
    # # model = templib.customFeatureLibrary()
    # #
    # # model.feature_agg(Data=X_train)
    # # model.F_test(Data=X_train,y=y_train)
    # # # print(X_train)
    # # # print('printing y train')
    # # # print(y_train)
    # # model.fit(Data=X_train,y=y_train,size=5)
    # # # model.score(X_test,y_test)