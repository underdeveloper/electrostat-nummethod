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

        self.play(Create(RedArc))
        self.play(Create(WhiteArc))
        self.play(ApplyMethod(RedArc.scale_about_point, 2, ORIGIN),
                  ApplyMethod(WhiteArc.scale_about_point, 2, ORIGIN))
        self.play(Write(RedVolt), Write(WhiteVolt))
        self.play(Create(RedSector), Create(WhiteSector))
        self.play(Write(RedPermissivity), Write(WhitePermissivity))
        self.play(Write(Text1))
        self.play(ApplyMethod(Text1.shift, 4.2*RIGHT),
                  Create(AngleArc), Write(AngleText))

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