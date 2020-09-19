# Removing Columns

# import pandas 
import pandas as pd 

# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()

## Remove Single Columns 

# remove single columns(axis=1 refers to columns, axis=0 refers to row)
ufo.drop('City', axis=1, inplace=True)
ufo.head()

## Remove Multiple Columns

# remove multiple columns 
ufo.drop(['Colors Reported', 'Time'], axis=1, inplace=True)
ufo.head()

# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()

# remove single column(axis=1 refers to colums)
movies.drop('genre', axis=1, inplace=True)
movies.head()

# remove multiple columns from DataFrame 
movies.drop(['actors_list', 'content_rating', 'duration'], axis=1, inplace=True)
movies.head()

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.mm