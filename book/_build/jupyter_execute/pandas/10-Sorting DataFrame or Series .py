# Sorting DataFrame or Series 

# import pandas 
import pandas as pd 

**Note**: None of the sorting methods below affect the underlying data. (In other words, the sorting is temporary).


# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()

# sort the 'title' Series in ascending order (returns a Series)
movies.title.sort_values().head()

# sort in descending order instead
movies.title.sort_values(ascending=False).head()

# sort the entire DataFrame by the 'title' Series (returns a DataFrame)
movies.sort_values('title', ascending=False).head()

# sort the entire DataFrame by the 'duration' Series (returns a DataFrame)
movies.sort_values('duration', ascending=False).head()

# sort by two columns: first sort_by duration and then content_rating
movies.sort_values(['duration', 'content_rating'], ascending=False).head()

# None of the sorting methods below affect the underlying data. (In other words, the sorting is temporary). 
movies.head() 

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m