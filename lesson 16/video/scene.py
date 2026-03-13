"""
Lesson 16 – Motion Direction
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 16/video"
    manim render -qh scene.py MotionDirectionExplainer
"""

from manim import *
from manim_voiceover import VoiceoverScene
from edge_tts_service import EdgeTTSService

C_BG = "#0f0f23"
C_BLUE = "#4fc3f7"
C_GREEN = "#81c784"
C_ORANGE = "#ffb74d"
C_PINK = "#f48fb1"
C_PURPLE = "#ce93d8"
C_YELLOW = "#fff176"
C_WHITE = "#e0e0e0"
C_RED = "#ef5350"
C_DIM = "#555577"
C_CYAN = "#4dd0e1"

FONT = "Noto Sans CJK HK"
MONO = "Menlo"


class MotionDirectionExplainer(VoiceoverScene):
    def construct(self):
        self.set_speech_service(EdgeTTSService(voice="zh-HK-HiuMaanNeural", rate="+0%"))
        self.camera.background_color = BLACK
        self.bg_image = ImageMobject("wallpaper1.jpg")
        self.bg_image.height = config.frame_height
        self.bg_image.width = config.frame_width
        self.add(self.bg_image)
        self.bg_overlay = Rectangle(width=config.frame_width + 0.5, height=config.frame_height + 0.5, fill_color=BLACK, fill_opacity=0.55, stroke_width=0)
        self.add(self.bg_overlay)
        self.watermark = self.zh("香港編程學會", font_size=18, color="#9999bb").to_corner(UL, buff=0.3)
        self.add(self.watermark)
        self.scene_intro()
        self.scene_apertures()
        self.scene_circular_aperture()
        self.scene_vertical_slit()
        self.scene_explanation()
        self.scene_summary()
        self.scene_outro()

    def zh(self, txt, **kw):
        kw.setdefault("font", FONT)
        kw.setdefault("color", C_WHITE)
        return Text(txt, **kw)

    def en(self, txt, **kw):
        kw.setdefault("color", C_WHITE)
        return Text(txt, **kw)

    def mono(self, txt, **kw):
        kw.setdefault("font", MONO)
        kw.setdefault("color", C_WHITE)
        return Text(txt, **kw)

    def clear(self):
        keep = {self.bg_image, self.bg_overlay, self.watermark}
        to_fade = [m for m in self.mobjects if m not in keep]
        if to_fade:
            self.play(*[FadeOut(m) for m in to_fade], run_time=0.5)

    def make_box(self, label, color, width=2.5, height=0.8):
        rect = RoundedRectangle(corner_radius=0.15, width=width, height=height, fill_color=color, fill_opacity=0.25, stroke_color=color)
        txt = self.zh(label, font_size=24, color=color).move_to(rect)
        return VGroup(rect, txt)

    def make_heading(self, text, color=C_BLUE, font_size=40):
        return self.zh(text, font_size=font_size, color=color).to_edge(UP, buff=0.5)

    def scene_intro(self):
        title = self.zh("運動方向", font_size=56, color=C_BLUE)
        sub_en = self.en("Motion Direction", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第十六課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第十六課。"
            "今日我哋會講運動方向嘅感知。"
            "孔徑嘅形狀會改變感知嘅方向。"
            "圓形孔徑、垂直狹縫都會產生唔同嘅效應，"
            "好似理髮店招牌效應咁。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_apertures(self):
        heading = self.make_heading("孔徑效應")
        frame_box = self.make_box("框架改變感知", C_GREEN, width=4.0, height=0.8)
        frame_box.shift(UP * 1.2)
        desc = self.zh(
            "同一運動，唔同孔徑形狀 → 唔同感知方向",
            font_size=22, color=C_WHITE,
        ).next_to(frame_box, DOWN, buff=0.4)
        examples = self.zh(
            "圓形孔徑、垂直狹縫、水平狹縫各有唔同效應",
            font_size=20, color=C_DIM,
        ).shift(DOWN * 0.3)
        with self.voiceover(
            text="孔徑效應係指框架會改變感知。"
            "同一種運動，唔同孔徑形狀會產生唔同嘅感知方向。"
            "圓形孔徑、垂直狹縫、水平狹縫各有唔同嘅效應。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(frame_box), FadeIn(desc), run_time=0.8)
            self.play(FadeIn(examples), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_circular_aperture(self):
        heading = self.make_heading("圓形孔徑")
        circle = Circle(radius=0.8, color=C_BLUE, stroke_width=3)
        circle.shift(UP * 0.5)
        line = Line(LEFT * 0.6, RIGHT * 0.6, color=C_ORANGE, stroke_width=4)
        line.move_to(circle.get_center()).rotate(45 * DEGREES)
        result = self.zh(
            "感知方向：垂直於線條方向",
            font_size=24, color=C_GREEN,
        ).next_to(circle, DOWN, buff=0.6)
        freq = self.zh(
            "圓形遮擋下投影方向嘅出現頻率可預測",
            font_size=20, color=C_DIM,
        ).shift(DOWN * 1.2)
        with self.voiceover(
            text="圓形孔徑入面，一條斜線運動。"
            "感知嘅方向會係垂直於線條嘅方向。"
            "呢個可以由圓形遮擋下投影方向嘅出現頻率嚟預測。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(Create(circle), Create(line), run_time=0.8)
            self.play(FadeIn(result), run_time=0.5)
            self.play(FadeIn(freq), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_vertical_slit(self):
        heading = self.make_heading("垂直狹縫：理髮店招牌效應")
        slit = Rectangle(width=0.3, height=1.5, color=C_PINK, stroke_width=3)
        slit.shift(UP * 0.5)
        barber = self.zh("理髮店招牌效應", font_size=28, color=C_PINK)
        barber.next_to(slit, DOWN, buff=0.5)
        observation = self.zh(
            "水平運動嘅條紋，透過垂直狹縫睇 → 感知為垂直運動",
            font_size=22, color=C_WHITE,
        ).shift(DOWN * 0.8)
        with self.voiceover(
            text="垂直狹縫產生理髮店招牌效應。"
            "水平運動嘅條紋，透過垂直狹縫睇嘅時候，"
            "會感知為垂直運動。"
            "最短嘅線長度可以正交填滿孔徑，"
            "短啲嘅線出現頻率更高，所以有正交偏向。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(Create(slit), run_time=0.5)
            self.play(FadeIn(barber), FadeIn(observation), run_time=0.8)
        self.wait(0.3)
        self.clear()

    def scene_explanation(self):
        heading = self.make_heading("經驗主義解釋")
        min_len = self.make_box("最短線長正交填滿孔徑", C_GREEN, width=4.5, height=0.8)
        min_len.shift(UP * 1.0)
        freq_box = self.make_box("短線出現頻率更高", C_ORANGE, width=4.5, height=0.8)
        freq_box.next_to(min_len, DOWN, buff=0.4)
        bias = self.zh(
            "正交偏向：感知方向偏向孔徑嘅正交方向",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 0.5)
        with self.voiceover(
            text="經驗主義嘅解釋係：最短嘅線長度可以正交填滿孔徑。"
            "短啲嘅線出現頻率更高。"
            "所以有正交偏向，感知方向會偏向孔徑嘅正交方向。"
            "遮擋線投影嘅出現頻率可以預測孔徑效應。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(min_len), FadeIn(freq_box), run_time=0.8)
            self.play(FadeIn(bias), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  孔徑形狀改變感知運動方向", font_size=24, color=C_GREEN),
            self.zh("•  圓形孔徑：感知垂直於線條方向", font_size=24, color=C_ORANGE),
            self.zh("•  垂直狹縫：理髮店招牌效應，水平變垂直", font_size=24, color=C_PINK),
            self.zh("•  正交偏向：短線頻率更高，由遮擋投影預測", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。孔徑形狀會改變感知嘅運動方向。"
            "圓形孔徑入面，感知方向垂直於線條。"
            "垂直狹縫產生理髮店招牌效應，水平運動睇落係垂直。"
            "正交偏向係因為短線出現頻率更高，可以由遮擋投影預測。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：物體大小", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講物體大小嘅感知，"
            "包括艾賓浩斯效應、大小距離悖論、同埋月亮錯覺。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
