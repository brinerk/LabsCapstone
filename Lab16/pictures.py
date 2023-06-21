from manim import *

class Potential(Scene):
    def construct(self):
        numberplane = NumberPlane()
        tex1 = Text("q1").next_to([-4,0,0],UP)
        tex2 = Text("q2").next_to([4,0,0],UP)

        tex3 = Text("-d/2").next_to([-4,0,0],DOWN)
        tex4 = Text("-d/2").next_to([4,0,0],DOWN)

        circle_1 = Circle(radius = 0.25, color=RED, fill_opacity = 1).next_to([4,0,0])
        circle_2 = Circle(radius = 0.25, color=RED, fill_opacity = 1).next_to([-4,0,0])

        self.add(numberplane, tex1, tex2, tex3, tex4, circle_1, circle_2)
