<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Exploring-Dataset" data-toc-modified-id="Exploring-Dataset-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Exploring Dataset</a></span><ul class="toc-item"><li><span><a href="#Head" data-toc-modified-id="Head-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Head</a></span></li><li><span><a href="#Tail" data-toc-modified-id="Tail-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Tail</a></span></li><li><span><a href="#Columns-Names" data-toc-modified-id="Columns-Names-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Columns Names</a></span></li><li><span><a href="#Observations-and-Variables(Rows-and-Columns)" data-toc-modified-id="Observations-and-Variables(Rows-and-Columns)-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Observations and Variables(Rows and Columns)</a></span></li><li><span><a href="#Data-Types" data-toc-modified-id="Data-Types-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Data Types</a></span></li><li><span><a href="#Basic-Information-about-Whole-Dataset" data-toc-modified-id="Basic-Information-about-Whole-Dataset-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Basic Information about Whole Dataset</a></span></li><li><span><a href="#Numerical-Summary-of-a-Dataset" data-toc-modified-id="Numerical-Summary-of-a-Dataset-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Numerical Summary of a Dataset</a></span></li></ul></li><li><span><a href="#Exploring-Series" data-toc-modified-id="Exploring-Series-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Exploring Series</a></span><ul class="toc-item"><li><span><a href="#Value-Counts" data-toc-modified-id="Value-Counts-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Value Counts</a></span></li><li><span><a href="#Unique()" data-toc-modified-id="Unique()-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Unique()</a></span></li><li><span><a href="#Cross-Tabulation" data-toc-modified-id="Cross-Tabulation-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Cross Tabulation</a></span></li><li><span><a href="#Describe" data-toc-modified-id="Describe-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Describe</a></span></li><li><span><a href="#Basic-STATS" data-toc-modified-id="Basic-STATS-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Basic STATS</a></span></li><li><span><a href="#Visualization" data-toc-modified-id="Visualization-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Visualization</a></span><ul class="toc-item"><li><span><a href="#About-the-Author" data-toc-modified-id="About-the-Author-2.6.1"><span class="toc-item-num">2.6.1&nbsp;&nbsp;</span>About the Author</a></span></li></ul></li></ul></li></ul></div>

# Exploring Dataset

# import pandas
import pandas as pd 

# read a dataset 
df = pd.read_csv("../data/framingham.csv")

## Head 

# head: by default shows first 5 rows 
df.head() 

# head(n); n = 1, 2, 3, 4, ....
df.head(8)

## Tail


# tail: by default shows last 5 rows 
df.tail() 

# tail(n); n=1, 2, 3, 4...
df.tail(8)

## Columns Names 

# Columns 
df.columns

## Observations and Variables(Rows and Columns)

# shape(rows x columns)
df.shape

## Data Types 

# check datatypes 
df.dtypes

## Basic Information about Whole Dataset

# info: it gives an overview of datasets 
df.info() 

## Numerical Summary of a Dataset

# describe: it gives summary statistics or five number summary 
df.describe() 

# for specific column 
df['age'].describe() 

# for multiple columns 
df[['age', 'BMI']].describe() 

# Exploring Series 

# read another dataset 
titanic = pd.read_csv('http://bit.ly/kaggletrain')

# examine first few rows 
titanic.head() 

## Value Counts 

# value_counts()
titanic['Sex'].value_counts() 

# value_counts() in percent
titanic['Sex'].value_counts(normalize=True) 

# returns a series 
type(titanic['Sex'].value_counts(normalize=True))

## Unique() 

# unique() 
titanic['Fare'].unique() 

# return a numpy.ndarray
type(titanic['Fare'].unique())

## Cross Tabulation

# crosstab 
pd.crosstab(titanic['Sex'], titanic['Survived'])

## Describe 

# describe a categorical column 
titanic['Age'].describe() 

## Basic STATS 

# mean()
titanic.Age.mean() 

# max()
titanic.Age.max() 

# min() 
titanic.Age.min() 

# median() 
titanic.Age.median() 

## Visualization

%matplotlib inline 

# barplot
titanic.Sex.value_counts().plot(kind="bar") 

# histogram
titanic.Age.plot(kind="hist")

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m