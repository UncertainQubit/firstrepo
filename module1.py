#All library imports

import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from ipywidgets import IntSlider

#Variable definitions

iowa_file_path = 'https://raw.githubusercontent.com/UncertainQubit/firstrepo/master/train.csv'
home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

#Functions

def CreateModel(leaves, ):
    model = DecisionTreeRegressor(max_leaf_nodes = leaves)
    if train:
        model.fit(train_X, train_y)
    else:
        model.fit(X,y)
    return model

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first
    

def FindError
