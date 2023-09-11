from manim import *

#Cricle
class Intro(Scene):
    def construct(self):
        circ = Circle(radius=3, color=WHITE)
        sqr = Square()
        numberplane = NumberPlane()
        equation = MathTex("x^2+y^2=r^2")
        diameter_signifier = Line(start=[0, 0, 0], end=[3, 0, 0])
        self.play(
            Write(equation)
        )

        self.play(equation.animate.move_to((3*UP+5*RIGHT)), run_time=2)
        self.wait()
        self.play(Create(diameter_signifier))
        radius_text = MathTex("r")
        self.play(Write(radius_text.move_to([1.5, -0.2, 0])))
        self.play(Rotate(VGroup(diameter_signifier,radius_text),2*PI,about_point=[0,0,0],run_time=2),Create(circ),run_time=2)
        
        self.wait()

