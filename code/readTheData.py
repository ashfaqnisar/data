import os
import csv

print(os.getcwd())

file = open("/home/lucifer/data_analysis/workshop/data/sales.csv","r");

reader = csv.reader(file)
