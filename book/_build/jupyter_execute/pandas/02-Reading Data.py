<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Reading-Data-into-Pandas" data-toc-modified-id="Reading-Data-into-Pandas-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Reading Data into Pandas</a></span><ul class="toc-item"><li><span><a href="#Read-CSV" data-toc-modified-id="Read-CSV-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Read CSV</a></span></li><li><span><a href="#Read-Excel-Sheet" data-toc-modified-id="Read-Excel-Sheet-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Read Excel Sheet</a></span></li><li><span><a href="#Read-Multiple-Excel-Sheets" data-toc-modified-id="Read-Multiple-Excel-Sheets-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Read Multiple Excel Sheets</a></span></li><li><span><a href="#From-URL" data-toc-modified-id="From-URL-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>From URL</a></span></li><li><span><a href="#Modify-Dataset" data-toc-modified-id="Modify-Dataset-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Modify Dataset</a></span></li><li><span><a href="#Read-Biological-Data(.txt)" data-toc-modified-id="Read-Biological-Data(.txt)-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Read Biological Data(.txt)</a></span></li><li><span><a href="#Read-Biological-Data(.tsv)" data-toc-modified-id="Read-Biological-Data(.tsv)-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Read Biological Data(.tsv)</a></span></li><li><span><a href="#Read-HTML-Data" data-toc-modified-id="Read-HTML-Data-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Read HTML Data</a></span><ul class="toc-item"><li><span><a href="#About-the-Author" data-toc-modified-id="About-the-Author-1.8.1"><span class="toc-item-num">1.8.1&nbsp;&nbsp;</span>About the Author</a></span></li></ul></li></ul></li></ul></div>

# Reading Data into Pandas

# conventional way to import pandas
import pandas as pd 

# Set options for displaying rows and columns 

## Read CSV

# read data from csv file 
corona = pd.read_csv("../data/covid-19_cleaned_data.csv")

# Examine first few rows 
corona.head() 

## Read Excel Sheet

# read data from excel file 
movies = pd.read_excel("../data/movies.xls")

# examine first few rows 
movies.head() 

## Read Multiple Excel Sheets 

import xlrd 
# Import xlsx file and store each sheet in to a df list
xl_file = pd.ExcelFile("../data/data.xls",)
# Dictionary comprehension
dfs = {sheet_name: xl_file.parse(sheet_name) for sheet_name in xl_file.sheet_names}

# Data from each sheet can be accessed via key
keylist = list(dfs.keys())

# Examine the sheet name 
keylist[1:10]

# Accessing first sheet
dfs[keylist[0]]

## From URL

# read a dataset of Chipotle orders directly from a URL and store the results in a DataFrame 
orders = pd.read_table('http://bit.ly/chiporders')

# examine the first 5 rows 
orders.head()

# examine the last 5 rows 
orders.tail()

# examine the first `n` number of rows
orders.head(10)

# examine the last `n` number of rows
orders.tail(10)

## Modify Dataset

# read a dataset of movie reviewers (modifying the default parameter values for read_table)
users = pd.read_table('http://bit.ly//movieusers')

# examine the first 5 rows 
users.head()

# DataFrame looks ugly. let's modify the default parameter for read_table 
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly//movieusers', sep='|' , header=None, names=user_cols)

# now take a look at modified dataset
users.head()

## Read Biological Data(.txt)

# read text/csv data into pandas 
chrom = pd.read_csv("../data/Encode_HMM_data.txt", delimiter="\t", header=None)

# Examine first few rows 
chrom.head()

# it's not much better to see. so we have to modify this dataset
cols_name = ['chrom', 'start', 'stop', 'type']
chrom = pd.read_csv("../data/Encode_HMM_data.txt", delimiter="\t", header=None, names=cols_name)

# now examine first few rows 
chrom.head()

## Read Biological Data(.tsv)

pokemon = pd.read_csv("../data/pokemon.tsv", sep="\t")

pokemon.head() 

## Read HTML Data

# Read HTML data from web 
url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
data = pd.io.html.read_html(url)

# Check type 
type(data)

# access data 
data[0]

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.mm