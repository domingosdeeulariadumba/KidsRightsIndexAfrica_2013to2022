# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 06:45:47 2023

@author: domingosdeeulariadumba
"""

# A quick glance at the file directory 

%pwd


""" Importing the required libraries """


# Libraries to extract and transform data

import os
import tabula as tb
import pandas as pd


# Ignoring warnings about possible compactibility issues

import warnings
warnings.filterwarnings('ignore')



"""" DATA PREPARATION """


# Reading tables from pdf files (KidsRights reports)


    """ 
    2013 REPORT
    """
    
        # Extracting the tables from pdf
        
pdf_13='C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/The-KidsRights-Index-2013_Scoretable.pdf'

        # Converting tables to dataframes

df_13=tb.read_pdf(pdf_13, stream=True, pages='all')

        # How many tables we've extracted from the pdf file?

print(len(df_13))

        # Concatenating all dataframes

DF_13=pd.concat([df_13[0],df_13[1],df_13[2],df_13[3],df_13[4]], ignore_index=True)

        # Inserting the report year column

DF_13.insert(loc=0, column='Year', value=2013)      


        """ 
        2014 REPORT
        """
    
        # Extracting the tables from pdf
        
pdf_14='C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/The-KidsRights-Index-2014_Scoretable.pdf'

        # Converting tables to dataframes

df_14=tb.read_pdf(pdf_14, stream=True, pages='all')

        # How many tables we've extracted from the pdf file?

print(len(df_14))

        # Concatenating all dataframes

DF_14=pd.concat([df_14[0],df_14[1],df_14[2],df_14[3],df_14[4]], ignore_index=True)

        # Inserting the report year column

DF_14.insert(loc=0, column='Year', value=2014)


        """ 
        2015 REPORT
        """
    
        # Extracting the tables from pdf
        
pdf_15='C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/The-KidsRights-Index-2015_Scoretable.pdf'

        # Converting tables to dataframes

df_15=tb.read_pdf(pdf_15, stream=True, pages='all')

        # How many tables we've extracted from the pdf file?

print(len(df_15))

        # Concatenating all dataframes

DF_15=pd.concat([df_15[0],df_15[1],df_15[2],df_15[3]], ignore_index=True)

        # Inserting the report year column

DF_15.insert(loc=0, column='Year', value=2015)


        """ 
        2016 REPORT
        """
    
        # Extracting the tables from pdf
        
pdf_16='C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/The-KidsRights-Index-2016_Scoretable.pdf'

        # Converting tables to dataframes

df_16=tb.read_pdf(pdf_16, stream=True, pages='all')

        # How many tables we've extracted from the pdf file?

print(len(df_16))

        # Concatenating all dataframes

DF_16=pd.concat([df_16[0],df_16[1],df_16[2],df_16[3]], ignore_index=True)

        # Inserting the report year column

DF_16.insert(loc=0, column='Year', value=2016)


        """ 
        2017 REPORT
        """
    
        # Extracting the tables from pdf
        
pdf_17='C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/The-KidsRights-Index-2017_Scoretable.pdf'

        # Converting tables to dataframes

df_17=tb.read_pdf(pdf_17, stream=True, pages='all')

        # How many tables we've extracted from the pdf file?

print(len(df_17))

        # Concatenating all dataframes

DF_17=pd.concat([df_17[0],df_17[1],df_17[2],df_17[3]], ignore_index=True)

        # Inserting the report year column

DF_17.insert(loc=0, column='Year', value=2017)


        """ 
        2018 REPORT
        """
    
        # Extracting the tables from pdf
        
pdf_18='C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/The-KidsRights-Index-2018_Scoretable.pdf'

        # Converting tables to dataframes

df_18=tb.read_pdf(pdf_18, stream=True, pages='all')

        # How many tables we've extracted from the pdf file?

print(len(df_18))

        # Concatenating all dataframes

DF_18=pd.concat([df_18[0],df_18[1],df_18[2],df_18[3]], ignore_index=True)

        # Inserting the report year column

DF_18.insert(loc=0, column='Year', value=2018)


        """ 
        2019 REPORT
        """
    
        # Extracting the tables from pdf
        
pdf_19='C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/The-KidsRights-Index-2019_Scoretable.pdf'

        # Converting tables to dataframes

df_19=tb.read_pdf(pdf_19, stream=True, pages='all')

        # How many tables we've extracted from the pdf file?

print(len(df_19))

        # Concatenating all dataframes

DF_19=pd.concat([df_19[0],df_19[1],df_19[2],df_19[3],df_19[4]], ignore_index=True)

        # Inserting the report year column

DF_19.insert(loc=0, column='Year', value=2019)


        """ 
        2020 REPORT
        """
    
        # Extracting the tables from pdf
        
pdf_20='C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/The-KidsRights-Index-2020_Scoretable.pdf'

        # Converting tables to dataframes

df_20=tb.read_pdf(pdf_20, stream=True, pages='all')

        # How many tables we've extracted from the pdf file?

