import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import data, for some reason pandas requires me to insert full path
dataframe_all = pd.read_csv("/Users/rexlow/Documents/Developer/Python/Dataset/pml-training.csv")
print dataframe_all