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

        # Integration by parts steps
        steps = [
            (r"u = \ln(x^2 + 1)", RED),
            (r"dv = x \, dx", RED),
            (r"du = \frac{2x}{x^2 + 1} \, dx", MAROON),
            (r"v = \frac{x^2}{2}", MAROON),
            (r"\int x \cdot \ln(x^2 + 1) \,", TEAL),
            (r"dx = \frac{x^2}{2} \cdot \ln(x^2 + 1)", TEAL),
            (r"- \int \frac{x^2}{2} \cdot \frac{2x}{x^2 + 1} \, dx", TEAL),
            (r"= \frac{x^2}{2} \cdot \ln(x^2 + 1)", TEAL),
            (r"- \int \frac{x^3}{x^2 + 1} \, dx", TEAL),
            (r"u = x^2 + 1", BLUE),
            (r"du = 2x \, dx", BLUE),
            (r"\int \frac{x^3}{x^2 + 1} \,", PURPLE),
            (r"dx = \frac{1}{2} \int (u - 1) \, du", PURPLE),
            (r"= \frac{1}{2} \left( \int u \, du - \int 1 \, du \right)", PURPLE),
            (r"= \frac{1}{2} \left( \frac{u^2}{2} - u \right) + C", PINK),
            (r"= \frac{1}{2} \left( \frac{(x^2 + 1)^2}{2} - (x^2 + 1) \right) + C", PINK),
            (r"= \frac{1}{4} (x^2 + 1)^2 - \frac{1}{2} (x^2 + 1) + C", GREEN)
        ]

        shift = 2
        step_objs = []
        for i, (tex, color) in enumerate(steps):
            step = MathTex(tex).set_color(color)
            self.play(Write(step))
            self.play(step.animate.shift(UP * (2 - 1.35 * (i % 5))))
            step_objs.append(step)
            
            if i % 5 == 4 or i == len(steps) - 1:
                self.wait(0.5)
                if i >= 4:
                    self.play(*[FadeOut(step_objs[j]) for j in range(i - 4, i + 1)])

        # Complete solution
        complete_solution = MathTex(
            r"\int x \cdot \ln(x^2 + 1) \, dx = ",
            r"\frac{x^2}{2} \cdot \ln(x^2 + 1) - \left( \frac{1}{4} (x^2 + 1)^2 - \frac{1}{2} (x^2 + 1) \right) + C"
        ).set_color(GOLD)
        self.play(Write(complete_solution))
        self.wait(2)
        self.play(complete_solution.animate.to_edge(DOWN))

        self.wait(5)
