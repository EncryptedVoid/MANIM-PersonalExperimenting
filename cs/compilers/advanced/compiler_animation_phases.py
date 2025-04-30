# compiler_animation_phases.py
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
        # Introduction sequence
        pass

    def animate_preprocessor_phase(self):
        # Preprocessor phase animation
        pass

    def animate_lexer_phase(self):
        # Lexer phase animation
        pass

    def animate_parser_phase(self):
        # Parser phase animation
        pass

    # Other phase-specific animation methods...
