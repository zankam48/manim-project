from manim import *

class GeometricSeriesReel(Scene):
    def construct(self):
        # Initial square
        square = Square(side_length=4, fill_opacity=1, color=BLUE)
        self.play(Create(square))
        self.wait(0.5)

        # Text overlay
        text = Text("1 + 1/2 + 1/4 + 1/8 + ... = ?", font_size=36)
        text.next_to(square, DOWN)
        self.play(Write(text))
        self.wait(1)

        # Iteratively divide and add
        fractions = [1/2, 1/4, 1/8, 1/16]  # Add more fractions for longer animation
        sum_so_far = 1
        for fraction in fractions:
            new_square = square.copy()
            new_square.scale(fraction)
            new_square.next_to(square, RIGHT, buff=0.1)
            self.play(Transform(square, new_square), run_time=0.8)
            sum_so_far += fraction

            # Update text with current sum (optional)
            # new_text = Text(f"Sum so far: {sum_so_far:.3f}", font_size=24)
            # new_text.next_to(square, DOWN)
            # self.play(Transform(text, new_text))

        # Zoom in on final result
        self.play(square.animate.scale(1.2))
        self.wait(0.5)

        # Final answer reveal
        answer_text = Text("= 2", font_size=48, color=YELLOW)
        answer_text.next_to(text, RIGHT)
        self.play(Write(answer_text))

        # End screen
        self.wait(1)
        end_text = Text("Follow for more math magic!", font_size=32)
        end_text.shift(DOWN * 2)
        self.play(FadeIn(end_text))
        self.wait(2)  # Show end screen for a bit longer
