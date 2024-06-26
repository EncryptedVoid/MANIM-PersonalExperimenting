from manim import *

class ln_xexp2_plus1(Scene):
    def construct(self):
        # Title
        title = Text("Integral of $x \\cdot \\ln(x^2 + 1) \\ dx$")
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Integral expression
        integral = MathTex("\\int x \\cdot \\ln(x^2 + 1) \\, dx")
        self.play(Write(integral))
        self.wait(2)
        self.play(integral.animate.to_edge(UP))

        # Integration by parts
        parts = VGroup(
            MathTex("u = \\ln(x^2 + 1)"),
            MathTex("dv = x \\, dx")
        ).arrange(DOWN)
        self.play(Write(parts))
        self.wait(2)

        # Derivatives
        derivatives = VGroup(
            MathTex("du = \\frac{2x}{x^2 + 1} \\, dx"),
            MathTex("v = \\frac{x^2}{2}")
        ).arrange(DOWN)
        self.play(Transform(parts, derivatives))
        self.wait(2)

        # Integration by parts formula
        formula = VGroup(
            MathTex("\\int x \\cdot \\ln(x^2 + 1) \\, dx = "),
            MathTex("\\frac{x^2}{2} \\cdot \\ln(x^2 + 1) - "),
            MathTex("\\int \\frac{x^2}{2} \\cdot \\frac{2x}{x^2 + 1} \\, dx")
        ).arrange(DOWN)
        self.play(Transform(parts, formula))
        self.wait(2)

        # Simplifying the integral
        simplified = MathTex(
            "\\int \\frac{x^2}{2} \\cdot \\frac{2x}{x^2 + 1} \\, dx = ",
            "\\int \\frac{x^3}{x^2 + 1} \\, dx"
        )
        self.play(Transform(parts, simplified))
        self.wait(2)

        # Substitution
        substitution = VGroup(
            MathTex("u = x^2 + 1"),
            MathTex("du = 2x \\, dx")
        ).arrange(DOWN)
        self.play(Transform(parts, substitution))
        self.wait(2)

        # Integral after substitution
        integral_sub = MathTex(
            "\\int \\frac{(u-1) du}{2} = ",
            "\\frac{1}{2} \\left( \\int u \\, du - \\int 1 \\, du \\right)"
        )
        self.play(Transform(parts, integral_sub))
        self.wait(2)

        # Result of the integral
        result = VGroup(
            MathTex("= \\frac{1}{2} \\left( \\frac{u^2}{2} - u \\right) + C"),
            MathTex("= \\frac{1}{2} \\left( \\frac{(x^2 + 1)^2}{2} - (x^2 + 1) \\right) + C"),
            MathTex("= \\frac{1}{4} (x^2 + 1)^2 - \\frac{1}{2} (x^2 + 1) + C")
        ).arrange(DOWN)
        self.play(Transform(parts, result))
        self.wait(2)

        # Complete solution
        complete_solution = MathTex(
            "\\int x \\cdot \\ln(x^2 + 1) \\, dx = ",
            "\\frac{x^2}{2} \\cdot \\ln(x^2 + 1) - \\left( \\frac{1}{4} (x^2 + 1)^2 - \\frac{1}{2} (x^2 + 1) \\right) + C"
        )
        self.play(Transform(parts, complete_solution))
        self.wait(2)
        self.play(parts.animate.to_edge(DOWN))

        self.wait(5)
