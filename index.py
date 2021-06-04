from manim import * #pylint: disable=unused-import, unused-wildcard-import

class Problem(Scene):
    def construct(self):

        thisTemplate = TexTemplate()
        thisTemplate.add_to_preamble(r"\usepackage{gensymb}")

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=2*DEFAULT_STROKE_WIDTH)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=2*DEFAULT_STROKE_WIDTH)

        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=2.0)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=2.0)

        Text1 = Text("Kedua batang ini terpisahkan\npada perubahan warna.").scale(0.35)

        RedVolt = Tex('$+1V$', color=RED).shift(1.7*LEFT+1.7*DOWN).scale(0.7)
        WhiteVolt = Tex('$-1V$', color=WHITE).shift(1.7*RIGHT+1.7*UP).scale(0.7)

        RedPermissivity = Tex('$4 \\epsilon _0$', color='#00ff00').shift(0.2*LEFT+1.5*DOWN).scale(0.7)
        WhitePermissivity = Tex('$\\epsilon _0$', color='#d2bdff').shift(0.2*RIGHT+1.5*UP).scale(0.7)

        AngleArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-TAU/3,
                       stroke_width=0.8*DEFAULT_STROKE_WIDTH).scale_about_point(0.5, ORIGIN)
        AngleText = Tex('$\\frac{2\\pi}{3}rad$', color=WHITE, 
                        tex_template=thisTemplate).shift(0.5*RIGHT+0.6*UP).scale(0.5)

        self.add_foreground_mobjects(RedArc, WhiteArc) # This permanently sticks the objects in the foreground!!!
        self.play(Create(RedArc))
        self.play(Create(WhiteArc))
        self.play(ApplyMethod(RedArc.scale_about_point, 2, ORIGIN),
                  ApplyMethod(WhiteArc.scale_about_point, 2, ORIGIN))
        self.play(Write(RedVolt), Write(WhiteVolt))
        self.play(Create(RedSector), Create(WhiteSector))
        # self.bring_to_front(RedArc, WhiteArc) # impossible to play continuously with create sectors?
        self.play(Write(RedPermissivity), Write(WhitePermissivity))
        self.play(Write(Text1))
        self.play(ApplyMethod(Text1.shift, 4.2*RIGHT),
                  Create(AngleArc), Write(AngleText))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait()

class EstablishFDM(Scene):
    def construct(self):
        # Declaring extra packages
        fdm_template = TexTemplate()
        fdm_template.add_to_preamble(r"\usepackage{derivative}")
        fdm_template.add_to_preamble(r"\usepackage{cancel}")

        # central_diff = Tex('$\\odv{\\Phi}{x}_{x_0} \\approx \\frac{\\Phi\\left ( x_0 + h \\right ) - \\Phi\\left ( x_0 - h \\right )}{2h} + \\frac{h^2}{3!2}\\odv[2]{\\Phi}{x}_{x_0}$', color=BLUE, tex_template=fdm_template)
        central_diff_r = Tex('$\\odv{\\Phi}{r}_{r_0} \\approx \\frac{\\Phi\\left ( r_0 + h \\right ) - \\Phi\\left ( r_0 - h \\right )}{2h} + \\frac{h^2}{3!2}\\odv[2]{\\Phi}{r}_{r_0}$', color=BLUE, tex_template=fdm_template)
        cdr_narration = Text("Ini adalah metode perbedaan tengah.").shift(UP)
        cdr_narration2 = Text("\"central difference method\"").scale(0.6)
        cdr_narration2.next_to(cdr_narration, UP)
        cdr_narration2.shift(1.5*RIGHT)

        laplace_eq = Tex('$\\nabla^2 \\Phi = 0$')

        laplacian_polar = Tex('$\\nabla^2 \\Phi = \\pdv[2]{\\Phi}{r} + \\frac{1}{r} \\pdv{\\Phi}{r} + \\frac{1}{r^2} \\pdv[2]{\\Phi}{\\theta}$', tex_template=fdm_template)
        laplacian_polar.shift(DOWN)

        self.play(Write(central_diff_r))
        self.play(Write(cdr_narration), Write(cdr_narration2)) 
        # There used to be a Transform() here, from a copy of cdr_narration into cdr_narration2.
        # I think that caused the problem with how cdr_narration2 interacts with animations? Not sure.

        # Found out the solution. Transform() defaults to that ^^
        # What I should be using instead is ReplacementTransform()!
        self.wait(1)
        self.play(FadeOut(cdr_narration), FadeOut(cdr_narration2))
        self.play(ApplyMethod(central_diff_r.shift, UP))
        self.play(Write(laplace_eq, duration=2), Write(laplacian_polar))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait()

