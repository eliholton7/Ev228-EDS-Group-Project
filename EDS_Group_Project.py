import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


path_data = '/Users/eliholton/GitHub/Ev228-EDS-Group-Project/'
file_name = 'IPHC-2024-FISS-Pacific-halibut_1998-2024b.csv'
out_path = '/Users/eliholton/GitHub/Ev228-EDS-Group-Project/'
out_name = 'Fork_Length.png'
df = pd.read_csv(path_data+file_name)
annual_mean = df.groupby('Year')['Fork length (cm)'].mean()
y1 = np.zeros(27)
np.shape(y1)
print(annual_mean)
x_var = np.arange(1998,2025)
#print(df)


fig, ax = plt.subplots(figsize=(12,6))
ax.plot(annual_mean, linewidth = 2.5,)
plt.rcParams['font.family'] = 'serif'
ax.set_xlabel('Year')
ax.set_ylabel('Fork Length (cm)')
ax.set_title('Pacific Halibut Size from 1998-2024')
ax.fill_between(x_var,annual_mean, y1, color='lightblue', alpha=0.5)
plt.xlim(1998,2024)
plt.ylim(81,95)
plt.savefig(out_path+out_name)
plt.show()


#annual_mean2 = df.groupby('Year')['Net wt (kg)'].mean()
#filtered_mean = annual_mean2.loc[1998:2024]
#print(filtered_mean)