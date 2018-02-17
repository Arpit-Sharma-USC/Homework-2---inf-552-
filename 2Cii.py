import pandas as pd
import numpy as np


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

feature_median_1=[]
feature_median_2=[]
feature_median_3=[]
feature_median_4=[]
feature_median_5=[]
feature_median_6=[]

feature_std_1=[]
feature_std_2=[]
feature_std_3=[]
feature_std_4=[]
feature_std_5=[]
feature_std_6=[]

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

feature_median_folder11 = []
feature_median_folder12 = []
feature_median_folder13 = []
feature_median_folder14 = []
feature_median_folder15 = []
feature_median_folder16 = []

feature_std_folder11 = []
feature_std_folder12 = []
feature_std_folder13 = []
feature_std_folder14 = []
feature_std_folder15 = []
feature_std_folder16 = []


count = 0

for i in range(1,8):

    count += 1
    dataframe = pd.read_csv("C:/Users/Sarah Riaz/Documents/ML/HW/HW2/AReM/bending1/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna()


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

    feature_median_folder11.append(dataframe['avg_rss12'].median())
    feature_median_folder12.append(dataframe['var_rss12'].median())
    feature_median_folder13.append(dataframe['avg_rss13'].median())
    feature_median_folder14.append(dataframe['var_rss13'].median())
    feature_median_folder15.append(dataframe['avg_rss23'].median())
    feature_median_folder16.append(dataframe['var_rss23'].median())

    feature_std_folder11.append(dataframe['avg_rss12'].std())
    feature_std_folder12.append(dataframe['var_rss12'].std())
    feature_std_folder13.append(dataframe['avg_rss13'].std())
    feature_std_folder14.append(dataframe['var_rss13'].std())
    feature_std_folder15.append(dataframe['avg_rss23'].std())
    feature_std_folder16.append(dataframe['var_rss23'].std())


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

feature_median_1.append(feature_median_folder11)
feature_median_2.append(feature_median_folder12)
feature_median_3.append(feature_median_folder13)
feature_median_4.append(feature_median_folder14)
feature_median_5.append(feature_median_folder15)
feature_median_6.append(feature_median_folder16)

feature_std_1.append(feature_std_folder11)
feature_std_2.append(feature_std_folder12)
feature_std_3.append(feature_std_folder13)
feature_std_4.append(feature_std_folder14)
feature_std_5.append(feature_std_folder15)
feature_std_6.append(feature_std_folder16)


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

feature_median_folder11 = []
feature_median_folder12 = []
feature_median_folder13 = []
feature_median_folder14 = []
feature_median_folder15 = []
feature_median_folder16 = []

feature_std_folder11 = []
feature_std_folder12 = []
feature_std_folder13 = []
feature_std_folder14 = []
feature_std_folder15 = []
feature_std_folder16 = []

for i in range(1,7):
    count += 1
    dataframe = pd.read_csv("C:/Users/Sarah Riaz/Documents/ML/HW/HW2/AReM/bending2/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna()

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

    feature_median_folder11.append(dataframe['avg_rss12'].median())
    feature_median_folder12.append(dataframe['var_rss12'].median())
    feature_median_folder13.append(dataframe['avg_rss13'].median())
    feature_median_folder14.append(dataframe['var_rss13'].median())
    feature_median_folder15.append(dataframe['avg_rss23'].median())
    feature_median_folder16.append(dataframe['var_rss23'].median())

    feature_std_folder11.append(dataframe['avg_rss12'].std())
    feature_std_folder12.append(dataframe['var_rss12'].std())
    feature_std_folder13.append(dataframe['avg_rss13'].std())
    feature_std_folder14.append(dataframe['var_rss13'].std())
    feature_std_folder15.append(dataframe['avg_rss23'].std())
    feature_std_folder16.append(dataframe['var_rss23'].std())

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

feature_median_1.append(feature_median_folder11)
feature_median_2.append(feature_median_folder12)
feature_median_3.append(feature_median_folder13)
feature_median_4.append(feature_median_folder14)
feature_median_5.append(feature_median_folder15)
feature_median_6.append(feature_median_folder16)

feature_std_1.append(feature_std_folder11)
feature_std_2.append(feature_std_folder12)
feature_std_3.append(feature_std_folder13)
feature_std_4.append(feature_std_folder14)
feature_std_5.append(feature_std_folder15)
feature_std_6.append(feature_std_folder16)

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

feature_median_folder11 = []
feature_median_folder12 = []
feature_median_folder13 = []
feature_median_folder14 = []
feature_median_folder15 = []
feature_median_folder16 = []

feature_std_folder11 = []
feature_std_folder12 = []
feature_std_folder13 = []
feature_std_folder14 = []
feature_std_folder15 = []
feature_std_folder16 = []

for i in range(1,16):
  count += 1
  # print('into cycling')
  # print(i)
  if(i==9 or i==14):
      dataframe = pd.read_csv("C:/Users/Sarah Riaz/Documents/ML/HW/HW2/AReM/cycling/dataset"+str(i)+".csv")
  else:
      dataframe = pd.read_csv("C:/Users/Sarah Riaz/Documents/ML/HW/HW2/AReM/cycling/dataset"+str(i)+".csv",skiprows = 4)
      dataframe.dropna()
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

      feature_median_folder11.append(dataframe['avg_rss12'].median())
      feature_median_folder12.append(dataframe['var_rss12'].median())
      feature_median_folder13.append(dataframe['avg_rss13'].median())
      feature_median_folder14.append(dataframe['var_rss13'].median())
      feature_median_folder15.append(dataframe['avg_rss23'].median())
      feature_median_folder16.append(dataframe['var_rss23'].median())

      feature_std_folder11.append(dataframe['avg_rss12'].std())
      feature_std_folder12.append(dataframe['var_rss12'].std())
      feature_std_folder13.append(dataframe['avg_rss13'].std())
      feature_std_folder14.append(dataframe['var_rss13'].std())
      feature_std_folder15.append(dataframe['avg_rss23'].std())
      feature_std_folder16.append(dataframe['var_rss23'].std())



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

  feature_median_1.append(feature_median_folder11)
  feature_median_2.append(feature_median_folder12)
  feature_median_3.append(feature_median_folder13)
  feature_median_4.append(feature_median_folder14)
  feature_median_5.append(feature_median_folder15)
  feature_median_6.append(feature_median_folder16)

  feature_std_1.append(feature_std_folder11)
  feature_std_2.append(feature_std_folder12)
  feature_std_3.append(feature_std_folder13)
  feature_std_4.append(feature_std_folder14)
  feature_std_5.append(feature_std_folder15)
  feature_std_6.append(feature_std_folder16)


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

feature_median_folder11 = []
feature_median_folder12 = []
feature_median_folder13 = []
feature_median_folder14 = []
feature_median_folder15 = []
feature_median_folder16 = []

feature_std_folder11 = []
feature_std_folder12 = []
feature_std_folder13 = []
feature_std_folder14 = []
feature_std_folder15 = []
feature_std_folder16 = []

for i in range(1,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Sarah Riaz/Documents/ML/HW/HW2/AReM/lying/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna()

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

    feature_median_folder11.append(dataframe['avg_rss12'].median())
    feature_median_folder12.append(dataframe['var_rss12'].median())
    feature_median_folder13.append(dataframe['avg_rss13'].median())
    feature_median_folder14.append(dataframe['var_rss13'].median())
    feature_median_folder15.append(dataframe['avg_rss23'].median())
    feature_median_folder16.append(dataframe['var_rss23'].median())

    feature_std_folder11.append(dataframe['avg_rss12'].std())
    feature_std_folder12.append(dataframe['var_rss12'].std())
    feature_std_folder13.append(dataframe['avg_rss13'].std())
    feature_std_folder14.append(dataframe['var_rss13'].std())
    feature_std_folder15.append(dataframe['avg_rss23'].std())
    feature_std_folder16.append(dataframe['var_rss23'].std())

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

feature_median_1.append(feature_median_folder11)
feature_median_2.append(feature_median_folder12)
feature_median_3.append(feature_median_folder13)
feature_median_4.append(feature_median_folder14)
feature_median_5.append(feature_median_folder15)
feature_median_6.append(feature_median_folder16)

feature_std_1.append(feature_std_folder11)
feature_std_2.append(feature_std_folder12)
feature_std_3.append(feature_std_folder13)
feature_std_4.append(feature_std_folder14)
feature_std_5.append(feature_std_folder15)
feature_std_6.append(feature_std_folder16)


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

feature_median_folder11 = []
feature_median_folder12 = []
feature_median_folder13 = []
feature_median_folder14 = []
feature_median_folder15 = []
feature_median_folder16 = []

feature_std_folder11 = []
feature_std_folder12 = []
feature_std_folder13 = []
feature_std_folder14 = []
feature_std_folder15 = []
feature_std_folder16 = []

for i in range(1,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Sarah Riaz/Documents/ML/HW/HW2/AReM/sitting/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna()

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

    feature_median_folder11.append(dataframe['avg_rss12'].median())
    feature_median_folder12.append(dataframe['var_rss12'].median())
    feature_median_folder13.append(dataframe['avg_rss13'].median())
    feature_median_folder14.append(dataframe['var_rss13'].median())
    feature_median_folder15.append(dataframe['avg_rss23'].median())
    feature_median_folder16.append(dataframe['var_rss23'].median())

    feature_std_folder11.append(dataframe['avg_rss12'].std())
    feature_std_folder12.append(dataframe['var_rss12'].std())
    feature_std_folder13.append(dataframe['avg_rss13'].std())
    feature_std_folder14.append(dataframe['var_rss13'].std())
    feature_std_folder15.append(dataframe['avg_rss23'].std())
    feature_std_folder16.append(dataframe['var_rss23'].std())

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

feature_median_1.append(feature_median_folder11)
feature_median_2.append(feature_median_folder12)
feature_median_3.append(feature_median_folder13)
feature_median_4.append(feature_median_folder14)
feature_median_5.append(feature_median_folder15)
feature_median_6.append(feature_median_folder16)

feature_std_1.append(feature_std_folder11)
feature_std_2.append(feature_std_folder12)
feature_std_3.append(feature_std_folder13)
feature_std_4.append(feature_std_folder14)
feature_std_5.append(feature_std_folder15)
feature_std_6.append(feature_std_folder16)


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

feature_median_folder11 = []
feature_median_folder12 = []
feature_median_folder13 = []
feature_median_folder14 = []
feature_median_folder15 = []
feature_median_folder16 = []

feature_std_folder11 = []
feature_std_folder12 = []
feature_std_folder13 = []
feature_std_folder14 = []
feature_std_folder15 = []
feature_std_folder16 = []

for i in range(1,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Sarah Riaz/Documents/ML/HW/HW2/AReM/standing/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna()
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

    feature_median_folder11.append(dataframe['avg_rss12'].median())
    feature_median_folder12.append(dataframe['var_rss12'].median())
    feature_median_folder13.append(dataframe['avg_rss13'].median())
    feature_median_folder14.append(dataframe['var_rss13'].median())
    feature_median_folder15.append(dataframe['avg_rss23'].median())
    feature_median_folder16.append(dataframe['var_rss23'].median())

    feature_std_folder11.append(dataframe['avg_rss12'].std())
    feature_std_folder12.append(dataframe['var_rss12'].std())
    feature_std_folder13.append(dataframe['avg_rss13'].std())
    feature_std_folder14.append(dataframe['var_rss13'].std())
    feature_std_folder15.append(dataframe['avg_rss23'].std())
    feature_std_folder16.append(dataframe['var_rss23'].std())


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

feature_median_1.append(feature_median_folder11)
feature_median_2.append(feature_median_folder12)
feature_median_3.append(feature_median_folder13)
feature_median_4.append(feature_median_folder14)
feature_median_5.append(feature_median_folder15)
feature_median_6.append(feature_median_folder16)

feature_std_1.append(feature_std_folder11)
feature_std_2.append(feature_std_folder12)
feature_std_3.append(feature_std_folder13)
feature_std_4.append(feature_std_folder14)
feature_std_5.append(feature_std_folder15)
feature_std_6.append(feature_std_folder16)


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

feature_median_folder11 = []
feature_median_folder12 = []
feature_median_folder13 = []
feature_median_folder14 = []
feature_median_folder15 = []
feature_median_folder16 = []

feature_std_folder11 = []
feature_std_folder12 = []
feature_std_folder13 = []
feature_std_folder14 = []
feature_std_folder15 = []
feature_std_folder16 = []

for i in range(1,16):
    count += 1
    dataframe = pd.read_csv("C:/Users/Sarah Riaz/Documents/ML/HW/HW2/AReM/walking/dataset"+str(i)+".csv", skiprows=4)
    dataframe.dropna()

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

    feature_median_folder11.append(dataframe['avg_rss12'].median())
    feature_median_folder12.append(dataframe['var_rss12'].median())
    feature_median_folder13.append(dataframe['avg_rss13'].median())
    feature_median_folder14.append(dataframe['var_rss13'].median())
    feature_median_folder15.append(dataframe['avg_rss23'].median())
    feature_median_folder16.append(dataframe['var_rss23'].median())

    feature_std_folder11.append(dataframe['avg_rss12'].std())
    feature_std_folder12.append(dataframe['var_rss12'].std())
    feature_std_folder13.append(dataframe['avg_rss13'].std())
    feature_std_folder14.append(dataframe['var_rss13'].std())
    feature_std_folder15.append(dataframe['avg_rss23'].std())
    feature_std_folder16.append(dataframe['var_rss23'].std())


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

feature_median_1.append(feature_median_folder11)
feature_median_2.append(feature_median_folder12)
feature_median_3.append(feature_median_folder13)
feature_median_4.append(feature_median_folder14)
feature_median_5.append(feature_median_folder15)
feature_median_6.append(feature_median_folder16)

feature_std_1.append(feature_std_folder11)
feature_std_2.append(feature_std_folder12)
feature_std_3.append(feature_std_folder13)
feature_std_4.append(feature_std_folder14)
feature_std_5.append(feature_std_folder15)
feature_std_6.append(feature_std_folder16)



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


print('now in median')

print(feature_median_1)
print(feature_median_2)
print(feature_median_3)
print(feature_median_4)
print(feature_median_5)
print(feature_median_6)

print('now in standard deviation')

print(feature_std_1)
print(feature_std_2)
print(feature_std_3)
print(feature_std_4)
print(feature_std_5)
print(feature_std_6)

print(count)
print(np.std(feature_min_1[0]))
print('-------------------------------')
f_min = []

f_min_net=[]
for lst in feature_min_1:
    f_min.extend(lst)
print(np.std(f_min))
f_min_net.append(f_min)
f_min = []
for lst in feature_min_2:
    f_min.extend(lst)
print(np.std(f_min))
f_min_net.append(f_min)

f_min = []
for lst in feature_min_3:
    f_min.extend(lst)
print(np.std(f_min))
f_min_net.append(f_min)

f_min = []
for lst in feature_min_4:
    f_min.extend(lst)
print(np.std(f_min))
f_min_net.append(f_min)

f_min = []
for lst in feature_min_5:
    f_min.extend(lst)
print(np.std(f_min))
f_min_net.append(f_min)

f_min = []
for lst in feature_min_6:
    f_min.extend(lst)
print(np.std(f_min))
f_min_net.append(f_min)

print('---------------------')
f_max_net=[]
f_max = []
for lst in feature_max_1:
    f_max.extend(lst)
print(np.std(f_max))
f_max_net.append(f_max)
f_max = []
for lst in feature_max_2:
    f_max.extend(lst)
print(np.std(f_max))
f_max_net.append(f_max)
f_max = []
for lst in feature_max_3:
    f_max.extend(lst)
print(np.std(f_max))
f_max_net.append(f_max)
f_max = []
for lst in feature_max_4:
    f_max.extend(lst)
print(np.std(f_max))
f_max_net.append(f_max)
f_max = []
for lst in feature_max_5:
    f_max.extend(lst)
print(np.std(f_max))
f_max_net.append(f_max)
f_max = []
for lst in feature_max_6:
    f_max.extend(lst)
print(np.std(f_max))
f_max_net.append(f_max)
print('---------------------')
f_mean = []
f_mean_net=[]
for lst in feature_mean_1:
    f_mean.extend(lst)
print(np.std(f_mean))
f_mean_net.append(f_mean)
f_mean = []
for lst in feature_mean_2:
    f_mean.extend(lst)
print(np.std(f_mean))
f_mean_net.append(f_mean)
f_mean = []
for lst in feature_mean_3:
    f_mean.extend(lst)
print(np.std(f_mean))
f_mean_net.append(f_mean)
f_mean = []
for lst in feature_mean_4:
    f_mean.extend(lst)
print(np.std(f_mean))
f_mean_net.append(f_mean)
f_mean = []
for lst in feature_mean_5:
    f_mean.extend(lst)
print(np.std(f_mean))
f_mean_net.append(f_mean)
f_mean = []
for lst in feature_mean_6:
    f_mean.extend(lst)
print(np.std(f_mean))
f_mean_net.append(f_mean)
print('---------------------')

f_median = []
f_median_net=[]
for lst in feature_median_1:
    f_median.extend(lst)
print(np.std(f_median))
f_median_net.append(f_median)
f_median = []
for lst in feature_median_2:
    f_median.extend(lst)
print(np.std(f_median))
f_median_net.append(f_median)
f_median = []
for lst in feature_median_3:
    f_median.extend(lst)
print(np.std(f_median))
f_median_net.append(f_median)
f_median = []
for lst in feature_median_4:
    f_median.extend(lst)
print(np.std(f_median))
f_median_net.append(f_median)
f_median = []
for lst in feature_median_5:
    f_median.extend(lst)
print(np.std(f_median))
f_median_net.append(f_median)
f_median = []
for lst in feature_median_6:
    f_median.extend(lst)
print(np.std(f_median))
f_median_net.append(f_median)
print('---------------------')
f_std_net=[]
f_std = []
for lst in feature_std_1:
    f_std.extend(lst)
print(np.std(f_std))
f_std_net.append(f_std)
f_std = []
for lst in feature_std_2:
    f_std.extend(lst)
print(np.std(f_std))
f_std_net.append(f_std)
f_std = []
for lst in feature_std_3:
    f_std.extend(lst)
print(np.std(f_std))
f_std_net.append(f_std)
f_std = []
for lst in feature_std_4:
    f_std.extend(lst)
print(np.std(f_std))
f_std_net.append(f_std)
f_std = []
for lst in feature_std_5:
    f_std.extend(lst)
print(np.std(f_std))
f_std_net.append(f_std)
f_std = []
for lst in feature_std_6:
    f_std.extend(lst)
print(np.std(f_std))
f_std_net.append(f_std)