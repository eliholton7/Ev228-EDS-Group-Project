import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path_data = '/Users/owenwyman/Data/ev228_data/'
file_name = 'EDS_3.csv'
df = pd.read_csv(path_data + file_name)

net_wt = df['Net wt (kg)']
dates = df['Year']

annual_mean = df.groupby('Year')['Net wt (kg)'].mean()

filtered_mean = annual_mean.loc[2019:2025]

print(filtered_mean.values)
fig, ax = plt.subplots(figsize=(8,6))
ax.bar(filtered_mean.index, filtered_mean.values, color='skyblue', edgecolor='darkblue', linewidth=2, width=0.8)
ax.set_ylim(bottom=5, top=8)
ax.set_xlabel('Year')
ax.set_ylabel('Average Halibut Weight (kg)')
ax.set_title('Pacific Halibut Weight from 2010-2024')
ax.set_xticks(filtered_mean.index)
plt.show()