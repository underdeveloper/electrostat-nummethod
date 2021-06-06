from manim import *
from manim.utils import tex_templates #pylint: disable=unused-import, unused-wildcard-import

DOT_LABEL_SIZE = 0.12

class MainProblem(Scene):
    def construct(self):

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

        self.wait(3)

        # ! fadeout

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait(2)

# ! Finite Difference Method

class FDM_part_1(Scene):
    def construct(self):

        self.wait(2)
        
        CIRCLE_RADIUS = 3

        memplate = TexTemplate()
        memplate.add_to_preamble(r"\usepackage{gensymb}")

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=2*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=2*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
                       
        RedVolt = Tex('$+1V$', color=RED).shift(2.6*LEFT+2.6*DOWN).scale(0.7)
        WhiteVolt = Tex('$-1V$', color=WHITE).shift(2.6*RIGHT+2.6*UP).scale(0.7)
        
        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=CIRCLE_RADIUS)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=CIRCLE_RADIUS)
        
        self.add(RedVolt, WhiteVolt, RedSector, WhiteSector)
        # BUGGY ALSO WILL BECOME DEPRECATED IN 1.0
        self.foreground_mobjects += RedArc
        self.foreground_mobjects += WhiteArc 


        min_theta = 0
        max_theta = TAU
        min_r = 0
        max_r = CIRCLE_RADIUS

        d_theta = TAU/6
        d_r = max_r/5

        theta = min_theta
        while theta <= max_theta:
            self.play(Create(ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=GREY, t_range=np.array((min_r, max_r)))), run_time=0.2)
            theta += d_theta

        deltaAngle = Tex('$\\Delta \\Phi = \\frac{\\pi}{3}$').shift(3.3*UP)
        deltaRadius = Tex('$\\Delta r = 2 cm$', tex_template=memplate).shift(3.3*DOWN)

        self.play(Write(deltaAngle))

        self.wait(2)

        r = min_r
        while r <= max_r:
            self.play(Create(ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_range=np.array((min_theta, max_theta)))), run_time=0.2)
            r += d_r

        self.play(Write(deltaRadius))

        self.wait(2)

        self.play(FadeOut(deltaAngle), FadeOut(deltaRadius))

        dots_oh_my: list[Dot()] = []
        dot_count = 0

        theta = min_theta
        r = min_r + d_r
        while (r < max_r):
            while (theta < max_theta):
                dots_oh_my.append(Dot(point=(r*np.sin(theta))*UP+(r*np.cos(theta))*RIGHT, radius=DOT_LABEL_SIZE))
                self.play(Create(dots_oh_my[dot_count]), run_time=0.1)
                theta += d_theta
                dot_count += 1
            r += d_r
            theta = min_theta
        
        dots_oh_my.append(Dot(radius=DOT_LABEL_SIZE))
        self.play(Create(dots_oh_my[dot_count]), runtime=0.1)
        
        self.wait(3)

        # I hate this so much.

        # circle_fdm = Group(*(self.mobjects+self.foreground_mobjects)) # so this DOES work! but does not remove foreground
        # print(circle_fdm)
        # self.play(FadeOut(circle_fdm)) # testing out group animations

        # self.wait(2)
        
        # ! fadeout

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait(2)

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
        self.wait(2)

        derivs = Group(deriv1st, deriv2nd)      
        laplacian_phi = Tex('$\\nabla^2 \\Phi = \\pdv[2]{\\Phi}{r} + \\frac{1}{r} \\pdv{\\Phi}{r} + \\frac{1}{r^2} \\pdv[2]{\\Phi}{\\theta} = 0$', tex_template=Xemplate)

        self.play(ApplyMethod(derivs.shift, 3*UP))
        self.play(Write(laplacian_phi))
        self.wait(2)

        self.play(ApplyMethod(laplacian_phi.shift, 3.35*DOWN))
        
        d2Pdr2 = Tex(r"$\odv[2]{\Phi}{r}\rvert_{\left(r_0,\theta_0\right)} = \frac{\Phi\left(r_0+h_r,\theta_0\right)+\Phi\left(r_0-h_r,\theta_0\right)-2\Phi\left(r_0,\theta_0\right)}{h_r^2}$", color=BLUE, tex_template=Xemplate).shift(1*UP)
        dPdr = Tex(r"$\odv{\Phi}{r}\rvert_{\left(r_0,\theta_0\right)} = \frac{\Phi\left(r_0+h_r,\theta_0\right)-\Phi\left(r_0-h_r,\theta_0\right)}{2h_r}$", color=BLUE, tex_template=Xemplate).shift(0*UP)
        d2Pdt2 = Tex(r"$\odv[2]{\Phi}{t}\rvert_{\left(r_0,\theta_0\right)} = \frac{\Phi\left(r_0,\theta_0+h_\theta\right)+\Phi\left(r_0,\theta_0-h_\theta\right)-2\Phi\left(r_0,\theta_0\right)}{\left(h_\theta r_0\right)^2}$", color=BLUE, tex_template=Xemplate).shift(-1*UP)
        derivs2 = Group(d2Pdr2, dPdr, d2Pdt2)

        self.play(TransformFromCopy(deriv2nd, d2Pdr2))
        self.play(TransformFromCopy(deriv1st, dPdr))
        self.play(TransformFromCopy(deriv2nd, d2Pdt2))

        self.wait(2)
        
        laplacian_phi1 = MathTex(r"""
        \nabla^2 \Phi = 0 &= \pdv[2]{\Phi}{r} \\ 
        &+ \frac{1}{r} \pdv{\Phi}{r} \\ 
        &+ \frac{1}{r^2} \pdv[2]{\Phi}{\theta}
        """, tex_template=Xemplate).shift(1.8*DOWN)

        self.play(FadeOut(derivs), ApplyMethod(derivs2.shift, 2.15*UP), ReplacementTransform(laplacian_phi, laplacian_phi1))
        self.wait(2)

        # Making this is such a mess. surely there is a better way.
        d2Pdr2_rect = Rectangle(color=YELLOW, height=1.22, width=1).next_to(laplacian_phi1, direction=0).shift(1.25*UP+1.05*RIGHT)
        
        self.play(Indicate(d2Pdr2, scale=1.1), ShowPassingFlash(d2Pdr2_rect, run_time= 1.5))
        
        laplacian_phi2 = MathTex(r"""
        \nabla^2 \Phi = 0 &= \frac{\Phi \left(r_0+h_r,\theta_0\right)+\Phi \left(r_0-h_r,\theta_0\right)-2\Phi\left(r_0,\theta_0\right)}{h_r^2} \\ 
        &+ \frac{1}{r} \pdv{\Phi}{r} \\ 
        &+ \frac{1}{r^2} \pdv[2]{\Phi}{\theta}
        """, tex_template=Xemplate).shift(1.8*DOWN)
        
        self.play(ReplacementTransform(laplacian_phi1, laplacian_phi2))

        dPdr_rect = Rectangle(color=YELLOW, height=1.22, width=0.8).next_to(laplacian_phi, direction=0).shift(-2.83*RIGHT+-0.05*UP)
        self.play(Indicate(dPdr, scale=1.1), ShowCreationThenDestruction(dPdr_rect, run_time= 1.5))

        laplacian_phi3 = MathTex(r"""
        \nabla^2 \Phi = 0 &= \frac{\Phi \left(r_0+h_r,\theta_0\right)+\Phi \left(r_0-h_r,\theta_0\right)-2\Phi\left(r_0,\theta_0\right)}{h_r^2} \\ 
        &+ \frac{1}{r_0}\frac{\Phi\left(r_0+h_r,\theta_0\right)-\Phi\left(r_0-h_r,\theta_0\right)}{2h_r} \\ 
        &+ \frac{1}{r^2} \pdv[2]{\Phi}{\theta}
        """, tex_template=Xemplate).shift(1.8*DOWN)

        self.play(ReplacementTransform(laplacian_phi2, laplacian_phi3))

        d2Pdt2_rect = Rectangle(color=YELLOW, height=1.22, width=0.9).next_to(laplacian_phi, direction=0).shift(-2.53*RIGHT+-1.37*UP)
        self.play(Indicate(d2Pdt2, scale=1.1), ShowCreationThenDestruction(d2Pdt2_rect, run_time= 1.5))

        laplacian_phi4 = MathTex(r"""
        \nabla^2 \Phi = 0 &= \frac{\Phi \left(r_0+h_r,\theta_0\right)+\Phi \left(r_0-h_r,\theta_0\right)-2\Phi\left(r_0,\theta_0\right)}{h_r^2} \\ 
        &+ \frac{1}{r_0}\frac{\Phi\left(r_0+h_r,\theta_0\right)-\Phi\left(r_0-h_r,\theta_0\right)}{2h_r} \\ 
        &+ \frac{1}{r_0^2}\frac{\Phi\left(r_0,\theta_0+h_\theta\right)+\Phi\left(r_0,\theta_0-h_\theta\right)-2\Phi\left(r_0,\theta_0\right)}{\left(h_\theta r_0\right)^2}
        """, tex_template=Xemplate).shift(1.8*DOWN)

        self.play(ReplacementTransform(laplacian_phi3, laplacian_phi4))

        self.wait(2)

        self.play(ApplyMethod(laplacian_phi4.move_to, ORIGIN), FadeOut(derivs2))

        self.wait(2)

