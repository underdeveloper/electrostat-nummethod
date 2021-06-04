from manim import * #pylint: disable=unused-import, unused-wildcard-import

class MainProblem(Scene):
    def construct(self):

        memplate = TexTemplate()
        memplate.add_to_preamble(r"\usepackage{gensymb}")

        RedArc = Arc(color=RED, start_angle=0, angle=-2*TAU /
                     3, stroke_width=2*DEFAULT_STROKE_WIDTH)
        WhiteArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-
                       TAU/3, stroke_width=2*DEFAULT_STROKE_WIDTH)

        self.play(Create(RedArc))
        self.play(Create(WhiteArc))
        self.play(ApplyMethod(RedArc.scale_about_point, 2, ORIGIN),
                  ApplyMethod(WhiteArc.scale_about_point, 2, ORIGIN))
        self.foreground_mobjects += RedArc
        self.foreground_mobjects += WhiteArc

        RedVolt = Tex('$+1V$', color=RED).shift(1.7*LEFT+1.7*DOWN).scale(0.7)
        WhiteVolt = Tex('$-1V$', color=WHITE).shift(1.7*RIGHT+1.7*UP).scale(0.7)

        self.play(Write(RedVolt), Write(WhiteVolt))

        RedSector = Sector(color='#021a00', start_angle=0,
                           angle=-2*TAU/3, outer_radius=2.0)
        WhiteSector = Sector(color='#0f0e12', start_angle=0,
                             angle=TAU/3, outer_radius=2.0)

        self.play(Create(RedSector), Create(WhiteSector))

        RedPermissivity = Tex('$4 \\epsilon _0$', color='#00ff00').shift(0.2*LEFT+1.5*DOWN).scale(0.7)
        WhitePermissivity = Tex('$\\epsilon _0$', color='#d2bdff').shift(0.2*RIGHT+1.5*UP).scale(0.7)

        self.play(Write(RedPermissivity), Write(WhitePermissivity))
        
        Text1 = Text("Kedua batang ini terpisahkan\npada perubahan warna.\n(diskontinu)").scale(0.35)

        self.play(Write(Text1))
        
        AngleArc = Arc(color=YELLOW_C, start_angle=-2*TAU/3, angle=-TAU/3,
                       stroke_width=0.8*DEFAULT_STROKE_WIDTH).scale_about_point(0.5, ORIGIN)
        AngleText = Tex('$\\frac{2\\pi}{3}rad$', color=YELLOW_C, 
                        tex_template=memplate).scale(0.5).next_to(AngleArc, direction=0.6*UP)

        RadiusLine = Line(ORIGIN, 2*RIGHT, color=YELLOW_A)
        RadiusText = Tex('$10cm$', color=YELLOW_A, 
                        tex_template=memplate).scale(0.5).next_to(RadiusLine, direction=0.6*UP)

        self.play(ApplyMethod(Text1.shift, 4.2*RIGHT))
        self.play(Write(AngleText), Write(RadiusText),
                    Create(AngleArc), Create(RadiusLine))

        Text2 = Text("Dengan menggunakan FDM dan MOM, akan dicari distribusi potensial\ndi area dalam lingkaran dan juga nilai kapasitansi yang ada.").scale(0.4).shift(3*DOWN)
        
        self.play(Write(Text2))

        self.wait(3)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait(1)