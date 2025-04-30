from manim import *

config.frame_height = 8.0  # Set the height of the frame in units
config.frame_width = 14.0  # Set the width of the frame in units
config.pixel_height = 1080  # Set the height of the exported video in pixels
config.pixel_width = 1920   # Set the width of the exported video in pixels

class SinProductIntegral(Scene):
    def construct(self):
        # Display the integral
        integral = MathTex(r"\int \sin(5x) \sin(3x) \, dx")
        self.play(Write(integral))
        self.wait(2)

        # Move the integral to the top
        self.play(integral.animate.to_edge(UP))

        # Step-by-step solution
        steps = [
            MathTex(r"\text{Use product-to-sum identities:}").shift(DOWN * 0.5),
            MathTex(r"\sin(A) \sin(B) = \frac{1}{2} [\cos(A - B) - \cos(A + B)]").shift(DOWN * 1.0),
            MathTex(r"A = 5x, \, B = 3x").shift(DOWN * 1.5),
            MathTex(r"\sin(5x) \sin(3x) = \frac{1}{2} [\cos(2x) - \cos(8x)]").shift(DOWN * 2.0),
            MathTex(r"\int \sin(5x) \sin(3x) \, dx = \int \frac{1}{2} [\cos(2x) - \cos(8x)] \, dx").shift(DOWN * 2.5),
            MathTex(r"= \frac{1}{2} \int \cos(2x) \, dx - \frac{1}{2} \int \cos(8x) \, dx").shift(DOWN * 3.0),
            MathTex(r"= \frac{1}{2} \cdot \frac{\sin(2x)}{2} - \frac{1}{2} \cdot \frac{\sin(8x)}{8}").shift(DOWN * 3.5),
            MathTex(r"= \frac{1}{4} \sin(2x) - \frac{1}{16} \sin(8x) + C").shift(DOWN * 4.0),
        ]

        for step in steps:
            self.play(Write(step))
            self.wait(2)
            self.play(FadeOut(step))

        # Show final result
        final_result = MathTex(r"\int \sin(5x) \sin(3x) \, dx = \frac{1}{4} \sin(2x) - \frac{1}{16} \sin(8x) + C")
        self.play(Write(final_result))
        self.wait(3)
