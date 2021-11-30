# noinspection PyUnresolvedReferences
import numpy as np
import pandas as pd


#importing the datset and forming a dataframe
data = pd.read_csv('/Users/gaoqian/Documents/GitHub/Customer_Personality_Aanlysis/marketing_campaign.csv')
df = pd.DataFrame(data)
df.head()
df.info()

# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt
# noinspection PyUnresolvedReferences
import seaborn as sns
df['Present Age'] = 2000 - df['Year_Birth'] + 21
avg_age = sum(list(df['Present Age']))/len(df['Present Age'])
print(avg_age)
