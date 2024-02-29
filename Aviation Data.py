#!/usr/bin/env python
# coding: utf-8

# __<center>Aviation Data Report</center>__<br>
# 
# The purpose of this project is to prepare a report giving a descriptive analysis of flight accidents from 1962 using Python.
# 
# Dataset: https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses

# __Importing Libraries__

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# __Loading Dataset__

# In[2]:


data = pd.read_csv('AviationData.csv', encoding='latin1', low_memory=False)


# __Description of the data in the DataFrame__

# In[3]:


data.describe()


# __Testing if the object has the right type of data__

# In[4]:


data.head().style.hide()


# __Data selection__

# In[5]:


data2 = data[['Investigation.Type', 'Event.Date','Country','Aircraft.damage','Total.Fatal.Injuries','Total.Serious.Injuries','Total.Minor.Injuries','Total.Uninjured','Broad.phase.of.flight']]
data2


# __Renaming column names__

# In[6]:


data2 = data2.rename(columns={'Investigation.Type': 'Investigation Type', 'Event.Date': 'Event Date', 'Aircraft.damage': 'Aircraft damage', 'Total.Fatal.Injuries': 'Total Fatal Injuries', 'Total.Serious.Injuries': 'Total Serious Injuries', 'Total.Minor.Injuries': 'Total Minor Injuries', 'Total.Uninjured': 'Total Uninjured', 'Broad.phase.of.flight': 'Broad phase of flight'})


# __Missing data - identification__

# In[7]:


data2.isnull().sum()


# __Filling empty cells with numerical data by inserting 0__

# In[8]:


data2 = data2.fillna({'Total Fatal Injuries': 0, 'Total Serious Injuries': 0, 'Total Minor Injuries': 0, 'Total Uninjured': 0 })
data2


# __Filling empty cells with textual data by inserting "Unknown"__

# In[9]:


data2 = data2.fillna('Unknown')


# __Missing data - current status__

# In[10]:


data2.isnull().sum()


# __Sorting by highest number of survivors (5 cases)__

# In[11]:


data2.sort_values(by='Total Uninjured', ascending=False).head(5)[['Investigation Type', 'Event Date', 'Country', 'Total Uninjured']]


# __Sorting by highest number of non-survivors (5 cases)__

# In[12]:


data2.sort_values(by='Total Fatal Injuries', ascending=False).head(5)[['Investigation Type', 'Event Date', 'Country', 'Total Fatal Injuries']]


# __Grouping by Total Uninjured - Country__

# In[13]:


data2.groupby('Country')['Total Uninjured'].sum().sort_values(ascending=False)


# __Grouping by Total Fatal Injuries - Country__

# In[14]:


data2.groupby('Country')['Total Fatal Injuries'].sum().sort_values(ascending=False)


# In[15]:


data2.describe()


# __Outliers__

# In[16]:


data2[['Total Fatal Injuries', 'Total Serious Injuries', 'Total Minor Injuries',
       'Total Uninjured']].hist(bins=2)


# In[17]:


sns.set_style('darkgrid')
sns.pairplot(data2[['Total Fatal Injuries', 'Total Serious Injuries',
       'Total Minor Injuries', 'Total Uninjured']], height = 3)
plt.show()


# __Accidents vs Incidents - comparing by Pie Chart__

# In[18]:


data2.columns


# In[19]:


Accident = data2.loc[data2['Investigation Type'] == 'Accident'].count()[0]
Accident


# In[20]:


Incident = data2.loc[data2['Investigation Type'] == 'Incident'].count()[0]
Incident


# In[21]:


plt.figure(figsize = (8,5))

labels = ['Accident', 'Incident']
colors = ['lightsteelblue', 'slategrey']

plt.pie([Accident, Incident], labels = labels, colors = colors, autopct = '%.2f %%')

plt.title('Investigation Type')

plt.show()


# __Aircraft damage__

# In[22]:


Destroyed = data2.loc[data2['Aircraft damage'] == 'Destroyed'].count()[0]
Destroyed


# In[23]:


Minor = data2.loc[data2['Aircraft damage'] == 'Minor'].count()[0]
Minor


# In[24]:


Substantial = data2.loc[data2['Aircraft damage'] == 'Substantial'].count()[0]
Substantial


# In[25]:


Unknown = data2.loc[data2['Aircraft damage'] == 'Unknown'].count()[0]
Unknown


# In[26]:


plt.figure(figsize = (8,5))

labels = ['Destroyed', 'Minor', 'Substantial', 'Unknown']
colors = ['lightsteelblue', 'steelblue', 'lightblue', 'slategrey']

plt.pie([Destroyed, Minor, Substantial, Unknown], labels = labels, colors = colors, autopct = '%.2f %%')

plt.title('Aircraft damage')

plt.show()


# The most common damage was substantial and the rarest was minor

# __Injuries by broad phase of flight__

# In[31]:


data2=data2[data2['Broad phase of flight'] !='Unknown']

data2_grouped = data2[['Total Minor Injuries', 'Total Serious Injuries', 'Total Fatal Injuries']].groupby(data2['Broad phase of flight']).sum()

data2_grouped.plot(kind='bar', color=['lightsteelblue', 'steelblue', 'lightblue', 'slategrey'])

plt.title('Injuries by broad phase of flight')
plt.xlabel('Broad phase of flight')
plt.ylabel('Total')
plt.show()
                  


# Fatal injuries - the highest number of fatal injuries was during the cruise phase<br>
# Serious injuries - the highest number of serious injuries was during the takeoff phase<br>
# Minor injuries - the highest number of minor injuries was during the takeoff phase

# In[28]:


data2['Year'] = pd.DatetimeIndex(data2['Event Date']).year


# In[29]:


data2.head()


# In[30]:


data2 = data2[(data2['Year']< 1945) | (data2['Year']> 1975)]

data2.sort_values('Year', inplace = True)

bar_width = 0.35
index = data2['Year']

fig, ax = plt.subplots()

bar1 = ax.bar(index, data2['Total Fatal Injuries'], bar_width, label='Total Fatal Injuries', color='slategrey')
bar2 = ax.bar(index + bar_width, data2['Total Uninjured'], bar_width, label='Total Uninjured', color='lightsteelblue')

ax.set_xlabel('Year')
ax.set_ylabel('Number of people')
ax.set_title('Total Fatal Injuries vs Total Uninjured over the years')
ax.legend()

plt.xticks(rotation=90)
plt.show()


# The highest number of total uninjured was in 1999 and the highest number of total fatal injuries was in 2001

# In[ ]:




