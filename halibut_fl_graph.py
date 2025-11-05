import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path_data = '/Users/owenwyman/Documents/GitHub/Ev228-EDS-Group-Project/'
file_name = 'IPHC-2024-FISS-Pacific-halibut_1998-2024b.csv'
fig_path = '/Users/owenwyman/Data/ev228_data/figures/'
fig_name = '3_hfl.png'

df = pd.read_csv(path_data + file_name)

net_wt = df['Fork length (cm)']
dates = df['Year']

annual_mean = df.groupby('Year')['Fork length (cm)'].mean()

data_to_plot = annual_mean.values
data_max = np.max(data_to_plot)
data_min = np.min(data_to_plot)
data_mean = np.mean(data_to_plot)
data_std = np.std(data_to_plot)

stats_label = (
    f'Max: {data_max:.2f} cm\n'
    f'Min: {data_min:.2f} cm\n'
    f'Mean: {data_mean:.2f} cm\n'
    f'Std Dev: {data_std:.2f} cm'
    f''
)
print (stats_label)

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(annual_mean.index, annual_mean.values, color='skyblue', edgecolor='darkblue', linewidth=2, width=0.8)
ax.set_ylim(bottom=80, top=95)
ax.set_xlabel('Year')
ax.set_ylabel('Average Halibut Fork Length (cm)')
ax.set_title('Pacific Halibut Fork Length from 1998-2024')
# ax.set_xticks(annual_mean.index)
ax.legend(handles=custom_handle, loc='best', title="Statistics (1998-2025)")
plt.savefig(fig_path + fig_name, dpi=400)

