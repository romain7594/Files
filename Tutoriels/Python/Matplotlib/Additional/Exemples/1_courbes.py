##### dia 14 #####
plt.plot(1, 2)
plt.show()


##### dia 16 #####
plt.plot(1, 2, "o")
plt.show()

#plt.plot(1, 2, marker="o")
#plt.show()


##### dia 18 #####
plt.plot(1, 2, "o")
plt.plot(1, 3, "o")
plt.show()

plt.plot(1, 2, marker="o")
plt.plot(1, 3, marker="o")
plt.show()


##### dia 20 #####
points = [(1,2), (3,1), (5,3)]

plt.plot(points[0][0], points[0][1], "o")
plt.plot(points[1][0], points[1][1], "o")
plt.plot(points[2][0], points[2][1], "o")

plt.show()

#for p in points :
	#plt.plot(p[0], p[1], "o")

#plt.show()


##### dia 22 #####
plt.plot([1,2], [3,4])
plt.show()


##### dia 24 #####
x = [1, 3, 4, 6, 7, 9, 10, 11]
y = [2, 1, 5, 8, 4, 1, 0, 7]

plt.plot(x, y)

plt.show()


##### dia 25 #####
plt.plot([1, 2, 3, 4, 5], [3, 1, 4, 7])
plt.show()



##### dia 26 #####
plt.plot([0, 2, 3, 4, 9], [3, 1, 4, 7, 6])
plt.plot([0, 2, 4, 7, 9], [6, 2, 9, 0, 2])

plt.show()


##### dia 27 #####
plt.plot([0, 2], [3, 1], [0, 2], [6, 2])
plt.show()


##### dia 28 #####
[5, 4, 7, 0, 5, 10, 4, 2, 6, 2, 3, 8, 10, 2, 10, 7, 3, 4, 7, 2]
[8, 4, 9, 9, 10, 4, 7, 1, 7, 2, 9, 6, 1, 8, 4, 3, 10, 3, 9, 2]


##### dia 33 #####
plt.plot(1, 2 "*")
plt.show()

plt.plot(1, 2, "d")
plt.show()

plt.plot(1, 2, "^")
plt.show()

#
x = [1, 3, 4, 6, 7, 9, 10, 11]
y = [2, 1, 5, 8, 4, 1, 0, 7]

plt.plot(x, y, ls=":")

plt.show()


##### dia 34 #####
x = [1, 3, 4, 6, 7, 9, 10, 11]
y = [2, 1, 5, 8, 4, 1, 0, 7]

plt.plot(x, y, "--")

plt.show()


##### dia 35 #####
x = [1, 3, 4, 6, 7, 9, 10, 11]
y = [2, 1, 5, 8, 4, 1, 0, 7]

plt.plot(x, y, linestyle="-.")

plt.show()


##### dia 37 #####
x = [1, 3, 4, 6, 7, 9, 10, 11]
y = [2, 1, 5, 8, 4, 1, 0, 7]

plt.plot(x, y, marker="s", linestyle="--")

plt.show()


##### dia 40 #####
plt.plot([1, 2, 3, 4, 5], [3, 1, 4, 7, 6], "o", color="r")
plt.plot([0, 8], [0, 8], c="b")

plt.show()


##### dia 43 #####
plt.plot([0, 10], [0, 10], color='FF00AF')
plt.plot([1, 2, 3, 4, 5], [4, 7, 1, 2, 9], "h", color=(1, 1, 0))

plt.show()


##### dia 45 #####
plt.plot([2, 5], [0, 8], "y--")
plt.plot([3, 3.5, 4], [2, 3, 4], "ro")

plt.show()


##### dia 47 #####
plt.plot([0, 5], [1, 2], linewidth=1)
plt.plot([0, 5], [1.5, 2.5], lw=2)
plt.plot([0, 5], [2, 3], lw=5.5)
plt.plot([0, 5], [2.5, 3.5], linewidth=10)

plt.show()
