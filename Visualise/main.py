import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import data, for some reason pandas requires me to insert full path
dataframe_all = pd.read_csv("/Users/rexlow/Documents/Developer/Python/Dataset/pml-training.csv", low_memory=False)
num_of_rows = dataframe_all.shape[0]

#Data Cleaning
null_data_count = dataframe_all.isnull().sum()
data_without_null = null_data_count[null_data_count==0]

#remove the columns with missing elements
dataframe_all = dataframe_all[data_without_null.keys()]

#remove the first 7 columns since they have no discriminative information
dataframe_all = dataframe_all.ix[:,7:]

#make all features to work at the same scale(mean and standard deviation) to improve the quality of the result

print dataframe_all