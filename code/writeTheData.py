import os
import csv
import numpy as np
import pandas as pd

print(os.getcwd())#prints the current directory

sales_data = pd.read_csv("/home/lucifer/data_analysis/workshop/data/sales.csv")


print(sales_data) #Printing the data in the file
sales_data_describe = sales_data.describe() #prints the statistics in the file

with open("/home/lucifer/data_analysis/workshop/data/sales_describe.csv","w") as describe_file:
    for x in sales_data_describe:
        describe_file.write(sales_data_describe)
describe_file.close()
