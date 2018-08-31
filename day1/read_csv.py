import pandas as pd

dataset = pd.read_csv('../data/athlete_events.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[ : , 3].values
print(dataset['Age'].mean())