from manim import *
from pathlib import Path

# Cricle
# %%manim -qm -v WARNING Intro 


# %%manim -qm -v WARNING Intro 



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
        self.play(Rotate(VGroup(diameter_signifier, radius_text), 2*PI,
                  about_point=[0, 0, 0], run_time=2), Create(circ), run_time=2)

        # chaine kura ho
        self.wait()

# class Triangle_rendering(Scene):
#     def construct(self):
        angular = PI/180 * 25
        vertices_sin = [
            np.array([0, 0, 0]),
            np.array([3*np.cos(angular), 3*np.sin(angular), 0]),
            np.array([3*np.cos(angular), 0, 0]),
        ]
       

        radius_tan = 3/np.cos(angular)
        vertices_tan = [
            np.array([0, 0, 0]),
            np.array([radius_tan*np.cos(angular),
                     radius_tan*np.sin(angular), 0]),
            np.array([3, 0, 0]),

        ]

        self.play(FadeOut(radius_text))
        triangle_sin = Polygon(*vertices_sin, color=BLUE)
        triangle_tan = Polygon(*vertices_tan, color=GREEN)

        alpha_signifier = ArcBetweenPoints(start=[0.5, 0, 0], end=[
                                           0.5, np.sin(angular)*0.5, 0], angle=angular, radius=0.3)
        theta_signifier = ArcBetweenPoints(
            start=[0.5, 0, 0], end=[0.50, np.tan(angular)*0.5, 0], angle=angular, radius=0.3)
        self.play(Create(triangle_sin), run_time=3)
        
        self.play(Create(triangle_tan), run_time=3)
        self.play(Create(theta_signifier))
        self.play(Create(alpha_signifier))
        theta=MathTex(r"\theta")
        theta_=MathTex(r"\theta")
        theta.font_size=30
        theta_.font_size=30
        self.add(theta.next_to(theta_signifier,RIGHT,buff=0.1)),
        self.add(theta_.next_to(alpha_signifier,RIGHT,buff=0.1))
        

        self.wait()
        together = VGroup(triangle_sin, circ, diameter_signifier,
                          triangle_tan, alpha_signifier, theta_signifier,theta,theta_)
        tan_group= VGroup(triangle_tan,alpha_signifier,theta_)
        self.play(together.animate.move_to(3*LEFT))
        # self.play((lines.animate.move_to(5*RIGHT+2*UP)))
        self.wait()


        vertices_sin_copy=Line(start=[-3,0,0],end=[np.cos(angular)*3-3,0,0],color=BLUE)
        self.add(vertices_sin_copy)
        self.play(tan_group.animate.rotate(-PI,about_point=[-3,0,0]))
        self.wait()
        vertices_sin_a = Line(start=[-3, 0, 0], end=[
                              3*np.cos(angular)-3, 3*np.sin(angular), 0])
        vertices_sin_b = Line(
            start=[3*np.cos(angular)-3, 0, 0], end=[3*np.sin(angular)-3, 0, 0])
        vertices_sin_c = Line(start=[3*np.sin(angular)-3, 0, 0], end=[-3, 0, 0])
       


        self.play(FadeOut(vertices_sin_copy))

