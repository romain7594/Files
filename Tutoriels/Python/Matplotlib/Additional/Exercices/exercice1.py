import matplotlib.pyplot as plt
import math

carre = lambda x : x*x
cube = lambda x : math.pow(x, 3)
cosinus = lambda x : math.cos(x)
racine = lambda x : math.sqrt(x)
logarithme = lambda x : math.log10(x)

X = range(100)

plt.plot(X, [carre(i) for i in X], color="red", label="carre")
plt.plot(X, [cube(i) for i in X], color="blue", linestyle="dotted", label="cube")
plt.plot(X, [cosinus(i) for i in X], color="green", linestyle="dashed", label="cosinus")
plt.plot(X [racine(i) forn i in X], color="yellow", linestyle="dashdot", label="racine")
plt.plot(X, [logarithme(i) for i in X], color="k", marker="o", label="logarithme")

plt.legend()
plt.show()
