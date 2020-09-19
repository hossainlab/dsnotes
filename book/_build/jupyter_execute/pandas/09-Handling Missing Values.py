# Handling Missing Values 

# import pandas 
import pandas as pd 

# read ufo data 
ufo = pd.read_csv("http://bit.ly/uforeports")

# last 5 rows 
ufo.tail() 

# check missing values 
ufo.isnull() 

__Note__
1. True: Missing 
2. False: Not Missing

# using notnull() 
ufo.notnull() 

__Note__
1. axis = 0: Rows 
2. axis = 1: Columns 

# sum of missing values: by default axis = 0
ufo.isnull().sum() 

# Let's create a series 
pd.Series([True, False, True]).sum() 

# filtering using isnull() 
ufo[ufo.City.isnull()]

# Check specific column
ufo.City.isnull().sum() 

## Drop Missing Values 

# shape 
ufo.shape 

# drop missing: drop row contains missing values 
# it is inplace = False 
ufo.dropna(how='any').shape

# how=all 
ufo.dropna(how='all').shape 

# subset: any 
ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape

# subset: all 
ufo.dropna(subset=['City', 'Shape Reported'], how='all').shape

## Filling Missing Values 

# value counts: by default drop = True 
ufo["Shape Reported"].value_counts() 

# value counts: false 
ufo["Shape Reported"].value_counts(dropna=False) 

# fillna() 
ufo["Shape Reported"].fillna(value="VARIOUS", inplace=True)

# now take a look 
ufo["Shape Reported"].value_counts() 

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m