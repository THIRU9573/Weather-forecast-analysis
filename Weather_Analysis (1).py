#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# In[2]:


data = pd.read_excel("C:/Users/thiru/Downloads/weather_dataset_stage2.xls")


# In[3]:


data


# # Correct years for given data set
# 

# In[4]:


year = 2022

data['Date'][0] = "'" + str(year) + data['Date'][0][4:] + "'"
for i in range(1, len(data)):
    curr_month = int(data['Date'][i][5:7])
    prev_month = int(data['Date'][i-1][6:8])
    if curr_month < prev_month:
        year += 1
    data['Date'][i] = "'" + str(year) + data['Date'][i][4:]
    print(year)


# In[5]:


data.drop('Date1', inplace = True, axis = 1)


# In[6]:


data


# In[7]:


data['Date'] = data['Date'].str.strip()


# In[8]:


data['Date'] = data['Date'].str.replace("'","")
data['Date'] = data['Date'].str.replace("/","-")


# In[9]:


data = data[~data['Date'].isin(['2022-02-29', '2029-02-29', '2033-02-29'])]


# In[10]:


data = data.copy()


# In[11]:


data['Date'] = pd.to_datetime(data['Date'], format = "%Y-%m-%d")


# In[12]:


data['Year'] = data['Date'].dt.strftime('%Y')
data['Month'] = data['Date'].dt.strftime('%B')


# In[13]:


data['Date'] = data['Date'].dt.strftime('%d-%m-%Y')


# # Remove Duplicate Rows and Culumns:
# 

# In[14]:


duplicates = data.duplicated().sum()
print(f"the number of duplicates is {duplicates}")


# In[15]:


data.drop_duplicates(keep = False , inplace  = True)


# In[16]:


duplicateColumns = data.T.duplicated().sum()
print(f"the number of duplicated columns is {duplicateColumns}")


# In[17]:


data.shape


# In[18]:


data.columns


# # Fix the label and values:
# 

# In[19]:


data[' Temperature'] = data[' Temperature'].str.replace("'", '').astype(float)


# In[20]:


data[' Average humidity (%'] = data[' Average humidity (%'].str.replace("'", '').astype(float)


# In[21]:


data[' Average dewpoint (°F'] = data[' Average dewpoint (°F'].str.replace("'", '').astype(float)


# In[22]:


data[' Average barometer (in'] = data[' Average barometer (in'].str.replace("'", '').astype(float)


# In[23]:


data[' Average windspeed (mph'] = data[' Average windspeed (mph'].str.replace("'", '').astype(float)


# In[24]:


data[' Average gustspeed (mph'] = data[' Average gustspeed (mph'].str.replace("'", '').astype(float)


# In[25]:


data[' Average direction (°deg'] = data[' Average direction (°deg'].str.replace("'", '').astype(float)


# In[26]:


data[' Rainfall for month (in'] = data[' Rainfall for month (in'].str.replace("'", '').astype(float)


# In[27]:


data['Rainfall for year (in'] = data['Rainfall for year (in'].str.replace("'", '').astype(float)


# In[28]:


data[' Maximum rain per minute'] = data[' Maximum rain per minute'].str.replace("'", '').astype(float)


# In[29]:


data[' Maximum temperature (°F'] = data[' Maximum temperature (°F'].str.replace("'", '').astype(float)


# In[30]:


data[' Minimum temperature (°F'] = data[' Minimum temperature (°F'].str.replace("'", '').astype(float)


# In[31]:


data[' Maximum humidity (%'] = data[' Maximum humidity (%'].str.replace("'", '').astype(float)


# In[32]:


data[' Minimum humidity (%'] = data[' Minimum humidity (%'].str.replace("'", '').astype(float)


# In[33]:


data[' Maximum pressure'] = data[' Maximum pressure'].str.replace("'", '').astype(float)


# In[34]:


data[' Minimum pressure'] = data[' Minimum pressure'].str.replace("'", '').astype(float)


# In[35]:


data[ ' Maximum windspeed (mph'] = data[ ' Maximum windspeed (mph'].str.replace("'", '').astype(float)


# In[36]:


data[' Maximum gust speed (mph'] = data[' Maximum gust speed (mph'].str.replace("'", '').astype(float)


# In[37]:


data[' Maximum heat index (°F'] = data[' Maximum heat index (°F'].str.replace("'", '').astype(float)


# In[38]:


data[ ' Month'] = data[ ' Month'].str.replace("'", '').astype(int)


# In[39]:


data[' diff_pressure'] = data[' diff_pressure'].str.replace("'", '').astype(float)


# In[40]:


data.isna().sum()


# In[41]:


data.describe()


# In[43]:


data.to_csv("C:/Users/thiru/Downloads/Rakesh/HiCounselor2/weather_dataset_stage.csv")


# In[44]:


from pandas_profiling import ProfileReport
data1 = ProfileReport(data)
data1.to_file("C:/Users/thiru/Downloads/profile_Report.html")


# In[45]:


data1


# In[ ]:




