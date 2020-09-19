# Filtering Rows 

# import pandas 
import pandas as pd 

# read movie data 
movies = pd.read_csv("http://bit.ly/imdbratings")

# examine first few rows 
movies.head() 

## Filtering Movies with `for` Loop

booleans = [] 
for length in movies.duration: 
    if length >= 200: 
        booleans.append(True)
    else: 
        booleans.append(False)

# Check length of booleans 
len(booleans)

# Inspect booleans elements 
booleans[0:5]

# create a pandas series 
is_long = pd.Series(booleans)

# Inspect few values 
is_long.head() 

# show dataframe all columns in duration 200 minutes 
movies[is_long]

## Filtering by Condition

# filtering by conditions 
is_long = movies.duration >= 200
is_long.head() 

# show the rows duration >200
movies[is_long]

## Filtering in DataFrame 

# filtering by columns 
movies[movies.duration >= 200]

# select only genre
movies[movies.duration >= 200].genre

# same as above 
movies[movies.duration >= 200]['genre']

# select columns by label 
movies.loc[movies.duration >= 200, 'genre']

## Multiple Filtering Criteria

# True and True == True 
# True and False == False 
# True or True == True 
# True or False == True 
# False or False == False 
True and True
True and False 
True or True 
True or False

# multiple criteria 
movies[(movies.duration >= 200) & (movies.genre == 'Drama')]

# multiple criteria 
movies[(movies.duration >= 200) | (movies.genre == 'Drama')]

# multiple or conditions 
movies[(movies.genre == "Crime") | (movies.genre == 'Drama') | (movies.genre == "Action")]

# multiple or using isin() method 
movies.genre.isin(["Drama", "Action", "Crime"])

# pass the series in DataFrame 
movies[movies.genre.isin(["Drama", "Action", "Crime"])]

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m