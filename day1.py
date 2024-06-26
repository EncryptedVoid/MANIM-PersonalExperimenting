from manim import *

class IntegralOfTan(Scene):
    def construct(self):
        # Title
        title = Text("Integral of \\( \\sqrt{\\tan(x)} \\)", font_size=48, color=YELLOW)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        
        # # Graph of the function sqrt(tan(x))
        # graph_title = Text("Graph of \\( \\sqrt{\\tan(x)} \\)", font_size=36, color=BLUE).to_edge(UP)
        # self.play(Write(graph_title))

        # axes = Axes(
        #     x_range=[0, 2 * PI, PI / 4],
        #     y_range=[0, 5, 1],
        #     axis_config={"color": GREEN},
        #     x_length=10,
        #     y_length=6,
        # ).shift(DOWN)
        # labels = axes.get_axis_labels(x_label="x", y_label="y")

        # def func1(x):
        #     return np.sqrt(np.tan(x))

        # graph1 = axes.plot(func1, color=RED, x_range=[0, PI / 2 - 0.01])
        # graph2 = axes.plot(func1, color=RED, x_range=[PI / 2 + 0.01, 3 * PI / 2 - 0.01])
        # graph3 = axes.plot(func1, color=RED, x_range=[3 * PI / 2 + 0.01, 2 * PI])

        # graph_label = axes.get_graph_label(graph1, label="\\sqrt{\\tan(x)}", x_val=PI / 4, direction=UP / 2)

        # self.play(Create(axes), Create(graph1), Create(graph2), Create(graph3), Write(labels), Write(graph_label))
        # self.wait(2)
        # self.play(FadeOut(axes, graph1, graph2, graph3, labels, graph_label, graph_title))

        # Integral
        integral = MathTex("\\int \\sqrt{\\tan(x)} \\, dx", font_size=48).to_edge(UP)
        self.play(Write(integral))
        self.wait(2)

        # Step 1: Substitution
        step1 = Text("Step 1: Substitution", font_size=36, color=BLUE).next_to(integral, DOWN, buff=1)
        subst = MathTex("u = \\sqrt{\\tan(x)}", font_size=36).next_to(step1, DOWN, buff=0.5)
        subst_eq = MathTex("u^2 = \\tan(x)", font_size=36).next_to(subst, DOWN, buff=0.5)
        deriv = MathTex("\\frac{d}{dx}(u^2) = \\frac{d}{dx}(\\tan(x))", font_size=36).next_to(subst_eq, DOWN, buff=0.5)
        simpl = MathTex("2u \\frac{du}{dx} = \\sec^2(x)", font_size=36).next_to(deriv, DOWN, buff=0.5)
        rearr = MathTex("dx = \\frac{2u \\, du}{1 + u^4}", font_size=36).next_to(simpl, DOWN, buff=0.5)

        self.play(Write(step1))
        self.wait(1)
        self.play(Write(subst))
        self.wait(1)
        self.play(Write(subst_eq))
        self.wait(1)
        self.play(Write(deriv))
        self.wait(1)
        self.play(Write(simpl))
        self.wait(1)
        self.play(Write(rearr))
        self.wait(1)
        self.play(FadeOut(step1, subst, subst_eq, deriv, simpl, rearr))

        # Step 2: Substitute Back
        step2 = Text("Step 2: Substitute Back", font_size=36, color=BLUE).next_to(integral, DOWN, buff=1)
        integral2 = MathTex("\\int u \\cdot \\frac{2u \\, du}{1 + u^4}", font_size=36).next_to(step2, DOWN, buff=0.5)
        simpl2 = MathTex("\\int \\frac{2u^2}{1 + u^4} \\, du", font_size=36).next_to(integral2, DOWN, buff=0.5)

        self.play(Write(step2))
        self.wait(1)
        self.play(Write(integral2))
        self.wait(1)
        self.play(Write(simpl2))
        self.wait(1)
        self.play(FadeOut(step2, integral2, simpl2))

        # Step 3: Simplification
        step3 = Text("Step 3: Simplification", font_size=36, color=BLUE).next_to(integral, DOWN, buff=1)
        u2_v = MathTex("u^2 = v", font_size=36).next_to(step3, DOWN, buff=0.5)
        du2 = MathTex("2u \\, du = dv", font_size=36).next_to(u2_v, DOWN, buff=0.5)
        integral3 = MathTex("\\int \\frac{v}{1 + v^2} \\, dv", font_size=36).next_to(du2, DOWN, buff=0.5)

        self.play(Write(step3))
        self.wait(1)
        self.play(Write(u2_v))
        self.wait(1)
        self.play(Write(du2))
        self.wait(1)
        self.play(Write(integral3))
        self.wait(1)
        self.play(FadeOut(step3, u2_v, du2, integral3))

        # Step 4: Final Integration
        step4 = Text("Step 4: Final Integration", font_size=36, color=BLUE).next_to(integral, DOWN, buff=1)
        integral4 = MathTex("\\int \\frac{v}{1 + v^2} \\, dv", font_size=36).next_to(step4, DOWN, buff=0.5)
        subst4 = MathTex("w = 1 + v^2", font_size=36).next_to(integral4, DOWN, buff=0.5)
        dw = MathTex("dw = 2v \\, dv", font_size=36).next_to(subst4, DOWN, buff=0.5)
        integral5 = MathTex("\\frac{1}{2} \\int \\frac{dw}{w}", font_size=36).next_to(dw, DOWN, buff=0.5)
        ln = MathTex("\\frac{1}{2} \\ln |w| + C", font_size=36).next_to(integral5, DOWN, buff=0.5)
        final_subst = MathTex("= \\frac{1}{2} \\ln |1 + v^2| + C", font_size=36).next_to(ln, DOWN, buff=0.5)
        final_subst2 = MathTex("= \\frac{1}{2} \\ln |1 + \\tan^2(x)| + C", font_size=36).next_to(final_subst, DOWN, buff=0.5)

        self.play(Write(step4))
        self.wait(1)
        self.play(Write(integral4))
        self.wait(1)
        self.play(Write(subst4))
        self.wait(1)
        self.play(Write(dw))
        self.wait(1)
        self.play(Write(integral5))
        self.wait(1)
        self.play(Write(ln))
        self.wait(1)
        self.play(Write(final_subst))
        self.wait(1)
        self.play(Write(final_subst2))
        self.wait(1)

        # Display the final answer
        final_answer = MathTex("\\frac{1}{2} \\ln |1 + \\tan^2(x)| + C", font_size=48, color=GREEN).next_to(integral, DOWN, buff=1)
        self.play(FadeOut(step4, integral4, subst4, dw, integral5, ln, final_subst, final_subst2))
        self.play(Write(final_answer))
        self.wait(2)
