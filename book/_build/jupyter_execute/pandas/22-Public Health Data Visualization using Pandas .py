# import library 
import pandas as pd 
import matplotlib.pyplot as plt 
# set style 
plt.style.use('seaborn') 
# set figuresize and fontsize 
plt.rcParams['figure.figsize'] = (8,6) 
plt.rcParams['font.size'] = 14 

# read data 
data = pd.read_csv("../data/framingham.csv")

# examine first few rows 
data.head() 

# shape 
data.shape

# data structure 
data.info() 

# numerical summary
data.describe() 

# rename male column 
data.rename(columns={"male": "sex"}, inplace=True)

# check data
data.head() 

# replace sex 1 = male and 0 = female 
data.sex.replace({1: "male", 0: "female"}, inplace=True)

# check data 
data.

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.mm