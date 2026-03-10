import pandas as pd

data = {
    "isim": ["A", "B", "C", "D"],
    "bölüm": ["AI", "data", "veri", "YZ"],
    "not": [1.5, 2.5, 3.5, 4.0]
}
df = pd.DataFrame(data)

yeni_kisi = pd.DataFrame([{"isim": "Boran", "bölüm": "YZ", "not": 0}])
df = pd.concat([df, yeni_kisi], ignore_index=True)
print(df)
df["durum"] = df["not"] >= 3.5
df.loc[df["isim"] == "Boran", "not"] = 100
print(df)

df1 = pd.read_csv("test.csv")
print(df1)