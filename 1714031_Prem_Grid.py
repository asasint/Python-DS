import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv("population_csv.csv",skiprows=[0], names=['CountryName','CountryCode','Year','Value'])
#print(df)
#df1=df.groupby(["CountryName"])
#print(df1.groups)
df1=df[df.CountryName == 'India']
#print(df1)

#plt.plot(df1.Year,df1.Value)
#plt.show()
df2=df[df.CountryName =='China']
df3=df[df.CountryName== "Arab World"]
df4=df[df.CountryName=="Uzbekistan"]
df5=df[df.CountryName=="United States"]
df6=df[df.CountryName=="Mexico"]

fig = plt.figure()
fig.subplots_adjust(hspace=1.2, wspace=1.2)



ax1 = fig.add_subplot(231)
ax1.title.set_text("Population of India")
xticklabels = ["1960","1970","1980","1990","2000","2010"]
ax1.set_xticklabels(xticklabels, rotation = 45)

ax1.plot(df1.Year,df1.Value)

ax2 = fig.add_subplot(232)
plt.gca().set_title("Population of China")
ax2.set_xticklabels(xticklabels, rotation = 45)

ax2.plot(df2.Year, df2.Value)

ax3 = fig.add_subplot(2,3,3)
plt.gca().set_title("Population of Arab")
#plt.xlim(1950, 2018)
ax3.set_xticklabels(xticklabels, rotation = 45)

ax3.plot(df3.Year, df3.Value)

ax4 = fig.add_subplot(2,3,4)
plt.gca().set_title("Population of Uzbekistan")
#plt.xlim(1950, 2018)
ax4.set_xticklabels(xticklabels, rotation = 45)

ax4.plot(df4.Year, df4.Value)
