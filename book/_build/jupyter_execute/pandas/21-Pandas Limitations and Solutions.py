## Pandas Limitations 
- It depends on the size of datasets.
- Pandas can be safely used 1-5GB Data. 
- Even if you use 1-30GB of Data

## Pandas Chunksize

import pandas as pd 
df = pd.read_csv('../data/drinks.csv', chunksize=30000)

## Dask

import dask

import dask.array as da 

a = da.random.randint(10, 100, 100000000).reshape(1000000, 100)
a.compute() 

import dask.dataframe as dd 

data = dd.read_csv('../data/drinks.csv')

data.compute() 

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m