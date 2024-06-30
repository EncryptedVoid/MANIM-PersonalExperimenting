from manim import *

class costan_over_cos2(Scene):
    def construct(self):
        # Display the integral
        integral = MathTex(r"\int \frac{\cos(\tan(x))}{\cos^2(x)} \, dx")
        self.play(Write(integral))
        self.wait(2)

        # Move the integral to the top
        self.play(integral.animate.to_edge(UP))

        # Step-by-step solution
        steps = [
            MathTex(r"\text{Let } u = \tan(x)"),
            MathTex(r"du = \sec^2(x) \, dx"),
            MathTex(r"\cos^2(x) = \frac{1}{1 + u^2}"),
            MathTex(r"dx = \frac{du}{1 + u^2}"),
            MathTex(r"\int \frac{\cos(u)}{\cos^2(x)} \cdot \frac{du}{1 + u^2}"),
            MathTex(r"= \int \cos(u) \cdot (1 + u^2) \, du"),
            MathTex(r"= \int \cos(u) \, du + \int u^2 \cos(u) \, du"),
            MathTex(r"= \sin(u) + \int u^2 \cos(u) \, du"),
            MathTex(r"\text{Integration by parts}"),
            MathTex(r"= \sin(u) + u^2 \sin(u) - \int 2u \sin(u) \, du"),
            MathTex(r"= \sin(u) + u^2 \sin(u) - (-2u \cos(u) + 2 \sin(u))"),
            MathTex(r"= \sin(u) + u^2 \sin(u) + 2u \cos(u) - 2 \sin(u)"),
            MathTex(r"\text{Substitute back } u = \tan(x)"),
        ]

        for step in steps:
            self.play(Write(step))
            self.wait(2)
            self.play(FadeOut(step))

        # Show final result
        finalResult1 = MathTex(r"= \sin(\tan(x)) + \tan^2(x) \sin(\tan(x))")
        finalResult2 = MathTex(r"+ 2 \tan(x) \cos(\tan(x)) - 2 \sin(\tan(x)) + C")

        self.play(Write(finalResult1))
        self.wait(3)

        finalResult1.shift(UP * 0.75)
        self.wait(3)

        self.play(Write(finalResult2))
        self.wait(3)

