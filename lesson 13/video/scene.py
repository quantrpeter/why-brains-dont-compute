"""
Lesson 13 – Color
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 13/video"
    manim render -qh scene.py ColorExplainer
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


class ColorExplainer(VoiceoverScene):
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

        self.intro()
        self.color_space()
        self.color_constancy()
        self.color_contrast()
        self.empirical_explanation()
        self.summary()
        self.outro()

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

    def intro(self):
        title = self.zh("顏色", font_size=56, color=C_BLUE)
        sub_en = self.en("Color", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第十三課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)

        with self.voiceover(
            text="大家好！歡迎嚟到第十三課。今日我哋會講顏色視覺。"
            "顏色係腦嘅經驗建構，唔係物理屬性。"
            "我哋會講色空間、顏色恆常性、顏色對比、同埋經驗主義解釋。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def color_space(self):
        heading = self.make_heading("色空間")

        dims = VGroup(
            self.zh("•  色相（hue）— 紅、橙、黃、綠、藍、紫", font_size=24, color=C_RED),
            self.zh("•  飽和度（saturation）— 顏色純度", font_size=24, color=C_ORANGE),
            self.zh("•  明度（lightness）— 明暗", font_size=24, color=C_YELLOW),
            self.zh("•  四種獨特色：紅、綠、黃、藍", font_size=24, color=C_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="色空間有三個維度：色相、飽和度、明度。"
            "色相係紅橙黃綠藍紫。飽和度係顏色純度。明度係明暗。"
            "有四種獨特色：紅、綠、黃、藍，其他色都係佢哋嘅混合。"
        ):
            self.play(Write(heading), run_time=0.6)
            for d in dims:
                self.play(FadeIn(d, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def color_constancy(self):
        heading = self.make_heading("顏色恆常性")

        key = self.zh(
            "表面喺唔同照明下保持表觀顏色",
            font_size=28, color=C_GREEN,
        ).shift(UP * 0.3)

        desc = self.zh(
            "日光、燈光、陰影 — 表面反射嘅光譜唔同，但感知顏色一樣",
            font_size=22, color=C_WHITE,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="顏色恆常性：表面喺唔同照明下保持表觀顏色。"
            "日光、燈光、陰影 — 表面反射嘅光譜唔同，但感知顏色一樣。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(key), run_time=0.8)
            self.play(FadeIn(desc), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def color_contrast(self):
        heading = self.make_heading("顏色對比")

        key = self.zh(
            "相同光譜喺唔同背景睇落唔同色",
            font_size=28, color=C_YELLOW,
        ).shift(UP * 0.3)

        note = self.zh(
            "唔係適應造成 — 係即時嘅對比效應",
            font_size=24, color=C_ORANGE,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="顏色對比：相同光譜喺唔同背景睇落唔同色。"
            "呢個唔係適應造成，係即時嘅對比效應。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(key), run_time=0.8)
            self.play(FadeIn(note), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def empirical_explanation(self):
        heading = self.make_heading("經驗主義解釋")

        key = self.zh(
            "光譜模式嘅發生頻率 → 預測對比同恆常性",
            font_size=26, color=C_GREEN,
        ).shift(UP * 0.3)

        desc = self.zh(
            "自然場景嘅光譜統計 — 唔係物理屬性，係腦為生物優勢而建構",
            font_size=24, color=C_WHITE,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="經驗主義解釋：光譜模式嘅發生頻率可以預測對比同恆常性。"
            "自然場景嘅光譜統計 — 顏色唔係物理屬性，係腦為生物優勢而建構嘅。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(key), run_time=0.8)
            self.play(FadeIn(desc), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def summary(self):
        heading = self.make_heading("總結", font_size=44)

        bullets = VGroup(
            self.zh("•  色相、飽和度、明度；四種獨特色", font_size=24, color=C_GREEN),
            self.zh("•  顏色恆常性：照明變但感知唔變", font_size=24, color=C_ORANGE),
            self.zh("•  顏色對比：背景改變表觀顏色", font_size=24, color=C_PINK),
            self.zh("•  光譜頻率預測對比同恆常性", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="總結：色相、飽和度、明度，四種獨特色。"
            "顏色恆常性：照明變但感知唔變。顏色對比：背景改變表觀顏色。"
            "光譜頻率可以預測對比同恆常性。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.5)
        self.clear()

    def outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)

        with self.voiceover(
            text="多謝收睇！下一課我哋會講顏色心理物理學，"
            "探討 JND 同 Bezold-Brücke 效應。記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)

        self.wait(1)
        self.play(FadeOut(thanks), run_time=0.8)