class EstablishFDM2(Scene):
    def construct(self):
        # Declaring extra packages
        fdm_template = TexTemplate()
        fdm_template.add_to_preamble(r"\usepackage{derivative}")
        fdm_template.add_to_preamble(r"\usepackage{cancel}")

        fdm_dr2 = Tex('$\\pdv[2]{\\Phi}{r} \\approx \\frac{\\Phi _1 + \\Phi _2 - 2\\Phi _0}{h_r^2}$',
                      tex_template=fdm_template).shift(UP)
        fdm_dr = Tex('$\\frac{1}{r} \\pdv{\\Phi}{r} \\approx \\frac{1}{r} \\frac{\\Phi_1 - \\Phi_2}{2h_r}$', tex_template=fdm_template)
        fdm_dT = Tex( '$\\frac{1}{r^2} \\pdv[2]{\\Phi}{\\theta} \\approx \\frac{1}{r^2} \\frac{\\Phi_3 + \\Phi_4 - 2\\Phi _0}{h_\\theta}$', tex_template=fdm_template).shift(DOWN)

        laplacian_fdm = Tex('$\\nabla^2 \\Phi \\approx \\frac{\\Phi _1 + \\Phi _2 - 2\\Phi _0}{h_r^2} + \\frac{1}{r} \\frac{\\Phi _1 - \\Phi _2}{2h_r} + \\frac{1}{r^2} \\frac{\\Phi _3 + \\Phi _4 - 2\\Phi _0}{h_\\theta}$', tex_template=fdm_template)
        laplacian_fdm2 = Tex('$\\nabla^2 \\Phi \\approx \\frac{\\Phi _1 + \\Phi _2 - 2\\Phi _0}{h_r^2} + \\frac{h_r}{2r} \\cdot \\frac{\\Phi _1 - \\Phi _2}{h_r^2} + \\frac{1}{r^2} \\frac{\\Phi _3 + \\Phi _4 - 2\\Phi _0}{h_\\theta}$', tex_template=fdm_template)
        laplacian_fdm3 = Tex('$\\nabla^2 \\Phi \\vert_{h_r = h_\\theta = h \\rightarrow 0} \\approx \\frac{\\Phi _1 + \\Phi _2 - 2\\Phi _0}{h_r^2} + \\frac{h_r}{2r} \\cdot \\frac{\\Phi _1 - \\Phi _2}{h_r^2} + \\frac{1}{r^2} \\frac{\\Phi _3 + \\Phi _4 - 2\\Phi _0}{h_\\theta}$', tex_template=fdm_template)
        laplacian_fdm3_cancel = Tex('$\\nabla^2 \\Phi \\vert_{h_r = h_\\theta = h \\rightarrow 0} \\approx \\frac{\\Phi _1 + \\Phi _2 - 2\\Phi _0}{h^2} + \\cancel{ \\frac{h}{2r} \\cdot \\frac{\\Phi _1 - \\Phi _2}{h^2} } + \\frac{1}{r^2} \\frac{\\Phi _3 + \\Phi _4 - 2\\Phi _0}{h}$', tex_template=fdm_template)
        laplacian_fdm4 = Tex('$\\nabla^2 \\Phi \\vert_{h_r = h_\\theta = h \\rightarrow 0} \\approx \\frac{\\Phi _1 + \\Phi _2 + \\Phi _3 + \\Phi _4 - 4\\Phi _0}{h}$', tex_template=fdm_template)

        # test = Tex('$\\Delta \\Phi \\mathrm{why{}is{}this{}thing{}not{}working!!!}$')

        self.play(Write(fdm_dr2), Write(fdm_dr), Write(fdm_dT))
        self.wait(1)

        self.play(FadeOut(fdm_dr2), FadeOut(fdm_dr), FadeOut(fdm_dT), Write(laplacian_fdm))
        self.wait(1)

        self.play(ReplacementTransform(laplacian_fdm, laplacian_fdm2))
        self.wait(1)

        self.play(ReplacementTransform(laplacian_fdm2, laplacian_fdm3))
        self.wait(1)

        self.play(ReplacementTransform(laplacian_fdm3, laplacian_fdm3_cancel))
        self.wait(1)

        self.play(ReplacementTransform(laplacian_fdm3_cancel, laplacian_fdm4))
        self.wait(1)
        
        laplacian_fdm5 = Tex('$\\nabla^2 \\Phi(r,\\theta) \\vert_{(r_0,\\theta_0), h} \\approx$ \\\\ $\\frac{\\Phi(r_0+h,\\theta_0) + \\Phi(r_0-h,\\theta_0) + \\Phi(r_0,\\theta_0+h) + \\Phi(r_0,\\theta_0-h) - 4\\Phi(r_0,\\theta_0)}{h}$', color=BLUE, tex_template=fdm_template)

        self.play(ApplyMethod(laplacian_fdm4.shift, 1.5*UP), Write(laplacian_fdm5))
        self.wait()


