# compiler_animation_base.py
from manim import *


class CompilerAnimationBase(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Base properties: colors, regions, timing
        self.all_objects = {}
        self.current_phase = None
        # Define color scheme
        self.colors = {
            "title": WHITE,
            "main_phase": BLUE_D,
            # ...other colors...
        }
        # Define screen regions
        self.regions = {
            "top": UP * 3.5,
            "title": UP * 3,
            # ...other regions...
        }
        # Define timing framework
        self.timing = {
            "brief": 0.5,
            "standard": 0.8,
            # ...other timings...
        }

    def create_element(
        self, element_type, content, size=24, position=ORIGIN, color=None, **kwargs
    ):
        """Create a tracked element with proper styling and positioning"""
        try:
            # Choose default color based on element type
            if color is None:
                color = self.colors.get(element_type, WHITE)

            # Create the appropriate object based on type
            if element_type == "title":
                obj = Text(content, font_size=36, weight=BOLD, color=color)
            elif element_type == "phase":
                obj = Text(content, font_size=30, weight=BOLD, color=color)
            elif element_type == "text":
                obj = Text(content, font_size=size, color=color)
            elif element_type == "code":
                obj = Code(
                    code=content,
                    language="cpp",
                    font_size=size,
                    background="window",
                    background_stroke_width=1,
                    **kwargs,
                )
            elif element_type == "math":
                obj = MathTex(content, font_size=size, color=color)
            elif element_type == "file":
                # Create file icon with text
                file_rect = Rectangle(height=1.2, width=0.9, color=self.colors["file"])
                file_corner = Polygon(
                    file_rect.get_corner(UR),
                    file_rect.get_corner(UR) + LEFT * 0.3,
                    file_rect.get_corner(UR) + LEFT * 0.3 + DOWN * 0.3,
                    color=self.colors["file"],
                )
                file_text = Text(content, font_size=size * 0.8, color=color)
                file_text.move_to(file_rect.get_center())
                obj = VGroup(file_rect, file_corner, file_text)
            elif element_type == "arrow":
                obj = Arrow(start=ORIGIN, end=RIGHT, color=color, **kwargs)
            elif element_type == "box":
                obj = Rectangle(
                    height=kwargs.get("height", 1),
                    width=kwargs.get("width", 2),
                    color=color,
                    fill_opacity=kwargs.get("fill_opacity", 0.1),
                )
                if "label" in kwargs:
                    label = Text(kwargs["label"], font_size=size * 0.8, color=color)
                    label.move_to(obj.get_center())
                    obj = VGroup(obj, label)
            else:
                # Default to regular text
                obj = Text(content, font_size=size, color=color)

            # Position the object
            obj.move_to(position)

            # Generate a unique identifier if not provided
            element_id = kwargs.get("id", f"{element_type}_{len(self.all_objects)}")

            # Store in tracking dictionary
            self.all_objects[element_id] = obj

            return element_id, obj

        except Exception as e:
            print(f"Error creating {element_type} '{content}': {e}")
            # Create a fallback object
            fallback = Text(f"[{element_type}]", font_size=size, color=RED)
            fallback.move_to(position)
            fallback_id = f"fallback_{len(self.all_objects)}"
            self.all_objects[fallback_id] = fallback
            return fallback_id, fallback

    def transition_to_phase(
        self, phase_name, phase_title, keep_ids=None, fade_duration=0.7
    ):
        """
        Transition to a new phase with improved cognitive scaffolding.
        Enhances retention by maintaining key context elements.
        """
        if keep_ids is None:
            keep_ids = []

        # Store a reference to the main phase object for later positioning
        phase_obj = None

        # Determine which objects to fade out
        to_fade = []
        for obj_id, obj in list(self.all_objects.items()):
            if obj_id not in keep_ids:
                to_fade.append(obj)
                del self.all_objects[obj_id]

        # Execute fade out with slight delay for cognitive processing
        if to_fade:
            self.play(FadeOut(Group(*to_fade)), run_time=fade_duration)
            self.wait(0.3)  # Brief pause for cognitive closure

        # Create connecting text to bridge conceptual gap
        if self.current_phase and phase_name:
            connection_text = self.phase_connections.get(
                (self.current_phase, phase_name),
                f"Moving from {self.current_phase} to {phase_name}...",
            )

            conn_id, conn_obj = self.create_element(
                "text",
                connection_text,
                size=18,
                position=self.regions["middle"],
                color=self.colors["sub_phase"],
            )

            # Brief connection message to maintain narrative flow
            self.play(Write(conn_obj), run_time=0.7)
            self.wait(0.5)
            self.play(FadeOut(conn_obj), run_time=0.4)

        # Set new phase
        self.current_phase = phase_name

        # Create phase title with emphasis
        if phase_title:
            phase_id, phase_obj = self.create_element(
                "phase",
                phase_title,
                position=self.regions["title"],
                color=self.colors["main_phase"],
            )

            # Add subtle highlight effect to enhance focus
            highlight = BackgroundRectangle(
                phase_obj, color=self.colors["main_phase"], fill_opacity=0.1, buff=0.2
            )

            self.play(
                FadeIn(highlight, rate_func=there_and_back_with_pause),
                Write(phase_obj),
                run_time=1,
            )

            return phase_id, phase_obj

        return None, None

    def create_wrapped_text(self, text, max_width, font_size=24):
        """Create text that automatically wraps to fit width."""
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            test_line = current_line + [word]
            test_text = Text(" ".join(test_line), font_size=font_size)

            if test_text.width <= max_width or not current_line:
                current_line = test_line
            else:
                lines.append(" ".join(current_line))
                current_line = [word]

        if current_line:
            lines.append(" ".join(current_line))

        result = VGroup(*[Text(line, font_size=font_size) for line in lines])
        result.arrange(DOWN, aligned_edge=LEFT)

        return result

    def cleanup_unused_objects(self, except_ids=None):
        """Explicitly remove objects that are no longer needed to improve memory usage"""
        if except_ids is None:
            except_ids = []

        # Identify objects to remove
        to_remove = []
        for obj_id in list(self.all_objects.keys()):
            if obj_id not in except_ids and obj_id not in self.persistent_objects:
                to_remove.append(obj_id)

        # Remove objects
        for obj_id in to_remove:
            del self.all_objects[obj_id]

    # Other core utility methods...
