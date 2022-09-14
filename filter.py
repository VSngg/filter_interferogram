#!/usr/bin/env python3
from skimage import io
from skimage.filters import gaussian
from skimage.restoration import denoise_nl_means
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys

img = io.imread(sys.argv[1], as_gray=True)


denoisedImg = denoise_nl_means(img, fast_mode=True, h=0.2)

denoisedGaussian = gaussian(denoisedImg, 3)

# ИЗМЕНИТЬ ЭТУ ПЕРЕМЕННУЮ ЧТОБЫ ПОЛУЧИТЬ ГРАФИК
target_plot = denoisedGaussian
# turn NP array into xyz plot
m,n = target_plot.shape
y,x = np.mgrid[:m,:n]
z = target_plot
#out = np.column_stack((C.ravel(),R.ravel(), denoisedGaussian.ravel()))

#######################
# ПОСТРОЕНИЕ ГРАФИКОВ #
#######################

fig = plt.figure()

ax=fig.add_subplot(211)
ax.imshow(denoisedGaussian, cmap='gray')
ax.set_title("denoised1")

# ax=fig.add_subplot(212)
# ax.imshow(img, cmap='gray')
# ax.set_title("original")

ax=fig.add_subplot(212, projection='3d')
ax.plot_surface(x, y ,z, cmap ='inferno')
ax.set_title("3д вид денойз+Гаусс")

plt.show()