#-----------------------------------------------------------------------
        important=Brace(vertices_sin_a,sharpness=2,direction=(vertices_sin_a.copy().rotate(PI/2).get_unit_vector()))
        self.play(Create(important))
        important_text=important.get_tex("r")
        self.play(Write(important_text))
        sin_=VGroup(triangle_sin,theta_signifier,theta,important,important_text)
        self.play(sin_.animate.move_to(5*RIGHT+1.5*UP))
        tex_1=MathTex(r"sin(\theta)=P_1/H")
        tex_2=MathTex(r"Hsin(\theta)=P_1")
        tex_3=MathTex(r"P_1=rsin(\theta)")
        tex_4=MathTex(r"P_1")
        self.play(Write(
        tex_1.next_to(triangle_sin,DOWN),))
        self.wait()
        self.play(Write(tex_2.next_to(tex_1,DOWN)))
        self.wait()
        self.play(Write(tex_3.next_to(tex_2,DOWN)))
        self.wait()

        vertices_sin_a = Line(start=[-3, 0, 0], end=[
                              3*np.cos(angular)-3, 3*np.sin(angular), 0])
        vertices_sin_b = Line(
            start=[3*np.cos(angular)+7-3,0.5, 0], end=[3*np.cos(angular)+7-3, 3*np.sin(angular)+0.5, 0])
        vertices_sin_c = Line(start=[-3*np.sin(angular)+3, 0, 0], end=[-3, 0, 0])
       
        self.play(
            FadeOut(tex_1),
            FadeOut(tex_2)),
        self.play(tex_3.animate.next_to(triangle_sin,DOWN))
        self.wait()
        self.play(sin_.animate.move_to(2*RIGHT+1.5*UP))
        
        important1=Brace(vertices_sin_b,sharpness=1,direction=(vertices_sin_b.copy().rotate(-PI/2).get_unit_vector()))
        self.play(important1.animate.next_to(triangle_sin,RIGHT))
        self.play(tex_3.animate.next_to(important1,RIGHT))
        self.wait()
       
        reverse=VGroup(triangle_sin,theta,theta_signifier,important,important_text,important1,tex_3)
        reverse_coordinates=[-PI,0,0]
        self.play(reverse.animate.align_to(reverse_coordinates,LEFT))
        self.play(reverse.animate.align_to([-3,0,0],DOWN))
        self.wait()
# np.array([0, 0, 0]),
#             np.array([radius_tan*np.cos(angular),
#                      radius_tan*np.sin(angular), 0]),
#             np.array([3, 0, 0]),

