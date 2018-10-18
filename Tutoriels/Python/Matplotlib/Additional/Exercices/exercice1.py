import matplotlib.pyplot as plt
import math

carre = lambda x : x*x
cube = lambda x : math.pow(x, 3)
cosinus = lambda x : math.cos(x)
racine = lambda x : math.sqrt(x)

plt.ylim(-15, 15)
plt.xlim(-15, 15)

X = range(-15, 15)
XX = range(15)

plt.plot(X, X, color="k", marker="o", label="x = x")
plt.plot(X, [carre(i) for i in X], color="red", label="carre")
plt.plot(X, [cube(i) for i in X], color="blue", linestyle="dotted", label="cube")
plt.plot(X, [cosinus(i) for i in X], color="green", linestyle="dashed", label="cosinus")
plt.plot(XX, [racine(i) for i in XX], color="black", linestyle="dashdot", label="racine")

plt.axvline(0, color="k", alpha=0.3)
plt.axhline(0, color="k", alpha=0.3)

plt.legend()
plt.show()
