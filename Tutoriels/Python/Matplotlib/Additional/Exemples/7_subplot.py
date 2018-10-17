##### dia 173 #####
plt.subplot(2,2,1)
plt.plot([0, 10], [0, 10])

plt.subplot(2,2,3)
plt.hist([random.randint(0, 5) for i in range(100)], 4)

plt.subplot(122)
plt.plot(range(10), range(10), "o")

plt.show()


##### dia 175 #####
plt.subplot(221)
plt.plot([0, 10], [0, 10])

plt.subplot(222)
plt.hist([random.randint(0, 5) for i in range(100)], 4)

plt.subplot(212)
plt.plot(range(10), range(10), "o")

plt.show()
