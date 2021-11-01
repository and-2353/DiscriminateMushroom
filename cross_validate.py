import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import cross_validate

# train dataの読み込み
data = pd.read_csv('agaricus-lepiota_data.csv', encoding='utf-8')

# ring-number 項目はstrで登録されているが量的変数なのでintに置換する
# 質的変量として判別分析してもほとんどスコアは変わらなかった(-0.000004 程度)。
data = data.replace({'ring-number': {'n': 0, 'o': 1, 't': 2}})
data = data.replace({'edible': {'e': 0, 'p': 1}})

X = data.drop('edible', axis=1)
y = data['edible']

print('元学習データ\n', data)

X = pd.get_dummies(X, drop_first=True)
"""
with open('dummied_data.csv', 'w') as f:
    f.write(X)
"""
X.to_csv('dummied_data.csv', index=False)

print('\nダミー変数導入後特徴量（学習データ）\n', X)
# print(X.columns)


clf = LDA()
scores = cross_validate(clf, X, y, cv=12, scoring=['accuracy', 'precision', 'recall', 'f1'])


# 予測, 評価
print(scores)
print(scores['test_accuracy'])
print(scores['test_accuracy'].mean())
