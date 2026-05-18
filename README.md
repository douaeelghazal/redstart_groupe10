# Redstart: A Lightweight Reusable Booster

![Redstart](public/images/redstart.png)

A computational project for modeling and controlling a reusable rocket booster during landing, inspired by SpaceX's Falcon Heavy boosters. Built with [Marimo](https://marimo.io) interactive notebooks.

## Overview

Redstart simulates a 2D rigid-body booster with an orientable thruster at its base. The project walks through the full control design pipeline:

1. **Physics modeling** — equations of motion, force decomposition, moment of inertia, ODE vector field
2. **Simulation** — numerical integration, freefall tests, open-loop controlled landing
3. **Visualization** — 2D booster drawing and animated trajectories
4. **Control design** — linearization, stability analysis, controllability, lateral dynamics
5. **Controller synthesis** — manual tuning, pole assignment, and LQR optimal control
6. **Validation** — closed-loop testing on the full nonlinear model

## Notebooks

| Notebook | Topics |
|---|---|
| `notebook-day-1.py` | Physical model, simulation, visualization, basic landing controller |
| `notebook-day-2.py` | Equilibria, linearized model, stability, pole assignment, LQR, validation |
| `notebook-day-3.py` | Extended control analysis, admissible paths, geometric interpretation |

## Model

The booster is modeled as a uniform rigid rod of length $\ell = 2\,\text{m}$ and mass $M = 1\,\text{kg}$ in 2D space. Its state is described by:

- $(x, y)$ — center of mass position
- $\theta$ — tilt angle from vertical (positive = left tilt)
- An orientable thruster producing force $f \geq 0$ at angle $\phi$ from the booster axis

Gravity is $g = 1\,\text{m/s}^2$ (simplified toy model).

## Getting Started

Install [pixi](https://prefix.dev) if you don't have it, then run:

```
pixi run dev
```

This opens Marimo in edit mode. Select a notebook file to start.

## Requirements

Managed automatically by pixi:

- Python
- NumPy
- SciPy
- Matplotlib
- Marimo ≥ 0.20
