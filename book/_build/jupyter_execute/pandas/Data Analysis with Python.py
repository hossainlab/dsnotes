# Data Analysis with Pandas
[<a href="#Bottom">Top to Bottom</a>] 

<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Data-Analysis-with-Pandas" data-toc-modified-id="Data-Analysis-with-Pandas-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Data Analysis with Pandas</a></span><ul class="toc-item"><li><span><a href="#What-is-Pandas?" data-toc-modified-id="What-is-Pandas?-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>What is Pandas?</a></span></li><li><span><a href="#Pandas-Series" data-toc-modified-id="Pandas-Series-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Pandas Series</a></span></li><li><span><a href="#Pandas-DataFrame" data-toc-modified-id="Pandas-DataFrame-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Pandas DataFrame</a></span></li><li><span><a href="#Advantages-of-Pandas" data-toc-modified-id="Advantages-of-Pandas-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Advantages of Pandas</a></span></li><li><span><a href="#Creating-Series" data-toc-modified-id="Creating-Series-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Creating Series</a></span></li><li><span><a href="#Exploring-Datasets" data-toc-modified-id="Exploring-Datasets-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Exploring Datasets</a></span></li><li><span><a href="#How-to-read-a-tabular-data-file-into-pandas?" data-toc-modified-id="How-to-read-a-tabular-data-file-into-pandas?-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>How to read a tabular data file into pandas?</a></span></li><li><span><a href="#How-to-select-a-pandas-series-from-a-DataFrame?" data-toc-modified-id="How-to-select-a-pandas-series-from-a-DataFrame?-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>How to select a pandas series from a DataFrame?</a></span></li></ul></li></ul></div>

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
s2['A'] > 700000

[<a href="#Data-Analysis-with-Pandas">Back to Top</a>] 

## Exploring Datasets

Filename | Description | Raw File | Original Source | Other
--- | --- | --- | --- | ---
[chipotle.tsv](data/chipotle.tsv) | Online orders from the Chipotle restaurant chain | [bit.ly/chiporders](http://bit.ly/chiporders) | [The Upshot](https://github.com/TheUpshot/chipotle) | [Upshot article](http://www.nytimes.com/interactive/2015/02/17/upshot/what-do-people-actually-order-at-chipotle.html)
[drinks.csv](data/drinks.csv) | Alcohol consumption by country | [bit.ly/drinksbycountry](http://bit.ly/drinksbycountry) | [FiveThirtyEight](https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption) | [FiveThirtyEight article](http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/)
[imdb_1000.csv](data/imdb_1000.csv) | Top rated movies from IMDb | [bit.ly/imdbratings](http://bit.ly/imdbratings) | [IMDb](http://www.imdb.com/search/title?groups=top_1000&sort=user_rating&view=simple) | [Web scraping script](https://github.com/justmarkham/DAT5/blob/master/code/08_web_scraping.py)
[stocks.csv](data/stocks.csv) | Small dataset of stock prices | [bit.ly/smallstocks](http://bit.ly/smallstocks) | [DataCamp](https://www.datacamp.com/courses/manipulating-dataframes-with-pandas?tap_a=5644-dce66f&tap_s=280411-a25fc8) | 
[titanic_test.csv](data/titanic_test.csv) | Testing set from Kaggle's Titanic competition | [bit.ly/kaggletest](http://bit.ly/kaggletest) | [Kaggle](https://www.kaggle.com/c/titanic) | [Data dictionary](https://www.kaggle.com/c/titanic/data)
[titanic_train.csv](data/titanic_train.csv) | Training set from Kaggle's Titanic competition | [bit.ly/kaggletrain](http://bit.ly/kaggletrain) | [Kaggle](https://www.kaggle.com/c/titanic) | [Data dictionary](https://www.kaggle.com/c/titanic/data)
[u.user](data/u.user) | Demographic information about MovieLens users | [bit.ly/movieusers](http://bit.ly/movieusers) | [GroupLens](http://grouplens.org/datasets/movielens/100k/) | [Data dictionary](http://files.grouplens.org/datasets/movielens/ml-100k-README.txt)
[ufo.csv](data/ufo.csv) | Reports of UFO sightings from 1930-2000 | [bit.ly/uforeports](http://bit.ly/uforeports) | [National UFO Reporting Center](http://www.nuforc.org/webreports.html) | [Web scraping script](https://github.com/josiahdavis/josiahdavis.github.io/blob/master/supporting%20material/get_ufo_data.py)

## How to read a tabular data file into pandas?

# conventional way to import pandas
import pandas as pd 

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

# read a dataset of movie reviewers (modifying the default parameter values for read_table)
users = pd.read_table('http://bit.ly//movieusers')

# examine the first 5 rows 
users.head()

# DataFrame looks ugly. let's modify the default parameter for read_table 
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly//movieusers', sep='|' , header=None, names=user_cols)

# now take a look at modified dataset
users.head()

# read text/csv data into pandas 
chrom = pd.read_csv("./data/Encode_HMM_data.txt", delimiter="\t", header=None)

chrom.head()

# it's not much better to see. so we have to modify this dataset
cols_name = ['chrom', 'start', 'stop', 'type']
chrom = pd.read_csv("./data/Encode_HMM_data.txt", delimiter="\t", header=None, names=cols_name)

# now 
chrom.head()

[Documentation for `read_table`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_table.html)

[<a href="#Data-Analysis-with-Pandas">Back to Top</a>] 

## How to select a pandas series from a DataFrame?

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

# select 'City' Series using dot(.) notation
ufo.City

**Note:
- Bracket notation will always work, whereas dot notation has **limitations**
- Dot notation doesn't work if there are **spaces** in the Series name
- Dot notation doesn't work if the Series has the same name as a **DataFrame method or attribute** (like 'head' or 'shape')
- Dot notation can't be used to define the name of a **new Series** (see below)

# create a new 'Location' Series (must use bracket notation to define the Series name)
ufo['Location'] = ufo.City + ', ' + ufo.State
ufo.head()

[<a href="#Data-Analysis-with-Pandas">Back to Top</a>]