#             vertices_tan_a=Line(start=[-3,0,0],end=[radius_tan*np.cos(angular)-3,]
        
        
        self.play(FadeOut(important,important_text))
        
        radius_tan_ez=Line(start=[-3,0,0],end=[-6,0,0])
        important_tan=Brace(radius_tan_ez,sharpness=1,direction=(radius_tan_ez.copy().rotate(-PI/2).get_unit_vector()))
        important_tan_text=important_tan.get_tex("r")
        self.play(FadeOut(tex_3),
        tex_4.animate.next_to(important1,RIGHT,buff=0.3)  
        )
        self.play(Create(important_tan))
        self.play(Write(important_tan_text))
        self.wait()

       

        tan_group_=VGroup(triangle_tan,alpha_signifier,theta_,important_tan,important_tan_text)
        self.play(tan_group_.animate.move_to(5*RIGHT+1.2*UP))

        tex_1_=MathTex(r"tan(\theta)=P_2/B")
        tex_2_=MathTex(r"Btan(\theta)=P_2")
        tex_3_=MathTex(r"P_2=rtan(\theta)",font_size=40)
        tex_4_=MathTex(r"P_2",font_size=40)
        self.play(Write(
        tex_1_.next_to(triangle_tan,DOWN),))
        self.wait()
        self.play(Write(tex_2_.next_to(tex_1_,DOWN)))
        self.wait()
        self.play(Write(tex_3_.next_to(tex_2_,DOWN)))
        self.wait()
        important_tan_=Brace(vertices_sin_b,sharpness=1,direction=(vertices_sin_b.copy().rotate(PI/2).get_unit_vector()))
        self.play(Create(important_tan_.next_to(triangle_tan,LEFT)))
        self.play(
            FadeOut(tex_1_),
            FadeOut(tex_2_),
            tex_3_.animate.next_to(triangle_tan,DOWN),
            FadeOut(important_tan),
            FadeOut(important_tan_text)
        )
        self.play(tex_3_.animate.next_to(important_tan_,LEFT))
        reverse_=VGroup(triangle_tan,theta_,alpha_signifier,important_tan_,tex_4_)
        self.play(FadeOut(tex_3_),
        tex_4_.animate.next_to(important_tan_,LEFT,buff=0.2)  
        )
        reverse_coordinates_=[-3,0,0]
        self.play(reverse_.animate.align_to(reverse_coordinates_,RIGHT))
        self.play(reverse_.animate.align_to([-6,0,0],UP))
        self.wait()

        self.wait()

        final_tex=MathTex(r"P_1",font_size=35)
        final_tex_=MathTex(r"p_2",font_size=35)
        
        final=VGroup(tex_4_,important_tan_)
        final_=VGroup(tex_4,important1)
        self.play(FadeOut(final),
                 FadeOut(final_)
        )
        self.play(tan_group.animate.rotate(PI,about_point=[-3,0,0]),run_time=3)
        self.play(FadeOut(alpha_signifier,theta_))
        important_signifier = ArcBetweenPoints(
            start=[0, 0, 0], end=[3*np.cos(angular)-3,3*np.sin(angular), 0], angle=angular, radius=3)
        line_important=Line(start=[3*np.cos(angular)-3,0,0],end=[3*np.cos(angular)-3,3*np.sin(angular),0],color=BLUE)
        line_important_=Line(start=[0,0,0],end=[radius_tan*np.cos(angular)-3,radius_tan*np.sin(angular), 0],color=GREEN)
        important_group=VGroup(important_signifier,line_important,line_important_)
        ggez=VGroup(triangle_tan,line_important_)

        self.play(ggez.animate.move_to(3*RIGHT))
        self.play(FadeOut(triangle_tan))
        self.play(line_important_.animate.rotate(PI/2))
        self.play(Write(tex_4_.next_to(line_important_,DOWN)))
        tex_3_=MathTex(r"P_2=rtan(\theta)",font_size=40)
        self.play(Write(tex_3_.next_to(tex_4_,DOWN)))

        imp_group=VGroup(line_important_,tex_3_,tex_4_)
        self.play(imp_group.animate.move_to(2*RIGHT+1*UP))


        important_group_1=VGroup(line_important,triangle_sin,theta,theta_signifier)
        self.play(important_group_1.animate.move_to(3*RIGHT))
        self.play(FadeOut(triangle_sin),
        FadeOut(theta),
        FadeOut(theta_signifier))

        self.play(line_important.animate.rotate(PI/2))
        self.play(Write(tex_4.next_to(line_important,DOWN)))
        self.play(Write(tex_3.next_to(tex_4,DOWN)))
        imp_group_=VGroup(tex_4,tex_3,line_important)
        self.play(imp_group_.animate.move_to(1*UP+5*RIGHT))
        line_imp=Line(start=[-3,0,0],end=[3*np.cos(angular)-3,3*np.sin(angular),0])
        self.play(Create(line_imp))

        last_group=VGroup(diameter_signifier,line_imp,important_signifier)
        self.play(last_group.animate.move_to(4*RIGHT+1*DOWN))
        self.play(
            FadeOut(diameter_signifier),
            FadeOut(line_imp)
        )        

        self.play(important_signifier.animate.rotate(-PI/2))
        r_text=MathTex(r"S=r\theta")
        self.play(Write(r_text.next_to(important_signifier,DOWN,buff=0.5))
        )

        self.play(important_signifier.animate.set_fill(RED))
        important_signifier.color=RED
        self.play(FadeOut(circ))
        tan_=Line(start=[-3,0,0],end=[radius_tan*np.cos(angular)-3,
                     radius_tan*np.sin(angular), 0])
        
        tex_imp=MathTex(r"S")
        self.play(FadeOut(r_text))
        self.play(tex_imp.animate.next_to(important_signifier,DOWN,buff=0.5)
        )
        
        self.play(triangle_tan.animate.move_to(3*LEFT))
        self.play(triangle_tan.animate.align_to([-3,0,0],DOWN))
        self.play(
            FadeOut(tex_3),
            FadeOut(tex_3_),
            
        )
       
        # tex_3=MathTex(r"P_2",font_size)
        tan_0=VGroup(line_important_,tex_4_)
        sin_0=VGroup(line_important,tex_4)
        arc_0=VGroup(important_signifier,tex_imp)
    
        self.play(tan_0.animate.rotate(PI/2))
        self.play(tan_0.animate.next_to(triangle_tan,RIGHT,buff=0))
        

        self.play(sin_0.animate.rotate(PI/2))
        
        self.play(sin_0.animate.move_to([PI*np.sin(angular)-2.8,0,0]))
        self.play(sin_0.animate.align_to([np.cos(angular)-3,0,0],DOWN))
    
        self.play(tex_4.animate.next_to(line_important,LEFT))
        self.play(important_signifier.animate.move_to([PI*np.sin(angular)-2.8,0,0]))
        self.play(important_signifier.animate.align_to([np.cos(angular)-3,0,0],DOWN))
        starting_coords=[3*np.cos(angular)-4.5,0,0]
        ending_coords=[3*np.cos(angular)-4.5,3*np.sin(angular),0]
        arc_important=ArcBetweenPoints(starting_coords,ending_coords,radius=3,color=RED)
        self.play(FadeOut(tex_imp))
        self.play(Transform(important_signifier,arc_important))

        alpha_signifier2 = ArcBetweenPoints(start=[-4, 0, 0], end=[
                                           -4, np.sin(angular)*0.5, 0], angle=angular, radius=0.3)
        self.play(Create(alpha_signifier2))
        self.add(theta.next_to(alpha_signifier2,RIGHT,buff=0.1))
        mega=VGroup(alpha_signifier2,theta,triangle_tan,arc_important,tex_4,tex_4_,line_important,line_important_)
        self.play(mega.animate.move_to(0*RIGHT+0*LEFT+0*UP+0*DOWN))
        self.play(important_signifier.animate.move_to(3*UP+4*LEFT))
        self.play(important_signifier.animate.rotate(PI/2))
        noob=ArcBrace(important_signifier)
        noob_=MathTex(r"S=r\theta",font_size=35)
        noob_tex=Tex("Remember that",font_size=35)
        order=MathTex(r"P_1=rsin(\theta)",font_size=35)
        order1=MathTex(r"P_2=rtan(\theta)",font_size=35)
        self.play(Write(noob_.next_to(important_signifier,DOWN)))
        self.play(Write(noob_tex.next_to(noob_,DOWN)))
        self.play(Write(order.next_to(noob_tex,DOWN)))
        self.play(Write(order1.next_to(order,DOWN)))
        self.play((ScaleInPlace(mega,2)))

        
        a=line_important.get_start()
        a_=line_important.get_end()

        b=line_important_.get_start()
        b_=line_important_.get_end()

        c=arc_important.get_start()
        c_=arc_important.get_end()

        self.play(mega.animate.move_to(0*LEFT+0*RIGHT+0*UP+0*DOWN))
        self.play(mega.animate.align_to([-4,-2,0],LEFT))
        self.play(mega.animate.align_to([0,-2,0],DOWN))
        mega_fuck=VGroup(theta)
        self.play(Transform(tex_4,order))
        self.play(Transform(tex_4_,order1))
        self.play(FadeOut(mega_fuck))
        self.play(line_important.animate.rotate(PI/2).next_to((order),RIGHT))
        self.play(line_important_.animate.rotate(PI/2).next_to((order1),RIGHT))
        text_imp=MathTex("=")
        self.play(FadeOut(triangle_tan,alpha_signifier2,arc_important))
        self.play(FadeOut(equation))
        ez=Tex(r"Let's Decrease the angle").move_to(3*RIGHT+3*UP)
        self.play(Write(ez))



        
        angular_tracker = ValueTracker(25)

       
        angular_display = DecimalNumber(angular_tracker.get_value(), num_decimal_places=2)
        angular_display.add_updater(lambda d: d.set_value(angular_tracker.get_value()))

      

        
        angular_label = MathTex(r"\theta =").next_to(angular_display, LEFT)
        ezDemon1=VGroup(angular_display,angular_label)

        tan_display = DecimalNumber(np.tan(np.radians(angular_tracker.get_value())), num_decimal_places=2)
        sin_display = DecimalNumber(np.sin(np.radians(angular_tracker.get_value())), num_decimal_places=2)

        tan_display.add_updater(lambda d: d.set_value(np.tan(np.radians(angular_tracker.get_value()))))
        sin_display.add_updater(lambda d: d.set_value(np.sin(np.radians(angular_tracker.get_value()))))


        sin_display=sin_display.next_to(ez,DOWN)
        tan_display=tan_display.next_to(sin_display,DOWN)
        tan_label = MathTex(r"\tan(\theta) =").next_to(tan_display, LEFT)
        sin_label = MathTex(r"\sin(\theta) =").next_to(sin_display, LEFT)
        
        self.play(Write(angular_label))
        self.play(Write(angular_display))
        
        self.play(Write(sin_label))
        self.play(Write(sin_display))

        self.play(Write(tan_label))
        self.play(Write(tan_display))

        




        
        angular_display=angular_display.next_to(tan_display,DOWN)
        angular_label=angular_label.next_to(angular_display,LEFT)

        
        


        self.wait(2)

        # Create initial shapes
        triangle_tan_1 = self.create_triangle_tan(angular_tracker.get_value())
        triangle_sin_1 = self.create_triangle_sin(angular_tracker.get_value())
        arc_sin_1 = self.create_arc_sin(angular_tracker.get_value())

        # Add the shapes and the angular display to the scene
        self.play(Create(triangle_tan_1))
        self.play(Create (triangle_sin_1))
        self.play(Create( arc_sin_1))
        self.play(Create(angular_display))

        # Animation to continuously update shapes
        self.play(
            angular_tracker.animate.set_value(0),
            UpdateFromFunc(triangle_tan_1, lambda mob: mob.become(self.create_triangle_tan(angular_tracker.get_value()))),
            UpdateFromFunc(triangle_sin_1, lambda mob: mob.become(self.create_triangle_sin(angular_tracker.get_value()))),
            UpdateFromFunc(arc_sin_1, lambda mob: mob.become(self.create_arc_sin(angular_tracker.get_value()))),
            run_time=7,
            rate_func=linear,
        )

        

    def create_triangle_tan(self, angular):
        starting_co_tan = [
            np.array([-4, -2, 0]),                # constant
            np.array([2, -2, 0]),                 # constant
            np.array([2, 6 * np.tan(np.radians(angular)) - 2, 0])
        ]
        return Polygon(*starting_co_tan, color=GREEN)

    def create_triangle_sin(self, angular):
        starting_co_sin = [
            np.array([-4, -2, 0]),                # constant
            np.array([1.437, -2, 0]),             # constant
            np.array([1.437, 6 * np.sin(np.radians(angular)) - 2, 0])
        ]
        return Polygon(*starting_co_sin, color=BLUE)

    def create_arc_sin(self, angular):
        arc_starting = [1.437, - 2, 0]
        arc_end = [1.437, 6 * np.sin(np.radians(angular))-2, 0]
        return ArcBetweenPoints(start=arc_starting, end=arc_end, angle=np.radians(angular), radius=6)

        self.wait(2)


