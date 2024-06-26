from manim import *

class sin2arcsinx(Scene):
    def construct(self):
        # Title
        title = Tex(r"Evaluate the integral $\int \sin(2\arcsin(x)) \, dx$").scale(0.9)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Step 1: Substitution
        step1 = Tex(r"Step 1: Let $u = \arcsin(x)$").scale(0.8)
        step1.next_to(title, DOWN, buff=0.5)
        substitution = Tex(r"Then $x = \sin(u)$ and $dx = \cos(u) \, du$").scale(0.8).set_color(BLUE)
        substitution.next_to(step1, DOWN, buff=0.5)
        self.play(Write(step1))
        self.wait(1)
        self.play(Write(substitution))
        self.wait(2)
        self.play(FadeOut(step1), FadeOut(substitution))

        # Step 2: Rewrite the integral
        step2 = Tex(r"Step 2: Rewrite the integral").scale(0.8)
        step2.next_to(title, DOWN, buff=0.5)
        integral_rewrite = Tex(r"$\int \sin(2\arcsin(x)) \, dx = \int \sin(2u) \cos(u) \, du$").scale(0.8).set_color(GREEN)
        integral_rewrite.next_to(step2, DOWN, buff=0.5)
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(integral_rewrite))
        self.wait(2)
        self.play(FadeOut(step2), FadeOut(integral_rewrite))

        # Step 3: Apply double-angle identity
        step3 = Tex(r"Step 3: Apply $\sin(2u) = 2\sin(u)\cos(u)$").scale(0.8)
        step3.next_to(title, DOWN, buff=0.5)
        double_angle_identity = Tex(r"$\int \sin(2u) \cos(u) \, du = \int 2\sin(u)\cos^2(u) \, du$").scale(0.8).set_color(ORANGE)
        double_angle_identity.next_to(step3, DOWN, buff=0.5)
        self.play(Write(step3))
        self.wait(1)
        self.play(Write(double_angle_identity))
        self.wait(2)
        self.play(FadeOut(step3), FadeOut(double_angle_identity))

        # Step 4: Substitute trigonometric values
        step4 = Tex(r"Step 4: Substitute trigonometric values").scale(0.8)
        step4.next_to(title, DOWN, buff=0.5)
        trig_substitution = Tex(r"Since $\sin(u) = x$ and $\cos(u) = \sqrt{1 - x^2}$, we get").scale(0.8)
        trig_substitution.next_to(step4, DOWN, buff=0.5)
        trig_values = Tex(r"$\cos^2(u) = 1 - x^2$").scale(0.8).set_color(PURPLE)
        trig_values.next_to(trig_substitution, DOWN, buff=0.5)
        integral_substitution = Tex(r"$\int 2\sin(u)\cos^2(u) \, du = \int 2x(1 - x^2) \, dx$").scale(0.8).set_color(PURPLE)
        integral_substitution.next_to(trig_values, DOWN, buff=0.5)
        self.play(Write(step4))
        self.wait(1)
        self.play(Write(trig_substitution))
        self.wait(1)
        self.play(Write(trig_values))
        self.wait(1)
        self.play(Write(integral_substitution))
        self.wait(2)
        self.play(FadeOut(step4), FadeOut(trig_substitution), FadeOut(trig_values), FadeOut(integral_substitution))

        # Step 5: Simplify the integral
        step5 = Tex(r"Step 5: Simplify the integral").scale(0.8)
        step5.next_to(title, DOWN, buff=0.5)
        integral_simplify = Tex(r"$\int 2x(1 - x^2) \, dx = \int 2x \, dx - \int 2x^3 \, dx$").scale(0.8).set_color(RED)
        integral_simplify.next_to(step5, DOWN, buff=0.5)
        self.play(Write(step5))
        self.wait(1)
        self.play(Write(integral_simplify))
        self.wait(2)
        self.play(FadeOut(step5), FadeOut(integral_simplify))

        # Step 6: Integrate each term
        step6 = Tex(r"Step 6: Integrate each term").scale(0.8)
        step6.next_to(title, DOWN, buff=0.5)
        integral1 = Tex(r"$\int 2x \, dx = x^2$").scale(0.8).set_color(YELLOW)
        integral1.next_to(step6, DOWN, buff=0.5)
        integral2 = Tex(r"$\int 2x^3 \, dx = \frac{x^4}{2}$").scale(0.8).set_color(YELLOW)
        integral2.next_to(integral1, DOWN, buff=0.5)
        self.play(Write(step6))
        self.wait(1)
        self.play(Write(integral1))
        self.wait(1)
        self.play(Write(integral2))
        self.wait(2)
        self.play(FadeOut(step6), FadeOut(integral1), FadeOut(integral2))

        # Step 7: Combine results
        step7 = Tex(r"Step 7: Combine results").scale(0.8)
        step7.next_to(title, DOWN, buff=0.5)
        combined_result = Tex(r"$x^2 - \frac{x^4}{2} + C$").scale(0.8).set_color(TEAL)
        combined_result.next_to(step7, DOWN, buff=0.5)
        self.play(Write(step7))
        self.wait(1)
        self.play(Write(combined_result))
        self.wait(2)
        self.play(FadeOut(step7), FadeOut(combined_result))

        # Final Result
        final_result = Tex(r"Therefore, $\int \sin(2\arcsin(x)) \, dx = x^2 - \frac{x^4}{2} + C$").scale(0.9).set_color(GOLD)
        final_result.next_to(title, DOWN, buff=1)
        self.play(Write(final_result))
        self.wait(2)

        # End scene
        self.play(FadeOut(final_result), FadeOut(title))
        self.wait(1)
