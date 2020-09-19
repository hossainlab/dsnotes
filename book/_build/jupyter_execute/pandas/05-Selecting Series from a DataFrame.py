<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Selecting-Series-from-DataFrame" data-toc-modified-id="Selecting-Series-from-DataFrame-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Selecting Series from DataFrame</a></span></li><li><span><a href="#Single-Series" data-toc-modified-id="Single-Series-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Single Series</a></span></li><li><span><a href="#Multiple-Series" data-toc-modified-id="Multiple-Series-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Multiple Series</a></span><ul class="toc-item"><li><span><a href="#About-the-Author" data-toc-modified-id="About-the-Author-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>About the Author</a></span></li></ul></li></ul></div>

## Selecting Series from DataFrame 

## Single Series

# conventional way to import pandas
import pandas as pd

# read a dataset of UFO reports into DataFrame 
ufo = pd.read_table('http://bit.ly/uforeports', sep=',')

# read a csv is equivalent to read_table, except it assumes a comma separator 
ufo = pd.read_csv('http://bit.ly/uforeports')

# examine first 5 rows 
ufo.head()

# select 'City' Series using bracket notation
ufo['City']

type(ufo['City'])

# select 'City' Series using dot(.) notation
ufo.City

__Note__
- Bracket notation will always work, whereas dot notation has **limitations**
- Dot notation doesn't work if there are **spaces** in the Series name
- Dot notation doesn't work if the Series has the same name as a **DataFrame method or attribute** (like 'head' or 'shape')
- Dot notation can't be used to define the name of a **new Series** (see below)

# create a new 'Location' Series (must use bracket notation to define the Series name)
ufo['Location'] = ufo.City + ', ' + ufo.State
ufo.head()

## Multiple Series

# select multiple series from dataframe 
ufo[['City', 'State', 'Time']]

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m