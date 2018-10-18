import matplotlib.pyplot as plt

marques = ["Renault", "Peugeot", "Citroen", "Volkswagen", "Dacia"]
ventes = [416577, 366872, 201373, 139360, 117865]

plt.pie(ventes, labels=marques, autopct='%.2f%%')

plt.title("Parts de ventes de voitures en France en 2017")

plt.show()
