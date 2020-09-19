import pandas as pd 

train = pd.read_csv("http://bit.ly/kaggletrain")

train.head() 

feature_cols = ['Pclass', 'Parch'] 
X = train.loc[:, feature_cols] 

X.shape

y = train.Survived

y.shape

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression() 
logreg.fit(X, y)

test = pd.read_csv("http://bit.ly/kaggletest")

test.head() 

X_new = test.loc[:, feature_cols] 

X_new.shape

new_pred_class = logreg.predict(X_new)

test.PassengerId

new_pred_class

pd.DataFrame({'PassengerID' : test.PassengerId, 'Survived': new_pred_class}).to_csv("sub.csv", index=False)

subdf = pd.read_csv("sub.csv")

subdf.head() 

<h3>About the Author</h3>
This repo was created by <a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> <br>
<a href="https://www.linkedin.com/in/jubayer28/" target="_blank">Jubayer Hossain</a> is a student of Microbiology at Jagannath University and the founder of <a href="https://github.com/hdro" target="_blank">Health Data Research Organization</a>. He is also a team member of a bioinformatics research group known as Bio-Bio-1. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.m