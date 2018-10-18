import matplotlib.pyplot as plt

prop = [50, 30, 10, 5, 5]
ingredients = ["Pate", "Sauce tomate", "Fromage", "Jambon", "Champignons"]

plt.pie(prop, labels=ingredients, colors=["lightgoldenrod", "orangered", "coral", "lightpink", "azure"], autopct='%.f%%')

plt.title("Pizza jambon fromage champignons")

plt.show()
