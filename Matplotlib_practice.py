#!/usr/bin/env python
# coding: utf-8

# ## Author - Prem kumar bharti 
# 
# # Matplotlib tutorial

# * Matplotlib is 2D and 3D plotting python library
# * It produce high quality graph
# * it also support animation

# **we use it for data visualization**

# In[1]:


# line plot-----------Relationship between independent and dependent variable
# Histogram-----------Distribution of data 
# Bar chart ---------- Relationship of descrete / categorical variable
# scatter plot-------------Realtionship , outliers , density
# Pie chart--------------data representation


# ### Lineplot

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


days = list(range(1,16))


# In[4]:


days


# In[5]:


delhi_temperature = [25 , 24 , 23 , 24.5 , 20.2 , 24 , 23.5 , 22 , 28 , 30 , 32.1 , 21 , 20 , 24 , 25.5]


# In[6]:


len(delhi_temperature)


# In[7]:


plt.plot(days , delhi_temperature)
plt.show()


# In[8]:


plt.plot(days,delhi_temperature)

plt.title(" weather forcast" , color = "green" , fontsize = 20)
plt.show()


# In[9]:


plt.plot(days,delhi_temperature)
plt.title(" weather forcast")
plt.xlabel("No. of days" , color ="green" , fontsize = 15)
plt.ylabel("temperature" , color = "red")
plt.show()


# ### Histogram

# In[10]:


import random
import numpy as np


# In[11]:


marks_maths_students = np.random.randint(23 , 80 , 60 )


# In[12]:


marks_maths_students 


# In[13]:


len(marks_maths_students)


# In[14]:


plt.hist(marks_maths_students)
plt.show()


# In[15]:


bins = [40 , 50, 60, 70, 80, 90, 100]


# In[16]:


plt.hist(marks_maths_students, bins = bins , align = "left" , rwidth=0.5, histtype= "bar",
         orientation='vertical',color = "black",label= "marks of maths")
plt.title("Marks" , fontsize = 18 , color = "b")
plt.xlabel("marks of student" , fontsize = 14)
plt.ylabel("number of student" , fontsize = 14)
plt.legend(loc = 0)
plt.show()


# ### Barchart

# In[17]:


Training_basket = ["data analysis", "Auditing", "bussiness environment", "Management Accounting", "IT in bussiness"]
Batch_1 = [30 , 40 , 50 , 60 , 70]


# In[18]:


plt.bar(Training_basket, Batch_1)
plt.title(" Batch information")
plt.ylabel("No of students" , color ="green", fontsize = 12)
plt.xlabel("Course name" , color = "red" , fontsize = 12)
plt.show()


# In[19]:


plt.barh(Training_basket, Batch_1)
plt.title(" Batch information")
plt.xlabel("No of students" , color ="green", fontsize = 12)
plt.ylabel("Course name" , color = "red" , fontsize = 12)
plt.show()


# ### scatter plot

# In[20]:


import pandas as pd


# In[21]:


df = pd.read_csv("SalaryGender.csv")


# In[22]:


df.head()


# In[23]:


x = df["Salary"]
y = df["Age"]


# In[24]:


#plt.figure(figsize = (15 , 10))
plt.scatter(x , y , s=500 ,  marker="*" ,alpha=1 , c = "aqua" , edgecolors="aqua" , linewidths=1)
plt.title("salary" , fontsize = 20)
plt.xlabel("salary")
plt.ylabel("age")
plt.show()


# In[25]:


plt.scatter(x , y )
plt.title("salary" , fontsize = 20)
plt.xlabel("salary")
plt.ylabel("age")
plt.show()


# ### Pie chart

# In[26]:


Training_basket = ["data analysis", "Auditing", "bussiness environment", "Management Accounting", "IT in bussiness"]
Batch_1 = ["30", "60", "35", "30", "50"]


# In[28]:


colors = ["r" , "yellow" , "m" , "b" , "aqua"]
explode = [0 , 0 , 0 , 0 , 0.1]
plt.pie(Batch_1 , labels=Training_basket  , explode = explode ,colors=colors ,  radius=1, startangle=90 ,autopct='%.3f' )
plt.title("pie chart" , color = "red" , fontsize = 20)
plt.show()


# In[ ]:


#plt.plot()
#plt.hist()
#plt.scatter()
#plt.pie()
#plt.bar()


# In[51]:


plt.pie(Batch_1 , labels=Training_basket)
plt.show()


# In[28]:


y = ["data analysis", "Auditing", "bussiness environment", "Management Accounting", "IT in bussiness"]
x = ["30", "60", "35", "30", "50"]


# In[29]:


colors = ["r" , "yellow" , "m" , "b" , "aqua"]
explode = [0 , 0 , 0 , 0 , 0.1]
plt.pie(x , labels=y  , explode = explode ,colors=colors ,  radius=1, startangle=90 ,autopct='%.3f' )
plt.title("pie chart" , color = "red" , fontsize = 20)
plt.show()


# In[30]:


colors=["r","yellow","m","b","aqua"]
explode=[0,0,0,0,0.1]
plt.pie(x,labels=y,colors=colors,radius=1,autopct='%3f')
plt.show()


# In[31]:


colors=["r","yellow","m","b","aqua"]
explode=[0,0,0,0,0.1]
plt.pie(x,labels=y,colors=colors,radius=1,autopct='%3f')
plt.show()


# In[ ]:




