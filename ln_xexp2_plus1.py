from manim import *

class ln_xexp2_plus1(Scene):
    def construct(self):
        # Display the integral to solve
        integral = MathTex(r"\int x \cdot \ln(x^2 + 1) \, dx")
        self.play(Write(integral))
        self.wait(2)
        
        # Move the integral to the top
        self.play(integral.animate.to_edge(UP))
        
        # Display the parts of integration by parts
        parts = MathTex(r"u = \ln(x^2 + 1)", r"dv = x \, dx")
        parts.arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(parts))
        self.wait(2)
        
        # Display du and v
        du_v = MathTex(r"du = \frac{2x}{x^2 + 1} \, dx", r"v = \frac{x^2}{2}")
        du_v.arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(du_v))
        self.wait(2)
        
        # Show the integration by parts formula
        formula = MathTex(r"\int u \, dv = uv - \int v \, du")
        self.play(Write(formula))
        self.wait(2)
        
        # Apply the formula
        applied = MathTex(
            r"\int x \ln(x^2 + 1) \, dx = \left( \ln(x^2 + 1) \cdot \frac{x^2}{2} \right) - \int \left( \frac{x^2}{2} \cdot \frac{2x}{x^2 + 1} \right) \, dx"
        )
        self.play(Write(applied))
        self.wait(4)
        
        # Simplify the integral on the right-hand side
        simplify = MathTex(
            r"\int \frac{x^3}{x^2 + 1} \, dx"
        )
        self.play(Write(simplify))
        self.wait(2)
        
        # Further breakdown
        breakdown = MathTex(
            r"\frac{x^3}{x^2 + 1} = x - \frac{x}{x^2 + 1}"
        )
        self.play(Write(breakdown))
        self.wait(2)
        
        # Evaluate separate integrals
        separate = MathTex(
            r"\int x \, dx = \frac{x^2}{2}", r"\int \frac{x}{x^2 + 1} \, dx = \frac{1}{2} \ln |x^2 + 1|"
        )
        separate.arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(separate))
        self.wait(2)
        
        # Show the final solution
        final_solution = MathTex(
            r"\int x \ln(x^2 + 1) \, dx = \frac{x^2}{2} \ln(x^2 + 1) - \frac{x^2}{2} + \frac{1}{2} \ln |x^2 + 1| + C"
        )
        self.play(Write(final_solution))
        self.wait(4)
        
        self.play(FadeOut(Group(integral, parts, du_v, formula, applied, simplify, breakdown, separate, final_solution)))

        # End of the scene
        self.wait(2)

# To generate the animation, use the following command in your terminal:
# manim -pql <this_script_file_name>.py IntegralByParts
