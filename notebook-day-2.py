import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, scipy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return animate_transform, svg, transform


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4], 
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )    
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),                
                )
            )
        ],
        justify="space-around"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center() 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Equilibrium conditions:
    \[
    \dot{x}=\dot{y}=\dot{\theta}=0,
    \qquad
    \ddot{x}=\ddot{y}=\ddot{\theta}=0
    \]

    Using the equations of motion:
    \[
    M\ddot{x}=-f\sin(\theta+\phi)=0
    \]
    \[
    M\ddot{y}=f\cos(\theta+\phi)-Mg=0
    \]
    \[
    J\ddot{\theta}=-f\frac{\ell}{2}\sin\phi=0
    \]

    Since \(f>0\) and \(\ell>0\),
    \[
    \sin\phi=0
    \]
    and with \(|\phi|<\frac{\pi}{2}\),
    \[
    \phi_e=0.
    \]

    Then,
    \[
    -f\sin\theta=0
    \]
    gives
    \[
    \theta_e=0
    \]
    (using \(|\theta|<\frac{\pi}{2}\)).

    Finally,
    \[
    f\cos(0)=Mg
    \]
    so
    \[
    f_e=Mg.
    \]

    Hence the equilibria are
    \[
    \boxed{
    (x_e,0,y_e,0,0,0),
    \qquad (x_e,y_e)\in\mathbb{R}^2
    }
    \]
    with equilibrium inputs
    \[
    \boxed{
    f_e=Mg,
    \qquad
    \phi_e=0.
    }
    \]extbf{Equilibrium conditions:}
    \[
    \dot{x}=\dot{y}=\dot{\theta}=0,
    \qquad
    \ddot{x}=\ddot{y}=\ddot{\theta}=0
    \]

    Using the equations of motion:
    \[
    M\ddot{x}=-f\sin(\theta+\phi)=0
    \]
    \[
    M\ddot{y}=f\cos(\theta+\phi)-Mg=0
    \]
    \[
    J\ddot{\theta}=-f\frac{\ell}{2}\sin\phi=0
    \]

    Since \(f>0\) and \(\ell>0\),
    \[
    \sin\phi=0
    \]
    and with \(|\phi|<\frac{\pi}{2}\),
    \[
    \phi_e=0.
    \]

    Then,
    \[
    -f\sin\theta=0
    \]
    gives
    \[
    \theta_e=0
    \]
    (using \(|\theta|<\frac{\pi}{2}\)).

    Finally,
    \[
    f\cos(0)=Mg
    \]
    so
    \[
    f_e=Mg.
    \]

    Hence the equilibria are
    \[
    \boxed{
    (x_e,0,y_e,0,0,0),
    \qquad (x_e,y_e)\in\mathbb{R}^2
    }
    \]
    with equilibrium inputs
    \[
    \boxed{
    f_e=Mg,
    \qquad
    \phi_e=0.
    }
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We introduce perturbation variables around the equilibrium:

    \[
    \cos(\theta+\phi)\approx 1
    \]

    The translational dynamics become:

    \[
    M\ddot{x}
    =
    -(Mg+\Delta f)(\Delta\theta+\Delta\phi)
    \]

    Neglecting second-order terms:

    \[
    M\ddot{x}\approx -Mg(\Delta\theta+\Delta\phi)
    \]

    thus:

    \[
    \ddot{x}=-g(\Delta\theta+\Delta\phi)
    \]

    For the vertical motion:

    \[
    M\ddot{y}=Mg+\Delta f-Mg
    \]

    hence:

    \[
    \ddot{y}=\frac{\Delta f}{M}
    \]

    The rotational dynamics become:

    \[
    J\ddot{\theta}
    =
    -(Mg)\frac{\ell}{2}\Delta\phi
    \]

    therefore:

    \[
    \ddot{\theta}
    =
    -\frac{Mg\ell}{2J}\Delta\phi
    \]

    Using:

    \[
    J=\frac{M\ell^2}{12}
    \]

    we obtain:

    \[
    \ddot{\theta}
    =
    -\frac{6g}{\ell}\Delta\phi
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The state vector:

    \[
    X=
    \begin{bmatrix}
    \Delta x \\
    \Delta\dot{x} \\
    \Delta y \\
    \Delta\dot{y} \\
    \Delta\theta \\
    \Delta\dot{\theta}
    \end{bmatrix}
    \]

    and the input vector:

    \[
    U=
    \begin{bmatrix}
    \Delta f \\
    \Delta\phi
    \end{bmatrix}
    \]

    The system can be written in standard state-space form:

    \[
    \dot{X}=AX+BU
    \]

    with:

    \[
    A=
    \begin{bmatrix}
    0&1&0&0&0&0\\
    0&0&0&0&-g&0\\
    0&0&0&1&0&0\\
    0&0&0&0&0&0\\
    0&0&0&0&0&1\\
    0&0&0&0&0&0
    \end{bmatrix}
    \]

    and:

    \[
    B=
    \begin{bmatrix}
    0&0\\
    0&-g\\
    0&0\\
    1/M&0\\
    0&0\\
    0&-6g/\ell
    \end{bmatrix}
    \]
    """)
    return


@app.cell
def _(J, M, g, l, np):
    def AB_matrices(M, g, l, J):
        A = np.array([
            [0, 1,   0, 0,  0,           0],
            [0, 0,   0, 0,  -g,          0],
            [0, 0,   0, 1,  0,           0],
            [0, 0,   0, 0,  0,           0],
            [0, 0,   0, 0,  0,           1],
            [0, 0,   0, 0,  0,           0],
        ], dtype=float)

        B = np.array([
            [0,      0          ],
            [0,      -g         ],
            [0,      0          ],
            [1/M,    0          ],
            [0,      0          ],
            [0,      -M*g*l/(2*J)],
        ], dtype=float)

        return A, B

    A, B = AB_matrices(M, g, l, J)
    print("A =\n", A)
    print("B =\n", B)
    return A, B


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To study the stability of the equilibrium, we compute the eigenvalues of the matrix \(A\).

    The eigenvalues are the solutions of:

    \[
    \det(A-\lambda I)=0
    \]

    The system matrix is:

    \[
    A=
    \begin{bmatrix}
    0&1&0&0&0&0\\
    0&0&0&0&-1&0\\
    0&0&0&1&0&0\\
    0&0&0&0&0&0\\
    0&0&0&0&0&1\\
    0&0&0&0&0&0
    \end{bmatrix}
    \]

    Thus:

    \[
    A-\lambda I=
    \begin{bmatrix}
    -\lambda&1&0&0&0&0\\
    0&-\lambda&0&0&-1&0\\
    0&0&-\lambda&1&0&0\\
    0&0&0&-\lambda&0&0\\
    0&0&0&0&-\lambda&1\\
    0&0&0&0&0&-\lambda
    \end{bmatrix}
    \]

    Since this matrix is upper triangular, its determinant is the product of its diagonal terms:

    \[
    \det(A-\lambda I)=(-\lambda)^6
    \]

    Therefore:

    \[
    (-\lambda)^6=0
    \]

    which gives:

    \[
    \lambda=0
    \]

    with multiplicity 6.

    Hence, all eigenvalues are equal to zero:

    \[
    \boxed{
    \lambda_1=\lambda_2=\cdots=\lambda_6=0
    }
    \]

    Consequently, the equilibrium is not asymptotically stable.
    """)
    return


@app.cell
def _(A, np):
    eigenvalues = np.linalg.eigvals(A)
    print("Eigenvalues:", eigenvalues)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To determine whether the linearized system is controllable, we compute the controllability matrix:

    \[
    \mathcal C
    =
    [B \ AB \ A^2B \ \dots \ A^{n-1}B]
    \]

    The system matrices are:

    \[
    A=
    \begin{bmatrix}
    0&1&0&0&0&0\\
    0&0&0&0&-1&0\\
    0&0&0&1&0&0\\
    0&0&0&0&0&0\\
    0&0&0&0&0&1\\
    0&0&0&0&0&0
    \end{bmatrix}
    \]

    and

    \[
    B=
    \begin{bmatrix}
    0&0\\
    0&-1\\
    0&0\\
    1&0\\
    0&0\\
    0&-3
    \end{bmatrix}
    \]

    We first compute:

    \[
    AB=
    \begin{bmatrix}
    0&-1\\
    0&0\\
    1&0\\
    0&0\\
    0&-3\\
    0&0
    \end{bmatrix}
    \]

    Then:

    \[
    A^2B=
    \begin{bmatrix}
    0&0\\
    0&3\\
    0&0\\
    0&0\\
    0&0\\
    0&0
    \end{bmatrix}
    \]

    The controllability matrix becomes:

    \[
    \mathcal C
    =
    \left[
    \begin{array}{cccccc}
    0&0&0&-1&0&0\\
    0&-1&0&0&0&3\\
    0&0&1&0&0&0\\
    1&0&0&0&0&0\\
    0&0&0&-3&0&0\\
    0&-3&0&0&0&0
    \end{array}
    \right]
    \]

    We observe that the columns are linearly independent. Therefore:

    \[
    \text{rank}(\mathcal C)=6
    \]

    Since the rank is equal to the dimension of the state vector (\(n=6\)), the system is completely controllable.

    \[
    \boxed{
    \text{The linearized system is controllable.}
    }
    \]
    """)
    return


@app.cell
def _(A, B, np):
    def controllability_matrix(A, B):
        n = A.shape[0]
        blocks = [np.linalg.matrix_power(A, k) @ B for k in range(n)]
        return np.hstack(blocks)

    C = controllability_matrix(A, B)
    rank = np.linalg.matrix_rank(C)
    print(f"Controllability matrix shape: {C.shape}")
    print(f"Rank: {rank}")
    print(f"State space dimension: {A.shape[0]}")
    print(f"Controllable: {rank == A.shape[0]}")
    return (controllability_matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We restrict the study to the lateral motion variables:

    \[
    X=
    \begin{bmatrix}
    x \\
    \dot{x} \\
    \theta \\
    \dot{\theta}
    \end{bmatrix}
    \]

    The thrust magnitude is fixed to

    \[
    f = Mg
    \]

    and the only control input is

    \[
    u=\phi
    \]

    Using the small-angle approximation:

    \[
    \sin(\theta+\phi)\approx \theta+\phi
    \]

    the lateral dynamics become

    \[
    \ddot{x}=-(\theta+\phi)
    \]

    and the rotational dynamics are

    \[
    \ddot{\theta}=-3\phi
    \]

    The reduced system can therefore be written in state-space form:

    \[
    \dot{X}=AX+Bu
    \]

    with

    \[
    A=
    \begin{bmatrix}
    0&1&0&0\\
    0&0&-1&0\\
    0&0&0&1\\
    0&0&0&0
    \end{bmatrix}
    \]

    and

    \[
    B=
    \begin{bmatrix}
    0\\
    -1\\
    0\\
    -3
    \end{bmatrix}
    \]



    The controllability matrix is defined by

    \[
    \mathcal{C}
    =
    \begin{bmatrix}
    B & AB & A^2B & A^3B
    \end{bmatrix}
    \]

    First, we compute:

    \[
    AB=
    \begin{bmatrix}
    -1\\
    0\\
    -3\\
    0
    \end{bmatrix}
    \]

    \[
    A^2B=
    \begin{bmatrix}
    0\\
    3\\
    0\\
    0
    \end{bmatrix}
    \]

    \[
    A^3B=
    \begin{bmatrix}
    3\\
    0\\
    0\\
    0
    \end{bmatrix}
    \]

    Thus,

    \[
    \mathcal{C}
    =
    \begin{bmatrix}
    0 & -1 & 0 & 3\\
    -1 & 0 & 3 & 0\\
    0 & -3 & 0 & 0\\
    -3 & 0 & 0 & 0
    \end{bmatrix}
    \]

    The rank of the controllability matrix is

    \[
    \mathrm{rank}(\mathcal{C})=4
    \]

    Since the rank equals the dimension of the state vector, the reduced system is fully controllable.

    Therefore, the single control input \(\phi\) is sufficient to control:

    \[
    x,\quad \dot{x},\quad \theta,\quad \dot{\theta}
    \]
    """)
    return


