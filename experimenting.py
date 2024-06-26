from manim import *

class IntegralVisualization(Scene):
    def construct(self):
        title = Tex(r"Evaluate $\int \frac{\sin^2(x)}{(1 + \cos(x))^2} \, dx$")
        title.to_edge(UP)
        title.set_color(RED)

        self.play(Write(title))
        self.wait(2)

        steps = [
            (r"\sin^2(x) = 1 - \cos^2(x)", BLUE),
            (r"\int \frac{1 - \cos^2(x)}{(1 + \cos(x))^2} \, dx", GREEN),
            (r"\frac{1 - \cos^2(x)}{(1 + \cos(x))^2} = \frac{(1 + \cos(x))(1 - \cos(x))}{(1 + \cos(x))^2} = \frac{1 - \cos(x)}{1 + \cos(x)}", ORANGE),
            (r"u = 1 + \cos(x), \, du = -\sin(x) \, dx", YELLOW),
            (r"\int \frac{1 - \cos(x)}{1 + \cos(x)} \, dx = \int \frac{1 - (u - 1)}{u} (-du)", PURPLE),
            (r"\int \left(\frac{2}{u} - 1\right) (-du) = -2 \int \frac{1}{u} \, du + \int du", PINK),
            (r"-2 \ln|u| + u + C", TEAL),
            (r"-2 \ln|1 + \cos(x)| + (1 + \cos(x)) + C", MAROON)
        ]
        
        previous_step = title
        for step, color in steps:
            step_tex = MathTex(step)
            step_tex.set_color(color)
            self.play(Write(step_tex))
            self.wait(2)
            step_tex.next_to(previous_step, DOWN, buff=0.5)
            self.play(step_tex.animate.shift(DOWN))
            previous_step = step_tex

        final_result = MathTex(r"\int \frac{\sin^2(x)}{(1 + \cos(x))^2} \, dx = -2 \ln|1 + \cos(x)| + (1 + \cos(x)) + C")
        final_result.set_color(GOLD)
        final_result.next_to(previous_step, DOWN, buff=0.5)
        self.play(Write(final_result))
        self.wait(2)
        self.play(final_result.animate.shift(DOWN))

        self.wait(2)
