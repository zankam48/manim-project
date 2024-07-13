from manim import *

class GeometricSeriesIntro(Scene):
    def construct(self):
        series = MathTex("1 + \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\ldots")
        self.play(Write(series))
        self.wait(2)

class WholeSquare(Scene):
    def construct(self):
        square = Square().scale(2)
        label = Tex("1").move_to(square.get_center())
        self.play(Create(square), Write(label))
        self.wait(1)
        self.play(square.animate.set_fill(BLUE, opacity=0.5))
        self.wait(2)

class AddHalf(Scene):
    def construct(self):
        square = Square().scale(2)
        half = Rectangle(width=2, height=1).move_to(square.get_center()).align_to(square, UP)
        label = Tex("1").move_to(square.get_center())
        half_label = Tex("1/2").move_to(half.get_center())
        self.play(Create(square), Write(label))
        self.wait(1)
        self.play(Create(half), Write(half_label))
        self.wait(1)
        self.play(half.animate.set_fill(YELLOW, opacity=0.5))
        self.wait(2)

class AddQuarter(Scene):
    def construct(self):
        square = Square().scale(2)
        half = Rectangle(width=2, height=1).move_to(square.get_center()).align_to(square, UP)
        quarter = Rectangle(width=1, height=1).next_to(half, DOWN, buff=0)
        label = Tex("1").move_to(square.get_center())
        half_label = Tex("1/2").move_to(half.get_center())
        quarter_label = Tex("1/4").move_to(quarter.get_center())
        self.play(Create(square), Write(label))
        self.wait(1)
        self.play(Create(half), Write(half_label))
        self.wait(1)
        self.play(half.animate.set_fill(YELLOW, opacity=0.5))
        self.play(Create(quarter), Write(quarter_label))
        self.wait(1)
        self.play(quarter.animate.set_fill(RED, opacity=0.5))
        self.wait(2)

class ContinueSeries(Scene):
    def construct(self):
        square = Square().scale(2)
        half = Rectangle(width=2, height=1).move_to(square.get_center()).align_to(square, UP)
        quarter = Rectangle(width=1, height=1).next_to(half, DOWN, buff=0)
        eighth = Rectangle(width=1, height=0.5).next_to(quarter, DOWN, buff=0)
        label = Tex("1").move_to(square.get_center())
        half_label = Tex("1/2").move_to(half.get_center())
        quarter_label = Tex("1/4").move_to(quarter.get_center())
        eighth_label = Tex("1/8").move_to(eighth.get_center())
        self.play(Create(square), Write(label))
        self.wait(1)
        self.play(Create(half), Write(half_label))
        self.wait(1)
        self.play(half.animate.set_fill(YELLOW, opacity=0.5))
        self.play(Create(quarter), Write(quarter_label))
        self.wait(1)
        self.play(quarter.animate.set_fill(RED, opacity=0.5))
        self.play(Create(eighth), Write(eighth_label))
        self.wait(1)
        self.play(eighth.animate.set_fill(GREEN, opacity=0.5))
        self.wait(2)

class SumSeries(Scene):
    def construct(self):
        series = MathTex("1 + \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\ldots = 2")
        self.play(Write(series))
        self.wait(2)

class Conclusion(Scene):
    def construct(self):
        final_result = MathTex("1 + \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\ldots = 2")
        check_mark = Tex("✓").scale(2).set_color(GREEN).next_to(final_result, RIGHT)
        self.play(Write(final_result))
        self.wait(1)
        self.play(Write(check_mark))
        self.wait(2)