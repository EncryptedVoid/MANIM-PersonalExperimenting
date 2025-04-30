# compiler_pipeline_animation.py
from manim import *
from compiler_animation_phases import CompilerAnimationPhases


class CompilerPipelineAnimation(CompilerAnimationPhases):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Any final initializations

    def construct(self):
        """
        Main method that orchestrates the entire compiler pipeline animation.

        This method serves as the entry point and coordinates the sequence
        of animation phases to create a cohesive educational experience.
        """
        # Set background color
        self.camera.background_color = "#111111"

        # Run the animation sequence
        self.animate_introduction()
        self.animate_preprocessor_phase()
        self.animate_lexer_phase()
        self.animate_parser_phase()
        self.animate_ir_phase()
        self.animate_optimizer_phase()
        self.animate_codegen_phase()
        self.animate_assembler_phase()
        self.animate_linker_phase()
        self.animate_summary()

        # Final cleanup
        self.play(*[FadeOut(obj) for obj in self.all_objects.values()], run_time=1.5)


# Create the scene for rendering
if __name__ == "__main__":
    scene = CompilerPipelineAnimation()
    scene.render()
