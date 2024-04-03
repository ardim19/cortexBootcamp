import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import matplotlib
# matplotlib.use('agg')
data = pd.read_csv('california_housing_test.csv')
print(data)
data['longitude'] = data['longitude'].astype(int)
# data['latitude'] = data['latitude'].round().astype('int64')


print(data.dtypes)
print(data.dropna(inplace=True))
print(data.head().to_string())
plt.hist(data['latitude'])
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.grid()
plt.show()
# Pilih beberapa kolom untuk ditampilkan
# selected_columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'median_income']

# # Buat subplot dengan ukuran 2x3
# plt.figure(figsize=(12, 8))
# for i, column in enumerate(selected_columns, 1):
#     plt.subplot(2, 3, i)
#     plt.hist(data[column])
#     plt.title(column)
# plt.tight_layout()
# plt.show()
