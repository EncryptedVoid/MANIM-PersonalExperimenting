# Manim Mathematical Animations

![Manim Logo](https://raw.githubusercontent.com/ManimCommunity/manim/main/logo/cropped.png)

## Project Overview

This repository contains a collection of mathematical animations created using Manim (Mathematical Animation Engine). These scripts visualize complex calculus concepts, particularly integral solutions, providing step-by-step visual explanations of mathematical processes.

## About Manim

[Manim](https://www.manim.community/) is an animation engine for explanatory math videos, designed originally by Grant Sanderson (3Blue1Brown). It uses Python to create precise animations that help explain mathematical concepts visually.

## Animations

### 1. Integral of x·ln(x² + 1)

`ln_xexp2_plus1.py` demonstrates the step-by-step solution of the integral:

$$\int x \cdot \ln(x^2 + 1) \, dx$$

Using integration by parts and substitution techniques, the animation breaks down the solution process with color-coded steps, making it easier to follow the mathematical reasoning.

### 2. Product of Sine Functions

`sin_product_integral.py` visualizes the solution to:

$$\int \sin(5x) \sin(3x) \, dx$$

This animation demonstrates the product-to-sum identity for trigonometric functions and shows how to apply it to solve the integral.

### 3. Sine of Double Arcsine

`sin2arcsinx.py` walks through the evaluation of:

$$\int \sin(2\arcsin(x)) \, dx$$

The animation demonstrates the substitution technique, double-angle identity for sine, and simplification steps to arrive at the final solution.

### 4. Sine Over Square Root of Cosine

`test.py` illustrates the solution to:

$$\int \frac{\sin(x)}{\sqrt{\cos(x)}} \, dx$$

This animation uses the substitution method to transform the integral into a simpler form before evaluating it.

### 5. Cosine of Tangent Over Cosine Squared

`costan_over_cos2.py` shows the solution for:

$$\int \frac{\cos(\tan(x))}{\cos^2(x)} \, dx$$

This more complex integral requires multiple techniques, including substitution and integration by parts, all visualized in a step-by-step manner.

## Features

- **Step-by-Step Visualization**: Each animation breaks down complex mathematical processes into understandable steps
- **Color-Coded Elements**: Different parts of equations are color-coded to help viewers track transformations
- **Animated Transitions**: Smooth transitions between steps create an intuitive flow
- **Mathematical Rigor**: All solutions follow proper calculus techniques and identities

## Running the Animations

### Prerequisites

- Python 3.7+
- Manim Community Edition
- LaTeX distribution (like TeX Live or MiKTeX)

### Installation

```bash
pip install manim
```

### Rendering an Animation

To render any of the animations:

```bash
manim -pql <script_name>.py <class_name>
```

For example:

```bash
manim -pql sin_product_integral.py SinProductIntegral
```

Parameters:
- `-p`: Plays the animation after rendering
- `-q`: Quality (l for low, m for medium, h for high)
- `-l`: Low quality (faster rendering)

## Customization

Each animation can be customized by modifying:

- Colors of mathematical elements
- Timing of transitions
- Text explanations
- Animation effects

## Learning Resources

If you're interested in learning more about Manim:

- [Manim Community Documentation](https://docs.manim.community/en/stable/)
- [Manim Community Examples](https://docs.manim.community/en/stable/examples.html)
- [3Blue1Brown YouTube Channel](https://www.youtube.com/c/3blue1brown)

## Future Enhancements

Potential improvements for these animations:

- Adding narration or text explanations
- Creating interactive elements
- Implementing more advanced animation techniques
- Building a comprehensive library of calculus concepts

## Acknowledgments

- Grant Sanderson (3Blue1Brown) for creating Manim
- The Manim Community for maintaining and improving the library
- Mathematical educators who inspire clear explanations of complex concepts