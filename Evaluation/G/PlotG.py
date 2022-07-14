import matplotlib.pyplot as plt
import numpy as np

from Evaluation.G.TwoCocycleG import summed_difference_simpl_const

f = summed_difference_simpl_const

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111, projection='3d')
ax1.set_zlim([-1, 2])

fig2 = plt.figure(2)
fig2.canvas.manager.window.move(800, 100)
ax2 = fig2.add_subplot(111)

extent = 5
resolution = 2 ** 7
x = np.linspace(-extent, extent, resolution)
y = np.linspace(-extent, extent, resolution)
(X, Y) = np.meshgrid(x, y)

gXY = np.array([f(tup) for tup in zip(X.flatten(), Y.flatten())]).reshape(X.shape)
maxgXY = max(max(r) for r in gXY)
gXY = gXY / maxgXY
print(gXY)

contour_res = 30
ax1.plot_wireframe(X, Y, gXY, cmap='viridis', rstride=contour_res, cstride=contour_res)
ax1.contourf(x, y, gXY, contour_res, zdir='z', offset=-1, cmap='viridis')

contourplot = ax2.contourf(X, Y, gXY, contour_res)
fig2.colorbar(contourplot)

plt.ion()

plt.pause(.25)

plt.ioff()

plt.show()
