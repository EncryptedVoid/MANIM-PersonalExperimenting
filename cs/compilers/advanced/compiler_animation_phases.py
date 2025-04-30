# compiler_animation_phases.py
from manim import *
from compiler_animation_educational import CompilerAnimationEducational


class CompilerAnimationPhases(CompilerAnimationEducational):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_code_example(self):
        """Create a C code example that effectively demonstrates compiler features"""
        return """// Example C program showing compiler features
#include <stdio.h>

// Macro for compile-time optimization opportunity
#define SUM_FORMULA(n) ((n) * ((n) + 1) / 2)

// Global variable to demonstrate data section
int result = 0;

// Function to demonstrate linking
void print_result(int value) {
    printf("Result: %d\\n", value);
}

int main() {
    // Loop that could be optimized
    for (int i = 1; i <= 100; i++) {
        result += i;
    }

    // Demonstrate constant folding potential
    int formula_result = SUM_FORMULA(100);

    // Check if optimization was correct
    if (result != formula_result) {
        printf("Error in calculation!\\n");
        return 1;
    }

    // External function call (linking example)
    print_result(result);
    return 0;
}"""

    def animate_introduction(self):
        """
        Animate the introduction to the compiler pipeline.

        Educational objectives:
        1. Introduce the concept of compilation
        2. Present the code example that will be compiled
        3. Show the high-level overview of the compilation process
        """
        # Create title
        title_id, title = self.create_element(
            "title", "The Compiler Pipeline", position=self.regions["title"]
        )
        self.play(Write(title), run_time=1.5)
        self.wait(1)

        # Create initial code example
        code_example = self.create_code_example()
        code_id, code = self.create_element(
            "code",
            code_example,
            size=18,
            position=self.regions["middle"],
            background_stroke_color=GRAY_D,
        )
        self.play(Create(code), run_time=2)
        self.wait(1)

        # Overview of compilation stages
        overview_text = "Source Code → Preprocessor → Lexer → Parser → Intermediate Representation → Optimizer → Code Generator → Assembler → Linker → Executable"
        overview_id, overview = self.create_element(
            "text", overview_text, size=20, position=self.regions["lower"], color=BLUE_B
        )
        self.play(Write(overview), run_time=2)
        self.wait(2)

        # Store reference to code for later phases
        self.code = code
        self.code_id = code_id

    def animate_preprocessor_phase(self):
        """
        Animate the preprocessor phase of compilation.

        Educational objectives:
        1. Demonstrate how preprocessor directives are processed
        2. Show include file expansion and macro substitution
        3. Illustrate the conversion from source to preprocessed code
        """
        # Begin preprocessor phase
        self.transition_to_phase(
            "preprocessor", "1. Preprocessor", keep_ids=[self.code_id]
        )

        # Position the code for better visibility
        self.play(self.code.animate.scale(0.8).to_edge(LEFT).shift(UP), run_time=1)

        # Show preprocessor directives
        directive_id, directive = self.create_element(
            "text",
            "Preprocessor Directives",
            size=22,
            position=UP + RIGHT * 3,
            color=self.colors["sub_phase"],
        )
        self.play(Write(directive), run_time=0.8)

        # Highlight and explain #include
        include_frame_id, include_frame = self.create_element(
            "box",
            "",
            position=self.code.get_center() + UP * 0.9,
            color=self.colors["highlight"],
            height=0.4,
            width=4.5,
            fill_opacity=0.2,
        )

        include_note_id, include_note = self.create_element(
            "text",
            "#include: Copy contents of stdio.h here",
            size=18,
            position=RIGHT * 3,
            color=self.colors["highlight"],
        )

        self.play(Create(include_frame), Write(include_note), run_time=1)
        self.wait(1)

        # Show stdio.h file
        stdio_id, stdio = self.create_element(
            "file", "stdio.h", position=RIGHT * 4 + UP * 1.5, color=WHITE
        )

        # Show arrow from stdio.h to code
        include_arrow_id, include_arrow = self.create_element(
            "arrow",
            "",
            color=self.colors["arrow"],
            position=RIGHT * 3 + UP * 1,
            buff=0.3,
        )
        include_arrow.put_start_and_end_on(
            stdio.get_bottom() + DOWN * 0.2, include_frame.get_right()
        )

        self.play(Create(stdio), GrowArrow(include_arrow), run_time=1.5)
        self.wait(1)

        # Highlight and explain #define
        define_frame_id, define_frame = self.create_element(
            "box",
            "",
            position=self.code.get_center() + UP * 0.6,
            color=self.colors["highlight"],
            height=0.4,
            width=3,
            fill_opacity=0.2,
        )

        define_note_id, define_note = self.create_element(
            "text",
            "#define: Replace SUM_FORMULA with calculation",
            size=18,
            position=RIGHT * 3 + DOWN * 0.5,
            color=self.colors["highlight"],
        )

        self.play(
            FadeOut(include_frame),
            FadeOut(include_note),
            FadeOut(stdio),
            FadeOut(include_arrow),
            Create(define_frame),
            Write(define_note),
            run_time=1,
        )
        self.wait(1)

        # Show macro replacement in the code
        macro_frame_id, macro_frame = self.create_element(
            "box",
            "",
            position=self.code.get_center() - UP * 0.1,
            color=self.colors["highlight"],
            height=0.4,
            width=1,
            fill_opacity=0.2,
        )

        macro_arrow_id, macro_arrow = self.create_element(
            "arrow", "", color=self.colors["arrow"], position=RIGHT * 1.5, buff=0.3
        )

        self.play(Create(macro_frame), GrowArrow(macro_arrow), run_time=1)

        macro_replace_id, macro_replace = self.create_element(
            "text",
            "((100) * ((100) + 1) / 2)",
            size=20,
            position=macro_arrow.get_end() + RIGHT * 0.5,
            color=self.colors["highlight"],
        )

        self.play(Write(macro_replace), run_time=0.8)
        self.wait(1)

        # Show preprocessed code
        preprocessed_code = """// Example C program
    #include <stdio.h> // Contents of stdio.h inserted here

    // Global variable in data section
    int result = 0;

    // Function included for linking example
    void print_result(int value) {
        printf("Result: %d\\n", value);
    }

    int main() {
        // Loop with constant values
        for (int i = 1; i <= 100; i++) {
            result += i;
        }

        // Macro expanded to formula
        int formula_result = ((100) * ((100) + 1) / 2);

        // Rest of the function...
        if (result != formula_result) {
            printf("Error in calculation!\\n");
            return 1;
        }

        print_result(result);
        return 0;
    }"""

        preprocessed_id, preprocessed = self.create_element(
            "code",
            preprocessed_code,
            size=18,
            position=RIGHT * 3 + DOWN * 1.5,
            background_stroke_color=GRAY_D,
        )

        self.play(
            FadeOut(define_frame),
            FadeOut(define_note),
            FadeOut(macro_frame),
            FadeOut(macro_arrow),
            FadeOut(macro_replace),
            Create(preprocessed),
            run_time=1.5,
        )

        preprocessed_file_id, preprocessed_file = self.create_element(
            "file",
            ".i file",
            position=preprocessed.get_top() + UP * 0.5,
            color=WHITE,
            size=18,
        )

        self.play(Create(preprocessed_file), run_time=0.8)

        # Save reference to preprocessed code for next phase
        self.preprocessed_code = preprocessed_code

        self.wait(1.5)

    def animate_lexer_phase(self):
        """
        Animate the lexical analysis (tokenization) phase of compilation.

        Educational objectives:
        1. Demonstrate how source code is broken into tokens
        2. Show the different types of tokens (keywords, identifiers, symbols)
        3. Explain how the token stream serves as input to the parser
        """
        self.transition_to_phase(
            "lexer", "2. Lexical Analysis (Tokenization)", fade_duration=1
        )

        # Create code display from preprocessed code
        code_id, code = self.create_element(
            "code",
            self.preprocessed_code,
            size=18,
            position=LEFT * 3 + UP * 1,
            background_stroke_color=GRAY_D,
        )

        self.play(Create(code), run_time=1.5)

        # Add description of lexer functionality
        lexer_desc_id, lexer_desc = self.create_element(
            "text",
            "The lexer breaks code into tokens (smallest meaningful units)",
            size=20,
            position=UP,
            color=self.colors["sub_phase"],
        )

        self.play(Write(lexer_desc), run_time=1.2)
        self.wait(0.5)

        # Create tokens visualization
        token_groups = [
            ("int", "KEYWORD"),
            ("main", "IDENTIFIER"),
            ("(", "SYMBOL"),
            (")", "SYMBOL"),
            ("{", "SYMBOL"),
            ("int", "KEYWORD"),
            ("sum", "IDENTIFIER"),
            ("=", "OPERATOR"),
            ("0", "NUMBER"),
            (";", "SYMBOL"),
            # More tokens would follow...
        ]

        # Create token boxes
        tokens_group = VGroup()
        token_labels = VGroup()

        for i, (token_text, token_type) in enumerate(token_groups):
            # Determine color based on token type
            if token_type == "KEYWORD":
                color = self.colors["code"]
            elif token_type == "IDENTIFIER":
                color = BLUE_B
            elif token_type == "SYMBOL":
                color = YELLOW_D
            elif token_type == "OPERATOR":
                color = RED_B
            elif token_type == "NUMBER":
                color = GREEN_D
            else:
                color = WHITE

            # Create token box
            token_box = Rectangle(
                height=0.6,
                width=max(len(token_text) * 0.2, 0.6),
                color=color,
                fill_opacity=0.3,
            )

            # Create token text
            token_text_obj = Text(token_text, font_size=18, color=color)
            token_text_obj.move_to(token_box.get_center())

            # Create token type label
            token_type_text = Text(token_type, font_size=12, color=color)
            token_type_text.next_to(token_box, DOWN, buff=0.1)

            # Group token box and text
            token = VGroup(token_box, token_text_obj)

            # Position token in row
            if i == 0:
                token.move_to(DOWN * 0.5)
            else:
                token.next_to(tokens_group[-1], RIGHT, buff=0.15)

            # Position type label
            token_type_text.next_to(token, DOWN, buff=0.1)

            tokens_group.add(token)
            token_labels.add(token_type_text)

        # Center the tokens horizontally
        tokens_group.move_to(ORIGIN)
        token_labels.move_to(tokens_group.get_center() + DOWN * 0.4)

        # Animate tokens appearance
        self.play(Create(tokens_group), run_time=1.5)

        self.play(Write(token_labels), run_time=1)
        self.wait(1)

        # Show token stream file as output of lexical analysis
        lexer_result_id, lexer_result = self.create_element(
            "file", "Token Stream", position=DOWN * 2.5, color=WHITE, size=20
        )

        # Show the output of the lexer
        self.play(Create(lexer_result), run_time=0.8)
        self.wait(1.5)

    def animate_parser_phase(self):
        """
        Animate the parsing (syntax analysis) phase of compilation.

        Educational objectives:
        1. Demonstrate how tokens are organized into a hierarchical structure
        2. Show the construction of an Abstract Syntax Tree (AST)
        3. Illustrate how syntax errors are caught during this phase
        """
        self.transition_to_phase("parser", "3. Parsing (Syntax Analysis)")

        # Show token stream as input to parser
        tokens_id, tokens = self.create_element(
            "text",
            "Token Stream: [INT, MAIN, (, ), {, INT, SUM, =, 0, ;, ...]",
            size=20,
            position=UP * 1.5,
            color=BLUE_B,
        )

        self.play(Write(tokens), run_time=1)

        # Add description of parser functionality
        parser_desc_id, parser_desc = self.create_element(
            "text",
            "The parser builds an Abstract Syntax Tree (AST) according to grammar rules",
            size=20,
            position=UP * 0.5,
            color=self.colors["sub_phase"],
        )

        self.play(Write(parser_desc), run_time=1.2)

        # Create the Abstract Syntax Tree
        # Root node
        program_node_id, program_node = self.create_element(
            "box",
            "",
            label="Program",
            position=ORIGIN,
            color=self.colors["code"],
            height=0.6,
            width=1.5,
        )

        # Main function node
        main_func_id, main_func = self.create_element(
            "box",
            "",
            label="FunctionDecl\n'main'",
            position=DOWN * 1 + LEFT * 2,
            color=BLUE_B,
            height=0.8,
            width=1.8,
        )

        # Return type node
        return_type_id, return_type = self.create_element(
            "box",
            "",
            label="ReturnType\n'int'",
            position=DOWN * 2 + LEFT * 3.5,
            color=TEAL_B,
            height=0.7,
            width=1.5,
        )

        # Function body
        func_body_id, func_body = self.create_element(
            "box",
            "",
            label="CompoundStmt",
            position=DOWN * 2 + LEFT * 0.5,
            color=YELLOW_D,
            height=0.7,
            width=1.8,
        )

        # Variable declarations
        var_decl_id, var_decl = self.create_element(
            "box",
            "",
            label="VarDecl\n'sum'",
            position=DOWN * 3 + LEFT * 2,
            color=GREEN_D,
            height=0.7,
            width=1.5,
        )

        # For loop
        for_loop_id, for_loop = self.create_element(
            "box",
            "",
            label="ForStmt",
            position=DOWN * 3,
            color=PURPLE_B,
            height=0.7,
            width=1.5,
        )

        # Return statement
        return_stmt_id, return_stmt = self.create_element(
            "box",
            "",
            label="ReturnStmt",
            position=DOWN * 3 + RIGHT * 2,
            color=RED_B,
            height=0.7,
            width=1.5,
        )

        # Create connecting lines for the AST
        line1_id, line1 = self.create_element("arrow", "", color=WHITE, buff=0.2)
        line1.put_start_and_end_on(program_node.get_bottom(), main_func.get_top())

        line2_id, line2 = self.create_element("arrow", "", color=WHITE, buff=0.2)
        line2.put_start_and_end_on(
            main_func.get_bottom() + LEFT * 0.4, return_type.get_top()
        )

        line3_id, line3 = self.create_element("arrow", "", color=WHITE, buff=0.2)
        line3.put_start_and_end_on(
            main_func.get_bottom() + RIGHT * 0.4, func_body.get_top()
        )

        line4_id, line4 = self.create_element("arrow", "", color=WHITE, buff=0.2)
        line4.put_start_and_end_on(
            func_body.get_bottom() + LEFT * 0.5, var_decl.get_top()
        )

        line5_id, line5 = self.create_element("arrow", "", color=WHITE, buff=0.2)
        line5.put_start_and_end_on(func_body.get_bottom(), for_loop.get_top())

        line6_id, line6 = self.create_element("arrow", "", color=WHITE, buff=0.2)
        line6.put_start_and_end_on(
            func_body.get_bottom() + RIGHT * 0.5, return_stmt.get_top()
        )

        # Animate the AST creation step by step
        self.play(Create(program_node), run_time=0.8)

        self.play(Create(main_func), GrowArrow(line1), run_time=0.8)

        self.play(
            Create(return_type),
            Create(func_body),
            GrowArrow(line2),
            GrowArrow(line3),
            run_time=1,
        )

        self.play(
            Create(var_decl),
            Create(for_loop),
            Create(return_stmt),
            GrowArrow(line4),
            GrowArrow(line5),
            GrowArrow(line6),
            run_time=1.2,
        )

        # Label the AST
        ast_label_id, ast_label = self.create_element(
            "text",
            "Abstract Syntax Tree (AST)",
            size=24,
            position=program_node.get_top() + UP * 0.4,
            color=self.colors["code"],
        )

        self.play(Write(ast_label), run_time=0.8)
        self.wait(2)

        # Store reference to AST for next phase
        self.ast = program_node

        # Syntax error example
        syntax_error_id, syntax_error = self.create_element(
            "text",
            "Syntax errors are caught during this phase",
            size=20,
            position=RIGHT * 3 + UP * 0.5,
            color=self.colors["error"],
        )

        error_code_id, error_code = self.create_element(
            "code",
            """int main() {
        int sum = 0
        for (int i = 1; i <= 100; i++) {
            sum += i;
        }
        return 0;
    }""",
            size=16,
            position=RIGHT * 3 + DOWN,
            background_stroke_color=GRAY_D,
        )

        error_indicator_id, error_indicator = self.create_element(
            "text",
            "Missing semicolon ↑",
            size=18,
            position=RIGHT * 4 + DOWN * 0.2,
            color=RED,
        )

        self.play(Write(syntax_error), run_time=0.8)

        self.play(Create(error_code), run_time=1)

        self.play(Write(error_indicator), run_time=0.8)
        self.wait(1.5)

    def animate_ir_phase(self):
        """
        Animate the Intermediate Representation (IR) phase of compilation.

        Educational objectives:
        1. Demonstrate the translation from AST to low-level IR
        2. Illustrate the structure and purpose of intermediate representation
        3. Show how IR serves as a bridge between high-level and machine code
        """
        self.transition_to_phase("ir", "4. Intermediate Representation (IR)")

        # Create small AST representation
        ast_small_id, ast_small = self.create_element(
            "box",
            "",
            label="AST",
            position=LEFT * 4 + UP * 1.5,
            color=self.colors["code"],
            height=1.2,
            width=1.2,
        )

        self.play(Create(ast_small), run_time=0.8)

        # Add descriptions of IR functionality
        ir_desc_id, ir_desc = self.create_element(
            "text",
            "The AST is converted to an Intermediate Representation (IR)",
            size=22,
            position=UP * 1.5,
            color=self.colors["sub_phase"],
        )

        ir_detail_id, ir_detail = self.create_element(
            "text",
            "IR is a lower-level representation that's easier to optimize and translate",
            size=20,
            position=UP * 0.8,
            color=self.colors["sub_phase"],
        )

        self.play(Write(ir_desc), run_time=1)

        self.play(Write(ir_detail), run_time=1)

        # Show IR conversion arrow
        ir_arrow_id, ir_arrow = self.create_element(
            "arrow", "", color=self.colors["arrow"], position=ORIGIN, buff=0.3
        )
        ir_arrow.put_start_and_end_on(ast_small.get_right(), LEFT * 2 + UP * 1.5)

        self.play(GrowArrow(ir_arrow), run_time=0.8)

        # Show IR code (LLVM-like)
        ir_code = """define i32 @main() {
    entry:
    %sum = alloca i32, align 4
    store i32 0, i32* %sum, align 4
    br label %for.cond

    for.cond:
    %i = phi i32 [ 1, %entry ], [ %inc, %for.body ]
    %cmp = icmp sle i32 %i, 100
    br i1 %cmp, label %for.body, label %for.end

    for.body:
    %0 = load i32, i32* %sum, align 4
    %add = add nsw i32 %0, %i
    store i32 %add, i32* %sum, align 4
    %inc = add nsw i32 %i, 1
    br label %for.cond

    for.end:
    ret i32 0
    }"""

        ir_code_id, ir_code = self.create_element(
            "code",
            ir_code,
            size=16,
            position=RIGHT * 2,
            language="llvm",
            background_stroke_color=GRAY_D,
        )

        ir_label_id, ir_label = self.create_element(
            "text",
            "LLVM Intermediate Representation",
            size=20,
            position=ir_code.get_top() + UP * 0.4,
            color=self.colors["instruction"],
        )

        self.play(Create(ir_code), run_time=1.2)

        self.play(Write(ir_label), run_time=0.8)
        self.wait(1)

        # Store references for next phase
        self.ir_code = ir_code
        self.ir_code_text = ir_code

        # Highlight important parts of IR
        ir_entry_id, ir_entry = self.create_element(
            "box",
            "",
            position=ir_code.get_center() + UP * 0.8 + LEFT * 0.5,
            color=self.colors["highlight"],
            height=0.4,
            width=1.5,
            fill_opacity=0.2,
        )

        entry_note_id, entry_note = self.create_element(
            "text",
            "Entry block",
            size=16,
            position=ir_entry.get_right() + RIGHT * 1.5,
            color=self.colors["highlight"],
        )

        self.play(Create(ir_entry), Write(entry_note), run_time=0.8)
        self.wait(0.5)

        self.play(FadeOut(ir_entry), FadeOut(entry_note), run_time=0.5)

        ir_phi_id, ir_phi = self.create_element(
            "box",
            "",
            position=ir_code.get_center() + UP * 0.2,
            color=self.colors["highlight"],
            height=0.4,
            width=4.5,
            fill_opacity=0.2,
        )

        phi_note_id, phi_note = self.create_element(
            "text",
            "PHI node (loop counter)",
            size=16,
            position=ir_phi.get_right() + RIGHT * 2,
            color=self.colors["highlight"],
        )

        self.play(Create(ir_phi), Write(phi_note), run_time=0.8)
        self.wait(0.5)

        self.play(FadeOut(ir_phi), FadeOut(phi_note), run_time=0.5)

        ir_load_id, ir_load = self.create_element(
            "box",
            "",
            position=ir_code.get_center() - UP * 0.7,
            color=self.colors["highlight"],
            height=0.4,
            width=3.5,
            fill_opacity=0.2,
        )

        load_note_id, load_note = self.create_element(
            "text",
            "Load from memory",
            size=16,
            position=ir_load.get_right() + RIGHT * 1.8,
            color=self.colors["highlight"],
        )

        self.play(Create(ir_load), Write(load_note), run_time=0.8)
        self.wait(0.5)

        self.play(FadeOut(ir_load), FadeOut(load_note), run_time=0.5)

        # IR file representation
        ir_file_id, ir_file = self.create_element(
            "file", ".ll file", position=DOWN * 2, color=WHITE, size=18
        )

        self.play(Create(ir_file), run_time=0.8)
        self.wait(1.5)

    def animate_optimizer_phase(self):
        """
        Animate the optimization phase of compilation.

        Educational objectives:
        1. Demonstrate how code optimizations improve efficiency
        2. Show specific optimization techniques like constant folding
        3. Illustrate the transformation from unoptimized to optimized IR
        """
        self.transition_to_phase("optimizer", "5. Optimization")

        # Create unoptimized IR representation
        ir_code_unopt_id, ir_code_unopt = self.create_element(
            "code",
            self.ir_code_text,
            size=16,
            position=LEFT * 3 + UP * 0.5,
            language="llvm",
            background_stroke_color=GRAY_D,
        )

        self.play(Create(ir_code_unopt), run_time=1)

        # Add description of optimizer functionality
        optimize_desc_id, optimize_desc = self.create_element(
            "text",
            "The optimizer performs various transformations to improve efficiency",
            size=22,
            position=UP * 2,
            color=self.colors["sub_phase"],
        )

        self.play(Write(optimize_desc), run_time=1)

        # Show optimization process with arrows
        optimize_arrow_id, optimize_arrow = self.create_element(
            "arrow", "", color=self.colors["arrow"], position=ORIGIN, buff=0.3
        )
        optimize_arrow.put_start_and_end_on(ir_code_unopt.get_right(), RIGHT * 1)

        self.play(GrowArrow(optimize_arrow), run_time=0.8)

        # Show optimized IR code
        optimized_code = """define i32 @main() {
    entry:
    ; Sum formula optimization: n*(n+1)/2
    ; where n = 100
    ret i32 5050
    }"""

        optimized_id, optimized = self.create_element(
            "code",
            optimized_code,
            size=16,
            position=RIGHT * 3 + UP * 0.5,
            language="llvm",
            background_stroke_color=GRAY_D,
        )

        optimized_label_id, optimized_label = self.create_element(
            "text",
            "Optimized IR Code",
            size=20,
            position=optimized.get_top() + UP * 0.4,
            color=self.colors["success"],
        )

        self.play(Create(optimized), Write(optimized_label), run_time=1.2)

        # Store reference for next phase
        self.optimized_code = optimized_code

        # List common optimizations
        optimizations_title_id, optimizations_title = self.create_element(
            "text",
            "Common Optimizations:",
            size=20,
            position=DOWN * 0.5,
            color=self.colors["sub_phase"],
        )

        optimizations = [
            "• Constant Folding & Propagation",
            "• Dead Code Elimination",
            "• Loop Unrolling",
            "• Inlining",
            "• Strength Reduction",
        ]

        opt_texts = []
        for i, opt in enumerate(optimizations):
            opt_id, opt_obj = self.create_element(
                "text", opt, size=18, position=DOWN * (1.0 + i * 0.4), color=WHITE
            )
            opt_texts.append((opt_id, opt_obj))

        self.play(Write(optimizations_title), run_time=0.8)

        for _, opt_obj in opt_texts:
            self.play(Write(opt_obj), run_time=0.5)

        self.wait(2)

    def animate_codegen_phase(self):
        """
        Animate the code generation phase of compilation.

        Educational objectives:
        1. Demonstrate the translation from IR to assembly code
        2. Show target-specific code generation
        3. Illustrate the structure of assembly language
        """
        self.transition_to_phase("codegen", "6. Code Generation")

        # Create small optimized IR representation
        ir_code_small_id, ir_code_small = self.create_element(
            "code",
            self.optimized_code,
            size=14,
            position=LEFT * 4 + UP * 1.5,
            language="llvm",
            background_stroke_color=GRAY_D,
        )

        self.play(Create(ir_code_small), run_time=0.8)

        # Add description of code generator functionality
        codegen_desc_id, codegen_desc = self.create_element(
            "text",
            "The code generator converts IR into target assembly code",
            size=22,
            position=UP * 2,
            color=self.colors["sub_phase"],
        )

        self.play(Write(codegen_desc), run_time=1)

        # Show code generation arrow
        codegen_arrow_id, codegen_arrow = self.create_element(
            "arrow", "", color=self.colors["arrow"], position=ORIGIN, buff=0.3
        )
        codegen_arrow.put_start_and_end_on(
            ir_code_small.get_right(), LEFT * 2 + UP * 1.5
        )

        self.play(GrowArrow(codegen_arrow), run_time=0.8)

        # Show x86-64 assembly code
        assembly_code = """    .text
        .globl  main
        .type   main, @function
    main:
        pushq   %rbp
        movq    %rsp, %rbp

        # Return value 5050 (0x13ba)
        movl    $5050, %eax

        popq    %rbp
        ret
        .size   main, .-main"""

        assembly_id, assembly = self.create_element(
            "code",
            assembly_code,
            size=16,
            position=RIGHT * 2,
            language="asm",
            background_stroke_color=GRAY_D,
        )

        assembly_label_id, assembly_label = self.create_element(
            "text",
            "x86-64 Assembly Code",
            size=20,
            position=assembly.get_top() + UP * 0.4,
            color=self.colors["instruction"],
        )

        self.play(Create(assembly), run_time=1.2)

        self.play(Write(assembly_label), run_time=0.8)

        # Store reference for next phase
        self.assembly_code = assembly_code

        # Highlight important parts of assembly
        asm_section_id, asm_section = self.create_element(
            "box",
            "",
            position=assembly.get_center() + UP * 1.3,
            color=self.colors["highlight"],
            height=0.4,
            width=1.5,
            fill_opacity=0.2,
        )

        section_note_id, section_note = self.create_element(
            "text",
            "Text section declaration",
            size=16,
            position=asm_section.get_right() + RIGHT * 2,
            color=self.colors["highlight"],
        )

        self.play(Create(asm_section), Write(section_note), run_time=0.8)
        self.wait(0.5)

        self.play(FadeOut(asm_section), FadeOut(section_note), run_time=0.5)

        asm_return_id, asm_return = self.create_element(
            "box",
            "",
            position=assembly.get_center() - UP * 0.1,
            color=self.colors["highlight"],
            height=0.4,
            width=2.5,
            fill_opacity=0.2,
        )

        return_note_id, return_note = self.create_element(
            "text",
            "Load 5050 into return register",
            size=16,
            position=asm_return.get_right() + RIGHT * 2.5,
            color=self.colors["highlight"],
        )

        self.play(Create(asm_return), Write(return_note), run_time=0.8)
        self.wait(0.5)

        self.play(FadeOut(asm_return), FadeOut(return_note), run_time=0.5)

        # Show architecture-specific options
        target_title_id, target_title = self.create_element(
            "text",
            "Target Architecture Options:",
            size=20,
            position=DOWN * 1,
            color=self.colors["sub_phase"],
        )

        targets = [
            "• x86-64 (Intel/AMD)",
            "• ARM (Mobile/Embedded)",
            "• RISC-V (Open Standard)",
            "• PowerPC (IBM)",
            "• MIPS (Education/Embedded)",
        ]

        target_texts = []
        for i, target in enumerate(targets):
            target_id, target_obj = self.create_element(
                "text", target, size=18, position=DOWN * (1.5 + i * 0.4), color=WHITE
            )
            target_texts.append((target_id, target_obj))

        self.play(Write(target_title), run_time=0.8)

        for _, target_obj in target_texts:
            self.play(Write(target_obj), run_time=0.4)

        # Assembly file representation
        asm_file_id, asm_file = self.create_element(
            "file",
            ".s file",
            position=assembly.get_bottom() + DOWN * 0.5,
            color=WHITE,
            size=18,
        )

        self.play(Create(asm_file), run_time=0.8)
        self.wait(1.5)

    def animate_assembler_phase(self):
        """
        Animate the assembler phase of compilation.

        Educational objectives:
        1. Demonstrate the conversion from assembly to machine code
        2. Show the structure of object files
        3. Illustrate the various sections in an object file
        """
        self.transition_to_phase("assembler", "7. Assembler")

        # Create small assembly code representation
        asm_code_small_id, asm_code_small = self.create_element(
            "code",
            self.assembly_code,
            size=14,
            position=LEFT * 4 + UP * 1,
            language="asm",
            background_stroke_color=GRAY_D,
        )

        self.play(Create(asm_code_small), run_time=0.8)

        # Add description of assembler functionality
        assembler_desc_id, assembler_desc = self.create_element(
            "text",
            "The assembler converts assembly code into machine code (object files)",
            size=22,
            position=UP * 2,
            color=self.colors["sub_phase"],
        )

        self.play(Write(assembler_desc), run_time=1)

        # Show assembler process arrow
        assembler_arrow_id, assembler_arrow = self.create_element(
            "arrow", "", color=self.colors["arrow"], position=ORIGIN, buff=0.3
        )
        assembler_arrow.put_start_and_end_on(
            asm_code_small.get_right(), LEFT * 2 + UP * 1
        )

        self.play(GrowArrow(assembler_arrow), run_time=0.8)

        # Show object file structure visualization
        obj_file_id, obj_file = self.create_element(
            "box",
            "",
            label="Object File (.o)",
            position=RIGHT * 0.5 + UP * 1,
            color=self.colors["file"],
            height=3,
            width=5,
            fill_opacity=0.1,
        )

        # Create sections within the object file
        text_section_id, text_section = self.create_element(
            "box",
            "",
            label=".text (Code)",
            position=obj_file.get_center() + UP * 0.9,
            color=self.colors["code"],
            height=0.6,
            width=4.5,
            fill_opacity=0.2,
        )

        data_section_id, data_section = self.create_element(
            "box",
            "",
            label=".data (Variables)",
            position=obj_file.get_center() + UP * 0.2,
            color=BLUE_C,
            height=0.6,
            width=4.5,
            fill_opacity=0.2,
        )

        bss_section_id, bss_section = self.create_element(
            "box",
            "",
            label=".bss (Uninitialized Data)",
            position=obj_file.get_center() - UP * 0.5,
            color=GREEN_C,
            height=0.6,
            width=4.5,
            fill_opacity=0.2,
        )

        symtab_section_id, symtab_section = self.create_element(
            "box",
            "",
            label=".symtab (Symbol Table)",
            position=obj_file.get_center() - UP * 1.2,
            color=YELLOW_C,
            height=0.6,
            width=4.5,
            fill_opacity=0.2,
        )

        # Animate the object file structure
        self.play(Create(obj_file), run_time=0.8)

        self.play(
            Create(text_section),
            Create(data_section),
            Create(bss_section),
            Create(symtab_section),
            run_time=1.2,
        )

        # Machine code representation
        machine_title_id, machine_title = self.create_element(
            "text",
            "Machine Code (Hexadecimal):",
            size=20,
            position=RIGHT * 4 + UP * 1,
            color=self.colors["instruction"],
        )

        machine_code_id, machine_code = self.create_element(
            "text",
            "55 48 89 E5 B8 BA 13 00 00 5D C3",
            size=18,
            position=RIGHT * 4 + UP * 0.5,
            color=WHITE,
            font="Courier New",
        )

        self.play(Write(machine_title), run_time=0.8)

        self.play(Write(machine_code), run_time=1)

        # Object file representation
        obj_file_icon_id, obj_file_icon = self.create_element(
            "file", ".o file", position=DOWN * 2, color=WHITE, size=18
        )

        self.play(Create(obj_file_icon), run_time=0.8)
        self.wait(1.5)

    def animate_linker_phase(self):
        """
        Animate the linker phase of compilation.

        Educational objectives:
        1. Demonstrate how multiple object files are combined
        2. Show the resolution of external references
        3. Illustrate the creation of an executable file
        """
        self.transition_to_phase("linker", "8. Linker")

        # Show multiple object files
        main_obj_id, main_obj = self.create_element(
            "file", "main.o", position=LEFT * 3.5 + UP * 1.5, color=WHITE, size=18
        )

        stdlib_obj_id, stdlib_obj = self.create_element(
            "file", "stdlib.o", position=LEFT * 3.5, color=WHITE, size=18
        )

        stdio_obj_id, stdio_obj = self.create_element(
            "file", "stdio.o", position=LEFT * 3.5 - UP * 1.5, color=WHITE, size=18
        )

        self.play(Create(main_obj), Create(stdlib_obj), Create(stdio_obj), run_time=1.2)

        # Add description of linker functionality
        linker_desc_id, linker_desc = self.create_element(
            "text",
            "The linker combines multiple object files and resolves references",
            size=22,
            position=UP * 2,
            color=self.colors["sub_phase"],
        )

        self.play(Write(linker_desc), run_time=1)

        # Show linker process with arrows
        linker_arrows = []

        main_arrow_id, main_arrow = self.create_element(
            "arrow", "", color=self.colors["arrow"], position=ORIGIN, buff=0.3
        )
        main_arrow.put_start_and_end_on(main_obj.get_right(), RIGHT * 0.5 + UP * 0.5)
        linker_arrows.append(main_arrow)

        stdlib_arrow_id, stdlib_arrow = self.create_element(
            "arrow", "", color=self.colors["arrow"], position=ORIGIN, buff=0.3
        )
        stdlib_arrow.put_start_and_end_on(stdlib_obj.get_right(), RIGHT * 0.5)
        linker_arrows.append(stdlib_arrow)

        stdio_arrow_id, stdio_arrow = self.create_element(
            "arrow", "", color=self.colors["arrow"], position=ORIGIN, buff=0.3
        )
        stdio_arrow.put_start_and_end_on(stdio_obj.get_right(), RIGHT * 0.5 - UP * 0.5)
        linker_arrows.append(stdio_arrow)

        self.play(*[GrowArrow(arrow) for arrow in linker_arrows], run_time=1)

        # Show executable file
        executable_id, executable = self.create_element(
            "box",
            "",
            label="Executable File",
            position=RIGHT * 2.5,
            color=self.colors["success"],
            height=3,
            width=4,
            fill_opacity=0.1,
        )

        # Create sections within the executable
        exe_header_id, exe_header = self.create_element(
            "box",
            "",
            label="ELF Header",
            position=executable.get_center() + UP * 1.1,
            color=PURPLE_B,
            height=0.6,
            width=3.5,
            fill_opacity=0.2,
        )

        exe_text_id, exe_text = self.create_element(
            "box",
            "",
            label=".text (Combined Code)",
            position=executable.get_center() + UP * 0.4,
            color=self.colors["code"],
            height=0.6,
            width=3.5,
            fill_opacity=0.2,
        )

        exe_data_id, exe_data = self.create_element(
            "box",
            "",
            label=".data (Combined Data)",
            position=executable.get_center() - UP * 0.3,
            color=BLUE_C,
            height=0.6,
            width=3.5,
            fill_opacity=0.2,
        )

        exe_libs_id, exe_libs = self.create_element(
            "box",
            "",
            label="Dynamic Libraries",
            position=executable.get_center() - UP * 1,
            color=TEAL_B,
            height=0.6,
            width=3.5,
            fill_opacity=0.2,
        )

        # Animate the executable file structure
        self.play(Create(executable), run_time=0.8)

        self.play(
            Create(exe_header),
            Create(exe_text),
            Create(exe_data),
            Create(exe_libs),
            run_time=1.2,
        )

        # Explain linking process
        linking_steps_id, linking_steps = self.create_element(
            "text",
            "Linking Process:",
            size=20,
            position=DOWN * 1.5 + LEFT * 2,
            color=self.colors["sub_phase"],
        )

        steps = [
            "1. Collect all object files and libraries",
            "2. Resolve external references (symbols)",
            "3. Combine all sections of same type",
            "4. Set memory addresses for code and data",
            "5. Create executable header and structure",
        ]

        step_texts = []
        for i, step in enumerate(steps):
            step_id, step_obj = self.create_element(
                "text",
                step,
                size=16,
                position=DOWN * (2 + i * 0.4) + LEFT * 1,
                color=WHITE,
            )
            step_texts.append((step_id, step_obj))

        self.play(Write(linking_steps), run_time=0.8)

        for _, step_obj in step_texts:
            self.play(Write(step_obj), run_time=0.5)

        # Executable file representation
        exe_file_id, exe_file = self.create_element(
            "file",
            "a.out",
            position=executable.get_bottom() + DOWN * 0.5,
            color=WHITE,
            size=18,
        )

        self.play(Create(exe_file), run_time=0.8)
        self.wait(2)

    def animate_summary(self):
        """
        Animate the summary of the compilation pipeline.

        Educational objectives:
        1. Reinforce understanding of the complete compilation process
        2. Summarize key insights from each phase
        3. Provide a cohesive overview of the compiler pipeline
        """
        # Display the summary points first before transitioning to summary phase
        summary_points = self.create_summary_points()
        summary_group = VGroup()

        for i, point in enumerate(summary_points):
            title = Text(point["title"], font_size=24, color=self.colors["main_phase"])
            insight = Text(point["insight"], font_size=18, color=WHITE)

            point_group = VGroup(title, insight)
            point_group.arrange(DOWN, aligned_edge=LEFT)

            if i == 0:
                point_group.to_edge(LEFT).shift(UP * 0.5)
            else:
                point_group.next_to(summary_group, DOWN, buff=0.4, aligned_edge=LEFT)

            summary_group.add(point_group)

            self.play(Write(title), run_time=self.timing["standard"])

            self.play(FadeIn(insight), run_time=self.timing["brief"])

            self.wait(self.timing["wait_brief"])

        # Transition to final summary phase
        self.transition_to_phase("summary", "Compiler Pipeline Summary")

        # Create a horizontal arrow representing the full pipeline
        pipeline_arrow_id, pipeline_arrow = self.create_element(
            "arrow", "", color=self.colors["arrow"], position=ORIGIN, buff=0.3
        )
        pipeline_arrow.put_start_and_end_on(LEFT * 5, RIGHT * 5)

        self.play(GrowArrow(pipeline_arrow), run_time=1.2)

        # Create labels for each step along the pipeline
        pipeline_steps = [
            "Source\nCode",
            "Preprocessor",
            "Lexer",
            "Parser",
            "IR",
            "Optimizer",
            "Code\nGenerator",
            "Assembler",
            "Linker",
            "Executable",
        ]

        step_positions = [
            LEFT * 5,
            LEFT * 4,
            LEFT * 3,
            LEFT * 2,
            LEFT * 1,
            ORIGIN,
            RIGHT * 1,
            RIGHT * 2,
            RIGHT * 3,
            RIGHT * 4,
        ]

        step_icons = []
        step_labels = []

        for i, (step, pos) in enumerate(zip(pipeline_steps, step_positions)):
            # Create a small icon for each step
            if i == 0:  # Source code
                icon_id, icon = self.create_element(
                    "file", ".c", position=pos + UP * 0.8, color=WHITE, size=16
                )
            elif i == 9:  # Executable
                icon_id, icon = self.create_element(
                    "file",
                    "exe",
                    position=pos + UP * 0.8,
                    color=self.colors["success"],
                    size=16,
                )
            else:
                icon_id, icon = self.create_element(
                    "box",
                    "",
                    position=pos + UP * 0.8,
                    color=self.colors["main_phase"],
                    height=0.4,
                    width=0.4,
                    fill_opacity=0.2,
                )

            # Create a label for each step
            label_id, label = self.create_element(
                "text", step, size=14, position=pos + DOWN * 0.5, color=WHITE
            )

            step_icons.append((icon_id, icon))
            step_labels.append((label_id, label))

        # Animate the pipeline steps
        self.play(*[Create(icon) for _, icon in step_icons], run_time=1.5)

        self.play(*[Write(label) for _, label in step_labels], run_time=1.5)

        # Final message
        final_id, final = self.create_element(
            "text",
            "The modern compiler is a complex pipeline that transforms\nhigh-level code into efficient machine instructions",
            size=24,
            position=DOWN * 2,
            color=self.colors["success"],
        )

        self.play(Write(final), run_time=1.5)

        # Add educational learning assessment
        self.wait(1.5)
        self.show_learning_assessment()
