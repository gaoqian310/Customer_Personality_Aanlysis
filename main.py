# noinspection PyUnresolvedReferences
import numpy as np
import pandas as pd


#importing the datset and forming a dataframe
data = pd.read_csv('/Users/gaoqian/Downloads/marketing_campaign.csv')
df = pd.DataFrame(data)
df.head()
df.info()


