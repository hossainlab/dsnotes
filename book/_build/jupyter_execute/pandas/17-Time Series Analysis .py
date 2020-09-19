# library 
import pandas as pd 
import matplotlib.pyplot as plt 
%matplotlib inline 

# read data 
d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv("../data/ETH_1h.csv", parse_dates=['Date'], date_parser = d_parser)

# Take a look 
df.head() 

df.loc[0, 'Date']

# day_name() method : it shows error 
df.loc[0, 'Date'].day_name() 

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p') 

df['Date'] 

df.loc[0, 'Date'].day_name() 

df['Date'].dt.day_name() 

df['DayofWeek'] = df['Date'].dt.day_name() 

df

# earliest date 
df['Date'].min()

# most recent 
df['Date'].max() 

# subtract 
df['Date'].max() - df['Date'].min()

# filter 
filt = (df['Date'] >= '2020')

df.loc[filt]

filt = (df['Date'] >= '2019') & (df['Date'] < '2020')
df.loc[filt]

filt = (df['Date'] >= pd.to_datetime('2019-01-01')) &(df['Date'] < pd.to_datetime('2020-01-01'))
df.loc[filt]

df.set_index('Date', inplace=True)

df 

df.loc['2019']

df.loc['2019-01-01']

df.loc['2019-01-01':'2020-02']

df.loc['2019-01':'2020-02']['Close']

df.loc['2020-01':'2020-02']['Close'].mean() 

df.loc['2019-01':'2020-02']['Close'].head(24)

df['2020-01-01']['High']

df['2020-01-01']['High'].max() 

df['High'].resample('D').max() 

highs = df['High'].resample('D').max() 

highs['2020-01-01']

highs.plot(); 

df.resample('W').mean() 

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m