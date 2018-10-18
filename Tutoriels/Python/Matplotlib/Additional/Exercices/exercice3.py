import matplotlib.pyplot as plt

onze = [5.4, 7.1, 10, 15.8, 17, 18.8, 18.5, 20, 19, 14.2, 10.5, 7.9]
douze = [7.2, 3, 11.5, 10.3, 16.3, 17.7, 19.6, 21.7, 16.7, 13.1, 8.2, 6.9]
treize = [4.2, 3.7, 6.1, 11.2, 12.9, 17.5, 22.9, 20.8, 17.5, 14.8, 7.9, 6.8]
X = range(12)

plt.plot(X, onze, label="2011")
plt.plot(X, douze, label="2012")
plt.plot(X, treize, label="2013")

plt.xlim(0, 11)
plt.xlabel("Mois")
plt.ylabel("Temperature (degres celcius)")
plt.xticks(range(12), ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"], rotation=20)
plt.title("Temperature moyenne\nau cours des annees 2011, 2012 et 2013")

plt.legend()
plt.grid(True)

plt.show()
