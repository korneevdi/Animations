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

We can also solve the system of equations for $x(t)$ and $y(t)$ a little differently, and then we get the dependence $y(x)$, that is, the equation for the projectile flight path:

$y(x) = H_0 + x\tan\alpha - \frac{gx^2}{2v_0^2\cos^2\alpha}$.

Now you can calculate the derivative $y'(x)$ of this function and equate it to zero to find the maximum height of the trajectory:

$y_{max} = H_0 + \frac{v_0^2\sin^2\alpha}{2g}$.

We need this value so that we can automatically adjust the size of the window in which the animation will be shown. So, now you can start programming!

## Code development