class FDM_part_3(Scene):
    def construct(self):
        Xemplate = TexTemplate()
        Xemplate.add_to_preamble(r"\usepackage{gensymb}")
        Xemplate.add_to_preamble(r"\usepackage{derivative}")
        Xemplate.add_to_preamble(r"\usepackage{cancel}")
        Xemplate.add_to_preamble(r"\usepackage{siunitx}")

        laplacian = MathTex(r"""
        \nabla^2 \Phi = 0 &= \frac{\Phi \left(r_0+h_r,\theta_0\right)+\Phi \left(r_0-h_r,\theta_0\right)-2\Phi\left(r_0,\theta_0\right)}{h_r^2} \\ 
        &+ \frac{1}{r_0}\frac{\Phi\left(r_0+h_r,\theta_0\right)-\Phi\left(r_0-h_r,\theta_0\right)}{2h_r} \\ 
        &+ \frac{1}{r_0^2}\frac{\Phi\left(r_0,\theta_0+h_\theta\right)+\Phi\left(r_0,\theta_0-h_\theta\right)-2\Phi\left(r_0,\theta_0\right)}{\left(h_\theta r_0\right)^2}
        """, tex_template=Xemplate)
        
        self.add(laplacian)
        self.play(ApplyMethod(laplacian.scale, 0.7))
        self.play(ApplyMethod(laplacian.shift, 2.3*UP))

        d_theta = TAU/24
        d_radial = 2

        min_theta = 0 * d_theta  # multiple of d_theta
        max_theta = 2 * d_theta  # multiple of d_theta
        min_radial = 1 * d_radial # multiple of d_radial
        max_radial = 3 * d_radial # multiple of d_radial

        sector_lines = []

        theta = min_theta
        while theta <= max_theta:
            sector_lines += ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=BLUE, t_range=np.array((min_radial, max_radial))).shift(-2.5*UP+-2*d_radial*RIGHT)
            theta += d_theta

        r = min_radial
        while r <= max_radial:
            sector_lines += ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=BLUE, t_range=np.array((min_theta, max_theta))).shift(-2.5*UP+-2*d_radial*RIGHT)
            r += d_radial

        sector = VGroup(*sector_lines)

        self.play(Create(sector), run_time=2.5)

        Phi0 = Dot(color=WHITE).next_to(sector, direction=0).shift(0.45*DOWN)
        Phi0Eq = Tex(r"$\Phi_0\left(r_0,\theta_0\right)$", color=WHITE).scale(0.75).next_to(Phi0).shift(0.2*LEFT+0.2*DOWN)
        Phi1 = Dot(color=GREEN).next_to(Phi0, direction=0).shift(
            # shift to "origin" of polar plot
            d_radial*np.sin(d_theta)*-2*UP+d_radial*np.cos(d_theta)*-2*RIGHT  
            # shift to correct position on the polar plot
            + d_radial*np.sin(2*d_theta)*2*UP+d_radial*np.cos(2*d_theta)*2*RIGHT  
            )
        Phi1Eq = Tex(r"$\Phi_1\left(r_0,\theta_0+h_\theta\right)$", color=GREEN).scale(0.75).next_to(Phi1, direction=LEFT).shift(0.2*RIGHT+0.2*UP)
        Phi2 = Dot(color=YELLOW).next_to(Phi0, direction=0).shift(
            # shift to "origin" of polar plot
            d_radial*np.sin(d_theta)*-2*UP+d_radial*np.cos(d_theta)*-2*RIGHT  
            # shift to correct position on the polar plot
            + d_radial*np.sin(0*d_theta)*2*UP+d_radial*np.cos(0*d_theta)*2*RIGHT  
            )
        Phi2Eq = Tex(r"$\Phi_2\left(r_0,\theta_0-h_\theta\right)$", color=YELLOW).scale(0.75).next_to(Phi2).shift(0.2*LEFT+0.3*DOWN)
        Phi3 = Dot(color=RED).next_to(Phi0, direction=0).shift(
            d_radial*np.sin(d_theta)*UP+d_radial*np.cos(d_theta)*RIGHT
            )
        Phi3Eq = Tex(r"$\Phi_3\left(r_0+h_r,\theta_0\right)$", color=RED).scale(0.75).next_to(Phi3).shift(0.2*LEFT+0.2*DOWN)
        Phi4 = Dot(color=PURPLE).next_to(Phi0, direction=0).shift(
            d_radial*np.sin(d_theta)*-1*UP+d_radial*np.cos(d_theta)*-1*RIGHT
            )
        Phi4Eq = Tex(r"$\Phi_4\left(r_0-h_r,\theta_0\right)$", color=PURPLE).scale(0.75).next_to(Phi4).shift(0.2*LEFT+0.2*DOWN)
        self.play(Create(Phi0), Create(Phi1), Create(Phi2), Create(Phi3), Create(Phi4))
        self.play(Write(Phi0Eq), Write(Phi1Eq), Write(Phi2Eq), Write(Phi3Eq), Write(Phi4Eq))

        self.wait(2)

        laplacian_numbered = MathTex(r"""
        \nabla^2 \Phi = 0 &= \frac{\Phi_1+\Phi_2-2\Phi_0}{h_r^2} \\ 
        &+ \frac{1}{r_0}\frac{\Phi_1-\Phi_2}{2h_r} \\ 
        &+ \frac{1}{r_0^2}\frac{\Phi_3+\Phi_4-2\Phi_0}{\left(h_\theta r_0\right)^2}
        """, tex_template=Xemplate).scale(0.7).shift(2.3*UP+2*LEFT)

        self.play(ReplacementTransform(laplacian, laplacian_numbered))

        approximation = MathTex(r"h_r \approx h_\theta r_0 = h \rightarrow 0", template=Xemplate).scale(0.7).next_to(laplacian_numbered)
        
        self.play(Write(approximation), run_time= 4)

        self.wait(2)

        laplacian_reordered = MathTex(r"""
        \nabla^2 \Phi = 0 &= \frac{\Phi_1+\Phi_2-2\Phi_0}{h^2} \\ 
        &+ \frac{h}{2r_0}\frac{\Phi_1-\Phi_2}{h^2} \\ 
        &+ \frac{1}{r_0^2}\frac{\Phi_3+\Phi_4-2\Phi_0}{h^2}
        """, tex_template=Xemplate).scale(0.7).shift(2.3*UP+2*LEFT)

        self.play(ReplacementTransform(laplacian_numbered, laplacian_reordered))

        self.wait(2)

        laplacian_reordered2 = MathTex(r"""
        0 &= \Phi_1+\Phi_2-2\Phi_0 \\ 
        &+ \frac{h}{2r_0} \left( \Phi_1-\Phi_2 \right) \\ 
        &+ \frac{1}{r_0^2} \left( \Phi_3+\Phi_4-2\Phi_0 \right)
        """, tex_template=Xemplate).scale(0.7).shift(2.3*UP+2*LEFT)

        self.play(ReplacementTransform(laplacian_reordered, laplacian_reordered2))
        
        self.wait(2)

        laplacian_reordered3 = MathTex(r"""
        0 &= \Phi_1+\Phi_2-2\Phi_0 \\ 
        &+ \cancel{\frac{h}{2r_0} \left( \Phi_1-\Phi_2 \right)} \\ 
        &+ \frac{1}{r_0^2} \left( \Phi_3+\Phi_4-2\Phi_0 \right)
        """, tex_template=Xemplate).scale(0.7).shift(2.3*UP+2*LEFT)

        self.play(Indicate(approximation), ReplacementTransform(laplacian_reordered2, laplacian_reordered3))

        self.wait(2)

        laplacian_reordered4 = MathTex(r"""
        0 &= \Phi_1+\Phi_2-2\Phi_0 \\ 
        &+ \frac{1}{r_0^2} \left( \Phi_3+\Phi_4-2\Phi_0 \right)
        """, tex_template=Xemplate).scale(0.7).shift(2.3*UP+2*LEFT)

        self.play(ReplacementTransform(laplacian_reordered3, laplacian_reordered4))

        self.wait(2)

        laplacian_final = MathTex(r"""
        0 = \Phi_1+\Phi_2-2\Phi_0
        + \frac{1}{r_0^2} \left( \Phi_3+\Phi_4-2\Phi_0 \right)
        """, tex_template=Xemplate).shift(2.5*UP)

        self.play(FadeOut(approximation), ReplacementTransform(laplacian_reordered4, laplacian_final))

        laplacian_text = Text("Ini adalah rumus pencarian potensial \nuntuk daerah permitivitas homogen.", size=0.7).next_to(laplacian_final, direction=DOWN)
        
        self.play(Write(laplacian_text))

        self.wait(2)

