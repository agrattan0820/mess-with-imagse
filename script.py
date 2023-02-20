from mpl_toolkits.mplot3d import Axes3D
import cv2
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

len(flags)

sea = cv2.imread("./images/sea.jpg")
sea = cv2.cvtColor(sea, cv2.COLOR_BGR2RGB)
# plt.imshow(sea)
# plt.show()


# Make a Colored 3D Scatter Plot
r, g, b = cv2.split(sea)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")

pixel_colors = sea.reshape((np.shape(sea)[0]*np.shape(sea)[1], 3))
norm = colors.Normalize(vmin=-1., vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()

axis.scatter(r.flatten(), g.flatten(), b.flatten(),
             facecolors=pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
plt.show()
