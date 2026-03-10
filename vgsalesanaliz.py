import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("vgsales.csv")


df.dropna(inplace=True)
#print(df.isnull().sum())
'''
sns.set_theme(style="darkgrid")
sns.countplot(x="Platform",data=df)
plt.show()'''
'''
sns.barplot(x="Platform",y="Global_Sales",data=df)
plt.show()'''

'''
maxSales = df["Global_Sales"].max()

print(maxSales)
print(df[df["Global_Sales"]==maxSales])
'''


'''
salesByYear = df.groupby("Year")["Global_Sales"].sum().reset_index()
plt.figure(figsize=(14,7))

sns.lineplot(data=salesByYear,x="Year",y="Global_Sales",marker="o",linewidth=2.5, color="#2ecc71")

plt.title("Sales By Year",fontsize=16,fontweight="bold")
plt.xlabel("Year",fontsize=12)
plt.ylabel("Global Sales",fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()'''

#Index(['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales','EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'], dtype='object')
  
       
salesInJP = df.groupby("Genre")["JP_Sales"].sum().reset_index().sort_values(by="JP_Sales", ascending = False)
#print(salesInJP)

salesInNA = df.groupby("Genre")["NA_Sales"].sum().reset_index().sort_values(by="NA_Sales", ascending = False)
#print(salesInNA)

salesInEU = df.groupby("Genre")["EU_Sales"].sum().reset_index().sort_values(by="EU_Sales", ascending = False)
#print(salesInEU)

salesInOther = df.groupby("Genre")["Other_Sales"].sum().reset_index().sort_values(by="Other_Sales", ascending = False)
#print(salesInOther) 

topGenresJP=salesInJP.head(5)
topGenresNA=salesInNA.head(5)
topGenresEU=salesInEU.head(5)
topGenresOther=salesInOther.head(5)

fig, axes = plt.subplots(2, 2, figsize=(16, 10))


sns.barplot(ax=axes[0, 0], x="JP_Sales", y="Genre", data=topGenresJP, palette="magma")
axes[0, 0].set_title("Japan")


sns.barplot(ax=axes[0, 1], x="NA_Sales", y="Genre", data=topGenresNA, palette="viridis")
axes[0, 1].set_title("North America")


sns.barplot(ax=axes[1, 0], x="EU_Sales", y="Genre", data=topGenresEU, palette="rocket")
axes[1, 0].set_title("Europe")


sns.barplot(ax=axes[1, 1], x="Other_Sales", y="Genre", data=topGenresOther, palette="mako")
axes[1, 1].set_title("Other Regions")

plt.tight_layout()
plt.show()

print("--- Locational BestSellers ---")
print("NA:", df.loc[df['NA_Sales'].idxmax()]['Name'])
print("EU:", df.loc[df['EU_Sales'].idxmax()]['Name'])
print("JP:", df.loc[df['JP_Sales'].idxmax()]['Name'])
print("Other:", df.loc[df['Other_Sales'].idxmax()]['Name'])


print("--- Genre BestSellers ---")
print("NA:", df.loc[df['NA_Sales'].idxmax()]['Genre'])
print("EU:", df.loc[df['EU_Sales'].idxmax()]['Genre'])
print("JP:", df.loc[df['JP_Sales'].idxmax()]['Genre'])
print("Other:", df.loc[df['Other_Sales'].idxmax()]['Genre'])