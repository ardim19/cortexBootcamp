import pandas as pd
member ={'nama':['asa','basu','dede'],'umur':[10,20,40]}
members_df = pd.Series(member)
# print(members_df)
members ={'nama':['asa','basu','dede'],'umur':[10,20,40]}
member_df = pd.DataFrame(members)
# print(member_df)
df = pd.read_csv('california_housing_test.csv')
# 10 data pertama
print(df.head(10))
# 5 data terakhir
print(df.tail())
# melihat jumlah dan perbandingan
print(df.describe())
# melihat data dari kolom tertentu
print(df['total_rooms'])
# print(df[['total_rooms','total_bedrooms']])

# melihat data dari baris tertentu
# print(df.iloc[0])
print(df.iloc[0:3])

print(df.plot(y=('total_bedrooms')))
