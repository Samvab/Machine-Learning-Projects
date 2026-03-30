       
        
import pandas as pd  

df = pd.read_csv("/content/insurance_claims.csv")

df.head()

df.tail()

df.shape

df.isnull().sum()

df.describe()

df.head()

df.replace({'region':{'Urban':0,'Rural':1,'Suburban':2}},inplace = True)

df.head()

"""#"""

