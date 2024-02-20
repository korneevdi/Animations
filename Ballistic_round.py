import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Initial parameters
S = 40              # distance to the target
H = 0              # target height
H0 = 1              # initial height


# General and design parameters
g = 9.81                                # acceleration of gravity
alpha = np.pi / 4             # throw angle in radians (the best angle is 45 degrees)

V0 = g * S**2 / (2 * (np.cos(alpha))**2 * (S * np.tan(alpha) + H0 - H))
Hmax = H0 + V0**2 * (np.sin(alpha))**2 / 2

print("V0 =", V0)
print("Hmax =", Hmax)



fig, ax = plt.subplots()

# создаем массив значений времени
t = np.arange(0.0, 1, 0.001)

# рисуем линию, по которой движется точка (это будет траектория точки)
s = t
l, = plt.plot(t, s)

ax = plt.axis([0, S, 0, Hmax])

# начальное положение точки
redDot, = plt.plot([0], [H0], 'ro')

# массивы для хранения предыдущих положений точки
previous_x = []
previous_y = []

def animate(i):
    global previous_x, previous_y
    
    # вычисляем новое положение точки
    x = i
    y = H0 + np.tan(alpha)*i - (g*i**2)/(2*V0**2*np.cos(alpha)**2)
    # обновляем данные точки
    redDot.set_data([x], [y])
    
    # сохраняем предыдущее положение точки
    previous_x.append(x)
    previous_y.append(y)
    
    # рисуем траекторию точки только для предыдущих положений
    l.set_data(previous_x, previous_y)
    
    # останавливаем анимацию, когда достигнуто определенное расстояние
    if x >= S:
        ani.event_source.stop()
    
    return redDot, l

# создаем анимацию
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, S, 0.1), 
                                      interval=100, blit=True, repeat=False)



plt.show()
