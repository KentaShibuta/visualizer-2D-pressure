import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np; np.random.seed(0)
import pandas as pd
import matplotlib.font_manager as fon
del fon.weight_dict['roman']
matplotlib.font_manager._rebuild()

plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
plt.rcParams["mathtext.fontset"] = "stix" # これを入れておくと，斜体にするときれいになる．
# 軸を内側に入れる
plt.rcParams['xtick.direction'] = 'in' # x axis in
plt.rcParams['ytick.direction'] = 'in' # y axis in

plt.rcParams["font.size"] = 14
f_name_node = "./20200109142851_node.csv"
f_name_nbool = "./20200109142851_nbool.csv"
f_name_pressure = "./20200109142851_pressure.csv"

nc = 30
rl1 = 10
rl2 = 20

nc_1 = nc + 1
nl = rl1 + 1

# ここまでの処理をpythonの中だけで行いたいよね．
############################################
#elem_node[nelem][4] # 要素番号と節点番号の対応
elem_node = np.loadtxt(f_name_nbool,
                    delimiter=",",
                    skiprows=0,
                    usecols=(3,4,5,6)
                    )
# 要素番号と節点番号の対応
node_data = np.loadtxt(f_name_node,
                    delimiter=",",
                    skiprows=0,
                    usecols=(1,2)
                    )

# 圧力データの読み込み
pressure_data = np.loadtxt(f_name_pressure,
                    delimiter=",",
                    skiprows=0,
                    usecols=(1)
                    )
pressure_new = ([])
for i in range(int(elem_node.shape[0])):
    if i >= 2100:
        pressure_data[i] = np.nan
    else:
        pressure_new = np.insert(pressure_new, i, pressure_data[i])



p_max = np.max(pressure_new)
p_min = np.min(pressure_new)
nelem = int(elem_node.shape[0])
color_num = int(pressure_new.shape[0])
print(pressure_data)
print(p_max)
print(np.argmax(pressure_new))
print(p_min)
print(np.argmin(pressure_new))
print(nelem)


# ここに要素番号順に並んだ圧力の値を置く

cmap = plt.cm.rainbow
norm = matplotlib.colors.Normalize(vmin=p_min, vmax=p_max)
# ここの最大値と最小値に液相の圧力
fig, ax = plt.subplots()

################################
elem_node_data = np.zeros((nelem,4,2))

#print(nelem)

for i in range(int(nelem)):
    elem_node_data[i][0] = node_data[int(elem_node[i][0])]
    elem_node_data[i][1] = node_data[int(elem_node[i][1])]
    elem_node_data[i][2] = node_data[int(elem_node[i][2])]
    elem_node_data[i][3] = node_data[int(elem_node[i][3])]

# ここに，要素番号と，要素の座標の値を置く
for i in range(int(nelem)):
    print(i)
    testx = [elem_node_data[i][0][0], elem_node_data[i][1][0], elem_node_data[i][2][0], elem_node_data[i][3][0], elem_node_data[i][0][0]]
    testy = [elem_node_data[i][0][1], elem_node_data[i][1][1], elem_node_data[i][2][1], elem_node_data[i][3][1], elem_node_data[i][0][1]]
    if i < color_num:
        ax.fill(testx,testy,color=cmap(norm(pressure_data[i])),alpha=0.5)
    else:
        ax.fill(testx,testy,color='w',alpha=0.5)
#ax.bar(df.x, df.y, color=cmap(norm(df.c.values)))
#ax.set_xticks(df.x)
color=cmap(norm(pressure_new))
print(color)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])  # only needed for matplotlib < 3.1
fig.colorbar(sm)

plt.xlabel('$\it{x}$'+" [m]")
plt.ylabel(' $\it{y}$'+" [m]")
plt.savefig("./20200101_pressure.svg",format = 'svg')
plt.show()