class Second(Scene):
    def construct(self):
        ez1 = Tex("Observe Closely")
        self.play(Write(ez1))
        self.wait(2)
        self.play(FadeOut(ez1))

        angular_tracker = ValueTracker(25)

        # Create DecimalNumber to display angular
        angular_display = DecimalNumber(angular_tracker.get_value(), num_decimal_places=2)
        angular_display.add_updater(lambda d: d.set_value(angular_tracker.get_value()))

        # Add a label for the angular display
        angular_label = MathTex(r"S=\theta =").next_to(angular_display, LEFT)
        ezDemon1 = VGroup(angular_display, angular_label)

        tan_display = DecimalNumber(np.tan(np.radians(angular_tracker.get_value())), num_decimal_places=5)
        sin_display = DecimalNumber(np.sin(np.radians(angular_tracker.get_value())), num_decimal_places=5)

        # Add updaters to continuously update tan and sin values
        tan_display.add_updater(lambda d: d.set_value(np.tan(np.radians(angular_tracker.get_value()))))
        sin_display.add_updater(lambda d: d.set_value(np.sin(np.radians(angular_tracker.get_value()))))

        # Position and add the displays to the scene
        angular_label = angular_label.move_to(3 * RIGHT + 3 * UP)
        angular_display = angular_display.next_to(angular_label, RIGHT)
        sin_label=MathTex(r"\sin(\theta) =").next_to(angular_label, DOWN)
        sin_display = sin_display.next_to(sin_label, RIGHT)
        tan_label = MathTex(r"\tan(\theta) =").next_to(sin_label, DOWN)
        tan_display = tan_display.next_to(tan_label, RIGHT)

        

        self.play(Write(angular_label))
        self.play(Write(angular_display))

        self.play(Write(sin_label))
        self.play(Write(sin_display))
        self.play(Write(tan_label))
        self.play(Write(tan_display))

        self.wait(2)

        # Create initial shapes
        triangle_tan_1 = self.create_triangle_tan(angular_tracker.get_value())
        triangle_sin_1 = self.create_triangle_sin(angular_tracker.get_value())
        arc_sin_1 = self.create_arc_sin(angular_tracker.get_value())

        # Add the shapes and the angular display to the scene
        self.play(Create(triangle_tan_1))
        self.play(Create(triangle_sin_1))
        self.play(Create(arc_sin_1))
        self.play(Create(angular_display))

        # Animation to continuously update shapes
        self.play(
            angular_tracker.animate.set_value(0),
            UpdateFromFunc(triangle_tan_1, lambda mob: mob.become(self.create_triangle_tan(angular_tracker.get_value()))),
            UpdateFromFunc(triangle_sin_1, lambda mob: mob.become(self.create_triangle_sin(angular_tracker.get_value()))),
            UpdateFromFunc(arc_sin_1, lambda mob: mob.become(self.create_arc_sin(angular_tracker.get_value()))),
            run_time=10,
            rate_func=linear,
        )

        # Code defined within construct(self) is executed here
        self.wait(3)
        ez3 = MathTex(r"\theta")
        self.add(ez3)

    def create_triangle_tan(self, angular):
        starting_co_tan = [
            np.array([-4, -2, 0]),  # constant
            np.array([2, -2, 0]),  # constant
            np.array([2, 6 * np.tan(np.radians(angular)) - 2, 0])
        ]
        return Polygon(*starting_co_tan, color=GREEN)

    def create_triangle_sin(self, angular):
        starting_co_sin = [
            np.array([-4, -2, 0]),  # constant
            np.array([1.437, -2, 0]),  # constant
            np.array([1.437, 6 * np.sin(np.radians(angular)) - 2, 0])
        ]
        return Polygon(*starting_co_sin, color=BLUE)

    def create_arc_sin(self, angular):
        arc_starting = [1.437, - 2, 0]
        arc_end = [1.437, 6 * np.sin(np.radians(angular)) - 2, 0]
        return ArcBetweenPoints(start=arc_starting, end=arc_end, angle=np.radians(angular), radius=6)
    
        
