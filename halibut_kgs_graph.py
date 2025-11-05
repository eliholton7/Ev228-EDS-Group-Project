import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path_data = '/Users/owenwyman/Data/ev228_data/EDS_data/'
file_name = 'EDS_3.csv'
fig_path = '/Users/owenwyman/Data/ev228_data/figures/'
fig_name = '1_kgs.png'

df = pd.read_csv(path_data + file_name)

net_wt = df['Net wt (kg)']
dates = df['Year']

annual_mean = df.groupby('Year')['Net wt (kg)'].mean()
filtered_mean = annual_mean.loc[2019:2025]
print(filtered_mean.values)

data_to_plot = filtered_mean.values
data_max = np.max(data_to_plot)
data_min = np.min(data_to_plot)
data_mean = np.mean(data_to_plot)
data_std = np.std(data_to_plot)

stats_label = (
    f'Max: {data_max:.2f} kg\n'
    f'Min: {data_min:.2f} kg\n'
    f'Mean: {data_mean:.2f} kg\n'
    f'Std Dev: {data_std:.2f} kg'
)
print(stats_label)

fig, ax = plt.subplots(figsize=(6,6))
ax.bar(filtered_mean.index, filtered_mean.values, color='red', edgecolor='darkred', linewidth=2, width=0.8,)
ax.set_ylim(bottom=5, top=8)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Average Halibut Weight (kg)', fontsize=15)
ax.set_title('Pacific Halibut Weight from 2019-2024', fontsize=20)
ax.set_xticks(filtered_mean.index)
# ax.legend(loc='best', title="Statistics (2019-2025)")
plt.savefig(fig_path + fig_name, dpi=400)