class FDM_part_4(Scene):
    def construct(self):
        Xemplate = TexTemplate()
        Xemplate.add_to_preamble(r"\usepackage{gensymb}")
        Xemplate.add_to_preamble(r"\usepackage{derivative}")
        Xemplate.add_to_preamble(r"\usepackage{cancel}")
        Xemplate.add_to_preamble(r"\usepackage{siunitx}")

        d_theta = TAU/12
        d_radial = 2

        min_theta = 0 * d_theta  # multiple of d_theta
        max_theta = 2 * d_theta  # multiple of d_theta
        min_radial = 1 * d_radial # multiple of d_radial
        max_radial = 3 * d_radial # multiple of d_radial

        RedSector = Sector(color='#021a00', start_angle=min_theta,
                           angle=d_theta, inner_radius=min_radial, outer_radius=max_radial).shift(-2.5*UP+-2*d_radial*RIGHT)
        WhiteSector = Sector(color='#0f0e12', start_angle=min_theta + d_theta,
                           angle=d_theta, inner_radius=min_radial, outer_radius=max_radial).shift(-2.5*UP+-2*d_radial*RIGHT)

        sector_lines = []

        theta = min_theta
        while theta <= max_theta:
            sector_lines += ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=BLUE, t_range=np.array((min_radial, max_radial))).shift(-2.5*UP+-2*d_radial*RIGHT)
            theta += d_theta

        r = min_radial
        while r <= max_radial:
            sector_lines += ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=BLUE, t_range=np.array((min_theta, max_theta))).shift(-2.5*UP+-2*d_radial*RIGHT)
            r += d_radial

        sector = VGroup(*sector_lines)

        contour_lines = []

        theta = min_theta + 0.5 * d_theta
        while theta <= min_theta + 1.5 * d_theta:
            contour_lines += ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=RED, t_range=np.array((min_radial + 0.5 * d_radial, min_radial + 1.5 * d_radial))).shift(-2.5*UP+-2*d_radial*RIGHT)
            theta += d_theta

        r = min_radial + 0.5 * d_radial
        while r <= min_radial + 1.5 * d_radial:
            contour_lines += ParametricFunction(lambda t: np.array((
                r*np.cos(t), r*np.sin(t), 0)), color=RED, t_range=np.array((min_theta + 0.5 * d_theta, min_theta + 1.5 * d_theta))).shift(-2.5*UP+-2*d_radial*RIGHT)
            r += d_radial

        contour = VGroup(*contour_lines)

        self.play(Create(RedSector), Create(WhiteSector), Create(sector), Create(contour))

        # self.wait(2)

        Phi0 = Dot(color=WHITE).next_to(sector, direction=0).shift(0.63*DOWN+0.03*LEFT)
        Phi0Eq = Tex(r"$\Phi_0$", color=WHITE).scale(0.75).next_to(Phi0).shift(0.2*LEFT+0.2*DOWN)
        Phi1 = Dot(color=GREEN).next_to(Phi0, direction=0).shift(
            # shift to "origin" of polar plot
            d_radial*np.sin(d_theta)*-2*UP+d_radial*np.cos(d_theta)*-2*RIGHT  
            # shift to correct position on the polar plot
            + d_radial*np.sin(2*d_theta)*2*UP+d_radial*np.cos(2*d_theta)*2*RIGHT  
            )
        Phi1Eq = Tex(r"$\Phi_1$", color=GREEN).scale(0.75).next_to(Phi1, direction=LEFT).shift(0.2*RIGHT+0.2*UP)
        Phi2 = Dot(color=YELLOW).next_to(Phi0, direction=0).shift(
            # shift to "origin" of polar plot
            d_radial*np.sin(d_theta)*-2*UP+d_radial*np.cos(d_theta)*-2*RIGHT  
            # shift to correct position on the polar plot
            + d_radial*np.sin(0*d_theta)*2*UP+d_radial*np.cos(0*d_theta)*2*RIGHT  
            )
        Phi2Eq = Tex(r"$\Phi_2$", color=YELLOW).scale(0.75).next_to(Phi2).shift(0.2*LEFT+0.3*DOWN)
        Phi3 = Dot(color=RED).next_to(Phi0, direction=0).shift(
            d_radial*np.sin(d_theta)*UP+d_radial*np.cos(d_theta)*RIGHT
            )
        Phi3Eq = Tex(r"$\Phi_3$", color=RED).scale(0.75).next_to(Phi3).shift(0.2*LEFT+0.1*DOWN)
        Phi4 = Dot(color=PURPLE).next_to(Phi0, direction=0).shift(
            d_radial*np.sin(d_theta)*-1*UP+d_radial*np.cos(d_theta)*-1*RIGHT
            )
        Phi4Eq = Tex(r"$\Phi_4$", color=PURPLE).scale(0.75).next_to(Phi4).shift(0.2*LEFT+0.1*DOWN)
        Phi0Eq.shift(0.1*UP)
        self.play(Create(Phi0), Create(Phi1), Create(Phi2), Create(Phi3), Create(Phi4))
        self.play(Write(Phi0Eq), Write(Phi1Eq), Write(Phi2Eq), Write(Phi3Eq), Write(Phi4Eq))

        Epsilon_A = MathTex(r'\epsilon _A', color='#d2bdff').next_to(Phi0, direction=0).scale(0.7).shift(2.5*UP+0.4*LEFT)
        Epsilon_B = MathTex(r'\epsilon _B', color='#00ff00').next_to(Phi0, direction=0).scale(0.7).shift(-1.7*UP-1.8*LEFT)
        self.play(Write(Epsilon_A), Write(Epsilon_B))

        self.wait(1)

        seccontour = Group(*self.mobjects)

        self.play(ApplyMethod(seccontour.scale, 0.75))
        self.play(ApplyMethod(seccontour.shift, 3*LEFT))

        gauss = MathTex(r"\oint_c \epsilon \mathbf{E} \cdot \mathbf{dl} = q = 0\\\mathbf{E} = -\mathbf{\nabla}\Phi",tex_template=Xemplate).shift(2*RIGHT+2*UP)

        gauss2 = MathTex(r"""\therefore 0 &= \oint_c \epsilon \left( -\mathbf{\nabla}\Phi \right) \cdot \mathbf{dl} \\
            &= \oint_c \epsilon \mathbf{\nabla}\Phi \cdot \mathbf{dl} \\
            &= \oint_c \epsilon \pdv{\Phi}{n} dl
            """, tex_template=Xemplate).shift(2*RIGHT+1*DOWN)

        self.play(Write(gauss))

        self.play(Write(gauss2))

        self.wait(2)

        gauss3 = MathTex(r"0 = \oint_c \epsilon \pdv{\Phi}{n} dl", tex_template=Xemplate).shift(2*RIGHT+2*UP)

        self.play(Unwrite(gauss), run_time=0.7)
        self.play(ReplacementTransform(gauss2, gauss3))
        
        gauss_discrete = MathTex(r"0 = \sum \epsilon \pdv{\Phi}{n} \Delta l", tex_template=Xemplate).shift(2*RIGHT)
        gauss_discrete2 = MathTex(r"""0 &= \sum \epsilon \pdv{\Phi}{n} \Delta l \\
            &= \sum \epsilon \frac{\Phi \left( n_0 + h_n \right) - \Phi \left( n_0 \right)}{h_n} \Delta l
            """, tex_template=Xemplate).scale(0.75).shift(2.5*RIGHT)

        self.play(TransformFromCopy(gauss3, gauss_discrete))
        self.wait(1) 

        self.play(ReplacementTransform(gauss_discrete, gauss_discrete2))
        self.wait(1)

        gauss_discrete_final = MathTex(r"""0 &= \epsilon \frac{\Phi_1 - \Phi_0}{h_r} \left( \epsilon_A h_r\right) \\
            &+ \epsilon \frac{\Phi_2 - \Phi_0}{h_r} \left( \epsilon_B h_r\right) \\
            &+ \epsilon \frac{\Phi_3 - \Phi_0}{r_0 h_\theta} \left( \frac{\epsilon_A + \epsilon_B}{2} \left(r_0 + \frac{h_r}{2} \right) h_\theta \right) \\
            &+ \epsilon \frac{\Phi_4 - \Phi_0}{r_0 h_\theta} \left( \frac{\epsilon_B + \epsilon_A}{2} \left(r_0 + \frac{h_r}{2} \right) h_\theta \right) \\         
            """, tex_template=Xemplate).scale(0.75).shift(2.5*RIGHT)

        self.play(FadeOut(gauss3), ReplacementTransform(gauss_discrete2, gauss_discrete_final))
        self.wait(1)

        gauss_text = Text("Ini adalah rumus pencarian potensial \npada daerah perbatasan permitivitas heterogen.", size=0.4).next_to(gauss_discrete_final, direction=DOWN)
        
        self.play(Write(gauss_text))

        self.wait(2)

        
        return

