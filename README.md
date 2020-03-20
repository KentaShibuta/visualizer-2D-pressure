# 圧力の可視化プログラム
## できること
* 空間分布する圧力(スカラー値)の可視化でできる．
    + 現在は2次元での可視化のみ．
    + 圧力値の大小をカラーコンターで表す．
## 入力ファイル
* 節点座標のデータ
    + csv形式
* 要素と節点の依存関係のデータ
    + csv形式
    + 依存関係とは，ある要素の番号とその要素を構成する節点の番号の組み合わせのことを意味する．
        - 要素番号, 節点0の節点番号, 節点1の節点番号, 節点2の節点番号, 節点3の節点番号
## 実行方法
* 可視化プログラムを実行
    + `python vis_2d_pressure.py`
    + "Input node file name >>>>"に続いて，節点座標のデータが記述されたファイルのパスを入力．
    + "Input nbool file name >>>>"に続いて，要素と節点の依存関係のデータが記述されているファイルのパスを入力．
    + "Input pressure file name >>>>"に続いて，圧力のデータが記述されたファイルのパスを入力．
### 実行例
* 2次元無重力下での液滴の振動現状の圧力分布
    + `sample_data`のなかのデータを用いて実行
        - 節点のデータ：`sample_data/20200302103450_node.csv`
        - 要素と節点の依存関係のデータ：`sample_data/20200302103450_nbool.csv`
        - 圧力のデータ：`sample_data/20200302103450_pressure.csv`
![result_pressure](https://gyazo.com/6cf1f3d0dd4755b8f50b039a0a180625/raw)
