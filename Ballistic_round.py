import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# define a function that takes 3 parameters entered by the user from the keyboard
def plot_trajectory():
    S = float(input("Enter distance to the target in meters: "))
    H = float(input("Enter target height in meters: "))
    H0 = float(input("Enter initial height in meters: "))
    
    # constants
    g = 9.81                                # acceleration of gravity
    alpha = np.pi / 4                       # throw angle in radians (the best angle is 45 degrees)

    # Calculate initial speed and maximal height
    V0 = math.sqrt(g * S**2 / (2 * (np.cos(alpha))**2 * (S * np.tan(alpha) + H0 - H)))
    Hmax = H0 + V0**2 * (np.sin(alpha))**2 / (2 * g)

    # create a new figure and a set of axes
    fig, ax = plt.subplots()

    # Create an array of time values
    t = np.arange(0.0, 1, 0.001)

    # Draw a line along which the point moves (this will be the trajectory of the point)
    #s = t
    l, = plt.plot(t, t)

    # Set the axes limits
    ax.axis([0, S * 1.2, 0, Hmax * 1.4])

    # Starting point position
    redDot, = plt.plot([0], [H0], 'ro')

    # Arrays for storing previous point positions in order to draw the trajectory
    previous_x = []
    previous_y = []

    # Add a target point
    fixed_point_x = S
    fixed_point_y = H

    # create a plot
    plt.scatter(fixed_point_x, fixed_point_y, color='blue', marker='o')

    # Add text to display: coordinates, V0 and Hmax
    ax.text(0.02, 0.9,
            f'Our coordinates: x = 0 m, y = {H0} m\nTarget coordinates: X = {S} m, Y = {H} m\nInitial speed: V0 = {V0:.2f} m/s\nMaximal height: Hmax = {Hmax:.2f} m', 
            horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)

    # define a function for animation
    def animate(i):
        nonlocal previous_x, previous_y
        
        # Calculate the new position of the point
        x = i
        y = H0 + x - x**2 * g / (2*V0**2*(np.cos(alpha))**2)
        
        # Update point data
        redDot.set_data([x], [y])
        
        # Save the previous position of the point
        previous_x.append(x)
        previous_y.append(y)
        
        # Draw the trajectory of the point only for previous positions
        l.set_data(previous_x, previous_y)
        
        # Stop the animation when a certain distance is reached
        if x >= S:
            ani.event_source.stop()
        
        return redDot, l

    # Create animation
    ani = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, S, S/300), 
                                          interval=100, blit=True, repeat=False)

    # open and display a window with a plot
    plt.show()


# Application example: call the function
plot_trajectory()
