import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 1000)
y = np.sin(x)

plt.title("wave")
plt.xlabel("X")
plt.ylabel("Y")

# X軸の範囲
plt.xlim(-5, 5)
# Y軸の範囲
plt.ylim(-1.0, 1.0)

plt.grid(True)
plt.plot(x, y)

plt.show()

# 散布図
x = np.random.randn(1000)
y = np.random.randn(1000)

plt.title("散布図", fontname="MS Gothic")
plt.scatter(x, y)
plt.show()


# ヒストグラム
plt.title("ヒストグラム", fontname="MS Gothic")
plt.hist(x)
plt.show()


