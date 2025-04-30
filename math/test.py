from manim import *

class IntegralSolution(Scene):
    def construct(self):
        # Display the problem
        problem = MathTex(r"\int \frac{\sin(x)}{\sqrt{\cos(x)}} \, dx")
        self.play(Write(problem))
        self.wait(2)
        
        # Step 1: Substitution
        substitution = MathTex(r"u = \cos(x)")
        du_equation = MathTex(r"du = -\sin(x) \, dx", r"\Rightarrow -du = \sin(x) \, dx")
        self.play(Transform(problem, substitution))
        self.play(Write(du_equation[0]))
        self.wait(2)
        self.play(Write(du_equation[1]))
        self.wait(2)
        
        # Step 2: Rewrite the Integral
        rewrite_integral = MathTex(r"\int \frac{\sin(x)}{\sqrt{\cos(x)}} \, dx = \int \frac{-du}{\sqrt{u}}")
        self.play(FadeOut(substitution), FadeOut(du_equation))
        self.play(Transform(problem, rewrite_integral))
        self.wait(2)
        
        # Step 3: Simplify the Integral
        simplify_integral = MathTex(r"\int \frac{-du}{\sqrt{u}} = -\int u^{-\frac{1}{2}} \, du")
        self.play(Transform(problem, simplify_integral))
        self.wait(2)
        
        # Step 4: Integrate
        integrate = MathTex(r"-\int u^{-\frac{1}{2}} \, du = -\left( \frac{u^{\frac{1}{2}}}{\frac{1}{2}} \right) + C", r"= -2u^{\frac{1}{2}} + C")
        self.play(Transform(problem, integrate[0]))
        self.wait(2)
        self.play(Write(integrate[1]))
        self.wait(2)
        
        # Step 5: Substitute Back
        final_answer = MathTex(r"-2u^{\frac{1}{2}} + C = -2\sqrt{\cos(x)} + C")
        self.play(FadeOut(integrate), Transform(problem, final_answer))
        self.wait(2)
        
        # Show the final answer
        final_result = MathTex(r"\int \frac{\sin(x)}{\sqrt{\cos(x)}} \, dx = -2\sqrt{\cos(x)} + C")
        self.play(Transform(problem, final_result))
        self.wait(2)

