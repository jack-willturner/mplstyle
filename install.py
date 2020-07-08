import matplotlib
from shutil import copyfile

dir = matplotlib.get_configdir()
copyfile('style.mplstyle', dir+'/stylelib/personal.mplstyle')