class Problem2(Scene):
    def construct(self):

        thisTemplate = TexTemplate()
        thisTemplate.add_to_preamble(r"\usepackage{gensymb}")
        thisTemplate.add_to_preamble(r"\usepackage{derivative}")
        thisTemplate.add_to_preamble(r"\usepackage{cancel}")
        thisTemplate.add_to_preamble(r"\usepackage{siunitx}")

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=2*DEFAULT_STROKE_WIDTH).scale_about_point(2, ORIGIN)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=2*DEFAULT_STROKE_WIDTH).scale_about_point(2, ORIGIN)

        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=2.0)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=2.0)

        RedVolt = Tex('$+1V$', color=RED).shift(1.7*LEFT+1.7*DOWN).scale(0.7)
        WhiteVolt = Tex('$-1V$', color=WHITE).shift(1.7 *
                                                    RIGHT+1.7*UP).scale(0.7)

        RedPermissivity = Tex('$4 \\epsilon _0$', color='#00ff00').shift(
            0.2*LEFT+1.5*DOWN).scale(0.7)
        WhitePermissivity = Tex('$\\epsilon _0$', color='#d2bdff').shift(
            0.2*RIGHT+1.5*UP).scale(0.7)

        ### TO-DONE: find how to add a mobject to the foreground WITHOUT drawing it on screen.
        ### or if possible, how to use bring_to_front() and bring_to_back() in conjunction with Play()

        ### SEE BELOW!!!

        # self.add_foreground_mobjects(RedArc, WhiteArc) # This permanently sticks the objects in the foreground!!! // OR NOT!!!
        # self.add_foreground_mobject(RedArc)
        # self.add_foreground_mobject(WhiteArc)
        
        testT = Text("Swag.")
        self.play(Write(testT))
        self.play(FadeOut(testT))

        self.play(Create(RedArc))
        self.play(Create(WhiteArc))

        ### TO-DONE :
        # Of course. it was obvious. add the objects to the foreground *after* they are drawn. duh.
        self.foreground_mobjects += RedArc
        self.foreground_mobjects += WhiteArc

        self.play(Write(RedVolt), Write(WhiteVolt))
        self.play(Create(RedSector), Create(WhiteSector))
        # self.bring_to_front(RedArc, WhiteArc) # impossible to play continuously with create sectors? (prev. line)

        self.play(Write(RedPermissivity), Write(WhitePermissivity))

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
        deltaRadius = Tex('$\\Delta r = 2 cm$', tex_template=thisTemplate).shift(2.5*DOWN)

        self.play(FadeOut(RedPermissivity), FadeOut(WhitePermissivity),
                  Write(deltaAngle))

        r = min_r
        while r <= max_r:
            self.play(Create(ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_min=min_theta, t_max=max_theta)), run_time=0.2)
            # self.add(ParametricFunction(lambda t: np.array((
            #     r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_min=min_theta, t_max=max_theta))
            r += 0.4

        self.play(Write(deltaRadius))

        dots_oh_my: list[Dot()] = []
        dot_count = 0

        theta = min_theta
        r = min_r + 0.4
        while (r < max_r):
            while (theta < max_theta):
                dots_oh_my.append(Dot(point=(r*np.sin(theta))*UP+(r*np.cos(theta))*RIGHT))
                self.play(Create(dots_oh_my[dot_count]), run_time=0.1)
                theta += TAU/6
                dot_count += 1
            r += 0.4
            theta = min_theta
        
        dots_oh_my.append(Dot())
        self.play(Create(dots_oh_my[dot_count]))
        
        self.wait(2)

