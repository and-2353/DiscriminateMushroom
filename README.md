# DiscriminateMushroom
キノコの物理的特徴に対して線形判別分析(LDA)を行う。<br>
データセットはほとんど全て質的変数なので、ダミー変数を導入し `one-hot` 特徴量に変換してLDAの入力としている。<br>

## データの収集
[Mushroom Data Set -UCI Machine Learing Repository](https://archive.ics.uci.edu/ml/datasets/mushroom) より。

## 使い方
- `cross_validate.py` を実行
> 線形判別分析が実行される。<br>
> 実行結果は交差検証で示される<br>
> 交差検証のkの大きさを変数 `cv` の指定により変更できる

- `leave_one_out.py` を実行
> 線形判別分析が実行される。<br>
> 実行結果は `leave-one-out` 交差検証で示される<br>

- `coef_.py` を実行
> `LDA` で判別式を求め、
> - 係数が高い(poisonousにする)項目<br>
> - 係数が低い(edibleにする)項目<br>
> を表示する。<br>
> 
> それぞれ10個ずつ表示するようになっている<br>
> 表示部の`for`ループに渡す`range`長を変更することで表示する属性の個数を調整可能
