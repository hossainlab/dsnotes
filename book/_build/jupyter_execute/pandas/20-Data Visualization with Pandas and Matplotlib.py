<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Data-Visualization-with-Pandas" data-toc-modified-id="Data-Visualization-with-Pandas-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Data Visualization with Pandas</a></span><ul class="toc-item"><li><span><a href="#Data-Exploration" data-toc-modified-id="Data-Exploration-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Data Exploration</a></span></li><li><span><a href="#Histogram:-show-the-distribution-of-a-numerical-variable" data-toc-modified-id="Histogram:-show-the-distribution-of-a-numerical-variable-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Histogram: show the distribution of a numerical variable</a></span></li><li><span><a href="#Scatter-Plot:-show-the-relationship-between-two-numerical-variables" data-toc-modified-id="Scatter-Plot:-show-the-relationship-between-two-numerical-variables-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Scatter Plot: show the relationship between two numerical variables</a></span></li><li><span><a href="#Bar-Plot:-show-a-numerical-comparison-across-different-categories" data-toc-modified-id="Bar-Plot:-show-a-numerical-comparison-across-different-categories-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Bar Plot: show a numerical comparison across different categories</a></span></li><li><span><a href="#Box-Plot:-show-quartiles-(and-outliers)-for-one-or-more-numerical-variables" data-toc-modified-id="Box-Plot:-show-quartiles-(and-outliers)-for-one-or-more-numerical-variables-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Box Plot: show quartiles (and outliers) for one or more numerical variables</a></span></li><li><span><a href="#Line-Plot:-show-the-trend-of-a-numerical-variable-over-time" data-toc-modified-id="Line-Plot:-show-the-trend-of-a-numerical-variable-over-time-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Line Plot: show the trend of a numerical variable over time</a></span></li><li><span><a href="#Grouped-Box-Plots:-show-one-box-plot-for-each-group" data-toc-modified-id="Grouped-Box-Plots:-show-one-box-plot-for-each-group-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Grouped Box Plots: show one box plot for each group</a></span></li><li><span><a href="#Grouped-Histograms:-show-one-histogram-for-each-group" data-toc-modified-id="Grouped-Histograms:-show-one-histogram-for-each-group-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Grouped Histograms: show one histogram for each group</a></span></li><li><span><a href="#Assorted-Functionality" data-toc-modified-id="Assorted-Functionality-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Assorted Functionality</a></span><ul class="toc-item"><li><span><a href="#About-the-Author" data-toc-modified-id="About-the-Author-1.9.1"><span class="toc-item-num">1.9.1&nbsp;&nbsp;</span>About the Author</a></span></li></ul></li></ul></li></ul></div>

# Data Visualization with Pandas 

# import library 
import pandas as pd 
import matplotlib.pyplot as plt 

# display plot in the notebook 
%matplotlib inline 

# set figuresize and fontsize 
plt.rcParams['figure.figsize'] = (8,6) 
plt.rcParams['font.size'] = 14 

# read data 
drink_cols = ["country", 'beer', 'spirit', 'wine', 'liters', 'continent']
drinks = pd.read_csv("../data/drinks.csv", header=0, names=drink_cols, na_filter=False)

## Data Exploration

# examine first few rows 
drinks.head() 

# observations and columns 
drinks.shape

# data structure 
drinks.info() 

# numerical summary 
drinks.describe() 

##  Histogram: show the distribution of a numerical variable

# sort the beer columns and split it into 3 groups 
drinks.beer.sort_values().values

# compare with histogram 
drinks.beer.plot(kind="hist", bins=3);

# try more bins 
drinks.beer.plot(kind="hist", bins=20); 

# add title and labels 
drinks.beer.plot(kind="hist", bins=20, title="Histogram of Beer Servings")
plt.xlabel("Beer Survings") 
plt.ylabel("Frequency")
# show plot 
plt.show() 

# compare with density plot(smooth version of a histogram) 
drinks.beer.plot(kind="density", xlim=(0, 500));

## Scatter Plot: show the relationship between two numerical variables

# select the beer and wine columns and sort by beer 
drinks[["beer", "wine"]].sort_values(by="beer").values

# comapre with scatter plot 
drinks.plot(kind="scatter", x="beer", y="wine"); 

