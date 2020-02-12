import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import xlrd
import numpy as np
from scipy import interpolate

# Read excel
print("Reading the data...")
# book = xlrd.open_workbook('before cooling.xlsx')
book = xlrd.open_workbook('after cooling.xlsx')
sheet1 = book.sheets()[0]
nrows = sheet1.nrows
ncols = sheet1.ncols
xdata = np.array(sheet1.col_values(1)[1:nrows])
ydata = np.array(sheet1.col_values(2)[1:nrows])
zdata = np.array(sheet1.col_values(3)[1:nrows])

boundary = 1000
x = np.linspace(np.min(xdata) + boundary, np.max(xdata) - boundary, 1000)
y = np.linspace(np.min(ydata) + boundary, np.max(ydata) - boundary, 1000)
X, Y = np.meshgrid(x, y)
Z = interpolate.griddata((xdata, ydata), zdata, (X, Y), method='cubic')
print("Ploting the data...")
fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
c = ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('rainbow'))
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$z$")

plt.show()

print("Plot completed")

