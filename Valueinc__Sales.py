# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 20:04:48 2023

@author: PC
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction - p1.csv')

data = pd.read_csv('transaction - p1.csv',sep=';')

#summary of the data 
data.info()

#playing around with variables

#working with calculations

#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#MATHEMATICAL operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem

SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem

#CostPerTransaction Column Calculation
#CostPerTransaction = CostPerItem * NumberOfItemsPurchased

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
data['CostPerTransaction'] = CostPerTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = sales - cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (sales - cost) / cost

data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction']  ) / data['CostPerTransaction']

roundmarkup = round(data['Markup'], 2)

data['Markup'] = roundmarkup

day = data['Day'] .astype(str)
year = data['Year'] .astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#Using split to split the clientkeywords field
#new_var = Column.str.split('sep' , expand = true)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using replace funtion 

data['ClientAge'] = data['ClientAge'].str.replace ('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#using lower function to change item names to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in new data set

seasons = pd.read_csv('value_inc_seasons (1) - p1.csv' , sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

#df = df.drop('column name' , axis = 1)

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

#export into csv

data.to_csv('ValueInc_Cleaned.csv', index=False)









