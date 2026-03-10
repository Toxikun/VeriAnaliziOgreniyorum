import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("vgsales.csv")


df.dropna(inplace=True)
print(df.isnull().sum())
'''
sns.set_theme(style="darkgrid")
sns.countplot(x="Platform",data=df)
plt.show()'''
'''
sns.barplot(x="Platform",y="Global_Sales",data=df)
plt.show()'''

iyi_oyun = df["Global_Sales"].max()

print(iyi_oyun)
print(df[df["Global_Sales"]==iyi_oyun])