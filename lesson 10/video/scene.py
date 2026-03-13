"""
Lesson 10 – Angles
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 10/video"
    manim render -qh scene.py AnglesExplainer
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


class AnglesExplainer(VoiceoverScene):
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
        self.perceived_angles()
        self.frequency_data()
        self.explanation()
        self.alternative_explanations()
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
        title = self.zh("角度", font_size=56, color=C_BLUE)
        sub_en = self.en("Angles", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第十課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)

        with self.voiceover(
            text="大家好！歡迎嚟到第十課。今日我哋會講角度嘅感知。"
            "點解銳角會被高估、鈍角會被低估？"
            "自然場景嘅角度投影頻率可以解釋呢個現象。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def perceived_angles(self):
        heading = self.make_heading("感知到嘅角度")

        points = VGroup(
            self.zh("•  銳角 — 被高估（睇落大過實際）", font_size=26, color=C_GREEN),
            self.zh("•  鈍角 — 被低估（睇落細過實際）", font_size=26, color=C_ORANGE),
            self.zh("•  系統性嘅錯估，唔係隨機誤差", font_size=26, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)

        with self.voiceover(
            text="銳角會被高估，睇落大過實際。鈍角會被低估，睇落細過實際。"
            "呢個係系統性嘅錯估，唔係隨機誤差。"
        ):
            self.play(Write(heading), run_time=0.6)
            for p in points:
                self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def frequency_data(self):
        heading = self.make_heading("角度來源嘅頻率")

        key = self.zh(
            "激光掃描顯示：90° 投影最唔常見",
            font_size=28, color=C_YELLOW,
        ).shift(UP * 0.3)

        reason = self.zh(
            "直角來源需要較大嘅平面表面 — 自然界較少見",
            font_size=24, color=C_GREEN,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="激光掃描自然場景顯示，九十度嘅投影最唔常見。"
            "點解？直角來源需要較大嘅平面表面，自然界較少見。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(key), run_time=0.8)
            self.play(FadeIn(reason), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def explanation(self):
        heading = self.make_heading("經驗主義解釋")

        prediction = self.zh(
            "投影角度嘅經驗排名 → 預測心理物理數據",
            font_size=26, color=C_GREEN,
        ).shift(UP * 0.3)

        desc = self.zh(
            "較少見嘅角度投影，感知上會被放大；較常見嘅會被縮細",
            font_size=24, color=C_WHITE,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="投影角度嘅經驗排名可以預測心理物理數據。"
            "較少見嘅角度投影，感知上會被放大；較常見嘅會被縮細。"
            "所以銳角高估、鈍角低估，同頻率數據吻合。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(prediction), run_time=0.8)
            self.play(FadeIn(desc), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def alternative_explanations(self):
        heading = self.make_heading("其他解釋點解唔成立")

        alts = VGroup(
            self.zh("•  眼睛解剖 — 冇證據支持", font_size=24, color=C_DIM),
            self.zh("•  側抑制 — 冇證據支持", font_size=24, color=C_DIM),
            self.zh("•  經驗排名係唯一能預測數據嘅框架", font_size=24, color=C_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)

        with self.voiceover(
            text="有人提出眼睛解剖、側抑制等解釋，但係冇證據支持。"
            "經驗排名係唯一能預測心理物理數據嘅框架。"
        ):
            self.play(Write(heading), run_time=0.6)
            for a in alts:
                self.play(FadeIn(a, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def summary(self):
        heading = self.make_heading("總結", font_size=44)

        bullets = VGroup(
            self.zh("•  銳角高估、鈍角低估", font_size=24, color=C_GREEN),
            self.zh("•  90° 投影最唔常見 — 直角需要大平面", font_size=24, color=C_ORANGE),
            self.zh("•  經驗排名預測心理物理數據", font_size=24, color=C_PINK),
            self.zh("•  其他解釋（解剖、側抑制）冇證據", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="總結：銳角高估、鈍角低估。九十度投影最唔常見，因為直角需要大平面。"
            "經驗排名可以預測心理物理數據。其他解釋冇證據支持。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.5)
        self.clear()

    def outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)

        with self.voiceover(
            text="多謝收睇！下一課我哋會講明暗度，"
            "探討點解亮度同感知嘅明暗唔成正比。記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)

        self.wait(1)
        self.play(FadeOut(thanks), run_time=0.8)