class FDM_part_5(Scene):
    def construct(self):

        CIRCLE_RADIUS = 3

        # Adding the circle

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=2*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=2*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
                       
        # RedVolt = Tex('$+1V$', color=RED).shift(1.7*LEFT+1.7*DOWN).scale(0.7)
        # WhiteVolt = Tex('$-1V$', color=WHITE).shift(1.7*RIGHT+1.7*UP).scale(0.7)
        
        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=CIRCLE_RADIUS)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=CIRCLE_RADIUS)

        # RedPermissivity = Tex('$4 \\epsilon _0$', color='#00ff00').shift(0.2*LEFT+1.5*DOWN).scale(0.7)
        # WhitePermissivity = Tex('$\\epsilon _0$', color='#d2bdff').shift(0.2*RIGHT+1.5*UP).scale(0.7)

        self.add(RedSector, WhiteSector)
        # self.add(RedVolt, WhiteVolt, RedPermissivity, WhitePermissivity) # probably dont need these lol
        
        # Adding the radial and angular lines

        d_theta = TAU/6
        d_radial = CIRCLE_RADIUS / 5

        min_theta = 0 * d_theta  # multiple of d_theta
        max_theta = 6 * d_theta  # multiple of d_theta
        min_radial = 0 * d_radial # multiple of d_radial
        max_radial = 5 * d_radial # multiple of d_radial

        theta = min_theta
        while theta <= max_theta:
            self.add(ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=GREY, t_range=np.array((min_radial, max_radial))))
            theta += d_theta

        r = min_radial
        while r <= max_radial:
            self.add(ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_range=np.array((min_theta, max_theta))))
            r += d_radial

        # these have to be in front of course
        self.add(RedArc, WhiteArc)

        circle = VGroup(*self.mobjects)

        # The dots!

        dots_oh_my: list[Dot()] = []
        lables_oh_my: list[Text()] = []
        dot_count = 0

        theta = min_theta + d_theta
        r = min_radial + d_radial
        while (theta < max_theta+d_radial): 
            while (r < max_radial):
                dots_oh_my.append(Dot(point=(r*np.sin(theta))*UP+(r*np.cos(theta))*RIGHT, radius=1.5*DOT_LABEL_SIZE))
                lables_oh_my.append(Text(text=str(dot_count+1), size=0.3, color=BLACK).next_to(dots_oh_my[dot_count], direction=0))
                self.play(Create(dots_oh_my[dot_count]), Write(lables_oh_my[dot_count]), run_time=0.05)
                r += d_radial
                dot_count += 1
            r = min_theta + d_radial
            theta += d_theta
        
        dots_oh_my.append(Dot(radius=1.5*DOT_LABEL_SIZE))
        lables_oh_my.append(Text(text=str(0), size=0.3, color=BLACK).next_to(dots_oh_my[dot_count], direction=0))
        self.play(Create(dots_oh_my[dot_count]), Write(lables_oh_my[dot_count]), runtime=0.05)

        self.wait(2)

        symmetry_line = Line(1.2*CIRCLE_RADIUS*np.sin(d_theta)*UP+1.2*CIRCLE_RADIUS*np.cos(d_theta)*RIGHT,1.2*CIRCLE_RADIUS*np.sin(d_theta)*DOWN+1.2*CIRCLE_RADIUS*np.cos(d_theta)*LEFT, color=BLUE_B, stroke_width=2.25*DEFAULT_STROKE_WIDTH)
        
        self.play(ShowPassingFlash(symmetry_line, run_time=3, time_width=1))

        self.wait(2)

        self.play(Indicate(mobject=Group(*dots_oh_my[4:12])), Indicate(mobject=Group(*lables_oh_my[4:12]), color=BLACK), Indicate(mobject=Group(*dots_oh_my[16:24])), Indicate(mobject=Group(*lables_oh_my[16:24]), color=BLACK))

        self.wait(2)

        self.play(FadeOut(Group(*(dots_oh_my[16:24] + lables_oh_my[16:24])))) # 0.0.7 kinda fucked this line

        self.wait(2)

        totalGroup = Group(*self.mobjects)

        self.play(FadeOut(totalGroup))
        
        self.wait(2)

class FDM_part_6(Scene):
    def construct(self):
        matrix_phi = MathTex(r"""\setcounter{MaxMatrixCols}{17}
        \begin{bmatrix}
            -11.5 & 0.5 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 2 & 0 & 0 & 0 \\
            1 & -4 & 1 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
            0 & 4 & -10 & 4 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 9 & -20 & 9 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 0 & 16 & -34 & 0 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
            1.25 & 1 & 0 & 0 & 0 & -10 & 3.75 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 1 & 0 & 0 & 7.5 & -25 & 12.5 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 0 & 1 & 0 & 0 & 18.75 & -50 & 26.25 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 0 & 0 & 1 & 0 & 0 & 35 & -85 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 0 \\
            4 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & -4 & 1 & 0 & 0 & 1 & 0 & 0 & 0 \\
            0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 4 & -10 & 4 & 0 & 0 & 1 & 0 & 0 \\
            0 & 0 & 0 & 0 & 0 & 0 & 0  & 1 & 0 & 0 & 9 & -20 & 9 & 0 & 0 & 1 & 0 \\
            0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 16 & -34 & 0 & 0 & 0 & 1 \\
            1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 0 & -4 & 1 & 0 & 0 \\
            0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 4 & -10 & 4 & 0 \\
            0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 9 & -20 & 9 \\
            0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 16 & -34
        \end{bmatrix}
        \begin{bmatrix}
            \Phi_0 \\
            \Phi_1 \\
            \Phi_2 \\
            \Phi_3 \\
            \Phi_4 \\
            \Phi_5 \\
            \Phi_6 \\
            \Phi_7 \\
            \Phi_8 \\
            \Phi_9 \\
            \Phi_{10} \\
            \Phi_{11} \\
            \Phi_{12} \\
            \Phi_{13} \\
            \Phi_{14} \\
            \Phi_{15} \\
            \Phi_{16}
        \end{bmatrix}
        =
        \begin{bmatrix}
            0 \\
            0 \\
            0 \\
            0 \\
            16 \\
            0 \\
            0 \\
            0 \\
            0 \\
            0 \\
            0 \\
            0 \\
            -16 \\
            0 \\
            0 \\
            0 \\
            -16
        \end{bmatrix}        
        """).scale_about_point(0.45, ORIGIN)
        
        self.play(Write(matrix_phi))

        self.wait(2)

        matrix_phi2 = MathTex(r"""\setcounter{MaxMatrixCols}{17}
        \begin{bmatrix}
            \Phi_0 \\
            \Phi_1 \\
            \Phi_2 \\
            \Phi_3 \\
            \Phi_4 \\
            \Phi_5 \\
            \Phi_6 \\
            \Phi_7 \\
            \Phi_8 \\
            \Phi_9 \\
            \Phi_{10} \\
            \Phi_{11} \\
            \Phi_{12} \\
            \Phi_{13} \\
            \Phi_{14} \\
            \Phi_{15} \\
            \Phi_{16}
        \end{bmatrix}
        =
        \begin{bmatrix}
            -11.5 & 0.5 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 2 & 0 & 0 & 0 \\
            1 & -4 & 1 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
            0 & 4 & -10 & 4 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 9 & -20 & 9 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 0 & 16 & -34 & 0 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
            1.25 & 1 & 0 & 0 & 0 & -10 & 3.75 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 1 & 0 & 0 & 7.5 & -25 & 12.5 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 0 & 1 & 0 & 0 & 18.75 & -50 & 26.25 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 0 & 0 & 1 & 0 & 0 & 35 & -85 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 0 \\
            4 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & -4 & 1 & 0 & 0 & 1 & 0 & 0 & 0 \\
            0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 4 & -10 & 4 & 0 & 0 & 1 & 0 & 0 \\
            0 & 0 & 0 & 0 & 0 & 0 & 0  & 1 & 0 & 0 & 9 & -20 & 9 & 0 & 0 & 1 & 0 \\
            0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 16 & -34 & 0 & 0 & 0 & 1 \\
            1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 0 & -4 & 1 & 0 & 0 \\
            0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 4 & -10 & 4 & 0 \\
            0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 9 & -20 & 9 \\
            0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 16 & -34
        \end{bmatrix} ^{-1}
        \begin{bmatrix}
            0 \\
            0 \\
            0 \\
            0 \\
            16 \\
            0 \\
            0 \\
            0 \\
            0 \\
            0 \\
            0 \\
            0 \\
            -16 \\
            0 \\
            0 \\
            0 \\
            -16
        \end{bmatrix}        
        """).scale_about_point(0.45, ORIGIN)

        self.play(ReplacementTransform(matrix_phi, matrix_phi2))
        self.wait(2)

        matrix_phi3 = MathTex(r"""\setcounter{MaxMatrixCols}{17}
        \begin{bmatrix}
            \Phi_0 \\
            \Phi_1 \\
            \Phi_2 \\
            \Phi_3 \\
            \Phi_4 \\
            \Phi_5 \\
            \Phi_6 \\
            \Phi_7 \\
            \Phi_8 \\
            \Phi_9 \\
            \Phi_{10} \\
            \Phi_{11} \\
            \Phi_{12} \\
            \Phi_{13} \\
            \Phi_{14} \\
            \Phi_{15} \\
            \Phi_{16}
        \end{bmatrix}
        =
        \begin{bmatrix}
            0.4424 \\
            0.3509 \\
            0.1489 \\
            -0.1479 \\
            -0.5323 \\
            0.4062 \\
            0.3384 \\
            0.2466 \\
            0.1334 \\
            0.4724 \\
            0.5454 \\
            0.6579 \\
            0.8093 \\
            0.4955 \\
            0.5948 \\
            0.7189 \\
            0.8565 
        \end{bmatrix}
        """).scale_about_point(0.55, ORIGIN)

        self.play(ReplacementTransform(matrix_phi2, matrix_phi3))
        self.wait(2)


        # argh!
        
        # ! Adding the circle

        circle: list[VMobject] = []

        CIRCLE_RADIUS = 3

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=2*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=2*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
  
        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=CIRCLE_RADIUS)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=CIRCLE_RADIUS)

        circle += [RedSector, WhiteSector]

        # Adding the radial and angular lines

        d_theta = TAU/6
        d_radial = CIRCLE_RADIUS / 5

        min_theta = 0 * d_theta  # multiple of d_theta
        max_theta = 6 * d_theta  # multiple of d_theta
        min_radial = 0 * d_radial # multiple of d_radial
        max_radial = 5 * d_radial # multiple of d_radial

        theta = min_theta
        while theta <= max_theta:
            circle.append(ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=GREY, t_range=np.array((min_radial, max_radial))))
            theta += d_theta

        r = min_radial
        while r <= max_radial:
            circle.append(ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_range=np.array((min_theta, max_theta))))
            r += d_radial

        # these have to be in front of course
        circle+= [RedArc, WhiteArc]

        # The dots!

        dots_oh_my: list[Dot()] = []
        lables_oh_my: list[Text()] = []
        dot_count = 0

        theta = min_theta + d_theta
        r = min_radial + d_radial
        while (theta < max_theta+d_radial): 
            while (r < max_radial):
                dots_oh_my.append(Dot(point=(r*np.sin(theta))*UP+(r*np.cos(theta))*RIGHT, radius=1.5*DOT_LABEL_SIZE))
                lables_oh_my.append(Text(text=str(dot_count+1 if dot_count<=15 else (dot_count-7 if dot_count <= 19 else dot_count-15)), size=0.3, color=BLACK).next_to(dots_oh_my[dot_count], direction=0))
                circle.append(dots_oh_my[dot_count])
                circle.append(lables_oh_my[dot_count])
                r += d_radial
                dot_count += 1
            r = min_theta + d_radial
            theta += d_theta
        
        dots_oh_my.append(Dot(radius=1.5*DOT_LABEL_SIZE))
        lables_oh_my.append(Text(text=str(0), size=0.3, color=BLACK).next_to(dots_oh_my[dot_count], direction=0))
        circle.append(dots_oh_my[dot_count])
        circle.append(lables_oh_my[dot_count])

        circleGroup = VGroup(*circle)

        self.play(ApplyMethod(matrix_phi3.shift, 4*LEFT), run_time=0.7)
        self.play(Create(circleGroup.shift(2*RIGHT)), run_time=2)

        self.wait(2)