class third(Scene):
    def construct(self):
        w=Tex("Lets look at the different values at 4 random instances in the previous scene",font_size=40)
        self.play(Write(w))
        self.wait(1.5)
        self.play(FadeOut(w))
        w1=MathTex(r"\theta(Radian)")
        w2=MathTex(r"sin(\theta)")
        w3=MathTex(r"tan(\theta)")
        w_4=MathTex(r"\theta(Degree)")
        t_0=MathTable(
            [[25,0.436,0.422,0.466],
            [18.67,0.325,0.320,0.337],
            [7.58,0.132,0.131,0.133],
            [0,0,0,0]],
        col_labels=[w_4,w1,w2,w3]
        )
        self.add((t_0))
        self.wait(5)
        g1=Group(t_0)
        self.play(ScaleInPlace(g1,0.5))
        self.play(g1.animate.to_edge(UP))

        w_1=Tex("From the table we conclude that:")
        self.play(Write(w_1))
        self.wait()
        self.play(w_1.animate.next_to(t_0,DOWN))
        w_2=MathTex(r"sin(\theta)\leq\theta\leq tan(\theta)")
        w_2=w_2.next_to(w_1,DOWN)
        self.play(Write(w_2))
        w_fuck=Tex(r"Only When Theta is measured in radians")
        w_fuck.next_to(w_2,DOWN)
        w_fuckbox=SurroundingRectangle(w_fuck,buff=0.1)
        self.play(Write(w_fuck))
        self.play(Create(w_fuckbox))
        self.wait(2)



