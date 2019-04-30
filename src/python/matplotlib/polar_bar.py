# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def polar_bar_demo():
    N = 70
    deltar = 0.1
    alphas = np.ones(N)
    radiuss = np.linspace(0, 0.1*N, N, endpoint=False)
    density = np.random.random(N)
    bottom = radiuss - deltar

    # force square figure and square axes looks better for polar, IMO
    fig = plt.figure(figsize=(8, 8))

    # 坐标含义[left,bottom,width,height]
    ax = fig.add_axes([0.1, 0.1, 0.7, 0.7], polar=True)
    cax = fig.add_axes([0.9, 0.1, 0.04, 0.7])

    cmap = plt.cm.jet_r
    colors = map(cmap, density)

    bars = ax.bar(0, deltar, width=np.pi*2, bottom=bottom, color=colors)

    # 设置角度怎么旋转, -1代表顺时针, 1代表逆时针
    ax.set_theta_direction(direction=-1)
    # 设置0度朝向, 共八个方向 东西南北和组合 NESW
    ax.set_theta_zero_location('W')
    # 设置角度的标签, 这里设置的是角度度数, fmt=‘’表示不显示
    ax.set_thetagrids(angles=np.arange(0, 360, 30))
    # 设置角度显示范围, 这里用的是弧度,类似0 ~ 2*np.pi
    ax.set_thetalim(0, np.pi*1.5)
    # 设置半径长度显示的位置, 这里用的是角度度数,类似0 ~ 360
    ax.set_rlabel_position(180)
    # 设置半径长度显示的范围刻度
    ax.set_rgrids(range(10))
    # 设置半径长度的范围
    ax.set_rlim(0, 8)

    # 设置colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 1))
    sm.set_array([])
    fig.colorbar(sm, cax=cax)
    plt.show()


if __name__ == '__main__':
    polar_bar_demo()

