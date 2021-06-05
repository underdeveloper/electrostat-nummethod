from manim import * #pylint: disable=unused-import, unused-wildcard-import

DOT_LABEL_SIZE = 0.12

class MainProblem(Scene):
    def construct(self):

        # !! CHAPTER 1: INTRODUCTION

        memplate = TexTemplate()
        memplate.add_to_preamble(r"\usepackage{gensymb}")

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=2*DEFAULT_STROKE_WIDTH)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=2*DEFAULT_STROKE_WIDTH)
                       
        RedVolt = Tex('$+1V$', color=RED).shift(1.7*LEFT+1.7*DOWN).scale(0.7)
        WhiteVolt = Tex('$-1V$', color=WHITE).shift(1.7*RIGHT+1.7*UP).scale(0.7)
        
        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=2.0)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=2.0)

        RedPermissivity = Tex('$4 \\epsilon _0$', color='#00ff00').shift(0.2*LEFT+1.5*DOWN).scale(0.7)
        WhitePermissivity = Tex('$\\epsilon _0$', color='#d2bdff').shift(0.2*RIGHT+1.5*UP).scale(0.7)

        Text1 = Text("Kedua batang ini terpisahkan\npada perubahan warna.\n(diskontinu)").scale(0.35)
        
        AngleArc = Arc(color=YELLOW_C, start_angle=-2*TAU/3, angle=-TAU/3,
                       stroke_width=0.8*DEFAULT_STROKE_WIDTH).scale_about_point(0.5, ORIGIN)
        AngleText = Tex('$\\frac{2\\pi}{3}rad$', color=YELLOW_C, 
                        tex_template=memplate).scale(0.5).next_to(AngleArc, direction=0.6*UP)

        RadiusLine = Line(ORIGIN, 2*RIGHT, color=YELLOW_A)
        RadiusText = Tex('$10cm$', color=YELLOW_A, 
                        tex_template=memplate).scale(0.5).next_to(RadiusLine, direction=0.6*UP)

        Text2 = Text("Dengan menggunakan FDM dan MOM, akan dicari distribusi potensial\ndi area dalam lingkaran dan juga nilai kapasitansi yang ada.").scale(0.4).shift(3*DOWN)
        
        self.play(Create(RedArc))
        self.play(Create(WhiteArc))
        self.play(ApplyMethod(RedArc.scale_about_point, 2, ORIGIN),
                  ApplyMethod(WhiteArc.scale_about_point, 2, ORIGIN))
        self.foreground_mobjects += RedArc
        self.foreground_mobjects += WhiteArc

        self.play(Write(RedVolt), Write(WhiteVolt))

        self.play(Create(RedSector), Create(WhiteSector))

        self.play(Write(RedPermissivity), Write(WhitePermissivity))

        self.play(Write(Text1))

        self.play(ApplyMethod(Text1.shift, 4.2*RIGHT))
        self.play(Write(AngleText), Write(RadiusText),
                    Create(AngleArc), Create(RadiusLine))

        self.play(Write(Text2))

        self.wait(2)

        # # ! fadeout

        # self.play(
        #     *[FadeOut(mob)for mob in self.mobjects]
        #     # All mobjects in the screen are saved in self.mobjects
        # )
        # self.wait(1)

class FDM_part_1(Scene):
    def construct(self):
        
        # !! CHAPTER 2: FDM DIVISION

        memplate = TexTemplate()
        memplate.add_to_preamble(r"\usepackage{gensymb}")

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=2*DEFAULT_STROKE_WIDTH, radius=2)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=2*DEFAULT_STROKE_WIDTH, radius=2)
                       
        RedVolt = Tex('$+1V$', color=RED).shift(1.7*LEFT+1.7*DOWN).scale(0.7)
        WhiteVolt = Tex('$-1V$', color=WHITE).shift(1.7*RIGHT+1.7*UP).scale(0.7)
        
        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=2.0)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=2.0)
        
        self.add(RedVolt, WhiteVolt, RedSector, WhiteSector)
        # BUGGY ALSO WILL BECOME DEPRECATED IN 1.0
        self.foreground_mobjects += RedArc
        self.foreground_mobjects += WhiteArc 

        min_theta = 0  # multiple of TAU/20
        max_theta = TAU  # multiple of TAU/20
        min_r = 0
        max_r = 2

        theta = min_theta
        while theta <= max_theta:
            self.play(Create(ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=GREY, t_min=min_r, t_max=max_r)), run_time=0.2)
            # self.add(ParametricFunction(lambda t: np.array((
            #     t*np.cos(theta), t*np.sin(theta), 0)), color=GREY, t_min=min_r, t_max=max_r))
            theta += TAU/6

        deltaAngle = Tex('$\\Delta \\Phi = \\frac{\\pi}{3}$').shift(2.5*UP)
        deltaRadius = Tex('$\\Delta r = 2 cm$', tex_template=memplate).shift(2.5*DOWN)

        self.play(Write(deltaAngle))

        self.wait(1)

        r = min_r
        while r <= max_r:
            self.play(Create(ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_min=min_theta, t_max=max_theta)), run_time=0.2)
            # self.add(ParametricFunction(lambda t: np.array((
            #     r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_min=min_theta, t_max=max_theta))
            r += 0.4

        self.play(Write(deltaRadius))

        self.wait(1)

        self.play(FadeOut(deltaAngle), FadeOut(deltaRadius))

        dots_oh_my: list[Dot()] = []
        dot_count = 0

        theta = min_theta
        r = min_r + 0.4
        while (r < max_r):
            while (theta < max_theta):
                dots_oh_my.append(Dot(point=(r*np.sin(theta))*UP+(r*np.cos(theta))*RIGHT, radius=DOT_LABEL_SIZE))
                self.play(Create(dots_oh_my[dot_count]), run_time=0.1)
                theta += TAU/6
                dot_count += 1
            r += 0.4
            theta = min_theta
        
        dots_oh_my.append(Dot(radius=DOT_LABEL_SIZE))
        self.play(Create(dots_oh_my[dot_count]), runtime=0.1)
        
        self.wait(2)

        # I hate this so much.

        # circle_fdm = Group(*(self.mobjects+self.foreground_mobjects)) # so this DOES work! but does not remove foreground
        # print(circle_fdm)
        # self.play(FadeOut(circle_fdm)) # testing out group animations

        # self.wait(1)
        
        # # ! fadeout

        # self.play(
        #     *[FadeOut(mob)for mob in self.mobjects]
        #     # All mobjects in the screen are saved in self.mobjects
        # )
        # self.wait(1)

