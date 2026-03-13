"""
Lesson 11 – Lightness and Darkness
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 11/video"
    manim render -qh scene.py LightnessDarknessExplainer
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


class LightnessDarknessExplainer(VoiceoverScene):
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
        self.simultaneous_contrast()
        self.physiological_explanation()
        self.gelb_experiment()
        self.empirical_approach()
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
        title = self.zh("明暗度", font_size=56, color=C_BLUE)
        sub_en = self.en("Lightness and Darkness", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第十一課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)

        with self.voiceover(
            text="大家好！歡迎嚟到第十一課。今日我哋會講明暗度嘅感知。"
            "點解亮度同感知嘅明暗唔成正比？"
            "同時對比、Gelb 實驗、同埋經驗主義嘅解釋。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def simultaneous_contrast(self):
        heading = self.make_heading("同時對比")

        luminance = self.zh("亮度 vs 明暗感", font_size=28, color=C_YELLOW).shift(UP * 0.5)
        desc = self.zh(
            "物理亮度（luminance）唔等於感知明暗（lightness）",
            font_size=24, color=C_WHITE,
        ).shift(UP * 0.1)

        contrast = self.zh(
            "同一灰度喺深色背景睇落較亮，喺淺色背景睇落較暗",
            font_size=24, color=C_GREEN,
        ).shift(DOWN * 0.5)

        with self.voiceover(
            text="亮度同明暗感唔一樣。物理亮度唔等於感知明暗。"
            "同時對比：同一灰度喺深色背景睇落較亮，喺淺色背景睇落較暗。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(luminance), FadeIn(desc), run_time=0.8)
            self.play(FadeIn(contrast), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def physiological_explanation(self):
        heading = self.make_heading("生理學解釋：感受野")

        points = VGroup(
            self.zh("•  視網膜神經節細胞有中心-周邊感受野", font_size=24, color=C_GREEN),
            self.zh("•  周邊抑制 — 周圍區域抑制中心反應", font_size=24, color=C_ORANGE),
            self.zh("•  似乎可以解釋同時對比", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)

        with self.voiceover(
            text="傳統解釋話視網膜神經節細胞有中心周邊感受野。"
            "周邊抑制，周圍區域會抑制中心反應。"
            "似乎可以解釋同時對比。但係呢個解釋有漏洞。"
        ):
            self.play(Write(heading), run_time=0.6)
            for p in points:
                self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def gelb_experiment(self):
        heading = self.make_heading("Gelb 實驗")

        setup = self.zh(
            "黑色紙喺強光下 — 睇落係白色",
            font_size=26, color=C_YELLOW,
        ).shift(UP * 0.3)

        key = self.zh(
            "當加多一張更亮嘅白紙，黑紙即刻睇返黑色",
            font_size=24, color=C_RED,
        ).shift(DOWN * 0.2)

        conclusion = self.zh(
            "語境決定明暗感 — 唔係單純周邊抑制",
            font_size=24, color=C_GREEN,
        ).shift(DOWN * 0.9)

        with self.voiceover(
            text="Gelb 實驗：黑色紙喺強光下睇落係白色。"
            "當加多一張更亮嘅白紙，黑紙即刻睇返黑色。"
            "語境決定明暗感，唔係單純周邊抑制可以解釋。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(setup), run_time=0.8)
            self.play(FadeIn(key), run_time=0.8)
            self.play(FadeIn(conclusion), run_time=0.6)

        self.wait(0.3)
        self.clear()

    def empirical_approach(self):
        heading = self.make_heading("經驗主義嘅 approach")

        key = self.zh(
            "自然表面嘅經驗決定感知明暗值",
            font_size=28, color=C_GREEN,
        ).shift(UP * 0.3)

        desc = self.zh(
            "唔係計算反射率，而係基於發生頻率嘅經驗排名",
            font_size=24, color=C_WHITE,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="經驗主義嘅 approach：自然表面嘅經驗決定感知明暗值。"
            "唔係計算反射率，而係基於發生頻率嘅經驗排名。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(key), run_time=0.8)
            self.play(FadeIn(desc), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def summary(self):
        heading = self.make_heading("總結", font_size=44)

        bullets = VGroup(
            self.zh("•  亮度 ≠ 明暗感；同時對比", font_size=24, color=C_GREEN),
            self.zh("•  感受野、周邊抑制 — 唔足以解釋", font_size=24, color=C_ORANGE),
            self.zh("•  Gelb 實驗：context 決定明暗", font_size=24, color=C_PINK),
            self.zh("•  經驗主義：發生頻率決定感知", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="總結：亮度唔等於明暗感，有同時對比。"
            "感受野同周邊抑制唔足以解釋。Gelb 實驗顯示 context 決定明暗。"
            "經驗主義話發生頻率決定感知。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.5)
        self.clear()

    def outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)

        with self.voiceover(
            text="多謝收睇！下一課我哋會講經驗排名，"
            "形式化刺激模式嘅發生頻率點樣決定感知。記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)

        self.wait(1)
        self.play(FadeOut(thanks), run_time=0.8)
