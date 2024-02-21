import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Initial parameters
S = 5              # distance to the target
H = 3              # target height
H0 = 0              # initial height


# General and design parameters
g = 9.81                                # acceleration of gravity
alpha = np.pi / 4             # throw angle in radians (the best angle is 45 degrees)

V0 = math.sqrt(g * S**2 / (2 * (np.cos(alpha))**2 * (S * np.tan(alpha) + H0 - H)))
#Hmax = H0 + V0**2 * (np.sin(alpha))**2 / 2

print("Initial speed: V0 =", V0, "m/s")
#print("Hmax =", Hmax)



fig, ax = plt.subplots()

# create an array of time values
t = np.arange(0.0, 1, 0.001)

# draw a line along which the point moves (this will be the trajectory of the point)
s = t
l, = plt.plot(t, s)

ax = plt.axis([0, S * 1.2, 0, 4])

# starting point position
redDot, = plt.plot([0], [H0], 'ro')

# arrays for storing previous point positions
previous_x = []
previous_y = []

def animate(i):
    global previous_x, previous_y
    
    # calculate the new position of the point
    x = i
    y = H0 + x - x**2 * g / (2*V0**2*(np.cos(alpha))**2)
    # update point data
    redDot.set_data([x], [y])
    
    # save the previous position of the point
    previous_x.append(x)
    previous_y.append(y)
    
    # draw the trajectory of the point only for previous positions
    l.set_data(previous_x, previous_y)
    
    # stop the animation when a certain distance is reached
    if x >= S:
        ani.event_source.stop()
    
    return redDot, l

# create animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, S, 0.04), 
                                      interval=100, blit=True, repeat=False)



plt.show()



