<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#What-is-Pandas?" data-toc-modified-id="What-is-Pandas?-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>What is Pandas?</a></span></li><li><span><a href="#Pandas-Series" data-toc-modified-id="Pandas-Series-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Pandas Series</a></span></li><li><span><a href="#Pandas-DataFrame" data-toc-modified-id="Pandas-DataFrame-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Pandas DataFrame</a></span></li><li><span><a href="#Advantages-of-Pandas" data-toc-modified-id="Advantages-of-Pandas-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Advantages of Pandas</a></span></li><li><span><a href="#Creating-Series" data-toc-modified-id="Creating-Series-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Creating Series</a></span></li><li><span><a href="#Creating-DataFrame" data-toc-modified-id="Creating-DataFrame-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Creating DataFrame</a></span><ul class="toc-item"><li><span><a href="#About-the-Author" data-toc-modified-id="About-the-Author-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>About the Author</a></span></li></ul></li></ul></div>

## What is Pandas?
The Pandas library is built on NumPy and provides easy-to-use data structures and data analysis tools for the Python programming language.

## Pandas Series 
A **one-dimensional** labeled array a capable of holding any data type

## Pandas DataFrame 
A **two-dimensional** labeled data structure with columns of potentially different types
![Pandas](../img/pandas.png)

## Advantages of Pandas 
- Data representation
- Less writing and more work done
- An extensive set of features
- Efficiently handles large data
- Makes data flexible and customizable
- Made for Python

# Conventional  way to import pandas 
import pandas as pd 

# Check pandas version
pd.__version__

# Show version of all packages 
pd.show_versions()

## Creating Series

# Create Series 
s1 = pd.Series([3, 6, 9, 12])
s1

# Check type 
type(s1)

# To see values 
s1.values

# To see index/keys 
s1.index

# Creating labeled series 
s2 = pd.Series([200000, 300000, 4000000, 500000], index=['A', 'B', 'C', 'D'])

s2

s2.values

s2.index

# Indexing
s2['A']

# Boolean indexing
s2[s2 > 700000]

## Creating DataFrame 

# Create a DataFrame 
data = {'Country': ['Belgium', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasília'],
        'Population': [11190846, 1303171035, 207847528]
}

df = pd.DataFrame(data, columns=["Country", "Capital", "Population"])

df

# Check type 
type(df)

# Indexing
df["Country"]

# or 
df.Country

# Boolean indexing 
df["Population"]  > 40000000

df["Country"] == "Belgium"

df["Capital"] == "Brasilia"

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m