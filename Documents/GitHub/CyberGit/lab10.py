import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

covid = pd.read_csv('04-06-2020.csv')

lat = covid['Lat'].values
lon = covid['Long_'].values
confirmed = covid['Confirmed'].values

plt.scatter(lon,lat)
plt.show()