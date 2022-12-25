# -*- coding:utf-8- -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

path="WHO-COVID-19-global-data.csv"
df=pd.read_csv(path)

#重命名列
df=df.rename(columns={'Date_reported':'Date'})

#时间线
time1=df['Date'].drop_duplicates().values.tolist()    #去掉重复行
time=[str(x) for x in time1] #转为str

#国家
df_Country=df.groupby(['Country'])  #按Country分组

#函数
#输入国家、类型，给出列表

#---CN
grouped=df_Country.get_group('China')
china_cases=grouped['Cumulative_cases'].tolist()

#---US
grouped=df_Country.get_group('United States of America')
us_cases=grouped['Cumulative_cases'].tolist()

#---Brazil
grouped=df_Country.get_group('Brazil')
brazil_cases=grouped['Cumulative_cases'].tolist()

#---India
grouped=df_Country.get_group('India')
india_cases=grouped['Cumulative_cases'].tolist()

#---France
grouped=df_Country.get_group('France')
france_cases=grouped['Cumulative_cases'].tolist()

#---Germany
grouped=df_Country.get_group('Germany')
germany_cases=grouped['Cumulative_cases'].tolist()

#---Italy
grouped=df_Country.get_group('Italy')
italy_cases=grouped['Cumulative_cases'].tolist()

#---Canada
grouped=df_Country.get_group('Canada')
canada_cases=grouped['Cumulative_cases'].tolist()

#---Japan
grouped=df_Country.get_group('Japan')
japan_cases=grouped['Cumulative_cases'].tolist()

#---北朝鲜
grouped=df_Country.get_group("Democratic People's Republic of Korea")
north_korea_cases=grouped['Cumulative_cases'].tolist()

#---韩国
grouped=df_Country.get_group('Republic of Korea')
south_korea_cases=grouped['Cumulative_cases'].tolist()


#画图
plt.plot(time,china_cases,'-.',color='green',label='China')
plt.plot(time,us_cases,'--',color='red',label='US')

plt.plot(time,brazil_cases,'-',color='blue',label='Brazil')
plt.plot(time,india_cases,'-',color='black',label='India')
plt.plot(time,france_cases,'-',color='yellow',label='France')
plt.plot(time,germany_cases,'-',color='pink',label='Germany')
plt.plot(time,italy_cases,'-',color='orange',label='Italy')
plt.plot(time,canada_cases,'-',color='#00FFFF',label='Canada')
plt.plot(time,japan_cases,'-',color='#C0C0C0',label='Japan')

plt.plot(time,south_korea_cases,'-',color='#808080',label='South Korea')
plt.plot(time,north_korea_cases,'-',color='#404040',label='North Korea')


plt.title('Confirmed number')
plt.xlabel('Date')
plt.ylabel('Number')
plt.grid(axis='both')


ax=plt.gca()#坐标句柄
ax.set_facecolor('#FFFAF0') #背景颜色

#调整x刻度，相隔x刻度显示1个，防止过多显示
x=30
ax.xaxis.set_major_locator(ticker.MultipleLocator(x))   
plt.xticks(rotation=60) #旋转x坐标时间标记，防止xlabel太长重合

plt.legend()
plt.tight_layout()    #自动调整
plt.show()