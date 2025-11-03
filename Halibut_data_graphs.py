import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path_data = '/Users/owenwyman/Data/ev228_data/'
file_name = 'EDS_3.csv'
df = pd.read_csv(path_data + file_name)

fork_length = df['Fork length (cm)']
dates = df['Year']

# average_fl = fork_length.mean(dim = 'Year')
# print(average_fl)

# df = pd.concat([output2, output1], axis=1)
# print(df)
# filtered_data = df[df['metANN'] != 999.90]
# print(filtered_data)

annual_mean = df.groupby('Year')['Fork length (cm)'].mean()


fig, ax = plt.subplots(figsize=(12,6))
ax.plot(annual_mean)
ax.set_xlabel('Year')
ax.set_ylabel('Average Halibut Fork Length (cm)')
ax.set_title('Halibut Fork Length Size from 2010-2024')
plt.show()