class FDM_part_7(Scene):
    def construct(self):
        CIRCLE_RADIUS = 3

        d_theta = TAU/6
        d_radial = CIRCLE_RADIUS / 5

        min_theta = 0 * d_theta  # multiple of d_theta
        max_theta = 6 * d_theta  # multiple of d_theta
        min_radial = 0 * d_radial # multiple of d_radial
        max_radial = 7 * d_radial # multiple of d_radial

        radial_theta_lines = []

        theta = min_theta
        while theta <= max_theta:
            radial_theta_lines.append(ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=GREY, t_range=np.array((min_radial, max_radial)), stroke_width=0.75*DEFAULT_STROKE_WIDTH))
            theta += d_theta

        r = min_radial
        while r <= max_radial:
            radial_theta_lines.append(ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_range=np.array((min_theta, max_theta)), stroke_width=0.75*DEFAULT_STROKE_WIDTH))
            r += d_radial

        lines = VGroup(*radial_theta_lines)

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=2*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=2*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
        
        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=CIRCLE_RADIUS)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=CIRCLE_RADIUS)

        self.play(Create(RedSector), Create(WhiteSector), Create(lines))
        self.play(Create(RedArc), Create(WhiteArc))
        
        self.wait(1)

        BlueCircle = Circle(color=BLUE, radius=0.3*np.sqrt(75)).shift(0.3*(5/2)*RIGHT+0.3*(13/3)*UP)

        self.play(Create(BlueCircle))

        self.wait(1)

        circle = Group(*self.mobjects)

        self.play(ApplyMethod(circle.scale, 0.5))
        self.play(ApplyMethod(circle.shift, 4*LEFT+UP))
        self.play(Uncreate(lines), Uncreate(BlueCircle))
        self.wait(1)

        Xemplate = TexTemplate()
        Xemplate.add_to_preamble(r"\usepackage{gensymb}")
        Xemplate.add_to_preamble(r"\usepackage{derivative}")
        Xemplate.add_to_preamble(r"\usepackage{cancel}")
        Xemplate.add_to_preamble(r"\usepackage{siunitx}")

        gauss = MathTex(r"\oint_c \epsilon \mathbf{E} \cdot \mathbf{dl} = q\\\mathbf{E} = -\mathbf{\nabla}\Phi",tex_template=Xemplate).shift(2*RIGHT+2*UP)

        gauss2 = MathTex(r"""\therefore q &= \oint_c \epsilon \left( -\mathbf{\nabla}\Phi \right) \cdot \mathbf{dl} \\
            &= \oint_c \epsilon \mathbf{\nabla}\Phi \cdot \mathbf{dl} \\
            &= \oint_c \epsilon \pdv{\Phi}{n} dl
            """, tex_template=Xemplate).shift(2*RIGHT+1*DOWN)

        capacitance = MathTex(r"C = \frac{q}{V}", tex_template=Xemplate).shift(-4*RIGHT+2.5*DOWN)

        self.play(Write(gauss))

        self.play(Write(gauss2))

        self.play(Write(capacitance))

        self.wait(2)

        cap_calc = MathTex(r"""q &=
        2\frac{-0.479 + 0.7296}{h_r}(\frac{5\sqrt{3}}{4}\epsilon_0h_r) \\
        &+\frac{-0.479 + 0.7487}{h_r}(\frac{5\sqrt{3}}{4}\epsilon_0h_r)\\
        &+2\frac{0.59 - 0.44}{h_r}(\frac{5\sqrt{3}}{4}4\epsilon_0h_r)\\
        &+\frac{0.6579 - 0.5454}{h_r}(\frac{5\sqrt{3}}{4}4\epsilon_0h_r)\\
        &+\frac{0.53 - 0.42}{h_r}(\frac{5\sqrt{3}}{4}4\epsilon_0h_r)\\
        &+2\frac{0.5948 - 0.4955}{h_r}(\frac{5\sqrt{3}}{4}4\epsilon_0h_r)\\
        &+\frac{0.58 - 0.42}{h_r}(\frac{5\sqrt{3}}{4}4\epsilon_0h_r)
        """).scale(0.6).shift(2*RIGHT)

        self.play(Unwrite(gauss), run_time=0.7)
        self.play(ReplacementTransform(gauss2, cap_calc))

        self.wait(2)

        charge_result = MathTex(r"q \approx 93.82 pC").shift(2*RIGHT+2*UP)
        cap_huh = MathTex(r"\Rightarrow C \approx \frac{93.82 pC}{2 V}").shift(2*RIGHT)
        cap_result = MathTex(r"\Leftrightarrow C \approx 46.91 pF").shift(2*RIGHT+-2*UP)
        
        self.play(ReplacementTransform(cap_calc, charge_result))
        self.wait(1)
        
        self.play(Indicate(charge_result), Indicate(capacitance))
        self.wait(1)
        
        self.play(Write(cap_huh))
        self.wait(1)

        self.play(TransformFromCopy(cap_huh, cap_result))

        self.wait(2)

        return

# ! Method of Moments

