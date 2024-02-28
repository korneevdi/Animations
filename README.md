## Description

The file **Ballistic_round** contains the code of the program that performs the animation of a projectile launched at a target. The user enters three parameters from the keyboard: the distance to the target, the height at which it is located, and the height at which the launcher is located. Consideration of the flight of a ballistic projectile in the simplest case is similar to the classical school problem of the movement of a body thrown at an angle to the horizon. In this repository, this problem is solved in Python and animation of the movement of a projectile using the **matplotlib** library is presented. The program will work in all four cases: ground-to-ground, ground-to-air, air-to-ground and air-to-air.

**Please note that this program was created solely for educational purposes in order to understand and demonstrate the capabilities of the Python matplotlib library. The author of this program exclusively supports world peace!** 😊🤝🏻

## Some physics

According to the laws of physics, the free movement of a body in the gravitational field of the earth can be described using kinematics equations:

$x(t) = x_0 + v_0t\cos\alpha$,

$y(t) = y_0 + v_0t\sin\alpha + \frac{at^2}{2}$,

where $x_0$ and $y_0$ are initial coordinates, $v_0$ is initial speed, $\alpha$ is the angle at which the body was thrown, $t$ is time and $a$ is acceleration. In our case, this acceleration $a = -g$, because it is the downward gravity acceleration.

We can introduce a coordinate system such that $x_0 = 0$. Since we want our projectile to hit the target, the trajectory should go through the point with coordinates $(S,H)$, which are input by the user. Then the at the final moment of time $T$ we can write:

$S = v_0T\cos\alpha$,

$H = H_0 + v_0T\sin\alpha - \frac{gT^2}{2}$.

This is a system of two equations with two unknown variables - the flight time $T$ and the initial speed $v_0$ of the projectile. We can obtain explicit expressions for both of them by solving the system of equations:

$v_0 = \frac{S}{\cos\alpha}\cdot\sqrt{\frac{g}{2(S\tan\alpha+H_0-H)}}$,

$T = \sqrt{\frac{2(S\tan\alpha+H_0-H)}{g}}$.

The formulas turn out to be cumbersome, but Python doesn't care :)

We can also solve the system of equations for $x(t)$ and $y(t)$ a little differently, and then we get the function $y(x)$, that is, the equation for the projectile flight trajectory:

$y(x) = H_0 + x\tan\alpha - \frac{gx^2}{2v_0^2\cos^2\alpha}$.

Now you can calculate the derivative $y'(x)$ of this function and equate it to zero to find the maximum height of the trajectory:

$y_{max} = H_0 + \frac{v_0^2\sin^2\alpha}{2g}$.

We need this value so that we can automatically adjust the size of the window in which the animation will be shown. So, now you can start programming!

## Code development

The function first asks the user for three input parameters: target distance **S**, target height **H**, and launcher height **H0**. This allows you to accurately calculate the trajectory of movement, given that the starting angle is $45^{\circ}$ (this is the optimal angle). Next, using constants, we calculate the initial speed of the projectile at the moment of launch, as well as the maximum height of its trajectory. The value of the initial speed will be displayed on the screen for the user, and we need the maximum height in order to optimally select the size of the panel where the animation will be shown (see below).

Next, the *plt.subplots()* method creates a new figure and a set of axes. In this case, we don't specify any arguments, so the method creates one figure with one set of axes. If you specify arguments (for example, *plt.subplots(nrows=2, ncols=2)*), a grid of figures will be created with the specified number of rows and columns. The **fig** variable contains a figure object, and the **ax** variable contains an axes set object. This is done using the unpacking mechanism in Python.

We then create an array **t** of time values, starting at 0.0 and ending with a value less than 1 (exclusively), in increments of 0.001. This array will be used as the **X** axis (abscissa) in the graph. The line *l, = plt.plot(t, t)* creates a line plot where the values on the **X** and **Y** axis correspond to the values in the **t** array. The **l** variable receives a line object (in this case, an object of type *Line2D*). We use a comma after **l** to unpack the return value of *plt.plot()* into a single variable. This makes the **l** variable a reference to a line object rather than a list of line objects.

In the line *ax.axis([0, S * 1.2, 0, Hmax * 1.4])* we set the axes values. This is where we use the distance **S** to the target and the maximum height **Hmax** of the trajectory so that the axes are automatically scaled depending on the values ​​entered by the user.

Next we create a variable, redDot, which refers to the line object representing the red dot on the graph (we again use a comma for this). The *plt.plot([0], [H0], 'ro')* function creates a point on the plot with coordinates *[0, H0]*, and the **'ro'** parameter specifies the use of red ('r') for the points and the shape 'o' (round) to display each point.