class Problem3(Scene):
    def construct(self):
        
        Xemplate = TexTemplate()
        Xemplate.add_to_preamble(r"\usepackage{gensymb}")
        Xemplate.add_to_preamble(r"\usepackage{derivative}")
        Xemplate.add_to_preamble(r"\usepackage{cancel}")
        Xemplate.add_to_preamble(r"\usepackage{siunitx}")


        deriv1st = Tex(r"$\odv{\Phi}{r}\rvert_{r_0} = \frac{\Phi\left(r_0+h\right)-\Phi\left(r_0-h\right)}{2h}$", tex_template=Xemplate).move_to(3*UP)
        deriv2nd = Tex(r"$\odv[2]{\Phi}{r}\rvert_{r_0} = \frac{\Phi\left(r_0+h\right)+\Phi\left(r_0-h\right)-2\Phi\left(r_0\right)}{h^2}$", tex_template=Xemplate).move_to(2*UP)
        
        self.play(Write(deriv1st), Write(deriv2nd))

        d_theta = TAU/6
        d_radial = 1.4

        min_theta = 0 * d_theta  # multiple of d_theta
        max_theta = 2 * d_theta  # multiple of d_theta
        min_radial = 1 * d_radial # multiple of d_radial
        max_radial = 3 * d_radial # multiple of d_radial

        theta = min_theta
        while theta <= max_theta:
            self.play(Create(ParametricFunction(lambda t: np.array((
                t*np.cos(theta), t*np.sin(theta), 0)), color=BLUE, t_min=min_radial, t_max=max_radial).shift(3*DOWN+2*LEFT)), run_time=0.2)
            # self.add(ParametricFunction(lambda t: np.array((
            #     t*np.cos(theta), t*np.sin(theta), 0)), color=GREY, t_min=min_radial, t_max=max_radial))
            theta += d_theta

        r = min_radial
        while r <= max_radial:
            self.play(Create(ParametricFunction(lambda t: np.array((
               r*np.cos(t), r*np.sin(t), 0)), color=BLUE, t_min=min_theta, t_max=max_theta).shift(3*DOWN+2*LEFT)), run_time=0.2)
            # self.add(ParametricFunction(lambda t: np.array((
            #     r*np.cos(t), r*np.sin(t), 0)), color=GREY, t_min=min_theta, t_max=max_theta))
            r += d_radial

        Phi0 = Dot(point=2*d_radial*np.cos(1*d_theta)*RIGHT+2*d_radial*np.sin(1*d_theta)*UP, color=WHITE).shift(3*DOWN+2*LEFT)
        Phi0Eq = Tex(r"$\Phi_0$", color=WHITE).next_to(Phi0)
        Phi1 = Dot(point=2*d_radial*np.cos(2*d_theta)*RIGHT+2*d_radial*np.sin(2*d_theta)*UP, color=GREEN).shift(3*DOWN+2*LEFT)
        Phi1Eq = Tex(r"$\Phi_1$", color=GREEN).next_to(Phi1).shift(0.1*DOWN+0.1*LEFT)
        Phi2 = Dot(point=2*d_radial*np.cos(0*d_theta)*RIGHT+2*d_radial*np.sin(0*d_theta)*UP, color=YELLOW).shift(3*DOWN+2*LEFT)
        Phi2Eq = Tex(r"$\Phi_2$", color=YELLOW).next_to(Phi2).shift(0.3*DOWN+0.1*LEFT)
        Phi3 = Dot(point=3*d_radial*np.cos(1*d_theta)*RIGHT+3*d_radial*np.sin(1*d_theta)*UP, color=RED).shift(3*DOWN+2*LEFT)
        Phi3Eq = Tex(r"$\Phi_3$", color=RED).next_to(Phi3)
        Phi4 = Dot(point=1*d_radial*np.cos(1*d_theta)*RIGHT+1*d_radial*np.sin(1*d_theta)*UP, color=PURPLE).shift(3*DOWN+2*LEFT)
        Phi4Eq = Tex(r"$\Phi_4$", color=PURPLE).next_to(Phi4)
        self.play(Create(Phi0), Create(Phi1), Create(Phi2), Create(Phi3), Create(Phi4))
        self.play(Write(Phi0Eq), Write(Phi1Eq), Write(Phi2Eq), Write(Phi3Eq), Write(Phi4Eq))

        self.wait(1)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            # All mobjects in the screen are saved in self.mobjects
        )

        laplacian_polar = Tex('$\\nabla^2 \\Phi = \\pdv[2]{\\Phi}{r} + \\frac{1}{r} \\pdv{\\Phi}{r} + \\frac{1}{r^2} \\pdv[2]{\\Phi}{\\theta} = 0$', tex_template=Xemplate).shift(1.5*UP)

        self.play(Write(laplacian_polar))

        dPdr = Tex(r"$\odv{\Phi}{r}\rvert_{\left(r_0,\theta_0\right)} = \frac{\Phi\left(r_0+h_r,\theta_0\right)-\Phi\left(r_0-h_r,\theta_0\right)}{2h_r}$", tex_template=Xemplate).shift(0.5*UP)
        d2Pdr2 = Tex(r"$\odv[2]{\Phi}{r}\rvert_{\left(r_0,\theta_0\right)} = \frac{\Phi\left(r_0+h_r,\theta_0\right)+\Phi\left(r_0-h_r,\theta_0\right)-2\Phi\left(r_0,\theta_0\right)}{h_r^2}$", tex_template=Xemplate).shift(-0.5*UP)
        d2Pdt2 = Tex(r"$\odv[2]{\Phi}{t}\rvert_{\left(r_0,\theta_0\right)} = \frac{\Phi\left(r_0,\theta_0+h_\theta\right)+\Phi\left(r_0,\theta_0-h_\theta\right)-2\Phi\left(r_0,\theta_0\right)}{\left(h_\theta r_0\right)^2}$", tex_template=Xemplate).shift(-1.5*UP)

        self.play(Write(dPdr), Write(d2Pdr2), Write(d2Pdt2))
        self.wait(1)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            # All mobjects in the screen are saved in self.mobjects
        )

        final_eq = MathTex(r"\therefore\nabla^2\Phi&=0\\&=\frac{\Phi\left(r_0+h_r,\theta_0\right)+\Phi\left(r_0-h_r,\theta_0\right)-2\Phi\left(r_0,\theta_0\right)}{h_r^2}\\&+\frac{1}{r_0}\frac{\Phi\left(r_0+h_r,\theta_0\right)-\Phi\left(r_0-h_r,\theta_0\right)}{2h_r}\\&+\frac{1}{r_0^2}\frac{\Phi\left(r_0,\theta_0+h_\theta\right)+\Phi\left(r_0,\theta_0-h_\theta\right)-2\Phi\left(r_0,\theta_0\right)}{\left(h_\theta r_0\right)^2}", tex_template=Xemplate)
        final_eq_numbered = MathTex(r"\therefore\nabla^2\Phi&=0\\&=\frac{\Phi_1+\Phi_2-2\Phi_0}{h_r^2}\\&+\frac{1}{r_0}\frac{\Phi_1-\Phi_2}{2h_r}\\&+\frac{1}{r_0^2}\frac{\Phi_3+\Phi_4-2\Phi_0}{\left(h_\theta r_0\right)^2}", tex_template=Xemplate)

        self.play(Write(final_eq), runtime=3)
        self.wait(1)
        self.play(ReplacementTransform(final_eq, final_eq_numbered))
        self.wait(1)

        assumptions = Tex(r"Asumsikan $h = h_r\approx h_\theta r_0$ dan $h \rightarrow 0$").shift(3*DOWN)
        self.play(Write(assumptions))
        self.wait(2)