class FDM_part_2(Scene):
    def construct(self):
        Xemplate = TexTemplate()
        Xemplate.add_to_preamble(r"\usepackage{gensymb}")
        Xemplate.add_to_preamble(r"\usepackage{derivative}")
        Xemplate.add_to_preamble(r"\usepackage{cancel}")
        Xemplate.add_to_preamble(r"\usepackage{siunitx}")

        deriv1st = Tex(r"$\odv{\Phi}{r}\rvert_{r_0} = \frac{\Phi\left(r_0+h\right)-\Phi\left(r_0-h\right)}{2h}$", tex_template=Xemplate).move_to(0.5*UP)
        deriv2nd = Tex(r"$\odv[2]{\Phi}{r}\rvert_{r_0} = \frac{\Phi\left(r_0+h\right)+\Phi\left(r_0-h\right)-2\Phi\left(r_0\right)}{h^2}$", tex_template=Xemplate).move_to(-0.5*UP)

        self.play(Write(deriv1st), runtime=2)
        self.play(Write(deriv2nd), runtime=3)
        self.wait(1)

        derivs = Group(deriv1st, deriv2nd)      
        laplacian_phi = Tex('$\\nabla^2 \\Phi = \\pdv[2]{\\Phi}{r} + \\frac{1}{r} \\pdv{\\Phi}{r} + \\frac{1}{r^2} \\pdv[2]{\\Phi}{\\theta} = 0$', tex_template=Xemplate)

        self.play(ApplyMethod(derivs.shift, 3*UP))
        self.play(Write(laplacian_phi))
        self.wait(1)

        d2Pdr2 = Tex(r"$\odv[2]{\Phi}{r}\rvert_{\left(r_0,\theta_0\right)} = \frac{\Phi\left(r_0+h_r,\theta_0\right)+\Phi\left(r_0-h_r,\theta_0\right)-2\Phi\left(r_0,\theta_0\right)}{h_r^2}$", tex_template=Xemplate).shift(1*UP)
        dPdr = Tex(r"$\odv{\Phi}{r}\rvert_{\left(r_0,\theta_0\right)} = \frac{\Phi\left(r_0+h_r,\theta_0\right)-\Phi\left(r_0-h_r,\theta_0\right)}{2h_r}$", tex_template=Xemplate).shift(0*UP)
        d2Pdt2 = Tex(r"$\odv[2]{\Phi}{t}\rvert_{\left(r_0,\theta_0\right)} = \frac{\Phi\left(r_0,\theta_0+h_\theta\right)+\Phi\left(r_0,\theta_0-h_\theta\right)-2\Phi\left(r_0,\theta_0\right)}{\left(h_\theta r_0\right)^2}$", tex_template=Xemplate).shift(-1*UP)

        self.play(ApplyMethod(laplacian_phi.shift, 3.35*DOWN))
        d1st_rect = Rectangle(color=YELLOW, height=1, width=1.2).next_to(laplacian_phi, direction=0).shift(0.1*RIGHT)
        
        self.play(Transform(deriv2nd, d2Pdr2), Transform(deriv1st, dPdr), Transform(deriv2nd, d2Pdt2))
        self.play(Indicate(dPdr, scale=1.1), ShowCreationThenDestruction(d1st_rect), runtime=0.7)


        self.wait(2)
