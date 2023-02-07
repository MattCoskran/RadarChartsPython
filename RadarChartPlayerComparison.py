import pandas as pd
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar
#read in the data
df = pd.read_csv('2022_23 Prem offensive stats Feb3rd.csv')
print(df)
#filter data
df = df[(df['Player']=='Roberto Firmino') | (df['Player']=='Gabriel Jesus')].reset_index()
print(df)
df = df.drop(['index', 'Rk', 'Nation', 'Pos', 'Squad', 'Age', 'Born', '90s', 'Dist', 'FK', 'PK', 'PKatt', 'npxG'],axis=1)
print(df)
#get parameters
params = list(df.columns)
params = params[1:10]
print(params)
ranges = []
a_values = []
b_values = []
for x in params:
    a = min(df[params][x])
    a = a - (a*.25)
    b = max(df[params][x])
    b = b + (b*.25)
    ranges.append((a,b))
for x in range(len(df['Player'])):
    if df['Player'][x] == 'Roberto Firmino':
        a_values = df.iloc[x].values.tolist()
    if df['Player'][x] == 'Gabriel Jesus':
        b_values = df.iloc[x].values.tolist()
a_values = a_values[1:]
b_values = b_values[1:]
values = [a_values,b_values]
#title
title = dict(
    title_name = 'Roberto Firmino',
    title_color = 'green',
    subtitle_name = 'Liverpool',
    subtitle_color = 'green',
    title_name_2 = 'Gabriel Jesus',
    title_color_2 = 'red',
    subtitle_name_2 = 'Arsenal',
    subtitle_color_2 = 'red',
    title_fontsize_2 = 18,
    subtitle_fontsize_2 = 15
)
end_note = ' github.com/MattCoskran \ndata via FBREF / Statsbomb'
radar = Radar()

fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,
                          radar_color=['green','red'],
                          alphas=[.75,.6],title=title,endnote=end_note,
                          compare=True,filename='Radar_FirminoVsJesus.jpeg')

