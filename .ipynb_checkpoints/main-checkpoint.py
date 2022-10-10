import pandas as pd
import numpy as np
import seaborn as sns

train = pd.read_csv('./dataset/train.csv')
print (train.iloc[0,0])