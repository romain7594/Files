import matplotlib.pyplot as plt

v = [35.2, 37.4, 26.4, 10.6, 111.2, 64, 48.2, 37, 49.1, 43.4, 69.7, 29]
X = range(12)

plt.bar(X, v, align="center")

plt.xticks(["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"], rotation=45)

plt.xlabel("Mois")
plt.ylabel("Precipitations (mm)")
plt.title("Precipitations au cours de l'annee 2013")

#plt.plot(X, v, "o")

plt.show()
