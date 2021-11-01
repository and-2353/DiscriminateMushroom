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

print('\nダミー変数導入後特徴量（学習データ）\n', X)

clf = LDA()
clf.fit(X, y)

print(clf.predict(X))
print(clf.score(X, y))
print(clf.coef_)
print('判別得点: ', (clf.coef_ * X).sum(axis=1))

print(len(X.columns), len(clf.coef_[0]))

dic = {X.columns[i]: coefficient for (i, coefficient) in enumerate(clf.coef_[0])}
dic_sorted = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print(dic_sorted)

print('\n係数が高い(poisonousにする)項目')
for i in range(10):
    print(dic_sorted[i])

print('\n係数が低い(edibleにする)項目')
for i in range(1, 11):
    print(dic_sorted[-i])

