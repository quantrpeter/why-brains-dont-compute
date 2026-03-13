"""
Lesson 12 – Empirical Ranking
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 12/video"
    manim render -qh scene.py EmpiricalRankingExplainer
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


class EmpiricalRankingExplainer(VoiceoverScene):
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
        self.recurrent_patterns()
        self.luminance_lightness()
        self.complex_patterns()
        self.feedback_loop()
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
        title = self.zh("經驗排名", font_size=56, color=C_BLUE)
        sub_en = self.en("Empirical Ranking", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第十二課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)

        with self.voiceover(
            text="大家好！歡迎嚟到第十二課。今日我哋會形式化經驗排名。"
            "刺激模式嘅發生頻率點樣決定感知質素？"
            "我哋會講重複模式、亮度同明暗、複雜模式、同埋反饋迴路。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def recurrent_patterns(self):
        heading = self.make_heading("刺激係重複模式")

        points = VGroup(
            self.zh("•  影像激活視網膜受體 — 每個模式有獨特激活", font_size=22, color=C_GREEN),
            self.zh("•  簡單嘅重複模式係關鍵", font_size=26, color=C_ORANGE),
            self.zh("•  唔係單一像素，而係模式嘅共現", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)

        with self.voiceover(
            text="影像激活視網膜受體，每個模式有獨特激活。"
            "簡單嘅重複模式係關鍵，唔係單一像素，而係模式嘅共現。"
        ):
            self.play(Write(heading), run_time=0.6)
            for p in points:
                self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def luminance_lightness(self):
        heading = self.make_heading("亮度同明暗")

        key = self.zh(
            "附近表面共享反射率同照明 → 頻率決定明暗感",
            font_size=26, color=C_GREEN,
        ).shift(UP * 0.3)

        desc = self.zh(
            "同一亮度模式在不同 context 出現嘅頻率 → 排名 → 感知",
            font_size=24, color=C_WHITE,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="附近表面共享反射率同照明，所以頻率決定明暗感。"
            "同一亮度模式在不同 context 出現嘅頻率，經排名後，決定感知。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(key), run_time=0.8)
            self.play(FadeIn(desc), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def complex_patterns(self):
        heading = self.make_heading("解釋複雜模式")

        key = self.zh(
            "亮度共現嘅百分位排名 → 預測對比效應",
            font_size=28, color=C_YELLOW,
        ).shift(UP * 0.3)

        desc = self.zh(
            "同時對比、Gelb 效應等複雜現象都可以用經驗排名預測",
            font_size=24, color=C_GREEN,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="亮度共現嘅百分位排名可以預測對比效應。"
            "同時對比、Gelb 效應等複雜現象都可以用經驗排名預測。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(key), run_time=0.8)
            self.play(FadeIn(desc), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def feedback_loop(self):
        heading = self.make_heading("反饋迴路")

        steps = VGroup(
            self.zh("1. 經驗排名 → 感知", font_size=26, color=C_GREEN),
            self.zh("2. 感知 → 行為", font_size=26, color=C_ORANGE),
            self.zh("3. 行為 → 生存", font_size=26, color=C_PINK),
            self.zh("4. 生存 → 強化經驗排名", font_size=26, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="經驗排名產生感知，感知引導行為，行為影響生存。"
            "生存成功會強化經驗排名嘅形成。"
            "呢個係一個正反饋迴路。"
        ):
            self.play(Write(heading), run_time=0.6)
            for s in steps:
                self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def summary(self):
        heading = self.make_heading("總結", font_size=44)

        bullets = VGroup(
            self.zh("•  刺激係重複模式；模式共現係關鍵", font_size=24, color=C_GREEN),
            self.zh("•  亮度共現頻率 → 明暗感", font_size=24, color=C_ORANGE),
            self.zh("•  百分位排名預測對比效應", font_size=24, color=C_PINK),
            self.zh("•  反饋迴路：經驗 → 感知 → 行為 → 生存", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="總結：刺激係重複模式，模式共現係關鍵。"
            "亮度共現頻率決定明暗感。百分位排名預測對比效應。"
            "反饋迴路：經驗產生感知，感知引導行為，行為影響生存。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.5)
        self.clear()

    def outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)

        with self.voiceover(
            text="多謝收睇！下一課我哋會講顏色，"
            "探討色相、飽和度、明度、同埋顏色恆常性。記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)

        self.wait(1)
        self.play(FadeOut(thanks), run_time=0.8)
