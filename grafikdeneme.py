import pandas as pd

df = pd.read_csv("test.csv")
import matplotlib.pyplot as plt
#plt.bar(df["isim"],df["puan"])


plt.title("Not dağılımı")
plt.xlabel("isim")
plt.ylabel("puan")
plt.plot(df["isim"],df["puan"],marker="o",color="r",linewidth=2)
plt.show()