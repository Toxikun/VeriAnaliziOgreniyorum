import pandas as pd
import seaborn as sns

df = pd.read_csv("trafik_verisi.csv")

df["risk"] = df["hava_kirliliği"] == "kirli"

print(df[df["risk"]==True])

import matplotlib.pyplot as plt

#plt.bar(df["saat"],df["arac_sayisi"])
#plt.title("Trafik Verisi")
#plt.xlabel("Saat")
#plt.ylabel("Arac Sayisi")
#plt.savefig("trafik_raporu.png")
#plt.show()


sns.set_theme(style="darkgrid")
sns.barplot(x="saat",y="arac_sayisi",data=df)
plt.show()
