# Pandas Indexing 

# import pandas 
import pandas as pd 

# read data 
drinks = pd.read_csv("http://bit.ly/drinksbycountry")

# head 
drinks.head() 

## DataFrame Index 

# index or rowlabels 
drinks.index 

# columns 
drinks.columns

# shape 
drinks.shape

# read movie data 
movies = pd.read_table("http://bit.ly/movieusers", sep='|', header=None)

# head 
movies.head() 

# filtering 
drinks[drinks.continent == "South America"]

# loc[index, colnames]
drinks.loc[23, "beer_servings"]

# set index 
drinks.set_index("country", inplace=True)
drinks.head() 

# check index 
drinks.index

# check columns 
drinks.columns

# shape 
drinks.shape

drinks.loc["Brazil", "beer_servings"]

drinks.index.name = None
drinks.head() 

# back into column 
drinks.index.name = "country"
drinks.reset_index(inplace=True)
drinks.head() 

# it's a dataframe 
drinks.describe() 

# index 
drinks.describe().index

# columns
drinks.describe().columns

# grab 25% 
drinks.describe().loc["25%", "beer_servings"]

## Series Index 

# select continent 
drinks.continent.head() 

# index of series 
drinks.continent.index

# set index 
drinks.set_index("country", inplace=True)
drinks.head() 

# now select continent 
drinks.continent.head() 

# it returns a series, so it has index and values 
drinks.continent.value_counts()

# index 
drinks.continent.value_counts().index

# values  
drinks.continent.value_counts().values

# select index 
drinks.continent.value_counts()['Africa']

## Sorting

# sorting values 
drinks.continent.value_counts().sort_values() 

# sorting index
drinks.continent.value_counts().sort_index() 

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m