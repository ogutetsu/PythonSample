import numpy as np
from pylab import plt, mpl

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

def f(x):
    return np.sin(x) + 0.5 * x

def create_plot(x,y,styles,labels, axlabels):
    plt.figure(figsize=(10,6))
    for i in range(len(x)):
        plt.plot(x[i],y[i],styles[i],label=labels[i])
        plt.xlabel(axlabels[0])
        plt.ylabel(axlabels[1])
    plt.legend(loc=0)

x = np.linspace(-2 * np.pi, 2 * np.pi, 50)
create_plot([x],[f(x)],['b'],['f(x)'],['x','f(x)'])

#plt.show()
plt.clf()

res = np.polyfit(x, f(x), deg=1, full=True)
print(res)

ry = np.polyval(res[0], x)
create_plot([x,x],[f(x),ry],['b','r'],['f(x)','regression'],['x','f(x)'])
#plt.show()

plt.clf()


reg = np.polyfit(x, f(x), deg=5)
ry = np.polyval(reg, x)
create_plot([x,x],[f(x),ry],['b','r.'],['f(x)','regression'],['x','f(x)'])
#plt.show()

plt.clf()

reg = np.polyfit(x, f(x), 7)
ry = np.polyval(reg, x)
np.allclose(f(x), ry)
print(np.mean((f(x)-ry)**2))
create_plot([x,x],[f(x),ry],['b','r.'],['f(x)','regression'],['x','f(x)'])
#plt.show()

plt.clf()

matrix = np.zeros((3+1,len(x)))
matrix[3,:] = x**3
matrix[2,:] = x**2
matrix[1,:] = x
matrix[0,:] = 1

reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0]
print(reg.round(4))

ry = np.dot(reg,matrix)
create_plot([x,x],[f(x),ry],['b','r.'],['f(x)','regression'],['x','f(x)'])
#plt.show()

plt.clf()


matrix[3,:] = np.sin(x)
reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0]
print(reg.round(4))
ry =  np.dot(reg,matrix)
print(np.allclose(f(x),matrix))

print(np.mean((f(x)-ry)**2))
create_plot([x,x],[f(x),ry],['b','r.'],['f(x)','regression'],['x','f(x)'])
#plt.show()

plt.clf()

xn = np.linspace(-2*np.pi,2*np.pi,50)
xn = xn + 0.15 * np.random.standard_normal(len(xn))
yn = f(xn) + 0.25 * np.random.standard_normal(len(xn))

reg = np.polyfit(xn, yn, 7)
ry = np.polyval(reg, xn)
create_plot([x,x],[f(x),ry],['b','r.'],['f(x)','regression'],['x','f(x)'])
#plt.show()

plt.clf()

xu = np.random.rand(50)*4*np.pi-2*np.pi
yu = f(xu)

print(xu[:10].round(2))
print(yu[:10].round(2))

reg = np.polyfit(xu,yu,5)
ry = np.polyval(reg,xu)
create_plot([xu,xu],[yu,ry],['b.','ro'],['f(x)','regression'],['x','f(x)'])
#plt.show()

plt.clf()

def fm(p):
    x,y = p
    return np.sin(x) + 0.25 * x + np.sqrt(y) + 0.05 * y ** 2

x = np.linspace(0, 10, 20)
y = np.linspace(0, 10, 20)
X, Y = np.meshgrid(x,y)
Z = fm((X,Y))
x = X.flatten()
y = Y.flatten()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap='coolwarm', linewidth=0.5, antialiased=True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
fig.colorbar(surf, shrink=0.5, aspect=5)

#plt.show()

plt.clf()


matrix = np.zeros((len(x), 6+1))
matrix[:,6] = np.sqrt(y)
matrix[:,5] = np.sin(x)
matrix[:,4] = y**2
matrix[:,3] = x**2
matrix[:,2] = y
matrix[:,1] = x
matrix[:,0] = 1

reg = np.linalg.lstsq(matrix, fm((x,y)), rcond=None)[0]
RZ = np.dot(matrix, reg).reshape((20,20))
fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
surf1 = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap='coolwarm', linewidth=0.5, antialiased=True)
surf2 = ax.plot_wireframe(X, Y, RZ, rstride=2, cstride=2, label='regression')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
ax.legend()
fig.colorbar(surf, shrink=0.5, aspect=5, ax = ax)

#plt.show()

plt.clf()

import scipy.interpolate as spi

x = np.linspace(-2 * np.pi, 2 * np.pi, 25)
def f(x):
    return np.sin(x) + 0.5 * x

ipo = spi.splrep(x, f(x), k=1)
iy = spi.splev(x, ipo)
np.allclose(f(x), iy)
create_plot([x,x],[f(x),iy], ['b','ro'],['f(x)','interpolation'],['x','f(x)'])
#plt.show()

plt.clf()

xd = np.linspace(1.0, 3.0, 50)
iyd = spi.splev(xd,ipo)
create_plot([xd,xd],[f(xd),iyd], ['b','ro'],['f(x)','interpolation'],['x','f(x)'])
#plt.show()

plt.clf()

ipo = spi.splrep(x, f(x), k=3)
iyd = spi.splev(xd,ipo)
np.allclose(f(xd), iyd)
np.mean((f(xd)-iyd)**2)
create_plot([xd,xd],[f(xd),iyd], ['b','ro'],['f(x)','interpolation'],['x','f(x)'])
#plt.show()

plt.clf()

def fm(p):
    x, y = p
    return (np.sin(x) + 0.05 * x ** 2 + np.sin(y) + 0.05 * y ** 2)

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X,Y = np.meshgrid(x, y)
Z = fm((X, Y))

fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap='coolwarm', linewidth=0.5, antialiased=True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
fig.colorbar(surf, shrink=0.5, aspect=5, ax = ax)
#plt.show()

plt.clf()

import scipy.optimize as sco

def fo(p):
    x, y = p
    z = np.sin(x) + 0.05 * x ** 2 + np.sin(y) + 0.05 * y ** 2
    if output == True:
        print('%8.4f | %8.4f | %8.4f' % (x, y, z))
    return z

output = False
opt1 = sco.brute(fo, ((-10,10.1,0.1),(-10,10.1,0.1)), finish=None)

print(opt1)
print(fm(opt1))