@app.cell
def _(A, B, controllability_matrix, np):
    # Extract lateral subsystem from full A, B
    lat_idx = [0, 1, 4, 5]   # rows/cols for x, vx, theta, omega

    A_lat = A[np.ix_(lat_idx, lat_idx)]
    B_lat = B[lat_idx, 1:2]  # column 1 = Delta phi input

    print("A_lat =\n", A_lat)
    print("B_lat =\n", B_lat)
    C_lat = controllability_matrix(A_lat, B_lat)
    rank_lat = np.linalg.matrix_rank(C_lat)
    print(f"Rank: {rank_lat}")
    print(f"Controllable: {rank_lat == A_lat.shape[0]}")
    return (A_lat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Linearized Model

    The nonlinear lateral dynamics are
    \[
    M\ddot{x}=-f\sin(\theta+\phi),
    \qquad
    J\ddot{\theta}=-f\frac{\ell}{2}\sin\phi.
    \]

    We linearize around the equilibrium
    \[
    \theta=0,
    \qquad
    \phi=0,
    \qquad
    f=Mg,
    \]
    using the small-angle approximations
    \[
    \sin(\theta+\phi)\approx \Delta\theta+\Delta\phi,
    \qquad
    \sin\phi\approx \Delta\phi.
    \]

    The linearized equations become
    \[
    \Delta\ddot{x}
    =
    -g(\Delta\theta+\Delta\phi),
    \qquad
    \Delta\ddot{\theta}
    =
    -\frac{Mg\ell}{2J}\Delta\phi.
    \]

    Defining the state
    \[
    s=
    \begin{pmatrix}
    \Delta x \\
    \Delta\dot{x} \\
    \Delta\theta \\
    \Delta\dot{\theta}
    \end{pmatrix},
    \]
    the system can be written as
    \[
    \dot{s}=As+B\Delta\phi,
    \]
    with
    \[
    A=
    \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix},
    \qquad
    B=
    \begin{bmatrix}
    0 \\
    -g \\
    0 \\
    -\dfrac{Mg\ell}{2J}
    \end{bmatrix}.
    \]

    For
    \[
    g=1,
    \qquad
    M=1,
    \qquad
    \ell=2,
    \qquad
    J=\frac{M\ell^2}{12}=\frac13,
    \]
    we obtain
    \[
    \frac{Mg\ell}{2J}=3.
    \]


    ## Free Evolution (\(\Delta\phi=0\))

    With no control input,
    \[
    \Delta\ddot{\theta}=0.
    \]

    Using the initial conditions
    \[
    \Delta\theta(0)=\frac{\pi}{4},
    \qquad
    \Delta\dot{\theta}(0)=0,
    \]
    we obtain
    \[
    \Delta\theta(t)=\frac{\pi}{4}.
    \]

    Then
    \[
    \Delta\ddot{x}
    =
    -g\,\Delta\theta
    =
    -\frac{\pi}{4},
    \]
    which is constant. Integrating twice with
    \[
    \Delta x(0)=0,
    \qquad
    \Delta\dot{x}(0)=0,
    \]
    gives
    \[
    \boxed{
    \Delta\theta(t)=\frac{\pi}{4},
    \qquad
    \Delta x(t)=-\frac{\pi}{8}t^2
    }.
    \]

    Thus, the tilt angle remains constant while the horizontal position diverges quadratically with time.
    """)
    return


@app.cell
def _(g, np, plt, scipy):
    # Linearized lateral dynamics matrix (phi = 0, f = Mg)
    # state: [Δx, Δvx, Δθ, Δω]
    A1 = np.array([
        [0, 1,  0, 0],
        [0, 0, -g, 0],
        [0, 0,  0, 1],
        [0, 0,  0, 0],
    ])

    print("A =\n", A1)
    print("Eigenvalues of A:", np.linalg.eigvals(A1))

    # Initial conditions: x=0, vx=0, theta=pi/4, omega=0
    s0 = np.array([0.0, 0.0, np.pi / 4, 0.0])

    # Numerical solution via matrix exponential s(t) = exp(A*t) @ s0
    t = np.linspace(0, 30, 3000)
    x_num     = np.array([scipy.linalg.expm(A1 * ti) @ s0 for ti in t])[:, 0]
    theta_num = np.array([scipy.linalg.expm(A1 * ti) @ s0 for ti in t])[:, 2]

    # Analytical solution
    x_ana     = -(g * np.pi / 8) * t**2
    theta_ana = np.full_like(t, np.pi / 4)

    # Plots
    fig, axes = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

    axes[0].plot(t, x_num, color="steelblue", lw=2, label="numerical $e^{At}s_0$")
    axes[0].plot(t, x_ana, color="orange",    lw=2, ls="--", label=r"analytical $-\frac{\pi}{8}t^2$")
    axes[0].set_ylabel(r"$\Delta x(t)$ (m)", fontsize=13)
    axes[0].set_title(r"Linearized free evolution — $\phi(t)=0$, $\theta(0)=\pi/4$", fontsize=13)
    axes[0].legend(fontsize=11)
    axes[0].grid(True, alpha=0.4)

    axes[1].plot(t, theta_num, color="tomato",  lw=2, label=r"numerical $\Delta\theta(t)$")
    axes[1].plot(t, theta_ana, color="purple",  lw=2, ls="--", label=r"analytical $\pi/4$")
    axes[1].axhline(np.pi/2,  color="grey", ls=":", lw=1, label=r"$\pm\pi/2$ validity limit")
    axes[1].axhline(-np.pi/2, color="grey", ls=":", lw=1)
    axes[1].set_ylabel(r"$\Delta\theta(t)$ (rad)", fontsize=13)
    axes[1].set_xlabel("time $t$ (s)", fontsize=13)
    axes[1].legend(fontsize=11)
    axes[1].grid(True, alpha=0.4)

    plt.tight_layout()
    plt.savefig("linearized_free_dynamics.png", dpi=150)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Interpretation and Stability Analysis

     What the Graphs Show

    The angle trajectory
    \[
    \theta(t)
    \]
    is a horizontal line at
    \[
    \frac{\pi}{4},
    \]
    showing that the tilt remains constant over time.

    The position trajectory
    \[
    x(t)
    \]
    is a downward-opening parabola:
    \[
    x(t)=-\frac{\pi}{8}t^2,
    \]
    which diverges to
    \[
    -\infty.
    \]

    The numerical simulation and analytical solution overlap perfectly, validating the model and computations.


    ## Stability Analysis

    The characteristic polynomial of the system matrix \(A\) is
    \[
    \lambda^4=0,
    \]
    so all four eigenvalues are
    \[
    \lambda_1=\lambda_2=\lambda_3=\lambda_4=0.
    \]

    Since \(A\) contains a non-trivial Jordan block,
    \[
    e^{At}
    \]
    grows polynomially with time. Therefore, the equilibrium is unstable.


    ## Physical Interpretation

    With
    \[
    \phi=0,
    \]
    the reactor produces no corrective torque, so any initial tilt persists indefinitely.

    This constant tilt permanently misaligns the thrust vector, creating a constant horizontal acceleration:
    \[
    \Delta\ddot{x}
    =
    -g\,\Delta\theta(0).
    \]

    As a result, the booster drifts sideways without bound. The system behaves like an inverted pendulum without restoring force, showing that active feedback through \(\phi\) is necessary for stabilization.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Thought Process

    With
    \[
    f = Mg
    \]
    fixed, the lateral subsystem has state
    \[
    s_{\text{lat}}
    =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}.
    \]

    The control law is
    \[
    \Delta \phi = -K s_{\text{lat}},
    \]
    with
    \[
    K = [\,0,\;0,\;k_3,\;k_4\,].
    \]

    Thus, the controller only feeds back \(\theta\) and \(\dot{\theta}\), so the \(\theta\)-subsystem is autonomous:
    \[
    J \ddot{\theta}
    =
    -\frac{f\ell}{2}\Delta \phi
    =
    Mg \cdot \frac{\ell}{2}
    \left(
    k_3 \Delta \theta
    +
    k_4 \Delta \dot{\theta}
    \right).
    \]

    With
    \[
    M = g = 1,
    \qquad
    \ell = 2,
    \qquad
    J = \frac{M\ell^2}{12} = \frac{1}{3},
    \]
    this simplifies to
    \[
    \ddot{\theta}
    =
    3\left(
    k_3 \Delta \theta
    +
    k_4 \Delta \dot{\theta}
    \right).
    \]

    The closed-loop characteristic polynomial for \(\theta\) is therefore
    \[
    s^2 - 3k_4 s - 3k_3 = 0.
    \]

    For asymptotic stability of \(\theta\), we require
    \[
    k_3 < 0
    \qquad \text{and} \qquad
    k_4 < 0.
    \]

    The constraint
    \[
    |\Delta \phi(0)| < \frac{\pi}{2}
    \]
    imposes
    \[
    |k_3 \theta(0)|
    =
    k_3 \cdot \frac{\pi}{4}
    <
    \frac{\pi}{2}
    \quad \Longrightarrow \quad
    |k_3| < 2.
    \]

    We iterate guesses, simulating the linearized system each time.
    """)
    return


@app.cell
def _(A_lat, J, M, g, l, np):
    # Δφ column of B: [0, -g, 0, -Mgl/2J] = [0, -1, 0, -3]
    b_lat = np.array([0.0, -g, 0.0, -M * g * l / (2 * J)], dtype=float)

    def simulate_lateral(A, b_col, K, s0=None, t_span=(0, 30), dt=0.01):
        A     = np.asarray(A,     dtype=float)
        b_col = np.asarray(b_col, dtype=float).flatten()
        K     = np.asarray(K,     dtype=float).flatten()

        if s0 is None:
            s0 = np.array([0.0, 0.0, 45 / 180 * np.pi, 0.0])

        t   = np.arange(t_span[0], t_span[1], dt)
        s   = np.zeros((len(t), 4))
        phi = np.zeros(len(t))
        s[0] = s0

        for i in range(len(t) - 1):
            dphi     = -(K @ s[i])
            s[i + 1] = s[i] + dt * (A @ s[i] + b_col * dphi)
            phi[i]   = dphi

        phi[-1] = phi[-2]
        return t, s, phi


    def check(K, label):
        t, s, phi = simulate_lateral(A_lat, b_lat, K)
        theta = s[:, 2]

        print(f"\n{label}: K = {K}")
        print(f"  max|Δθ| = {np.max(np.abs(theta)):.3f} rad  (limit π/2 = {np.pi/2:.3f})")
        print(f"  max|Δφ| = {np.max(np.abs(phi)):.3f} rad  (limit π/2 = {np.pi/2:.3f})")

        above  = np.where(np.abs(theta) > 0.05)[0]
        settle = t[above[-1]] if len(above) > 0 else 0.0
        print(f"  settling time (|Δθ|<0.05) ≈ {settle:.1f} s")

        ok = (
            np.max(np.abs(theta)) < np.pi / 2 and
            np.max(np.abs(phi))   < np.pi / 2 and
            settle <= 20
        )
        return t, s, phi


    # k3 < 0, k4 < 0  (stability), |k3| < 2  (φ constraint)
    K1 = np.array([0.0, 0.0, -0.10, -0.30])
    K2 = np.array([0.0, 0.0, -0.30, -0.80])
    K3 = np.array([0.0, 0.0, -0.50, -1.20])
    K4 = np.array([0.0, 0.0, -0.15, -0.65])

    for Ki, label in [
        (K1, "Guess 1"),
        (K2, "Guess 2"),
        (K3, "Guess 3"),
        (K4, "Final")
    ]:
        check(Ki, label)
    return b_lat, simulate_lateral


@app.cell
def _(A_lat, b_lat, np, plt, simulate_lateral):
    K_final = np.array([0.0, 0.0, -0.15, -0.65])
    t1, s, phi = simulate_lateral(A_lat, b_lat, K_final)

    fig1, axes1 = plt.subplots(2, 1, figsize=(9, 9), sharex=True)

    axes1[0].plot(t1, s[:, 2], label=r"$\Delta\theta(t)$")
    axes1[0].axhline( np.pi/2, color="grey", ls="--", label=r"$\pm\pi/2$")
    axes1[0].axhline(-np.pi/2, color="grey", ls="--")
    axes1[0].axhline(0, color="black", lw=0.5)
    axes1[0].set_ylabel("rad"); axes1[0].legend(); axes1[0].grid(True)
    axes1[0].set_title(r"Final controller $K=[0,\,0,\,-0.15,\,-0.65]$: tilt $\Delta\theta(t)$")

    axes1[1].plot(t1, phi, color="tab:orange", label=r"$\Delta\phi(t)$")
    axes1[1].axhline( np.pi/2, color="grey", ls="--", label=r"$\pm\pi/2$")
    axes1[1].axhline(-np.pi/2, color="grey", ls="--")
    axes1[1].axhline(0, color="black", lw=0.5)
    axes1[1].set_ylabel("rad"); axes1[1].set_xlabel("time $t$ (s)")
    axes1[1].legend(); axes1[1].grid(True)
    axes1[1].set_title(r"Control input $\Delta\phi(t)$")

    plt.tight_layout()
    plt.savefig("controller_manual.png", dpi=150)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    \[
    K = [0,\; 0,\; -0.15,\; -0.65]
    \]

    The two non-zero gains were found by reasoning on the decoupled $\theta$-dynamics:

    $k_3 = -0.15$: proportional gain on $\Delta \theta$. Kept small so that:
    \[
    |\Delta \phi(0)| = |k_3| \cdot \frac{\pi}{4} \ll \frac{\pi}{2}
    \]

    $k_4 = -0.65$: derivative gain on $\Delta \dot{\theta}$. Provides damping and controls the settling speed.

    The $\theta$-subsystem poles are:
    \[
    s = -0.2675 \quad \text{and} \quad s = -1.6825
    \]

    These poles have negative real parts, hence $\theta$ converges.

    However, the full closed-loop system has two eigenvalues at $0$, corresponding to $x$ and $\dot{x}$ (which are not controlled by $K$). Therefore:

    The closed-loop system is \textbf{stable but NOT asymptotically stable}:
    - $\Delta \theta(t) \to 0$ (converges to zero within approximately $11\,\text{s}$)
    - $\Delta x(t)$ may drift

    ---

    Full asymptotic stability requires the complete gain matrix $K_{pp}$ obtained via pole placement (next question).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The reduced lateral dynamics are

    \[
    \dot X = AX + B \Delta \phi
    \]

    with

    \[
    X =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot x \\
    \Delta \theta \\
    \Delta \dot \theta
    \end{bmatrix}
    \]

    \[
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -1 & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix},
    \qquad
    B =
    \begin{bmatrix}
    0 \\
    -1 \\
    0 \\
    -3
    \end{bmatrix}
    \]

    We use the state feedback law

    \[
    \Delta \phi = -K_{pp} X
    \]

    and choose the desired poles

    \[
    \{-0.25,\,-0.30,\,-0.35,\,-0.40\}
    \]

    because poles with real parts around \(-0.2\) give a settling time approximately equal to

    \[
    T_s \approx \frac{4}{0.2} = 20 \text{ s}
    \]

    Using pole placement,

    \[
    K_{pp} = \mathrm{place}(A,B,\text{poles})
    \]

    gives

    \[
    K_{pp} =
    \begin{bmatrix}
    -0.00357 &
    -0.02655 &
    -0.21310 &
    -0.43333
    \end{bmatrix}
    \]

    The closed-loop matrix is

    \[
    A_{cl} = A - BK_{pp}
    \]

    whose eigenvalues are exactly

    \[
    \{-0.25,\,-0.30,\,-0.35,\,-0.40\}
    \]

    Therefore, the closed-loop system is asymptotically stable and satisfies

    \[
    \Delta x(t) \to 0,
    \qquad
    \Delta \theta(t) \to 0
    \]

    in approximately \(20\) seconds.
    """)
    return


@app.cell
def _(np, plt):
    from scipy.signal import place_poles
    from scipy.integrate import solve_ivp


    A2 = np.array([
        [0, 1,  0, 0],
        [0, 0, -1, 0],
        [0, 0,  0, 1],
        [0, 0,  0, 0]
    ])

    B2 = np.array([
        [0],
        [-1],
        [0],
        [-3]
    ])


    # DESIRED POLES


    desired_poles = [-0.25, -0.30, -0.35, -0.40]

    Kpp = place_poles(A2, B2, desired_poles).gain_matrix

    print(Kpp)
    print("Kpp =")
    print(Kpp)


    # CLOSED-LOOP MATRIX


    Acl = A2 - B2 @ Kpp

    print("\nClosed-loop eigenvalues:")
    print(np.linalg.eigvals(Acl))


    # CLOSED-LOOP DYNAMICS


    def closed_loop_dynamics(time, X):

        # control law
        dphi = -(Kpp @ X).item()

        # state derivative
        dX = A2 @ X + B2.flatten() * dphi

        return dX

    # INITIAL CONDITIONS


    X0 = np.array([
        0.0,          # Δx(0)
        0.0,          # Δx_dot(0)
        np.pi / 4,    # Δtheta(0)
        0.0           # Δtheta_dot(0)
    ])


    # SIMULATION


    t0 = 0
    tf = 30

    time = np.linspace(t0, tf, 3000)

    solution = solve_ivp(
        closed_loop_dynamics,
        [t0, tf],
        X0,
        t_eval=time
    )


    # EXTRACT STATES


    x = solution.y[0]
    vx = solution.y[1]
    theta = solution.y[2]
    omega = solution.y[3]

    # control input
    phi1 = np.array([
        -(Kpp @ solution.y[:, i]).item()
        for i in range(len(time))
    ])


    # PLOTS


    plt.figure(figsize=(10, 20))


    # Δx(t)


    plt.subplot(3,1,1)

    plt.plot(time, x, linewidth=2)

    plt.grid(True)

    plt.ylabel(r'$\Delta x(t)$')

    plt.title("Pole Placement Controller")


    # Δθ(t)


    plt.subplot(3,1,2)

    plt.plot(time, theta, linewidth=2)

    plt.axhline(np.pi/2, color='red', linestyle='--')
    plt.axhline(-np.pi/2, color='red', linestyle='--')

    plt.grid(True)

    plt.ylabel(r'$\Delta \theta(t)$')


    # Δφ(t)


    plt.subplot(3,1,3)

    plt.plot(time, phi1, linewidth=2)

    plt.axhline(np.pi/2, color='red', linestyle='--')
    plt.axhline(-np.pi/2, color='red', linestyle='--')

    plt.grid(True)

    plt.ylabel(r'$\Delta \phi(t)$')

    plt.xlabel("Time (s)")

    plt.tight_layout()

    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


if __name__ == "__main__":
    app.run()