class Matrix1(Scene):
    def construct(self):
        matrix = Tex(r"$\begin{bmatrix}1&2&3\\2&4&3\\8&1&2\end{bmatrix}\begin{bmatrix}\Phi_0\\\Phi_1\\\Phi_2\end{bmatrix}=\begin{bmatrix}0\\0\\1\end{bmatrix}$")
        matrix2 = MathTex(r"""
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
    \end{bmatrix}""").scale_about_point(0.7, ORIGIN)
        # self.play(Write(matrix2))

        matrix3 = MathTex(r"""\setcounter{MaxMatrixCols}{17}
    \begin{bmatrix}
        -11.5 & 0.5 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 2 & 0 & 0 & 0 \\
        1 & -4 & 1 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
        0 & 4 & -10 & 4 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
        0 & 0 & 9 & -20 & 9 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 16 & -34 & 0 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
        2.5 & 1 & 0 & 0 & 0 & -15 & 7.5 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
        0 & 0 & 1 & 0 & 0 & 15 & -45 & 25 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 1 & 0 & 0 & 37.5 & -95 & 52.5 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 0 & 1 & 0 & 0 & 68 & -165 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 0 \\
        4 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & -4 & 1 & 0 & 0 & 1 & 0 & 0 & 0 \\
        0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 4 & -10 & 4 & 0 & 0 & 1 & 0 & 0 \\
        0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 9 & -20 & 9 & 0 & 0 & 1 & 0 \\
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
    \end{bmatrix}""").scale_about_point(0.45, ORIGIN)

        self.play(Write(matrix3))
        self.wait(2)


class MoM(Scene):
    def construct(self):
        # potential3d = MathTex(r"\Phi = \frac{1}{4\pi\epsilon_0} \sum_{i=1}^{n} \frac{Q_i}{r_i}")
        gauss2d = MathTex(r"\oint_c \epsilon \mathbf{E} \cdot \hat{\mathbf{n}} dl = \oint_c \rho_l dl")
        # \Leftrightarrow \epsilon E \oint_c dl = \rho_l \Delta l \\
        # \Leftrightarrow \epsilon E \cdot 2\pi r = \rho_l \Delta l \\
        # \Leftrightarrow E = \frac{\rho_l \Delta l}{2\pi\epsilon r}
        # \end{alignat*}""")
        self.play(Write(gauss2d))
        self.wait(2)