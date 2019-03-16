import os
import csv
import numpy as np
import pandas as pd

print(os.getcwd())#prints the current directory

file1 = pd.read_csv("/home/lucifer/data_analysis/workshop/data/sales.csv")
print(file1) #Printing the data in the file
print(file1.describe()) #prints the statistics in the file