class MOM_part_1(Scene):
    def construct(self):
        CIRCLE_RADIUS = 3

        # Adding the circle

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=4*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=4*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
                       
        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=CIRCLE_RADIUS)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=CIRCLE_RADIUS)

        self.play(Create(RedSector), Create(WhiteSector), run_time=0.7)

        # Adding the radial and angular lines

        d_theta = TAU/6
        d_radial = CIRCLE_RADIUS / 5

        min_theta = 0 * d_theta  # multiple of d_theta
        max_theta = 6 * d_theta  # multiple of d_theta
        min_radial = 0 * d_radial # multiple of d_radial
        max_radial = 5 * d_radial # multiple of d_radial

        # dont need this just yet methinks

        theta = min_theta
        while theta <= max_theta:
            self.play(Create(ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=GREY, t_range=np.array((min_radial, max_radial)))), run_time=0.2)
            theta += d_theta

        r = min_radial
        while r <= max_radial:
            self.play(Create(ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_range=np.array((min_theta, max_theta)))), run_time=0.2)
            r += d_radial

        # these have to be in front of course
        self.play(Create(RedArc), Create(WhiteArc), run_time=0.4)

        circle = VGroup(*self.mobjects)

        segment_colours = ["#222222", "#555555", "#AAAAAA", "#AAFFAA", "#55FF55", "#22FF22"]
        segments: list[ParametricFunction] = []
        rhos: list[Tex] = []
        charges: list[Dot] = []

        theta = min_theta+d_theta
        i = 0
        while theta < max_theta:
            segments.append(ParametricFunction(lambda t: np.array((
                (max_radial)*np.cos(t), (max_radial)*np.sin(t), 0)), color=segment_colours[i], t_range=np.array((theta, theta+d_theta)), stroke_width=1.5*DEFAULT_STROKE_WIDTH))
            charges.append(Dot((max_radial)*np.cos(theta+d_theta/2)*RIGHT + (max_radial)*np.sin(theta+d_theta/2)*UP, color=BLUE_C))
            rhos.append(MathTex(r"Q_" + str(i+1), size=0.4, color=BLUE_C).move_to((max_radial+0.5)*np.cos(theta+d_theta/2)*RIGHT + (max_radial+0.5)*np.sin(theta+d_theta/2)*UP))
            
            theta += d_theta
            i += 1
        
        segmentsGroup = VGroup(*segments)
        rhosGroup = VGroup(*rhos)
        chargesGroup = VGroup(*charges)

        self.play(Create(segmentsGroup), run_time=1.5)
        self.play(Write(rhosGroup), Create(chargesGroup))

        self.wait(2)

        dots_oh_my: list[Dot()] = []
        lables_oh_my: list[Text()] = []
        dot_count = 0

        theta = min_theta + d_theta
        r = min_radial + d_radial
        while (theta < max_theta+d_radial): 
            while (r < max_radial):
                dots_oh_my.append(Dot(point=(r*np.sin(theta))*UP+(r*np.cos(theta))*RIGHT, radius=1.5*DOT_LABEL_SIZE))
                lables_oh_my.append(Text(text=str(dot_count+1), size=0.3, color=BLACK).next_to(dots_oh_my[dot_count], direction=0))
                self.play(Create(dots_oh_my[dot_count]), Write(lables_oh_my[dot_count]), run_time=0.05)
                r += d_radial
                dot_count += 1
            r = min_theta + d_radial
            theta += d_theta
        
        dots_oh_my.append(Dot(radius=1.5*DOT_LABEL_SIZE))
        lables_oh_my.append(Text(text=str(0), size=0.3, color=BLACK).next_to(dots_oh_my[dot_count], direction=0))
        self.play(Create(dots_oh_my[dot_count]), Write(lables_oh_my[dot_count]), runtime=0.05)

        self.wait(2)

class MOM_part_2(Scene):
    def construct(self):
        MOMemplate = TexTemplate()
        # MOMemplate.add_to_preamble(r"\usepackage{unicode-math}") # this one is really buggy.
        # MOMemplate.add_to_preamble(r"\usepackage{gensymb}")
        # MOMemplate.add_to_preamble(r"\usepackage{derivative}")

        gauss_3d = MathTex(r"\oint _s \epsilon \mathbf{E} \cdot \mathbf{dA} = \int \rho_s ds", tex_template=MOMemplate).shift(3*UP)

        self.play(Write(gauss_3d))
        self.wait(2)

        gauss_2d = MathTex(r"\oint _c \epsilon \mathbf{E} \cdot \mathbf{dl} = \int \rho_l dl", tex_template=MOMemplate).shift(1.5*UP)

        self.play(Indicate(gauss_3d), Write(gauss_2d))
        self.wait(1)

        gauss_2d_2 = MathTex(r"\Rightarrow 2 \pi r \epsilon E = \int \rho_l dl", tex_template=MOMemplate).shift(0*DOWN)

        self.play(TransformFromCopy(gauss_2d, gauss_2d_2))
        self.wait(1)

        gauss_2d_3 = MathTex(r"\Rightarrow 2 \pi r \epsilon E = \rho_l \Delta l", tex_template=MOMemplate).shift(1.5*DOWN)
        
        self.play(TransformFromCopy(gauss_2d_2, gauss_2d_3))
        self.wait(1)

        gauss_2d_4 = MathTex(r"\therefore E = \frac{\rho_l \Delta l}{2 \pi r \epsilon}", tex_template=MOMemplate).shift(3*DOWN)
        
        self.play(TransformFromCopy(gauss_2d_3, gauss_2d_4))
        self.wait(1)

        electric_field = Group(*self.mobjects)

        self.play(ApplyMethod(electric_field.shift, 3*LEFT))
        self.wait(1)

        potential = MathTex(r"E = - \nabla \Phi", tex_template=MOMemplate).shift(3*UP, 3*RIGHT)
        
        self.play(Write(potential))
        self.wait(1)

        potential2 = MathTex(r"\Rightarrow \Phi = - \int E dl", tex_template=MOMemplate).shift(1.5*UP, 3*RIGHT)

        self.play(TransformFromCopy(potential, potential2))
        self.wait(1)

        self.play(Circumscribe(potential2), Indicate(gauss_2d_4))
        self.wait(1)

        potential3 = MathTex(r"\Rightarrow \Phi = - \int \frac{\rho_l \Delta l}{2 \pi r \epsilon} dr", tex_template=MOMemplate).shift(0*UP, 3*RIGHT)
        
        self.play(TransformFromCopy(potential2, potential3))
        self.wait(1)

        potential4 = MathTex(r"\Leftrightarrow \Phi = - \frac{\rho_l \Delta l}{2 \pi \epsilon} ln \lvert r \rvert", tex_template=MOMemplate).shift(-1.5*UP, 3*RIGHT)
        self.play(TransformFromCopy(potential3, potential4))
        self.wait(1)

        potential5 = MathTex(r"\therefore \Phi = \sum - \frac{\rho_l \Delta l}{2 \pi \epsilon} ln \lvert r - r' \rvert", tex_template=MOMemplate).shift(-3*UP, 3*RIGHT)
        self.play(TransformFromCopy(potential4, potential5))
        self.wait(1)

        self.wait(2)

class MOM_part_3(Scene):
    def construct(self):
        arc = ParametricFunction(lambda t: np.array((
            3*np.cos(t), 3*np.sin(t), 0)), color=RED, t_range=np.array((1*TAU/12, 5*TAU/12)), stroke_width=5*DEFAULT_STROKE_WIDTH).shift(2*DOWN)
        self.play(Create(arc), run_time=2)
        self.wait(1)

        point_a = Dot(point=3*np.cos(1*TAU/12)*RIGHT+3*np.sin(1*TAU/12)*UP, radius=2*DOT_LABEL_SIZE).shift(2*DOWN)
        point_b = Dot(point=3*np.cos(5*TAU/12)*RIGHT+3*np.sin(5*TAU/12)*UP, radius=2*DOT_LABEL_SIZE).shift(2*DOWN)

        label_a = Text("A", size=0.7, color=BLACK).shift(3*np.cos(1*TAU/12)*RIGHT+3*np.sin(1*TAU/12)*UP+2*DOWN)
        label_b = Text("B", size=0.7, color=BLACK).shift(3*np.cos(5*TAU/12)*RIGHT+3*np.sin(5*TAU/12)*UP+2*DOWN)

        self.play(Create(point_a), Create(point_b))
        self.play(Write(label_a), Write(label_b))

        self.wait(1)

        arc_group = Group(*self.mobjects)

        self.play(ApplyMethod(arc_group.shift, 4*LEFT))

        potential = MathTex(r"\Phi = \int _{A} ^ {B} - \frac{\rho_l \Delta l}{2 \pi \epsilon} ln \lvert r \rvert dr").shift(3*UP+2.5*RIGHT)
        self.play(Write(potential))

        potential2 = MathTex(r"\Leftrightarrow \Phi = \int _{-\frac{h_\theta r_0}{2}} ^ {+\frac{h_\theta r_0}{2}} - \frac{\rho_l \Delta l}{2 \pi \epsilon} ln \lvert r \rvert dr").shift(1.2*UP+2.5*RIGHT)
        self.play(TransformFromCopy(potential, potential2))

        potential_notes = MathTex(r"h_\theta r_0 = 0.1 \frac{\pi}{3}", color=RED).shift(0*UP+2.5*RIGHT)
        self.play(Write(potential_notes))

        potential3 = MathTex(r"\Rightarrow \Phi = - \frac{\rho_l \Delta l}{2 \pi \epsilon} \left( r ln \lvert r \rvert - r\right) \vert _{-0.1 \frac{\pi}{6}} ^{+0.1 \frac{\pi}{6}}").shift(-1.2*UP+2.5*RIGHT)
        self.play(Write(potential3))

        potential4 = MathTex(r"\therefore \Phi \approx \frac{\rho_l \Delta l}{2 \pi \epsilon} \left( 0.3995 \right)").shift(-2.4*UP+2.5*RIGHT)
        self.play(TransformFromCopy(potential3, potential4))

        text_this = Text("(ini adalah potensial pada titik singuler)", size=0.4).next_to(potential4, direction=DOWN)
        self.play(Write(text_this))

        self.wait(2)

