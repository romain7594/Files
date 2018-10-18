import matplotlib.pyplot as plt

plt.xlim(0, 20)
plt.ylim(0, 10)

plt.axvline(5, color="blue")
plt.axvline(15, color="blue")

plt.axhline(8, linestyle="dotted", color="black")
plt.plot(range(21), [5]*21, color="red", marker="o")
plt.axhline(2, linestyle="dashdot", color="black")

plt.axhspan(7.5, 8.5, color="red", alpha=0.5, hatch='/')
plt.axhspan(4, 6, color="yellow", alpha=0.5)

plt.axvspan(2, 3, 0.85, 1, color="black")
plt.axvspan(17, 18, 0.85, 1, color="black")
plt.axvspan(9, 11, color="black", alpha=0.5)

y = [4, 6]*5
y.append(4)
plt.plot(range(0, 21, 2), y)
y1 = [7, 3]*5
y1.append(7)
plt.plot(range(0, 21, 2), y1, color="red")

plt.axhline(1, 0.125, 0.375, color="red", linestyle="--", linewidth=5)
plt.axhline(1, 0.625, 0.875, color="red", linestyle="--", linewidth=5)

plt.show()
