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

        Text1 = Text(
            "Kedua batang ini terpisahkan\npada perubahan warna.").scale(0.35)

        RedVolt = Tex('$+1V$', color=RED).shift(1.7*LEFT+1.7*DOWN).scale(0.7)
        WhiteVolt = Tex('$-1V$', color=WHITE).shift(1.7 *
                                                    RIGHT+1.7*UP).scale(0.7)

        RedPermissivity = Tex('$4 \\epsilon _0$', color='#00ff00').shift(
            0.2*LEFT+1.5*DOWN).scale(0.7)
        WhitePermissivity = Tex('$\\epsilon _0$', color='#d2bdff').shift(
            0.2*RIGHT+1.5*UP).scale(0.7)

        AngleArc = Arc(color=WHITE, start_angle=-2*TAU/3, angle=-TAU/3,
                       stroke_width=0.8*DEFAULT_STROKE_WIDTH).scale_about_point(0.5, ORIGIN)
        AngleText = Tex('$\\frac{2\\pi}{3}rad$', color=WHITE, tex_template=thisTemplate).shift(
            0.5*RIGHT+0.6*UP).scale(0.5)

        self.play(Create(RedArc))
        self.play(Create(WhiteArc))
        self.play(ApplyMethod(RedArc.scale_about_point, 2, ORIGIN),
                  ApplyMethod(WhiteArc.scale_about_point, 2, ORIGIN)
                  )
        self.play(Write(RedVolt), Write(WhiteVolt))
        self.play(Create(RedSector), Create(WhiteSector))
        self.play(Write(RedPermissivity), Write(WhitePermissivity))
        self.play(Write(Text1))
        self.play(ApplyMethod(Text1.shift, 4.2*RIGHT),
                  Create(AngleArc), Write(AngleText))
        self.wait(3)
