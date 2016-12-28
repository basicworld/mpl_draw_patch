# -*- coding: utf-8 -*-
"""
拓展shapfile
构建填充色块的功能
"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
THIS_DIR = os.path.realpath(os.path.dirname(__file__))
shapefiles_DIR = os.path.join(THIS_DIR, 'shapefiles')

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def mpl_draw_patch(ax,
                   m,
                   sf_name,
                   by_filter=(None, None),
                   drawbounds=True,
                   facecolor='#78D2F9',
                   edgecolor='k',
                   linewidth=0.5):
    """
    使用shapefile数据填充特定区域的颜色
    """
    # 获取shapefile的名字
    base_sf_name = os.path.basename(sf_name)

    # 如果没有加载shapefile文件就加载
    if not hasattr(m, base_sf_name):
        sf_info = m.readshapefile(sf_name, base_sf_name,
                                  drawbounds=drawbounds)
    # 筛选字段和筛选条件
    by, by_f = by_filter
    by_all = True if by == '_all' else False  # 画所有色块标示
    if not isinstance(by_f, (list, tuple)):
        by_f = [by_f]
    if by:
        patches = []  # 色块
        for info, shape in zip(getattr(m, base_sf_name+'_info'),
                               getattr(m, base_sf_name)):
            if by_all or info[by] in by_f:
                patches.append(Polygon(shape, closed=True))
        # 将色块画在图中
        ax.add_collection(PatchCollection(patches,
                          facecolor=facecolor,
                          edgecolor=edgecolor,
                          linewidth=linewidth))

    pass

def test():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # 构建地图实例
    m = Basemap(projection='merc',
                llcrnrlon=73,
                llcrnrlat=15,
                urcrnrlon=135,
                urcrnrlat=55,
                resolution='c',
                lat_0=38.5,
                lon_0=95)
    filename = 'shapefiles/CHN_adm_shp/CHN_adm1'
    # mpl_draw_patch(ax, m, filename, ('_all', None))
    mpl_draw_patch(ax, m, filename, ('ID_1', (1,2,3,4)))
    plt.show()


if __name__ == '__main__':
    test()
