import matplotlib.pyplot as plt
import platform

# 中文字体
import matplotlib.font_manager as fm


def matplot_ch_font():
    if platform.system() == 'Windows':
        fm.findSystemFonts(fontpaths=None, fontext="ttf")
        fm.findfont("SimSun")  # for windows
        plt.rcParams['font.sans-serif'] = ['SimSun']  # for windows

    elif platform.system() == 'Darwin':
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # for mac
