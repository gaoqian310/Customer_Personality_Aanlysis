#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd


#importing the datset and forming a dataframe
data = pd.read_csv('marketing_data.csv')
df = pd.DataFrame(data)
df.head()


# In[6]:


df.info()


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns
df['Present Age'] = 2000 - df['Year_Birth'] + 21
avg_age = sum(list(df['Present Age']))/len(df['Present Age'])
print(avg_age)


# In[8]:


sns.set(rc={'figure.figsize':(25,15)})
sns.countplot(x = df['Present Age'],data=df)


# In[9]:


df['TotalPurchaseThroughCampaign'] = df['AcceptedCmp1'] + df['AcceptedCmp2'] + df['AcceptedCmp3'] + df['AcceptedCmp4']  + df['AcceptedCmp5'] + df['Response']
df['TotalPurchaseThroughCampaign'].head()
sns.heatmap(data = df[['AcceptedCmp1','AcceptedCmp2','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5','Response','TotalPurchaseThroughCampaign']].corr(),annot = True)


# In[10]:


#calculating percentage of purchases through each campaign
count = 0
for i in df['AcceptedCmp1']:
  if i == 1:
    count = count+1
print((count/2240)*100)    

count = 0
for i in df['AcceptedCmp2']:
  if i == 1:
    count = count+1
print((count/2240)*100) 

count = 0
for i in df['AcceptedCmp3']:
  if i == 1:
    count = count+1
print((count/2240)*100) 

count = 0
for i in df['AcceptedCmp4']:
  if i == 1:
    count = count+1
print((count/2240)*100) 

count = 0
for i in df['AcceptedCmp5']:
  if i == 1:
    count = count+1
print((count/2240)*100) 

count = 0
for i in df['Response']:
  if i == 1:
    count = count+1
print((count/2240)*100) 


# In[11]:


plt.figure(figsize=(10,7))
l,a = list(set(data["Education"])),[]
for i in range(len(l)):
    a.append(data["Education"].to_list().count(l[i]))
    l[i] = l[i]+"("+str(a[i]*100/len(data["Education"])) + "%)"
plt.pie(a,labels=l, radius=2)
plt.show()
#relation between education and number of kids
sns.displot(x="Education",y="Kidhome",data=data)
#relation between education and response to the campaign
sns.displot(x="Education",y="Response",data=data)


# In[12]:


#heatmap
sns.set(rc={'figure.figsize':(25,20)})
sns.heatmap(data = df.corr(),annot=True)


# In[13]:


#relation between in store purchases and income
sns.set(rc={'figure.figsize':(5,5)})
sns.heatmap(df[['Income','NumStorePurchases']].corr(),annot=True)


# In[ ]:





# In[ ]:




