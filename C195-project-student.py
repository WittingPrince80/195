#!/usr/bin/env python
# coding: utf-8

# In[11]:


print("Name:")
print("We will be cleaning heart disease data, and conclude which age group has high risk of heart stroke as per diabetes and hight blood pressure level")
print("We will also find which gender has the most not normal platelets count in blood, and plot a pie chart around it")



# # Task 1 - Find the diabetic and hight blood pressure patients across all age groups, and conclude the risk heart stroke is higher in which age group

# In[10]:


#Import libraries
import pandas as pd
import matplotlib.pyplot as plt 

#read the csv
df = pd.read_csv('heart_disease.csv')
df


# In[2]:


#Filter by diabetes(condition will be who has diabetes) and create new dataframe
df['age'] = pd.DatetimeIndex(df['diabetes']).age
df




# In[3]:


#On this new data frame perform group operation as per age and create new dataframe 
group_by_age = df.groupby('age')[['HighAge','TempAge']].mean().reset_index()
group_by_age


# In[4]:


#Filter by high_blood_pressure(condition will be who has high_blood_pressure) and create new dataframe
df['age'] = pd.DatetimeIndex(df['high_blood_pressure']).age




# In[5]:


#On this new data frame perform group operation as per age and create new dataframe 
group_by_age = df.groupby('age')[['HighAge','LowAge']].mean().reset_index()
group_by_age


# In[6]:


#Plot a point scatter graph for the average temperature and humidity as per months 
month = group_by_month['age']
TempHighF = group_by_month['diabetes']

plt.scatter(month, TempHighF, label = "Average age")

HumidityHighPercent = group_by_month['diabetes']

plt.scatter(age, Diabeties , label = "Average diabetes")

plt.legend()


# Conclusion - 

# # Task 2 - Find as per gender who has not normal platelets level in blood

# In[7]:


#Filter by platelets(condition lesser then 150000 OR greater then 450000) and create new dataframe



# In[8]:


#On this new dataframe perform group operation as per gender and create new dataframe 





# In[9]:


#Plot a pie chart as per the gender to show the percentage of male and female who has not normal platelets


# Conclusion - 

# In[ ]:




