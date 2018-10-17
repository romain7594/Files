##### dia 154 #####
import matplotlib.pyplot as plt

plt.pie([1, 2, 3, 4, 5])
plt.show()


##### dia 155 #####
import matplotlib.pyplot as plt

plt.pie(1)
plt.show()


##### dia 158 #####
import matplotlib.pyplot as plt

plt.pie([1, 2, 3, 4, 5], explode=[0, 0.3, 0, 0.5, 0])
plt.show()


##### dia 160 #####
import matplotlib.pyplot as plt

plt.pie([1, 2, 3, 4, 5], startangle=90)
plt.show()

plt.pie([1, 2, 3, 4, 5], startangle=140)
plt.show()

#
import matplotlib.pyplot as plt
import math

angle = math.degrees((3*math.pi)/2) # 270 degres

plt.pie([1, 2, 3, 4, 5], startangle=angle)
plt.show()


##### dia 161 #####
import matplotlib.pyplot as plt

plt.pie([1, 2, 3, 4, 5])
plt.show()

plt.pie([1, 2, 3, 4, 5], counterclock=False)
plt.show()


##### dia 162 #####
import matplotlib.pyplot as plt

plt.pie([1, 2, 3, 4, 5], radius=1)
plt.show()

plt.pie([1, 2, 3, 4, 5], radius=0.6)
plt.show()


##### dia 164 #####
import matplotlib.pyplot as plt

plt.pie([1, 2, 3, 4, 5], autopct='%.f%%')
plt.show()

plt.pie([1, 2, 3, 4, 5], autopct='%.2f%%')
plt.show()


##### dia 166 #####
import matplotlib.pyplot as plt

labels = ["ZONE "+str(i) for i in range(1, 6)]

plt.pie([1, 2, 3, 4, 5], autopct='%.1f%%', labels=labels, pctdistance=1.2, labeldistance=0.5)
plt.show()


##### dia 167 #####
import matplotlib.pyplot as plt

labels = ["ZONE "+str(i) for i in range(1, 6)]

plt.pie(
	[1, 2, 3, 4, 5],
	explode = [0.2, 0, 0, 0.2, 0],
	autopct = '%.1f%%',
	labels = labels,
	shadow = True,
	colors = ["yellowgreen", "gold", "lightskyblue", "lightcoral", "OrangeRed"]
	startangle = 45
)

plt.title("Diagramme circulaire)

plt.show()