class fourth(Scene):
    def construct(self):
        w_2=MathTex(r"sin(\theta)\leq\theta\leq tan(\theta),",font_size=40)
        w_2.to_edge(UP)
        self.play(Write(w_2))
        self.wait(2)
        w_fuck_=MathTex(r"\theta=\quad radian",font_size=40)
        w_fuck_.next_to(w_2,RIGHT,buff=0.5)
        self.play(Write(w_fuck_))
        self.wait()
        w_fuck_box=SurroundingRectangle(w_fuck_,buff=0.1)
        self.play(Create(w_fuck_box))
        w_3=MathTex(r"\frac{1}{sin(\theta)} \geq \frac{1}{\theta} \geq \frac{1}{tan(\theta)}",font_size=40)
        w_3.next_to(w_2,DOWN)
        w_4=Tex("Since inversing terms in an equality changes the equality sign")
        self.play(Write(w_3))
        w_4.next_to(w_3,DOWN)
        self.play(Write(w_4))
        self.wait(2)
        self.play(FadeOut(w_4))
        w_5=MathTex(r"Multiplying \quad by \quad sin(\theta)\quad in \quad all \quad sides. ")
        self.play(Write(w_5))
        self.wait(1.5)
        w_6=MathTex(r"\frac{sin(\theta)}{sin(\theta)} \geq \frac{sin(\theta)}{\theta} \geq \frac{sin(\theta)}{tan(\theta)}",font_size=40)
        w_6.next_to(w_5,DOWN)
        self.play(Write(w_6))
        self.wait()
        self.play(FadeOut(w_5))
        self.play(w_6.animate.next_to(w_3,DOWN))
        self.wait()
        w2_7=MathTex(r"1 \geq\frac{sin(\theta)}{\theta}\geq\frac{sin(\theta)}{tan(\theta)}",font_size=40)
        w2_7.next_to(w_6,DOWN)
        self.play(Write(w2_7))
        w2_8=MathTex(r"Since, \quad tan(\theta)=\frac{sin(\theta)}{cos(\theta)}",font_size=40)
        w2_8.next_to(w2_7,DOWN)
        self.play(Write(w2_8))
        self.wait(1.5)
        self.play(FadeOut(w2_8))
        w2_9=MathTex(r"1\geq \frac{sin(\theta)}{\theta}\geq cos(\theta)",font_size=40)
        w2_9.next_to(w2_7,DOWN)
        self.play(Write(w2_9))
        self.wait()
        fade_group=VGroup(w_3,w_6,w2_7)
        self.play(FadeOut(fade_group))
        self.play(w2_9.animate.next_to(w_2,DOWN))
        w2_10=Tex(r"Taking limit as x approaches 0 in all sides")
        w2_10.next_to(w2_9,DOWN)
        self.play(Write(w2_10))
        w2_11=MathTex(r"\lim_{\theta\to0} 1 \geq \lim_{\theta\to0} \frac{sin(\theta)}{\theta} \geq \lim_{\theta\to0} cos(\theta)")
        w2_11.next_to(w2_10,DOWN)
        self.play(Write(w2_11))
        self.wait()
        w_main=MathTex(r"1 \geq \lim_{\theta\to0}\frac{sin(\theta)}{\theta} \geq 1")
        w_main.next_to(w2_11,DOWN)
        self.play(Write(w_main))
        mega_fuck_=Group(w2_9,w2_10,w2_11)
        self.play(FadeOut(mega_fuck_))
        self.play(w_main.animate.next_to(w_2,DOWN))
        self.wait(2)
        w_main_=Tex("What this means, is when x approaches 0 in (sin(x)/(x) the limit is either less than or equal to 1 but it is also greater than or equal to 1. Both this statement are only true when the limit is 1. Meaning," ,font_size=40 )
        self.play(Write(w_main_))
        self.wait()
        w_final=MathTex(r"\lim_{\theta\to0}\frac{sin(\theta)}{\theta}     =    1")
        w_final.next_to(w_main_,DOWN)
        self.play(Write(w_final))
        frame_=SurroundingRectangle(w_final,buff=0.1)
        self.play(Create(frame_))
        remarks=Tex("Adish",font_size=35)
        remarks.to_edge(LEFT)
        remarks.to_edge(DOWN)
        self.play(Write(remarks))
        self.wait(5)

        ##ggez
       




# %%
