import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#print(os.getcwd())#prints the current directory

sales_data = pd.read_csv("/home/lucifer/data_analysis/workshop/data/sales.csv")


# print(sales_data) #Printing the data in the file

sales_data_describe = sales_data.describe() #prints the statistics in the file
sales_data_cov = sales_data.cov()
sales_data_corr = sales_data.corr()

sales_data_head = sales_data.head()#The top of data of the file
sales_data_tail = sales_data.tail()#The bottom of data of the file

sales_data_pivot_location = sales_data.pivot_table(sales_data,index = ['Location'])

sales_data_info  = sales_data.info()

sales_data_gender_info = sales_data['Gender'].value_counts() #
sales_data_location_info = sales_data['Location'].value_counts()

sales_data_male_info = sales_data[sales_data['Gender'].str.contains('Male')]
sales_data_female_info = sales_data[sales_data['Gender'].str.contains('Female')]

sales_data_female_location_info = sales_data[sales_data['Gender'].str.contains('Female') & sales_data['Location'].str.contains('Hyderabad')]
sales_data_male_location_info = sales_data[sales_data['Gender'].str.contains('Male') & sales_data['Location'].str.contains('Hyderabad')]

sales_data_graph_data_age = sales_data['Age'].hist(bins=10)
sales_data_graph_data_sales = sales_data['Sales in Rs'].hist(bins=10)

print(sales_data_pivot_location,'\n')

print(sales_data['Age'].unique())
# print(sales_data_head,'\n')
# print(sales_data_tail,'\n')
# print(sales_data_describe,'\n')
# print(sales_data_cov,'\n')
# print(sales_data_corr,'\n')
