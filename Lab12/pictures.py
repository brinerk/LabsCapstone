from manim import *

class Scattering(Scene):
    def construct(self):
        numberplane = NumberPlane()
        tex1 = Text("m1")
        tex2 = Text("m2").next_to(ORIGIN,DOWN)

        tex3 = Text("m2").next_to([4,2,0],UP)
        tex4 = Text("m1").next_to([3,-2,0],DOWN)

        circle_1 = Circle(radius = 1.0, color=BLUE, fill_opacity =1)
        circle_2 = Circle(radius = 1.0, color=RED, fill_opacity = 1)

        circle3 = Circle(radius = 1.0, color=BLUE).shift(3*RIGHT + 2*DOWN)
        circle4 = Circle(radius = 1.0, color=RED).shift(4*RIGHT + 2*UP)

        group = Group(circle_1, tex1)
        group2 = Group(circle_2, tex2)

        group3 = Group(tex3, circle3)
        group4 = Group(tex4, circle4)

        arrow = Arrow(ORIGIN, [4,2,0], buff = 0)
        arrow2 = Arrow(ORIGIN, [3,-2,0], buff = 0)

        group.shift(1*DOWN + 4*LEFT)


        self.add(numberplane, group, group2, group3, group4, arrow, arrow2)