class MOM_part_4(Scene):
    def construct(self):
        CIRCLE_RADIUS = 3

        # Adding the circle...

        circle = []

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=4*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=4*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
                       
        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=CIRCLE_RADIUS)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=CIRCLE_RADIUS)

        circle += [RedSector,WhiteSector]

        # Adding the radial and angular lines

        d_theta = TAU/6
        d_radial = CIRCLE_RADIUS / 5

        min_theta = 0 * d_theta  # multiple of d_theta
        max_theta = 6 * d_theta  # multiple of d_theta
        min_radial = 0 * d_radial # multiple of d_radial
        max_radial = 5 * d_radial # multiple of d_radial

        theta = min_theta
        while theta <= max_theta:
            circle.append(ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=GREY, t_range=np.array((min_radial, max_radial))))
            theta += d_theta

        r = min_radial
        while r <= max_radial:
            circle.append(ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_range=np.array((min_theta, max_theta))))
            r += d_radial

        # these have to be in front of course
        circle += [RedArc, WhiteArc]

        circleGroup = VGroup(*circle)

        self.play(Create(circleGroup), run_time= 4)

        # Segments!

        segment_colours = ["#222222", "#555555", "#AAAAAA", "#AAFFAA", "#55FF55", "#22FF22"]
        segments: list[ParametricFunction] = []
        rhos: list[Tex] = []
        charges: list[Dot] = []

        theta = min_theta+d_theta
        i = 0
        while theta < max_theta:
            segments.append(ParametricFunction(lambda t: np.array((
                (max_radial)*np.cos(t), (max_radial)*np.sin(t), 0)), color=segment_colours[i], t_range=np.array((theta, theta+d_theta)), stroke_width=1.5*DEFAULT_STROKE_WIDTH))
            charges.append(Dot((max_radial)*np.cos(theta+d_theta/2)*RIGHT + (max_radial)*np.sin(theta+d_theta/2)*UP, color=BLUE_C))
            rhos.append(MathTex(r"Q_" + str(i+1), size=0.4, color=BLUE_C).move_to((max_radial+0.5)*np.cos(theta+d_theta/2)*RIGHT + (max_radial+0.5)*np.sin(theta+d_theta/2)*UP))
            
            theta += d_theta
            i += 1
        
        segmentsGroup = VGroup(*segments)
        rhosGroup = VGroup(*rhos)
        chargesGroup = VGroup(*charges)

        self.play(Create(segmentsGroup), run_time=1.5)
        self.play(Write(rhosGroup), Create(chargesGroup))

        self.wait(2)

        # Dots and labels, oh my!

        dots_oh_my: list[Dot()] = []
        lables_oh_my: list[Text()] = []
        dot_count = 0

        theta = min_theta + d_theta
        r = min_radial + d_radial
        while (theta < max_theta+d_radial): 
            while (r < max_radial):
                dots_oh_my.append(Dot(point=(r*np.sin(theta))*UP+(r*np.cos(theta))*RIGHT, radius=1.5*DOT_LABEL_SIZE))
                lables_oh_my.append(Text(text=str(dot_count+1), size=0.3, color=BLACK).next_to(dots_oh_my[dot_count], direction=0))
                # self.play(Create(dots_oh_my[dot_count]), Write(lables_oh_my[dot_count]), run_time=0.05)
                r += d_radial
                dot_count += 1
            r = min_theta + d_radial
            theta += d_theta
        
        dots_oh_my.append(Dot(radius=1.5*DOT_LABEL_SIZE))
        lables_oh_my.append(Text(text=str(0), size=0.3, color=BLACK).next_to(dots_oh_my[dot_count], direction=0))
        # self.play(Create(dots_oh_my[dot_count]), Write(lables_oh_my[dot_count]), runtime=0.05)

        dotlabGroup = VGroup(*dots_oh_my, *lables_oh_my)

        # self.play(Create(dotlabGroup))

        for charge in charges:
            for charge_prime in charges:
                if charge != charge_prime:
                    self.play(ShowPassingFlash(Line(charge.get_center(), charge_prime.get_center()), time_width=2), run_time=0.75)
            self.wait(0.5)

        AllGroup = VGroup(circleGroup, segmentsGroup, chargesGroup, rhosGroup)

        self.wait(2)

        self.play(ApplyMethod(AllGroup.shift, 15*LEFT))

        charges_matrix = MathTex(r"""
            \begin{bmatrix}
        -1.598 & 0.4log(0.1) & 0.1log(0.1\sqrt{3}) & 0.1log(0.2) & 0.1log(0.1\sqrt{3}) & 0.1log(0.1) \\
        0.4log(0.1) & -1.598 & 0.1log(0.1) & 0.1log(0.1\sqrt{3}) & 0.1log(0.2) & 0.1log(0.1\sqrt{3}) \\
        0.4log(0.1\sqrt{3}) & 0.4log(0.1) & -0.3995 & 0.1log(0.1) & 0.1log(0.1\sqrt{3}) & 0.1log(0.2) \\
        0.4log(0.2) & 0.4log(0.1\sqrt{3}) & 0.1log(0.1) & -0.3995 & 0.1log(0.1) & 0.1log(0.1\sqrt{3}) \\
        0.4log(0.1\sqrt{3}) & 0.4log(0.2) & 0.1log(0.1\sqrt{3}) & 0.1log(0.1) & -0.3995 & 0.1log(0.1) \\
        0.4log(0.1) & 0.4log(0.1\sqrt{3}) & 0.1log(0.2) & 0.1log(0.1\sqrt{3}) & 0.1log(0.1) & -0.3995 \\
            \end{bmatrix}
            \begin{bmatrix}
        \rho_l{}_1 \\
        \rho_l{}_2 \\
        \rho_l{}_3 \\
        \rho_l{}_4 \\
        \rho_l{}_5 \\
        \rho_l{}_6 \\
            \end{bmatrix}
        =
            \begin{bmatrix}
        2\pi\epsilon_0 \\
        2\pi\epsilon_0 \\
        -8\pi\epsilon_0 \\
        -8\pi\epsilon_0 \\
        -8\pi\epsilon_0 \\
        -8\pi\epsilon_0 \\
            \end{bmatrix}        
        """).scale(0.5)

        charges_matrix2 = MathTex(r"""
        \begin{bmatrix}
            \rho_l{}_1 \\
            \rho_l{}_2 \\
            \rho_l{}_3 \\
            \rho_l{}_4 \\
            \rho_l{}_5 \\
            \rho_l{}_6 \\
        \end{bmatrix}
        =
        \begin{bmatrix}
            -0.1694\mathrm{x}10^{-9} \\
            -0.1694\mathrm{x}10^{-9} \\
            0.6924\mathrm{x}10^{-9} \\
            0.2688\mathrm{x}10^{-9} \\
            0.2688\mathrm{x}10^{-9} \\
            0.6924\mathrm{x}10^{-9} \\
        \end{bmatrix}     
        """)

        self.play(Write(charges_matrix))
        self.wait(1)

        self.play(ReplacementTransform(charges_matrix, charges_matrix2))

        self.wait(2)

