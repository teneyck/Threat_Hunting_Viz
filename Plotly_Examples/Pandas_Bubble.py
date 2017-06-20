# Learn about API authentication here: https://plot.ly/pandas/getting-started
# Find your api_key here: https://plot.ly/settings/api
# Cufflinks binds plotly to pandas dataframes in IPython notebook. Read more

import plotly as py
import cufflinks as cf
import pandas as pd

cf.set_config_file(offline=False, world_readable=True, theme='pearl')

df = pd.read_csv('gapminderDataFiveYear.txt', sep='\t')
df2007 = df[df.year==2007]
df.head(2)

py.offline.plot(kind='bubble', x=df2007.gdpPercap, y=df2007.lifeExp, size=df2007.pop, text=df2007.country, xTitle='GDP per Capita', yTitle='Life Expectancy', filename='cufflinks/simple-bubble-chart')
