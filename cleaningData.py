#!/usr/bin/env python
# coding: utf-8

# ### Import pandas



import pandas as pd


# ### Import the data in the CSV file
# You can find the data [here](https://raw.githubusercontent.com/axrd/datasets/master/gdpmessy2.csv). Should have a shape of (222,3). Use this [resource](https://www.iban.com/country-codes) to clean values correctly.



df = pd.read_csv('https://raw.githubusercontent.com/axrd/datasets/master/gdpmessy2.csv')


# ### Quickly inspect the head



df.head()


# ### Inspect the tail



df.tail()


# ### What is the shape of the DataFrame? Does it correspond to what we expected? 



df.shape # Yes, it corresponds to what we expected.


# ### Do you need to change the index?



df = df.drop(['Unnamed: 0'], axis=1)
df.columns


# ### Missing values?
# Find all the missing values and correct them. 



df[df.isnull().any(axis=1)]




df.at[6, "countrys"] = "Anguilla"
df.at[14, "code"] = "BHS"
df.at[16, "GDP"] = 186.60
df.at[20, "countrys"] = "Belize"
df.at[55, "code"] = "DNK"
df.at[70, "GDP"] = 2902.0
df.at[90, "code"] = "HUN"
df.at[96, "GDP"] = 245.80
df.at[100, "code"] = "JAM"
df.at[106, "countrys"] = "Kiribati"
df.at[200, "code"] = "TGO"
df.at[206, "countrys"] = "Tuvalu"




df[df.isnull().any(axis=1)]


# ### Find duplicate values  
# Clean where necessary:  
# *   France has a GDP of 2902.0 billion.
# *   Ireland has a GDP of 245.80 billion.
# *   Bangladesh has a GDP of 186.60 billion.



df["GDP"].value_counts(sort=True).head(4)




df[df['GDP'] == 0.18]




df[df['GDP'] == 0.75]




df[df['GDP'] == 0.16]




df.at[6, "GDP"] = 0.31
df.at[47, "GDP"] = 0.29
df.at[3, "GDP"] = 0.65
df.at[106, "GDP"] = 0.19




df["code"].value_counts(sort=True).head(3)




df[df['code'] == "ZMB"]




df[df['code'] == "ARG"]




df.at[221, "code"] = "ZWE"
df.at[209, "code"] = "ARE"


# ### Verify the change persisted!



df["GDP"].value_counts(sort=True).head(2)




df["code"].value_counts(sort=True).head(2)




df["countrys"].value_counts(sort=True).head(2)