class MOM_part_5(Scene):
    def construct(self):
        charge_dist = MathTex(r"""
        \begin{bmatrix}
            \rho_l{}_1 \\
            \rho_l{}_2 \\
            \rho_l{}_3 \\
            \rho_l{}_4 \\
            \rho_l{}_5 \\
            \rho_l{}_6 \\
        \end{bmatrix}
        =
        \begin{bmatrix}
            -0.1694\mathrm{x}10^{-9} \\
            -0.1694\mathrm{x}10^{-9} \\
            0.6924\mathrm{x}10^{-9} \\
            0.2688\mathrm{x}10^{-9} \\
            0.2688\mathrm{x}10^{-9} \\
            0.6924\mathrm{x}10^{-9} \\
        \end{bmatrix}     
        """)

        self.play(Write(charge_dist))
        self.wait(1)

        self.play(ApplyMethod(charge_dist.shift, 4*LEFT))

        # ! Adding the circle...
        CIRCLE_RADIUS = 3

        circle = []

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=4*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=4*DEFAULT_STROKE_WIDTH, radius=CIRCLE_RADIUS)
                       
        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=CIRCLE_RADIUS)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=CIRCLE_RADIUS)

        circle += [RedSector,WhiteSector]

        # Adding the radial and angular lines

        d_theta = TAU/6
        d_radial = CIRCLE_RADIUS / 5

        min_theta = 0 * d_theta  # multiple of d_theta
        max_theta = 6 * d_theta  # multiple of d_theta
        min_radial = 0 * d_radial # multiple of d_radial
        max_radial = 5 * d_radial # multiple of d_radial

        theta = min_theta
        while theta <= max_theta:
            circle.append(ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=GREY, t_range=np.array((min_radial, max_radial))))
            theta += d_theta

        r = min_radial
        while r <= max_radial:
            circle.append(ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_range=np.array((min_theta, max_theta))))
            r += d_radial

        # these have to be in front of course
        circle += [RedArc, WhiteArc]

        circleGroup = VGroup(*circle)

        # self.play(Create(circleGroup), run_time= 4)

        # Segments!

        segment_colours = ["#222222", "#555555", "#AAAAAA", "#AAFFAA", "#55FF55", "#22FF22"]
        segments: list[ParametricFunction] = []
        rhos: list[Tex] = []
        charges: list[Dot] = []

        theta = min_theta+d_theta
        i = 0
        while theta < max_theta:
            segments.append(ParametricFunction(lambda t: np.array((
                (max_radial)*np.cos(t), (max_radial)*np.sin(t), 0)), color=segment_colours[i], t_range=np.array((theta, theta+d_theta)), stroke_width=1.5*DEFAULT_STROKE_WIDTH))
            charges.append(Dot((max_radial)*np.cos(theta+d_theta/2)*RIGHT + (max_radial)*np.sin(theta+d_theta/2)*UP, color=BLUE_C))
            rhos.append(MathTex(r"Q_" + str(i+1), size=0.4, color=BLUE_C).move_to((max_radial+0.5)*np.cos(theta+d_theta/2)*RIGHT + (max_radial+0.5)*np.sin(theta+d_theta/2)*UP))
            
            theta += d_theta
            i += 1
        
        segmentsGroup = VGroup(*segments)
        rhosGroup = VGroup(*rhos)
        chargesGroup = VGroup(*charges)

        # self.play(Create(segmentsGroup), run_time=1.5)
        # self.play(Write(rhosGroup), Create(chargesGroup))

        # self.wait(2)

        # Dots and labels, oh my!

        dots_oh_my: list[Dot()] = []
        lables_oh_my: list[Text()] = []
        dot_count = 0

        theta = min_theta + d_theta
        r = min_radial + d_radial
        while (theta < max_theta+d_radial): 
            while (r < max_radial):
                dots_oh_my.append(Dot(point=(r*np.sin(theta))*UP+(r*np.cos(theta))*RIGHT, radius=1.5*DOT_LABEL_SIZE))
                lables_oh_my.append(Text(text=str(dot_count+1 if dot_count<=15 else (dot_count-7 if dot_count <= 19 else dot_count-15)), size=0.3, color=BLACK).next_to(dots_oh_my[dot_count], direction=0))
                # self.play(Create(dots_oh_my[dot_count]), Write(lables_oh_my[dot_count]), run_time=0.05)
                r += d_radial
                dot_count += 1
            r = min_theta + d_radial
            theta += d_theta
        
        dots_oh_my.append(Dot(radius=1.5*DOT_LABEL_SIZE))
        lables_oh_my.append(Text(text=str(0), size=0.3, color=BLACK).next_to(dots_oh_my[dot_count], direction=0))
        # self.play(Create(dots_oh_my[dot_count]), Write(lables_oh_my[dot_count]), runtime=0.05)

        dotlabGroup = VGroup(*dots_oh_my, *lables_oh_my)

        AllGroup = VGroup(circleGroup, segmentsGroup, chargesGroup, rhosGroup, dotlabGroup)

        self.play(Create(AllGroup.shift(3*RIGHT)), run_time=4, rate_func=rate_functions.linear)

        self.wait(2)

        # ! CIRCLE DONE

        what_IS_Q_though = MathTex(r"\Phi = \sum - \frac{\rho_l \Delta l}{2 \pi \epsilon} ln \lvert r - r' \rvert").next_to(charge_dist, direction=DOWN)

        self.play(Write(what_IS_Q_though))
        self.wait(2)

        potential_dist = MathTex(r"""\setcounter{MaxMatrixCols}{17}
        \begin{bmatrix}
            \Phi_0 \\
            \Phi_1 \\
            \Phi_2 \\
            \Phi_3 \\
            \Phi_4 \\
            \Phi_5 \\
            \Phi_6 \\
            \Phi_7 \\
            \Phi_8 \\
            \Phi_9 \\
            \Phi_{10} \\
            \Phi_{11} \\
            \Phi_{12} \\
            \Phi_{13} \\
            \Phi_{14} \\
            \Phi_{15} \\
            \Phi_{16}
        \end{bmatrix}
        =
        \begin{bmatrix}
            0.6145 \\
            0.4723 \\
            0.3095 \\
            0.1111 \\
            -0.1740 \\
            0.6318 \\
            0.6877 \\
            0.7983 \\
            1.0165 \\
            0.6685\\
            0.7725 \\
            0.8579 \\
            0.9244 \\
            0.7183 \\
            0.8254 \\
            0.8875 \\
            0.9349 
        \end{bmatrix}
        """).scale_about_point(0.7, ORIGIN).shift(4*LEFT)

        self.play(ApplyMethod(charge_dist.shift,10*LEFT), Unwrite(what_IS_Q_though))
        self.play(Write(potential_dist))

        self.wait(3)

        self.play(Unwrite(potential_dist))
        self.play(ApplyMethod(charge_dist.shift,10*RIGHT))
        
        
        what_is_Q = MathTex(r"Q = \rho_l \Delta l ; \Delta l \approx 0.1").next_to(charge_dist, direction=DOWN)

        self.play(Write(what_is_Q))
        self.wait(2)
  
        charges_lol = MathTex(r"""
        \begin{bmatrix}
            Q_1 \\
            Q_2 \\
            Q_3 \\
            Q_4 \\
            Q_5 \\
            Q_6 \\
        \end{bmatrix}
        =
        \begin{bmatrix}
           -0.1694\mathrm{x}10^{-10} \\
           -0.1694\mathrm{x}10^{-10} \\
            0.6924\mathrm{x}10^{-10} \\
            0.2688\mathrm{x}10^{-10} \\
            0.2688\mathrm{x}10^{-10} \\
            0.6924\mathrm{x}10^{-10} \\
        \end{bmatrix}     
        """).scale(0.7).shift(4*LEFT+2*UP)

        self.play(Unwrite(what_is_Q), ReplacementTransform(charge_dist, charges_lol), ApplyMethod(AllGroup.scale, 0.8))
        self.wait(2)

        capacitance = MathTex(r"C = \frac{q}{V}").next_to(charge_dist, direction=DOWN)

        whats_lowercase_q = Tex(r"Ambil $q$ sebagai \\ muatan konduktor +1V.", size=0.8).next_to(capacitance, direction=DOWN)

        self.play(Write(capacitance))
        self.wait(1)

        self.play(Write(whats_lowercase_q), Indicate(VGroup(*(charges[1:5]+rhos[1:5])), run_time=2))
        self.wait(1)
        
        capacitance2 = MathTex(r"q = Q_2 + Q_3 + Q_4 + Q_5", size=0.9).next_to(whats_lowercase_q, direction=DOWN)
        capacitance3 = MathTex(r"q = 0.1992 nC").next_to(whats_lowercase_q, direction=DOWN)

        self.play(Write(capacitance2))
        self.wait(1)

        self.play(ReplacementTransform(capacitance2, capacitance3))
        self.wait(1)

        capacitance_final = MathTex(r"C = \frac{0.1992 nC}{2 V}").next_to(charge_dist, direction=DOWN)

        self.play(ReplacementTransform(capacitance, capacitance_final), Unwrite(capacitance3), Unwrite(whats_lowercase_q), Unwrite(charges_lol))
        self.wait(1)

        capacitance_result = MathTex(r"C = 96.12 pF").next_to(capacitance_final, direction=DOWN)
        self.play(TransformFromCopy(capacitance_final, capacitance_result))
        self.wait(3)