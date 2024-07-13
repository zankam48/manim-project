from manim import *

class Positioning(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT) # RIGHT == [1, 0, 0]
        self.add(red_dot, green_dot)
