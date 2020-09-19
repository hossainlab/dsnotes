<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Methods-and-Attributes" data-toc-modified-id="Methods-and-Attributes-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Methods and Attributes</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#About-the-Author" data-toc-modified-id="About-the-Author-1.0.1"><span class="toc-item-num">1.0.1&nbsp;&nbsp;</span>About the Author</a></span></li></ul></li></ul></li></ul></div>

# Methods and Attributes
__Remember__
* Methods ends with **parentheses**, while **attributes** don't
* df.shape: Attribute
* df.info(): Method

# import pandas 
import pandas as pd 

# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')

# example method: show the first 5 rows 
movies.head()

# example method: calculate summary statistics
movies.describe()

# example attribute: number of rows and columns 
movies.shape

# example attribute: data type of each column
movies.dtypes

# use an optional parameter to the describe method to summarize only 'object' column
movies.describe(include='object')

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m