# utf-8
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import scipy.linalg as spla


def f1(X):
    x, y = X[0], X[1]
    f1 = x - np.sin(-3 * x * (y + 1))
    f2 = -(y + 1)
    return 4 / 5 * np.array([f1, f2])


def f2(X):
    x, y = X[0], X[1]
    f1 = 1 / 2 * x * (2 - x) * (2 + x) - 1 / 2 * np.cos(2 * x * (y - 0.5))
    f2 = np.exp(-x ** 2 - (y + 1) ** 2) + 1 / 2 * (y - 1 / 2 + np.cos(x * (y + 0.5)))
    return np.array([f1, f2])


def g(f, x):
    return 1 / 2 * np.inner(f(x), f(x))


def compute_jacobian(f, x, dx=1e-8):
    fx = f(x)
    n, m = len(x), len(fx)
    jac = np.zeros((m, n))
    for j in range(n):
        h = (abs(x[j]) * dx if x[j] != 0 else dx)
        xph = np.array([(xi if k != j else xi + h) for k, xi in enumerate(x)])
        xmh = np.array([(xi if k != j else xi - h) for k, xi in enumerate(x)])
        jac[:, j] = (f(xph) - f(xmh)) / (2 * h)
    return jac


def newton(f, x0, tol=1e-4, max_steps=50):
    ax1.scatter(x0[0], x0[1], zs=g(f, x0), s=80, color='black')
    ax2.scatter(x0[0], x0[1], s=80, color='black')
    xk = x0
    steps = 0
    deltaxk = 1

    while not (spla.norm(deltaxk) <= tol or steps == max_steps):
        fxk = f(xk)
        dfxk = compute_jacobian(f, xk)
        Q, R = spla.qr(dfxk)
        z = Q.T.dot(-fxk)
        deltaxk = spla.solve_triangular(R, z)
        xk = xk + deltaxk
        steps = steps + 1
        ax1.scatter(xk[0], xk[1], zs=g(f, xk), s=80, color='blue')
        ax2.scatter(xk[0], xk[1], s=80, color='blue')

    ax1.scatter(xk[0], xk[1], zs=g(f, xk), s=80, color='green')
    ax2.scatter(xk[0], xk[1], s=80, color='green')
    plt.pause(.25)

    return xk


# =============================================================================
# Hauptprogramm
# =============================================================================


"""
Hier auswählen, welche Funktion gerade betrachtet werden soll (f1 oder f2).
"""
f = f2  # <--------------

"""
Hier den Startwert angeben.
"""
# x0 = np.array([0.75, -0.75])  # <--------- für f1 gegeben
x0 = np.array([-0.5, -0.5])


# =============================================================================
# Visualisierung
# (Ab hier sind keine Änderungen mehr nötig!)
# =============================================================================

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111, projection='3d')
fig1.canvas.manager.window.move(100, 100)
ax1.set_zlim([-1, 2])

fig2 = plt.figure(2)
fig2.canvas.manager.window.move(800, 100)
ax2 = fig2.add_subplot(111)

# Gebiet Omega deklarieren über ein Gitter in x- und y-Richtung
x = np.linspace(-1, 1, 201)
y = np.linspace(-2, 1, 201)
(X, Y) = np.meshgrid(x, y)

# Auswerten von g im Gitter
gXY = np.array([g(f, np.array(tup)) for tup in zip(X.flatten(), Y.flatten())]
               ).reshape(X.shape)

# Plot der Funktion g bzw. der Höhenlinien
st = 20
ax1.plot_wireframe(X, Y, gXY, cmap='viridis', rstride=st, cstride=st)
ax1.contourf(x, y, gXY, 20, zdir='z', offset=-1, cmap='viridis')

contourplot = ax2.contourf(X, Y, gXY, 50)
fig2.colorbar(contourplot)

# Start interaktiver Modus
plt.ion()

# Gauss-Newton-Verfahren, Rückgabe die Approximation eines Minimums
xhat = newton(f, x0)
print("Berechnetes x:", xhat)

plt.pause(.25)

# Ende interaktiver Modus
plt.ioff()

plt.show()

# =============================================================================
# =============================================================================