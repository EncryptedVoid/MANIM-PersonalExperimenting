from manim import *

class CostanOverCos2(Scene):
    def construct(self):

        steps = [
            MathTex(r"\text{Let } u = \tan(x)").set_color(RED), 
            MathTex(r"du = \sec^2(x) \, dx").set_color(RED),
            MathTex(r"\cos^2(x) = \frac{1}{1 + u^2}").set_color(RED),

            MathTex(r"dx = \frac{du}{1 + u^2}").set_color(MAROON),
            MathTex(r"\int \frac{\cos(u)}{\cos^2(x)} \cdot \frac{du}{1 + u^2}").set_color(MAROON),
            MathTex(r"= \int \cos(u) \cdot (1 + u^2) \, du").set_color(MAROON),

            MathTex(r"= \int \cos(u) \, du").set_color(TEAL),
            MathTex(r"+ \int u^2 \cos(u) \, du").set_color(TEAL),

            MathTex(r"= \sin(u)").set_color(BLUE),
            MathTex(r"+ \int u^2 \cos(u) \, du").set_color(BLUE),

            MathTex(r"\text{Integration by parts}").set_color(BLUE),

            MathTex(r"= \sin(u) + u^2 \sin(u)").set_color(BLUE),
            MathTex(r"- \int 2u \sin(u) \, du").set_color(BLUE),

            MathTex(r"= \sin(u) + u^2 \sin(u)").set_color(PURPLE),
            MathTex(r"- (-2u \cos(u) + 2 \sin(u))").set_color(PURPLE),

            MathTex(r"= \sin(u) + u^2 \sin(u)").set_color(PINK),
            MathTex(r"+ 2u \cos(u) - 2 \sin(u)").set_color(PINK),

            MathTex(r"\text{Substitute back }").set_color(GREEN),
            MathTex(r"u = \tan(x)").set_color(GREEN)
        ]

        # Display the integral
        integral = MathTex(r"\int \frac{\cos(\tan(x))}{\cos^2(x)} \, dx").set_color(GOLD)
        self.play(Write(integral))
        self.play(integral.animate.shift(UP * 3))

        # Step-by-step solution
        shift = 2
        for i in range(0, len(steps)):

            if (i%5 == 0):
                shift = 2
                self.play(FadeOut(steps[i-5]))
                self.play(FadeOut(steps[i-4]))
                self.play(FadeOut(steps[i-3]))
                self.play(FadeOut(steps[i-2]))
                self.play(FadeOut(steps[i-1]))
             
            self.play(Write(steps[i]))
            self.play(steps[i].animate.shift(UP * shift))
            shift -= 1.35
            i += 1

        self.play(FadeOut(steps[len(steps)-4]))
        self.play(FadeOut(steps[len(steps)-3]))
        self.play(FadeOut(steps[len(steps)-2]))
        self.play(FadeOut(steps[len(steps)-1]))  

        # Show final result
        final = [
            MathTex(r"= \sin(\tan(x))").set_color(GOLD),
            MathTex(r"+ \tan^2(x) \sin(\tan(x))").set_color(GOLD),
            MathTex(r"+ 2 \tan(x) \cos(\tan(x))").set_color(GOLD),
            MathTex(r"- 2 \sin(\tan(x)) + C").set_color(GOLD)
        ]

        self.play(Write(final[0]))
        self.play(final[0].animate.shift(UP * 2))
        
        self.play(Write(final[1]))
        self.play(final[1].animate.shift(UP * 1))
        
        self.play(Write(final[2]))

        self.play(Write(final[3]))
        self.play(final[3].animate.shift(UP * -1))