print(len(df_20))

        # Concatenating all dataframes

DF_20=pd.concat([df_20[0],df_20[1],df_20[2],df_20[3],df_20[4]], ignore_index=True)

        # Inserting the report year column

DF_20.insert(loc=0, column='Year', value=2020)


        """ 
        2021 REPORT
        """
   
        # Extracting the tables from pdf
        
pdf_21='C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/The-KidsRights-Index-2021_Scoretable.pdf'

        # Converting tables to dataframes

df_21=tb.read_pdf(pdf_21, stream=True, pages='all')

        # How many tables we've extracted from the pdf file?

print(len(df_21))

        # Concatenating all dataframes

DF_21=pd.concat([df_21[0],df_21[1],df_21[2],df_21[3],df_21[4]], ignore_index=True)

        # Inserting the report year column

DF_21.insert(loc=0, column='Year', value=2021)


        """ 
        2022 REPORT
        """
    
        # Extracting the tables from pdf
        
pdf_22='C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/The-KidsRights-Index-2022_Scoretable.pdf'

        # Converting tables to dataframes

df_22=tb.read_pdf(pdf_22, stream=True, pages='all')

        # How many tables we've extracted from the pdf file?

print(len(df_22))

        # Concatenating all dataframes

DF_22=pd.concat([df_22[0],df_22[1],df_22[2],df_22[3],df_22[4]], ignore_index=True)

        # Inserting the report year column

DF_22.insert(loc=0, column='Year', value=2022)


# Saving dataframes in different xlsx sheets to better organize in Excel

with pd.ExcelWriter ('C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/KidsRights.xlsx') as sheets:
    DF_13.to_excel(sheets, sheet_name='2013', index=False)
    DF_14.to_excel(sheets, sheet_name='2014', index=False)
    DF_15.to_excel(sheets, sheet_name='2015', index=False)
    DF_16.to_excel(sheets, sheet_name='2016', index=False)
    DF_17.to_excel(sheets, sheet_name='2017', index=False)
    DF_18.to_excel(sheets, sheet_name='2018', index=False)
    DF_19.to_excel(sheets, sheet_name='2019', index=False)
    DF_20.to_excel(sheets, sheet_name='2020', index=False)
    DF_21.to_excel(sheets, sheet_name='2021', index=False)
    DF_22.to_excel(sheets, sheet_name='2022', index=False)


# Reloading the dataset organized in Excel

AllSheets=pd.read_excel('C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/KidsRights_def.xlsx', sheet_name=None)

df_KidsRights=pd.concat(AllSheets.values(), ignore_index=True)



# Loading the countries dataset to extract only those which are from africa

df_countries= pd.read_excel('C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/africa_countries.xlsx')

africa=df_countries['Country'].tolist()


df_KidsRights['Continent']=''


for i in range(len(df_KidsRights['Country'])):
    for j in range (len(africa)):
        if df_KidsRights['Country'][i] == africa[j]:
            df_KidsRights['Continent'][i]='Africa'
        

# Updating Eswatini name for all years

df_KidsRights=df_KidsRights.replace('Swaziland', 'Eswatini', regex=True)


# Filtering Africa countries

df_KidsRights=df_KidsRights[df_KidsRights['Continent']=='Africa']


# Droping the Continent column

df_KidsRights=df_KidsRights.drop(['Continent'], axis=1)


# Checking the dataset

df_KidsRights.info()


# Handling missing values

    """
    Since 0.01 is the minimum value for any KidsRights index, according to this
    organization, for the imputation approach to handle missing values, it is
    the score that'll be used.
    """

df_KidsRights=df_KidsRights.fillna(0.01)


# Converting the float types recorded as object

df_KidsRights['Life']=df_KidsRights['Life'].astype(float)
df_KidsRights['Health']=df_KidsRights['Health'].astype(float)
df_KidsRights['Education']=df_KidsRights['Education'].astype(float)
df_KidsRights['Protection']=df_KidsRights['Protection'].astype(float)


# Replacing strings found on float type columns

df_KidsRights=df_KidsRights.replace('x','0.01', regex=True)
df_KidsRights=df_KidsRights.replace('-','0.01', regex=True)


# Converting the columns with strings replaced to float

df_KidsRights['Life']=df_KidsRights['Life'].astype(float)
df_KidsRights['Health']=df_KidsRights['Health'].astype(float)
df_KidsRights['Education']=df_KidsRights['Education'].astype(float)
df_KidsRights['Protection']=df_KidsRights['Protection'].astype(float)


# Checking again the datatypes

df_KidsRights.dtypes


# Saving file to continue in Power BI

df_KidsRights.to_csv('C:/Users/domingosdeeularia/Documents/notyourbusiness/CodingAndAnalytics/Projects/AfricaKidsIndex/KidsRights/KidsRights_Africa_2013-2022.csv')
_______________________________________________________________________End__________________________________________________________________________________________









