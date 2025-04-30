from manim import *


class CompilerOverview(Scene):
    def construct(self):
        # Title
        title = Text("How a Compiler Works", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Source Code
        source_code = MathTex(r"\text{int } a \text{ = 5;}").scale(2).to_edge(DOWN)
        self.play(Write(source_code))
        self.wait(1)

        # Lexical Analysis (Tokenization)
        lexer_title = Text("Lexical Analysis", font_size=24).next_to(title, DOWN)
        self.play(Write(lexer_title))
        tokens = (
            VGroup(*[Tex(t) for t in ["int", "a", "=", "5", ";"]])
            .arrange(buff=1)
            .next_to(lexer_title, DOWN)
        )
        token_texts = [
            tokens[i].animate.set_color(colors[i]) for i in range(len(tokens))
        ]
        self.play(*token_texts, run_time=2)
        self.wait(1)

        # Parsing (Building a Parse Tree)
        parser_title = Text("Parsing", font_size=24).next_to(lexer_title, DOWN)
        self.play(Write(parser_title))
        parse_tree = (
            VGroup(Tex("Parse Tree:"), Tex("{"), Tex("|"), Tex("int a 5 ;"))
            .arrange(DOWN)
            .next_to(parser_title, DOWN)
        )

        # Animate the tree structure with arrows
        self.play(Write(parse_tree[0]), Write(parse_tree[1]))
        brace = Brace(parse_tree[2:], UP)
        label = (
            MathTex("Root", color=WHITE)
            .set_color_by_tex("Root", GREEN)
            .scale(0.75)
            .next_to(brace, UP)
        )
        self.play(GrowFromCenter(brace), Write(label))
        self.wait(1)

        # Code Generation (Turning Parse Tree into Machine Instructions)
        code_gen_title = Text("Code Generation", font_size=24).next_to(
            parser_title, DOWN
        )
        self.play(Write(code_gen_title))
        machine_code = (
            MathTex(r"\text{LOAD } 5 \text{ INTO } a")
            .scale(1.5)
            .next_to(code_gen_title, DOWN)
        )
        self.play(Write(machine_code))
        self.wait(2)

        # Final cleanup and scene end
        self.play(
            FadeOut(
                VGroup(
                    title,
                    lexer_title,
                    parser_title,
                    code_gen_title,
                    source_code,
                    tokens,
                    parse_tree,
                    brace,
                    label,
                    machine_code,
                )
            )
        )
