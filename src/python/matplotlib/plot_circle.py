# -*- coding:utf-8 -*-

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_polar = pd.read_csv('phia1.txt', names=['alpha', 'radius', 'density1', 'density2'],
                       delimiter='\s+')

# force square figure and square axes looks better for polar, IMO
fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.7, 0.7], polar=True)
cax = fig.add_axes([0.9, 0.1, 0.04, 0.7])

_df_polar = df_polar[df_polar.alpha==1]
N = 60000
alphas = _df_polar.alpha[:N]
radiuss = _df_polar.radius[:N]
density = _df_polar.density2[:N]
#density1 = [0.2, 0.6]
bottom = radiuss - 0.05

cmap = plt.cm.jet_r
colors = map(cmap, density)

data = sorted(zip(bottom, colors), key=lambda r:r[0])
bars = ax.bar(0, 0.05, width=np.pi*2, bottom=data[0][0], color=data[0][1])
# 设置半径长度的范围
ax.set_rlim(0, 7)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 1))
sm.set_array([])
fig.colorbar(sm, cax=cax)

def update_ax(frame):
    ax.bar(0, 0.05, width=np.pi*2, bottom=data[frame][0], color=data[frame][1])


#line_ani = animation.FuncAnimation(fig, update_ax, 25, fargs=(data, lines), interval=300, blit=False)
line_ani = animation.FuncAnimation(fig, update_ax, len(data)-1, interval=100, blit=False)
plt.show()

