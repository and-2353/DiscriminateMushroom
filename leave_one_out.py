import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import cross_validate
from sklearn.model_selection import LeaveOneOut


# train dataの読み込み
data = pd.read_csv('agaricus-lepiota_data.csv', encoding='utf-8')

data = data.replace({'ring-number': {'n': 0, 'o': 1, 't': 2}})
data = data.replace({'edible': {'e': 0, 'p': 1}})

X = data.drop('edible', axis=1)
y = data['edible']

print('元学習データ\n', data)

X = pd.get_dummies(X, drop_first=True)

print('\nダミー変数導入後特徴量（学習データ）\n', X)
# print(X.columns)

clf = LDA()
loo = LeaveOneOut()
scores = cross_validate(clf, X, y, cv=loo)


# 予測, 評価
print(scores)
print(scores['test_score'].mean())

