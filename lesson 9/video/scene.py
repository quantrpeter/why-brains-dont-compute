"""
Lesson 9 – Spatial Intervals
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 9/video"
    manim render -qh scene.py SpatialIntervalsExplainer
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


class SpatialIntervalsExplainer(VoiceoverScene):
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
        self.discrepancies()
        self.frequency_of_occurrence()
        self.vertical_horizontal()
        self.empirical_ranking()
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
        title = self.zh("空間間距", font_size=56, color=C_BLUE)
        sub_en = self.en("Spatial Intervals", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第九課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)

        with self.voiceover(
            text="大家好！歡迎嚟到第九課。今日我哋會講空間間距嘅感知。"
            "點解感知到嘅線段長度同物理測量唔一樣？"
            "我哋會用自然場景嘅發生頻率數據嚟解釋。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def discrepancies(self):
        heading = self.make_heading("差異：同一投影，唔同來源")

        problem = self.zh(
            "同一種視網膜投影可以嚟自唔同嘅物理長度同方向",
            font_size=26, color=C_RED,
        ).shift(UP * 0.3)

        example = self.zh(
            "短線近距離 vs 長線遠距離 — 投影可以一樣",
            font_size=24, color=C_ORANGE,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="同一種視網膜投影可以嚟自好多唔同嘅物理來源。"
            "短線近距離，同長線遠距離，投影可以完全一樣。"
            "腦冇辦法單靠投影計算出真實長度。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(problem), run_time=0.8)
            self.play(FadeIn(example), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def frequency_of_occurrence(self):
        heading = self.make_heading("點樣測定發生頻率")

        points = VGroup(
            self.zh("•  激光掃描自然場景", font_size=26, color=C_GREEN),
            self.zh("•  用模板採樣線段投影", font_size=26, color=C_ORANGE),
            self.zh("•  統計唔同投影出現嘅頻率", font_size=26, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)

        with self.voiceover(
            text="科學家用激光掃描自然場景，用模板採樣線段投影。"
            "然後統計唔同投影出現嘅頻率。"
            "呢啲數據可以預測我哋點樣感知長度。"
        ):
            self.play(Write(heading), run_time=0.6)
            for p in points:
                self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def vertical_horizontal(self):
        heading = self.make_heading("垂直同水平錯覺")

        illusion = self.zh(
            "垂直線睇落比水平線長 — 即使物理長度一樣",
            font_size=28, color=C_YELLOW,
        ).shift(UP * 0.3)

        reason = self.zh(
            "深度中嘅表面會縮短；重力限制垂直延伸 → 短垂直投影更常見",
            font_size=22, color=C_GREEN,
        ).shift(DOWN * 0.3)

        peak = self.zh(
            "約 30° 偏離垂直時，感知長度最大",
            font_size=24, color=C_PINK,
        ).shift(DOWN * 1.0)

        with self.voiceover(
            text="經典例子：垂直線睇落比水平線長，即使物理長度一樣。"
            "點解？深度中嘅表面會縮短，重力限制咗垂直延伸。"
            "所以短嘅垂直投影更常見。約三十度偏離垂直時，感知長度最大。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(illusion), run_time=0.8)
            self.play(FadeIn(reason), run_time=0.8)
            self.play(FadeIn(peak), run_time=0.6)

        self.wait(0.3)
        self.clear()

    def empirical_ranking(self):
        heading = self.make_heading("經驗排名")

        key = self.zh(
            "按頻率尺度排名 → 預測心理物理結果",
            font_size=28, color=C_GREEN,
        ).shift(UP * 0.3)

        desc = self.zh(
            "發生頻率高嘅投影，感知長度較大；頻率低嘅，感知較短",
            font_size=24, color=C_WHITE,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="關鍵係經驗排名。按頻率尺度排名，可以預測心理物理結果。"
            "發生頻率高嘅投影，感知長度較大；頻率低嘅，感知較短。"
            "呢個就係經驗主義對空間間距嘅解釋。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(key), run_time=0.8)
            self.play(FadeIn(desc), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def summary(self):
        heading = self.make_heading("總結", font_size=44)

        bullets = VGroup(
            self.zh("•  同一投影可嚟自唔同物理長度同方向", font_size=24, color=C_GREEN),
            self.zh("•  激光掃描測定自然場景嘅投影頻率", font_size=24, color=C_ORANGE),
            self.zh("•  垂直線錯覺：短垂直投影更常見", font_size=24, color=C_PINK),
            self.zh("•  經驗排名預測心理物理結果", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="總結：同一投影可嚟自唔同物理長度。"
            "激光掃描測定自然場景嘅投影頻率。"
            "垂直線錯覺可以用短垂直投影更常見嚟解釋。"
            "經驗排名可以預測心理物理結果。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.5)
        self.clear()

    def outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)

        with self.voiceover(
            text="多謝收睇！下一課我哋會講角度，"
            "探討點解銳角會被高估、鈍角會被低估。記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)

        self.wait(1)
        self.play(FadeOut(thanks), run_time=0.8)
