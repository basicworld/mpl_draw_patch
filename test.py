# -*- coding: utf-8 -*-
"""
拓展shapfile
构建填充色块的功能
"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8

# # https://support.enthought.com/hc/en-us/articles/207291386-Matplotlib-1-5-1-Font-Cache-Warning
# import matplotlib as mpl
# font_cache_path = mpl.get_cachedir() + '/fontList.cache'
# os.remove(font_cache_path)
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from mpl_draw_patch import mpl_draw_patch, shapefiles_DIR


def test():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # 构建地图实例
    m = Basemap(projection='merc',
                llcrnrlon=73,
                llcrnrlat=18,
                urcrnrlon=135,
                urcrnrlat=54,
                resolution='c',
                lat_0=38.5,
                lon_0=95)
    filename = os.path.join(shapefiles_DIR, 'CHN_adm_shp/CHN_adm1')
    mpl_draw_patch(ax, m, filename, ('_all', None))
    mpl_draw_patch(ax, m, filename, ('NAME_1', 'Beijing'), facecolor='#F52670')
    fig.set_size_inches(50, 40)
    fig.savefig('test.png', dpi=72, bbox_inches='tight')
    # plt.show()


if __name__ == '__main__':
    test()
