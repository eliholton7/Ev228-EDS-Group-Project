import fun_process_data as fpd
import matplotlib.pyplot as plt
import pandas as pd

output1, output2 = fpd.process_data('/Users/owenwyman/Data/ev228_data/EDS_Data.csv', 'Fork length (cm)', 'Year')


fig, ax = plt.subplots(figsize=(12,6))
ax.plot(filtered_data['Year'], filtered_data['Fork length (cm)'])
ax.set_xlabel('Year')
ax.set_ylabel('Annual Mean Temperature (°C)')
ax.set_title('Annual Mean Temperature')
plt.show()