# add transparency 
drinks.plot(kind='scatter', x="beer", y="wine", alpha=0.3); 

# vary point color by spirit servings 
drinks.plot(kind="scatter", x="beer", y="wine", c="spirit", colormap="Blues"); 

# scatter matrix of 3 numerical columns 
pd.plotting.scatter_matrix(drinks[['beer', 'wine', 'spirit']]); 

# increase figure size 
# scatter matrix of 3 numerical columns 
pd.plotting.scatter_matrix(drinks[['beer', 'wine', 'spirit']], figsize=(10,8)); 

##  Bar Plot: show a numerical comparison across different categories

# count the number of countries in each continent 
drinks.continent.value_counts()

# compare with bar plot 
drinks.continent.value_counts().plot(kind="bar"); 

# calculate the mean alcohol amounts for each continent 
drinks.groupby('continent').mean() 

# side-by-side bar plots 
drinks.groupby('continent').mean().plot(kind='bar'); 

# drop the liters column
drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar'); 

# stacked bar plots 
drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar', stacked=True); 

## Box Plot: show quartiles (and outliers) for one or more numerical variables
__Five-Number Summary__
* min = minimum value
* 5% = first quartile (Q1) = median of the lower half of the data
* 50% = second quartile (Q2) = median of the data
* 75% = third quartile (Q3) = median of the upper half of the data
* max = maximum value
(More useful than mean and standard deviation for describing skewed distributions)
* Interquartile Range (IQR) = Q3 - Q1

__Outliers__ 
* below Q1 - 1.5 * IQR
* above Q3 + 1.5 * IQR

# sort the spirit column 
drinks.spirit.sort_values().values 

# show five-number summary of spirit 
drinks.spirit.describe() 

# compare with boxplot 
drinks.spirit.plot(kind='box');  

# include multiple variables 
drinks.drop('liters', axis=1).plot(kind='box'); 

## Line Plot: show the trend of a numerical variable over time

# read ufo data 
ufo = pd.read_csv("../data/ufo.csv")
ufo['Time'] = pd.to_datetime(ufo.Time) 
ufo['Year'] = ufo.Time.dt.year 

# examine first few rows  
ufo.head() 

# observations and columns 
ufo.shape 

# data structure 
ufo.info() 

# numerical summary 
ufo.describe()  

# count the number of ufo reports each year (and sort by year)
ufo.Year.value_counts().sort_index() 

# compare with line plot 
ufo.Year.value_counts().sort_index().plot();

# don't use a line plot when there is no logical ordering 
drinks.continent.value_counts().plot(kind='line'); 

## Grouped Box Plots: show one box plot for each group

# remainder: boxplot of beer survings 
drinks.beer.plot(kind='box'); 

# boxplot of beer survings group by continent 
drinks.boxplot(column='beer', by='continent'); 

# boxplot of all numerical columns group by continent 
drinks.boxplot(by='continent'); 

## Grouped Histograms: show one histogram for each group

# remainder: histogram of beer survings 
drinks.beer.plot(kind='hist', bins=20); 

# histogram of beer  survings group by continent 
drinks.hist(column='beer', by='continent'); 

# share the x-axis 
drinks.hist(column='beer', by='continent', sharex=True); 

# share the x and y axis 
drinks.hist(column='beer', by='continent', sharex=True, sharey=True); 

# change the layout 
drinks.hist(column='beer', by='continent', sharex=True, layout=(2, 3));

 ## Assorted Functionality

# saving a plot to a file 
drinks.beer.plot(kind='hist', bins=20, title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Freequency")
plt.savefig("beer_survings.png") # .png, .tiff, .pdf, .jpeg 

# list available plot style 
plt.style.available

# use plot style: ggplot 
plt.style.use('ggplot')

# histogram of beer survings in ggplot style 
drinks.beer.plot(kind="hist", title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Frequnecy")

# use plot style: ggplot 
plt.style.use('seaborn') 

# histogram of beer survings in seaborn style 
drinks.beer.plot(kind="hist", title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Frequnecy")

# use plot style: ggplot 
plt.style.use('fivethirtyeight') 

# histogram of beer survings in fivethirtyeight style 
drinks.beer.plot(kind="hist", title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Frequnecy")

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.mm