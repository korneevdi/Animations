import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plot_trajectory(S, H, H0):
    # General and design parameters
    g = 9.81                                # acceleration of gravity
    alpha = np.pi / 4                       # throw angle in radians (the best angle is 45 degrees)

    # Calculate initial speed and maximal height
    V0 = math.sqrt(g * S**2 / (2 * (np.cos(alpha))**2 * (S * np.tan(alpha) + H0 - H)))
    Hmax = H0 + V0**2 * (np.sin(alpha))**2 / (2 * g)

    fig, ax = plt.subplots()

    # Create an array of time values
    t = np.arange(0.0, 1, 0.001)

    # Draw a line along which the point moves (this will be the trajectory of the point)
    s = t
    l, = plt.plot(t, s)

    # Set the axes limits
    ax.axis([0, S * 1.2, 0, Hmax * 1.4])

    # Starting point position
    redDot, = plt.plot([0], [H0], 'ro')

    # Arrays for storing previous point positions
    previous_x = []
    previous_y = []

    # Add a target point
    fixed_point_x = S
    fixed_point_y = H
    plt.scatter(fixed_point_x, fixed_point_y, color='blue', marker='o')

    # Add text to display V0 and Hmax
    ax.text(0.02, 0.9, f'Our coordinates: x = 0 m, y = {H0} m\nTarget coordinates: X = {S} m, Y = {H} m\nInitial speed: V0 = {V0:.2f} m/s\nMaximal height: Hmax = {Hmax:.2f} m', 
            horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)

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

    plt.show()

# Input parameters from user
S = float(input("Enter distance to the target (S): "))
H = float(input("Enter target height (H): "))
H0 = float(input("Enter initial height (H0): "))

# Plot trajectory
plot_trajectory(S, H, H0)

