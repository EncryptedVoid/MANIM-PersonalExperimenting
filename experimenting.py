from manim import *
import random

class ConfettiEffect(VGroup):
    def __init__(self, n_confetti=50, **kwargs):
        super().__init__(**kwargs)
        colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, PINK, TEAL, GOLD, MAROON]
        for _ in range(n_confetti):
            confetti = Dot(color=random.choice(colors))
            confetti.move_to(np.array([random.uniform(-6, 6), random.uniform(-4, 4), 0]))
            confetti.scale(random.uniform(0.1, 0.3))
            self.add(confetti)

    def create_animation(self):
        animations = []
        for confetti in self:
            animation = confetti.animate.move_to(confetti.get_center() + np.array([random.uniform(-1, 1), random.uniform(-1, 1), 0])).rotate(random.uniform(0, 360))
            animations.append(animation)
        return animations

class IntegralVisualization(Scene):
    def construct(self):
        # Set the title
        title = Tex(r"Evaluate $\int \frac{\sin^2(x)}{(1 + \cos(x))^2} \, dx$")
        title.to_edge(UP)
        title.set_color(RED)
        self.play(Write(title))
        self.wait(1)

        # Define the steps and their colors
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

        previous_steps = []
        for i, (step, color) in enumerate(steps):
            step_tex = MathTex(step)
            step_tex.set_color(color)
            step_tex.next_to(title if i == 0 else previous_steps[-1], DOWN, buff=0.5)

            self.play(Write(step_tex))
            self.wait(2)

            previous_steps.append(step_tex)

            if len(previous_steps) > 3:
                self.play(FadeOut(previous_steps.pop(0)))
                for j, step in enumerate(previous_steps):
                    step.next_to(title, DOWN, buff=0.5 + j*1.5)
                    self.play(step.animate.shift(UP), run_time=0.5)

        final_result = MathTex(r"\int \frac{\sin^2(x)}{(1 + \cos(x))^2} \, dx = -2 \ln|1 + \cos(x)| + (1 + \cos(x)) + C")
        final_result.set_color(GOLD)
        final_result.next_to(previous_steps[-1], DOWN, buff=0.5)
        self.play(Write(final_result))
        self.wait(2)

        # Add the confetti effect at the end
        confetti = ConfettiEffect()
        self.add(confetti)
        self.play(*confetti.create_animation(), run_time=5)
        self.wait(2)

# Config settings for high-quality rendering
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 60
config.quality = "high_quality"
