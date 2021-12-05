#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


#importing the datset and forming a dataframe
data = pd.read_csv('marketing_data.csv')
df = pd.DataFrame(data)
df.head()



# In[3]:


df.info()


# ## Quesiton 1: What are the age demographics of customers?

# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns
df['Present Age'] = 2000 - df['Year_Birth'] + 21
avg_age = sum(list(df['Present Age']))/len(df['Present Age'])
print(avg_age)


# In[21]:


sns.set(rc={'figure.figsize':(25,20)})
sns.countplot(x = df['Present Age'],data = df,palette = ['#338999'])


# ## Question 2: What is the contribution of each individual compaigns in the total response.
# the response to previous compaigns are stored in "AcceptedCmp1-5" and the most recently launched campaign is in "Response". "TotalPurchaseThroughCampaign" is created to visualize the contribution of individual campaigns.

# In[6]:


df['TotalPurchaseThroughCampaign'] = df['AcceptedCmp1'] + df['AcceptedCmp2'] + df['AcceptedCmp3'] + df['AcceptedCmp4']  + df['AcceptedCmp5'] + df['Response']
df['TotalPurchaseThroughCampaign'].head()
sns.heatmap(data = df[['AcceptedCmp1','AcceptedCmp2','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5','Response','TotalPurchaseThroughCampaign']].corr(),annot = True)


# ## Calculating percentage of purchases through each campaign

# In[23]:


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


# ## Question 3: What are the education demographics of customers? 

# In[25]:


plt.figure(figsize=(10,7))
l,a = list(set(data["Education"])),[]
for i in range(len(l)):
    a.append(data["Education"].to_list().count(l[i]))
    l[i] = l[i]+"("+str(a[i]*100/len(data["Education"])) + "%)"
plt.pie(a,labels=l, radius=2)
plt.show()


# ## Question 4: What the relation between the education level and number of kids?

# In[27]:


#relation between education and number of kids
sns.displot(x="Education",y="Kidhome",data=data)


# ## Question 5: What's the relation between education level and response to the campaign?

# In[28]:


#relation between education and response to the campaign
sns.displot(x="Education",y="Response",data=data)


# ## Question 6: What's the corrolation we can discover from the heatmaps?

# In[9]:


#heatmap
sns.set(rc={'figure.figsize':(25,20)})
sns.heatmap(data = df.corr(),annot=True)


# We can see the pattern that edible itesm such as wine, fruit, meet an fish are often brought together and often brouhgt from the store.
# And if a customer have a kid at home, he tend to order online to avoid taking kid out to shop for groceries.

# In[13]:


#relation between in store purchases and income
sns.set(rc={'figure.figsize':(5,5)})
sns.heatmap(df[['Income','NumStorePurchases']].corr(),annot=True)


# We can see with the income increases, the customers prefer to by their products in store rather than from a website.

# In[ ]:




