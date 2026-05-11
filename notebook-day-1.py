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

    return np, plt, sci


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():

    g = 1.0      #m/s²
    M = 1.0      #kg
    l = 2.0      #m
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(np):
    def force_components(f, theta, phi):
        fx = -f * np.sin(theta + phi)
        fy =  f * np.cos(theta + phi)
        return fx, fy


    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On considère la force de poussée exercée par le moteur sur le booster.

    Cette force est de norme $f$ et est dirigée selon l'axe du moteur, qui peut être incliné d'un angle $\phi$ par rapport à l'axe du booster.

    Le booster lui-même est orienté d'un angle $\theta$ dans le repère inertiel.

    Ainsi, l'orientation absolue de la force dans le repère fixe est :

    $$
    \alpha = \theta + \phi
    $$



    Dans le repère orthonormé $(\vec{e}_x, \vec{e}_y)$, on projette le vecteur force :

    - composante horizontale (axe $x$)
    - composante verticale (axe $y$)

    La force s'écrit alors :

    $$
    \vec{F} = \begin{pmatrix} f_x \\ f_y \end{pmatrix}
    $$



    En utilisant la trigonométrie dans le plan :

    $$
    f_x = -f \sin(\theta + \phi)
    $$

    $$
    f_y =  f \cos(\theta + \phi)
    $$



    ## Justification du signe

    Le signe négatif dans $f_x$ provient du choix de convention :

    - $\theta$ est mesuré positivement dans le sens trigonométrique
    - la projection sur l'axe $x$ dépend de l'orientation du repère
    - la décomposition respecte la rotation du vecteur force dans le plan



    $$
    \boxed{f_x = -f \sin(\theta + \phi)}
    $$

    $$
    \boxed{f_y =  f \cos(\theta + \phi)}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell
def _(np):
    def center_of_mass_dynamics(M, f, theta, phi, g):

        ax = -f * np.sin(theta + phi) / M
        ay =  f * np.cos(theta + phi) / M - g
        return ax, ay

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    \[
    \text{En appliquant la deuxième loi de Newton : } M\vec{a} = \vec{F}
    \]

    \[
    \text{Les forces appliquées sont la poussée du moteur et la gravité.}
    \]

    \[
    \text{Composante horizontale :}
    \quad \ddot{x}(t) = \frac{-f \sin(\theta + \phi)}{M}
    \]

    \[
    \text{Composante verticale :}
    \quad \ddot{y}(t) = \frac{f \cos(\theta + \phi)}{M} - g
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell
def _(M, l):

    #Moment d'inertie (tige mince uniforme autour de son centre)
    J = (1/12) * M * l**2

    print(f"Moment d'inertie J = {J} kg·m²")
    print(f"J = {J:.4f} kg·m²")

    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Moment d'inertie d'une tige uniforme de longueur $\ell$ autour de son centre**

    On part de la définition générale du moment d'inertie :

    $$J = \int r^2 \, dm$$

    La tige est uniforme, donc sa densité linéique vaut :

    $$\lambda = \frac{M}{\ell}$$

    Ainsi :

    $$dm = \lambda \, dx = \frac{M}{\ell} \, dx$$

    L'axe de rotation passe par le centre, donc la distance d'un élément $dm$ à l'axe est $|x|$, où $x$ varie de $-\ell/2$ à $\ell/2$ :

    $$J = \int_{-\ell/2}^{\ell/2} x^2 \cdot \frac{M}{\ell} \, dx$$

    $$J = \frac{M}{\ell} \int_{-\ell/2}^{\ell/2} x^2 \, dx$$

    $$\int_{-\ell/2}^{\ell/2} x^2 \, dx = \left[ \frac{x^3}{3} \right]_{-\ell/2}^{\ell/2} = \frac{(\ell/2)^3}{3} - \frac{(-\ell/2)^3}{3}$$

    $$= \frac{\ell^3/8}{3} + \frac{\ell^3/8}{3} = \frac{\ell^3}{12}$$

    $$J = \frac{M}{\ell} \times \frac{\ell^3}{12} = \frac{M \ell^2}{12}$$

    $$\boxed{J = \frac{1}{12} M \ell^2}$$

    **Application numérique** ($M = 1$ kg, $\ell = 2$ m) :

    $$J = \frac{1}{12} \cdot M \cdot \ell^2 = \frac{1}{12} \cdot 1 \cdot 2^2 = \frac{4}{12} = \frac{1}{3} \; \text{kg} \cdot \text{m}^2$$
    """)
    return


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
    En mécanique, le moment (scalaire) d'une force $\vec{F}$ appliquée au point $P$ par rapport au point $G$ est donné par :

    $$
    \boxed{\tau = (\overrightarrow{GP} \times \vec{F}) \cdot \vec{e}_z}
    $$

    En 2D, dans un repère orthonormé direct $(G, \vec{e}_x, \vec{e}_y, \vec{e}_z)$, cette expression devient :

    $$
    \tau = (GP)_x \, F_y - (GP)_y \, F_x \qquad \text{(forme scalaire)}
    $$



    On se place dans le **repère lié au booster** $R_b = (G, \vec{e}_x, \vec{e}_y)$ :

    - Origine : centre de masse $G$ du booster
    - $\vec{e}_y$ : axe du booster, orienté **vers le haut**
    - $\vec{e}_x$ : perpendiculaire à l'axe du booster, orienté **vers la droite**
    - $\vec{e}_z = \vec{e}_x \times \vec{e}_y$ : perpendiculaire au plan, sortant

    Ce repère est orthonormé direct et mobile (il tourne avec le booster).





    Le réacteur est situé à la **base** du booster, à une distance $\dfrac{\ell}{2}$ **sous** le centre de masse $G$.

    Dans $R_b$ :

    $$
    \boxed{\overrightarrow{GP} = \begin{pmatrix} 0 \\ -\dfrac{\ell}{2} \\ 0 \end{pmatrix}_{R_b}}
    $$


    La poussée a une intensité $f \geq 0$ et fait un angle $\phi$ par rapport à l'axe $\vec{e}_y$ du booster.

    Dans $R_b$ :

    $$
    \boxed{\vec{F} = \begin{pmatrix} f \sin\phi \\ f \cos\phi \\ 0 \end{pmatrix}_{R_b}}
    $$



    Appliquons la formule $\tau = r_x F_y - r_y F_x$ :

    $$
    \begin{aligned}
    \tau &= (0) \cdot (f \cos\phi) - \left(-\dfrac{\ell}{2}\right) \cdot (f \sin\phi) \\
         &= 0 + \dfrac{\ell}{2} \, f \sin\phi
    \end{aligned}
    $$

    $$
    \boxed{\tau = \dfrac{\ell}{2} \, f \sin\phi}
    $$

    **Interprétation du signe :**
    - $\phi > 0$ $\Rightarrow$ $\sin\phi > 0$ $\Rightarrow$ $\tau > 0$ $\Rightarrow$ rotation **anti-horaire** (sens trigonométrique)



    Dans le repère fixe galiléen, autour du centre de masse $G$ :

    $$
    J \, \ddot{\theta} = \sum \tau_{\text{ext}}
    $$

    Seule la poussée crée un couple (le poids s'applique en $G$, bras de levier nul).

    Donc :

    $$
    J \, \ddot{\theta} = \dfrac{\ell}{2} \, f \sin\phi
    $$

    $$
    \boxed{\ddot{\theta} = \dfrac{\ell}{2J} \, f \sin\phi}
    $$




    Le booster est modélisé comme une **tige mince uniforme** de masse $M$ et longueur $\ell$.

    Moment d'inertie par rapport au centre de masse :

    $$
    \boxed{J = \dfrac{1}{12} M \ell^2}
    $$



    En substituant $J$ :

    $$
    \begin{aligned}
    \ddot{\theta} &= \dfrac{\ell}{2 \cdot \dfrac{1}{12} M \ell^2} \, f \sin\phi \\[8pt]
                  &= \dfrac{\ell}{\dfrac{1}{6} M \ell^2} \, f \sin\phi \\[8pt]
                  &= \dfrac{6}{M \ell} \, f \sin\phi
    \end{aligned}
    $$

    $$
    \boxed{\ddot{\theta} = \dfrac{6}{M \ell} \, f \sin\phi}
    $$

    ---

    ##  Application numérique

    Données :
    $$
    M = 1\ \text{kg}, \qquad \ell = 2\ \text{m}, \qquad g = 1\ \text{m/s}^2
    $$

    Calcul :
    $$
    \frac{6}{M \ell} = \frac{6}{1 \times 2} = 3
    $$

    $$
    \boxed{\ddot{\theta} = 3 \, f \sin\phi}
    $$
    """)
    return


@app.cell
def _(J, M, l, np):
    def torque(f, phi, l=l):
        return 0.5 * l * f * np.sin(phi)


    def theta_ddot(f, phi, J=J, l=l):
        return torque(f, phi, l) / J


    def theta_ddot_simplified(f, phi, M=M, l=l):
        return (6.0 / (M * l)) * f * np.sin(phi)



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
    We model the booster motion in the 2D plane using the state vector:

    $$ s = (x, y, v_x, v_y, \theta, \omega) \in \mathbb{R}^6 $$

    where $x, y$ are the position of the center of mass, $v_x, v_y$ the linear velocities, $\theta$ the inclination angle, and $\omega = \dot{\theta}$ the angular velocity.

    The system is controlled by the thrust force $f$ and its orientation $\phi$.

    The dynamics are given by Newton's laws:

    $$ \dot{x} = v_x, \quad \dot{y} = v_y $$

    $$ \dot{v_x} = -\frac{f}{M}\sin(\theta+\phi), \quad \dot{v_y} = \frac{f}{M}\cos(\theta+\phi) - g $$

    $$ \dot{\theta} = \omega, \quad \dot{\omega} = \frac{\ell}{2J} f \sin(\phi) $$

    The system can be written in compact form:

    $$ \dot{s} = F(s, f, \phi) $$

    where $F$ is defined as:

    $$ F(s,f,\phi) = \begin{pmatrix} v_x \\ v_y \\ -\frac{f}{M}\sin(\theta+\phi) \\ \frac{f}{M}\cos(\theta+\phi) - g \\ \omega \\ \frac{\ell}{2J} f \sin(\phi) \end{pmatrix} $$
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


@app.cell
def _(J, M, g, l, np, sci):
    def redstart_solve(t_span, y0, f_phi):
        def dynamics(t, s):
            x, vx, y, vy, theta, omega = s
            f, phi = f_phi(t, s)

            ax = -f * np.sin(theta + phi) / M
            ay = (f * np.cos(theta + phi) / M) - g
            alpha = (l/2 * f * np.sin(phi)) / J

            return [vx, ax, vy, ay, omega, alpha]

    
        res = sci.solve_ivp(dynamics, t_span, y0, dense_output=True, method='RK45')
    
        return res.sol

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


@app.cell
def _(l, np, plt, redstart_solve):

    def free_fall_f_phi(t, s):
        return np.array([0.0, 0.0])

    t_span = (0, 6)

    y0 = [
        0.0,
        0.0,
        10.0,
        0.0,
        0.0,
        0.0
    ]

    sol = redstart_solve(t_span, y0, free_fall_f_phi)

    t = np.linspace(0, 6, 500)
    y_sol = sol(t)

    y = y_sol[2]

    plt.figure()

    plt.plot(t, y, label="y(t) center of mass")
    plt.axhline(l, linestyle="--", color="gray", label="y = ℓ = 2 m")
    plt.axvline(4, linestyle=":", color="red", label="t = 4 s (theoretical)")

    plt.xlabel("Time t (s)")
    plt.ylabel("Height y (m)")
    plt.title("Redstart Free Fall Verification")
    plt.grid()
    plt.legend()

    plt.show()
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
    mo.md(r"""
    We consider a purely vertical motion with:

    - $x = 0$
    - $\theta = 0$
    - $\phi = 0$ (thrust aligned with the vertical axis)

    The dynamics reduce to a 1D model:

    $$
    \begin{cases}
    \dot{y} = v_y \\[4pt]
    \dot{v}_y = \dfrac{f(t)}{M} - g
    \end{cases}
    $$

    with:

    $$
    M = 1,\qquad g = 1,\qquad f(t) \geq 0
    $$


    We impose:

    $$
    y(0) = 10,\qquad v_y(0) = -2
    $$

    $$
    y(5) = 1,\qquad v_y(5) = 0
    $$


    We seek a polynomial trajectory of degree 3:

    $$
    y(t) = a t^3 + b t^2 + c t + d
    $$

    Its derivative is:

    $$
    v_y(t) = \dot{y}(t) = 3a t^2 + 2b t + c
    $$


    **At $t = 0$:**

    $$
    d = 10,\qquad c = -2
    $$

    **At $t = 5$:**

    Position:

    $$
    125a + 25b + 5c + d = 1
    $$

    $$
    125a + 25b - 10 + 10 = 1
    $$

    $$
    125a + 25b = 1 \qquad (1)
    $$

    Velocity:

    $$
    75a + 10b + c = 0
    $$

    $$
    75a + 10b - 2 = 0
    $$

    $$
    75a + 10b = 2 \qquad (2)
    $$



    From equation (1):

    $$
    b = \frac{1 - 125a}{25}
    $$

    Substituting into (2):

    $$
    75a + 10 \cdot \frac{1 - 125a}{25} = 2
    $$

    $$
    75a + 0.4 - 50a = 2
    $$

    $$
    25a = 1.6
    $$

    $$
    a = 0.064
    $$

    Then:

    $$
    b = \frac{1 - 8}{25} = -0.28
    $$


    $$
    \boxed{y(t) = 0.064 t^3 - 0.28 t^2 - 2t + 10}
    $$

    $$
    \boxed{v_y(t) = 0.192 t^2 - 0.56 t - 2}
    $$


    The dynamic equation gives:

    $$
    \dot{v}_y = f(t) - g \quad \text{with } g = 1
    $$

    Therefore:

    $$
    f(t) = \dot{v}_y + 1
    $$

    Now:

    $$
    \dot{v}_y(t) = 0.384 t - 0.56
    $$

    Thus:

    $$
    \boxed{f(t) = 0.384 t + 0.44}
    $$
    """)
    return


@app.cell
def _(np, plt):

    from scipy.integrate import solve_ivp


    def controlled_landing_simulation():
    
        # Parameters
        M = 1.0
        g = 1.0
        l = 2.0

        # Control law (from analytical solution)
        def f_phi(t, y):
            f = 0.384 * t + 0.44
            phi = 0.0
            return np.array([f, phi])

        # Dynamics
        def dynamics(t, state):
            x, vx, y_pos, vy, theta, omega = state
            f, phi = f_phi(t, state)

            dxdt = vx
            dvxdt = -f * np.sin(theta + phi) / M
            dydt = vy
            dvydt = f * np.cos(theta + phi) / M - g
            dthetadt = omega
            domegadt = 3 * f * np.sin(phi)  # simplified model

            return [dxdt, dvxdt, dydt, dvydt, dthetadt, domegadt]

        # Initial conditions
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        # Time span
        t_span = (0.0, 5.0)
        t_eval = np.linspace(0, 5, 1000)

        # Solve
        sol = solve_ivp(dynamics, t_span, y0, t_eval=t_eval)

        # Extract
        t = sol.t
        y_pos = sol.y[2]
        vy = sol.y[3]
        f = 0.384 * t + 0.44

        # Plot
        plt.figure(figsize=(10, 8))

        plt.subplot(3, 1, 1)
        plt.plot(t, y_pos)
        plt.axhline(1, linestyle='--')
        plt.title("Controlled Landing")
        plt.ylabel("y(t)")
        plt.grid()

        plt.subplot(3, 1, 2)
        plt.plot(t, vy)
        plt.axhline(0, linestyle='--')
        plt.ylabel("vy(t)")
        plt.grid()

        plt.subplot(3, 1, 3)
        plt.plot(t, f)
        plt.ylabel("f(t)")
        plt.xlabel("t")
        plt.grid()

        plt.tight_layout()
        plt.show()

        # Verification
        print("y(5) =", y_pos[-1])
        print("vy(5) =", vy[-1])


        return sol


    controlled_landing_simulation()
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

    return


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
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


if __name__ == "__main__":
    app.run()
