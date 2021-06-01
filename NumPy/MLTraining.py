import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(20)*8-4
# サインカーブにノイズを加える
y = np.sin(x) + np.random.randn(20)*0.2

# -4～4の間を100等分した数列
xx = np.linspace(-4, 4, 100)

plt.title('training data')
plt.xlabel('X')
plt.ylabel('y')
plt.grid()
plt.scatter(x, y, marker='x', c='red')
plt.plot(xx, np.sin(xx))
plt.show()

a = np.empty((6,6))
for i in range(6):
    for j in range(6):
        a[i][j] = np.sum(x**(i+j))

b = np.empty(6)
for i in range(6):
    b[i] = np.sum(x**i*y)

o = np.dot(np.linalg.inv(a), b.reshape(-1,1))
f = np.poly1d(o.flatten()[::-1])

plt.title('training data')
plt.xlabel('X')
plt.ylabel('y')
plt.grid()
plt.scatter(x, y, marker='x', c='red')
plt.plot(xx, f(xx), color='green')
plt.plot(xx, np.sin(xx), color='blue')
plt.show()

# フィッティングを行う
o2 = np.polyfit(x, y, 5)
f2 = np.poly1d(o2)
plt.title('training data')
plt.xlabel('X')
plt.ylabel('y')
plt.grid()
plt.scatter(x, y, marker='x', c='red')
plt.plot(xx, f2(xx), color='green')
plt.plot(xx, np.sin(xx), color='blue')
plt.show()
