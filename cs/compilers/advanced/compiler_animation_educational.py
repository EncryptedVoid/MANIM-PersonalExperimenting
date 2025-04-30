# compiler_animation_educational.py
from manim import *
import numpy as np
from compiler_animation_base import CompilerAnimationBase


class CompilerAnimationEducational(CompilerAnimationBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Educational connections between phases
        self.phase_connections = {
            (
                "preprocessor",
                "lexer",
            ): "With preprocessed code ready, we can now break it into meaningful tokens...",
            (
                "lexer",
                "parser",
            ): "These tokens serve as the building blocks for constructing the AST...",
            (
                "parser",
                "ir",
            ): "With a complete syntax tree, we can now translate to an architecture-independent form...",
            (
                "ir",
                "optimizer",
            ): "This intermediate representation allows for systematic optimizations...",
            (
                "optimizer",
                "codegen",
            ): "The optimized code now needs to be translated to target assembly...",
            (
                "codegen",
                "assembler",
            ): "Assembly code must be converted to binary machine instructions...",
            (
                "assembler",
                "linker",
            ): "Object files need to be combined with libraries to form a complete program...",
        }

        self.timing = {
            "brief": 0.5,  # Quick transitions
            "standard": 0.8,  # Standard animations
            "emphasis": 1.2,  # Important concepts
            "complex": 1.5,  # Complex transformations
            "wait_brief": 0.3,  # Short pauses
            "wait_std": 0.7,  # Standard pauses
            "wait_long": 1.2,  # Longer cognitive processing
        }

    def focus_attention(
        self, obj, highlight_color=None, duration=0.5, fade_others=False, opacity=0.2
    ):
        """
        Creates attentional focus on an object to guide viewer attention.

        Parameters:
            obj: The object to focus on
            highlight_color: Color to use for highlighting (defaults to highlight color)
            duration: Duration of the focusing animation
            fade_others: Whether to fade other objects
            opacity: Opacity for the highlighting effect
        """
        if highlight_color is None:
            highlight_color = self.colors["highlight"]

        # Create a highlight effect
        if isinstance(obj, (Mobject, VMobject)):
            highlight = SurroundingRectangle(
                obj,
                color=highlight_color,
                stroke_width=2,
                buff=0.15,
                fill_opacity=opacity,
                fill_color=highlight_color,
            )

            # Flash effect for attention
            self.play(FadeIn(highlight, rate_func=there_and_back), run_time=duration)

            return highlight
        return None

    def create_context_box(
        self,
        text,
        target_object,
        position_offset=RIGHT * 3,
        buff=0.3,
        max_width=4,
        font_size=16,
    ):
        """
        Creates an educational context box that explains a concept with clear visual connection.
        """
        # Create text with automatic wrapping for better readability
        text_obj = self.create_wrapped_text(text, max_width, font_size)

        # Create background for better visibility
        bg = SurroundingRectangle(
            text_obj, color=self.colors["sub_phase"], buff=buff, fill_opacity=0.1
        )

        # Group text and background
        group = VGroup(bg, text_obj)

        # Position relative to target
        if isinstance(position_offset, np.ndarray):
            group.move_to(target_object.get_center() + position_offset)
        else:
            group.next_to(target_object, position_offset, buff=buff)

        # Create connection line
        line = Line(
            target_object.get_center(),
            group.get_center(),
            stroke_width=1,
            color=self.colors["arrow"],
        )

        # Add little dot at target end for emphasis
        dot = Dot(line.get_start(), radius=0.03, color=self.colors["highlight"])

        return VGroup(group, line, dot)

    def educational_pause(self, duration_category="standard", pulse_object=None):
        """Strategic pauses with optional visual pulse to maintain attention"""
        duration = self.timing.get(f"wait_{duration_category}", 0.7)

        if pulse_object is not None:
            # Create subtle pulse effect during wait
            original_scale = pulse_object.scale
            self.play(
                pulse_object.animate.scale(1.05).set_opacity(0.9),
                rate_func=there_and_back,
                run_time=duration,
            )
        else:
            self.wait(duration)

    def visualize_ir_transformation(self, ast_obj, ir_code_obj):
        """Create a detailed visualization of AST to IR transformation"""

        # Create transformation stages
        stages = [
            "Analyze AST structure",
            "Convert to basic blocks",
            "Generate SSA form",
            "Apply target-independent optimizations",
        ]

        # Middle point between AST and IR
        midpoint = (ast_obj.get_center() + ir_code_obj.get_center()) / 2

        # Create transformation pipeline
        for i, stage in enumerate(stages):
            # Calculate position based on progression
            progress = (i + 1) / (len(stages) + 1)
            position = (
                ast_obj.get_center() * (1 - progress)
                + ir_code_obj.get_center() * progress
            )

            stage_id, stage_obj = self.create_element(
                "text",
                stage,
                size=16,
                position=position + DOWN * 1.5,
                color=self.colors["sub_phase"],
            )

            # Show conversion step
            step_arrow_id, step_arrow = self.create_element(
                "arrow", "", color=self.colors["arrow"], position=position, buff=0.2
            )

            if i == 0:
                step_arrow.put_start_and_end_on(
                    ast_obj.get_right(), position + LEFT * 0.5
                )
            elif i == len(stages) - 1:
                step_arrow.put_start_and_end_on(
                    position + RIGHT * 0.5, ir_code_obj.get_left()
                )
            else:
                prev_position = ast_obj.get_center() * (
                    1 - (i) / (len(stages) + 1)
                ) + ir_code_obj.get_center() * ((i) / (len(stages) + 1))
                step_arrow.put_start_and_end_on(
                    prev_position + RIGHT * 0.5, position + LEFT * 0.5
                )

            self.play(Write(stage_obj), GrowArrow(step_arrow), run_time=0.8)

            # Brief explanation of this stage
            explanation_text = {
                "Analyze AST structure": "Extract control flow and expressions",
                "Convert to basic blocks": "Create sequences of straight-line code",
                "Generate SSA form": "Each variable assigned exactly once",
                "Apply target-independent optimizations": "Prepare IR for code generation",
            }[stage]

            explanation_id, explanation_obj = self.create_element(
                "text",
                explanation_text,
                size=14,
                position=stage_obj.get_center() + DOWN * 0.5,
                color=WHITE,
            )

            self.play(FadeIn(explanation_obj), run_time=0.5)

            self.wait(0.7)

            if i < len(stages) - 1:
                self.play(FadeOut(explanation_obj), run_time=0.4)

    def create_summary_points(self):
        """Create educational summary points highlighting key insights"""
        summary_points = [
            {
                "title": "Preprocessor",
                "insight": "Text-based transformations that prepare code for parsing",
                "icon": "file",
            },
            {
                "title": "Lexer & Parser",
                "insight": "Transforms raw text into structured abstract syntax tree",
                "icon": "tree",
            },
            {
                "title": "IR Generation",
                "insight": "Provides platform-independent optimizable representation",
                "icon": "code",
            },
            {
                "title": "Optimizer",
                "insight": "Transforms code to improve efficiency without changing behavior",
                "icon": "optimize",
            },
            {
                "title": "Code Generation",
                "insight": "Translates IR into specific assembly for target architecture",
                "icon": "instruction",
            },
            {
                "title": "Assembler & Linker",
                "insight": "Creates executable that can directly run on hardware",
                "icon": "executable",
            },
        ]

        return summary_points

    def show_learning_assessment(self):
        """End with questions that reinforce key learning points"""

        title_id, title = self.create_element(
            "text",
            "Key Concepts Review",
            size=28,
            position=UP * 3,
            color=self.colors["main_phase"],
        )

        questions = [
            "Which phase converts source code into tokens?",
            "What is the primary purpose of intermediate representation?",
            "How does the linker differ from the assembler?",
            "Why is optimization placed between IR and code generation?",
        ]

        question_objects = []

        for i, question in enumerate(questions):
            q_id, q_obj = self.create_element(
                "text",
                f"Q{i+1}: {question}",
                size=20,
                position=UP * (1.5 - i * 1),
                color=WHITE,
            )
            question_objects.append(q_obj)

        self.play(Write(title), run_time=1)

        # Show questions one by one
        for q_obj in question_objects:
            self.play(Write(q_obj), run_time=1)
            self.wait(0.5)

        self.wait(3)

        # Show closing message
        closing_id, closing = self.create_element(
            "text",
            "Understanding the compiler pipeline helps you write more efficient code",
            size=24,
            position=DOWN * 2,
            color=self.colors["success"],
        )

        self.play(Write(closing), run_time=1.5)
        self.wait(2)

    def show_real_world_context(self):
        """Provide educational context by showing real-world compiler examples"""

        title_id, title = self.create_element(
            "text",
            "Real-world Compilers",
            size=28,
            position=UP * 2,
            color=self.colors["main_phase"],
        )

        compilers = [
            {
                "name": "GCC",
                "languages": "C, C++, Fortran",
                "notable": "Open source, highly portable",
            },
            {
                "name": "Clang/LLVM",
                "languages": "C, C++, Objective-C",
                "notable": "Modular design, excellent diagnostics",
            },
            {
                "name": "Rust Compiler",
                "languages": "Rust",
                "notable": "Strong safety guarantees",
            },
            {
                "name": "GHC",
                "languages": "Haskell",
                "notable": "Advanced optimizations for functional code",
            },
            {
                "name": "V8",
                "languages": "JavaScript",
                "notable": "JIT compilation for web browsers",
            },
        ]

        compiler_objects = []

        for i, compiler in enumerate(compilers):
            # Create a box for each compiler
            box_id, box = self.create_element(
                "box",
                "",
                position=RIGHT * (i - 2) * 2.5,
                color=self.colors["main_phase"],
                height=2,
                width=2,
                fill_opacity=0.1,
            )

            # Add compiler name
            name_id, name = self.create_element(
                "text",
                compiler["name"],
                size=20,
                position=box.get_center() + UP * 0.5,
                color=self.colors["main_phase"],
            )

            # Add language info
            lang_id, lang = self.create_element(
                "text",
                f"Languages: {compiler['languages']}",
                size=14,
                position=box.get_center(),
                color=WHITE,
            )

            # Add notable features
            notable_id, notable = self.create_element(
                "text",
                compiler["notable"],
                size=14,
                position=box.get_center() + DOWN * 0.5,
                color=BLUE_B,
            )

            compiler_group = VGroup(box, name, lang, notable)
            compiler_objects.append(compiler_group)

        # Show title
        self.play(Write(title), run_time=1)

        # Show compilers one by one
        for compiler in compiler_objects:
            self.play(FadeIn(compiler), run_time=0.7)

        self.wait(2)

        # Fade out
        self.play(
            FadeOut(title),
            *[FadeOut(compiler) for compiler in compiler_objects],
            run_time=1,
        )

    # Other educational enhancement methods...
