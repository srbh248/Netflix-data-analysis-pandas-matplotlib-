#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df= pd.read_csv(r"C:\Users\acer\Downloads\archive (1)\netflix1.csv")


# In[3]:


df


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


df.dtypes


# In[7]:


df.describe()


# In[8]:


df.rename(columns={"listed_in":"genre"}, inplace= True)


# In[9]:


df.rename(columns=str.upper, inplace=True)


# In[10]:


df


# In[11]:


df[df["DIRECTOR"].str.contains("Not Given")]


# In[12]:


df['DATE_ADDED']= pd.to_datetime(df["DATE_ADDED"])


# In[13]:


df


# # VISUALISATION

# In[14]:


showtype= df["TYPE"].value_counts().reset_index()


# In[15]:


showtype


# In[16]:


plt.figure(figsize=(20,6))
plt.pie(showtype['count'],labels=['Movie','TVshow'],autopct='%1.3f%%',explode=[0,0.1])
plt.show()


# This shows that movies are more than double than the TV shows on the site

# In[17]:


country=df["COUNTRY"].value_counts().reset_index()


# In[18]:


country


# In[50]:


plt.figure(figsize=(20,6))
plt.plot(country['COUNTRY'],country["count"], color='r')
plt.xticks(rotation=90)
plt.show;


# US produces movies/Tvshows more than any other country followed by India and United Kingdom

# In[28]:


top10countries=country[['COUNTRY','count']][0:10]


# In[29]:


top10countries


# In[49]:


plt.figure(figsize=(20,6))
c=['r', 'y', 'g', 'b', 'm', 'r', 'y', 'g', 'b', 'm']
plt.bar(top10countries['COUNTRY'], top10countries['count'], color= c)
plt.xticks(rotation=90)
plt.show;


# Top 10 movies/tvshows producers are as follows

# In[31]:


directors=df['DIRECTOR'].value_counts().reset_index().head(10)


# In[32]:


directors


# In[33]:


plt.figure(figsize=(20,6))
plt.bar(directors['DIRECTOR'], directors['count'])
plt.show;


# it is clearly visible that most of the directors are not given in the dataset, and others arw as follows

# In[34]:


release_year=df['RELEASE_YEAR'].value_counts().reset_index()


# In[35]:


release_year


# In[53]:


sns.barplot(x='RELEASE_YEAR', y='count', data= release_year)
plt.xticks(rotation=90);


# The highest number of movies/tv shows are released in year 2018. also the numbers have been increasing since the initial days of cinema indutry

# In[37]:


ratings=df['RATING'].value_counts().reset_index()


# In[38]:


ratings


# In[39]:


sns.barplot(x='RATING', y='count', data= ratings)
plt.xticks(rotation=90);


# Most of the movies/tv shows produced are TV-MA which is not suited for people below 17 years of age, followed by TV-14 and TV-PG

# In[40]:


ratingpertype=df[['RATING', 'TYPE']].value_counts().reset_index().sort_values(by= 'RATING', ascending= True)


# In[41]:


ratingpertype


# In[42]:


ratingpertype.set_index("RATING", inplace=True)


# In[43]:


ratingpertype.reset_index(inplace=True)


# In[44]:


ratingpertype['rating-type']= ratingpertype['RATING'] + ' ' + ratingpertype['TYPE']


# In[45]:


ratingpertype


# In[46]:


sns.barplot(x='rating-type', y='count', data= ratingpertype).set(title='rating as per type')
plt.xticks(rotation=90);


# the above graph shows the ratio of movies and TVshows produced under each rating category

# In[ ]:





# In[ ]:




