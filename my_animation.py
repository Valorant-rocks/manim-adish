from manim import *
from pathlib import Path
#Cricle

##%%manim -qm Intro
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

        # chaine kura ho
        self.wait()
        
# class Triangle_rendering(Scene):
#     def construct(self):
        angular=PI/180 *25
        vertices_sin = [
            np.array([0, 0, 0]), 
            np.array([3*np.cos(angular),3*np.sin(angular), 0]),  
            np.array([3*np.cos(angular),0, 0]), 
        ]
        radius_tan=3/np.cos(angular)
        vertices_tan =[
            np.array([0,0,0]),
            np.array([radius_tan*np.cos(angular),radius_tan*np.sin(angular),0]),
            np.array([3,0,0]),
          
        ]

     

        triangle_sin = Polygon(*vertices_sin, color=WHITE)
        triangle_tan = Polygon(*vertices_tan, color=WHITE)
        self.play(Create(triangle_sin),run_time=3)
        self.play(Create(triangle_tan),run_time=3)
        self.wait()
        together=VGroup(triangle_sin,circ,diameter_signifier,triangle_tan,radius_text)
        self.play(together.animate.move_to(3*LEFT))        
        self.play((triangle_sin.animate.move_to(5*RIGHT+2*UP)))
        self.wait()        

        # duplicate both the triangles, enlarge it and use theta and arc symbol