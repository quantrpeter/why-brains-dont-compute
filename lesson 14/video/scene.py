"""
Lesson 14 – Color Psychophysics
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 14/video"
    manim render -qh scene.py ColorPsychophysicsExplainer
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


class ColorPsychophysicsExplainer(VoiceoverScene):
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
        self.scene_psychophysics()
        self.scene_jnd_function()
        self.scene_bezold_brucke()
        self.scene_empirical_prediction()
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
        title = self.zh("顏色心理物理學", font_size=56, color=C_BLUE)
        sub_en = self.en("Color Psychophysics", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第十四課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第十四課。"
            "今日我哋會講顏色嘅心理物理學。"
            "複雜嘅色度函數，好似剛好可察覺差異同 Bezold-Brücke 效應，"
            "都可以用自然場景嘅光譜統計嚟預測。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_psychophysics(self):
        heading = self.make_heading("顏色心理物理學")
        params_box = self.make_box("系統性變化", C_GREEN, width=4.0, height=0.8)
        params_box.shift(UP * 1.0)
        params_text = self.zh(
            "色相、飽和度、明度嘅參數變化",
            font_size=22, color=C_WHITE,
        ).next_to(params_box, DOWN, buff=0.3)
        method = self.zh(
            "心理物理學用精確嘅刺激變化嚟量度感知閾值",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 0.5)
        with self.voiceover(
            text="顏色心理物理學係系統性咁變化色相、飽和度、明度嘅參數。"
            "心理物理學用精確嘅刺激變化嚟量度感知閾值。"
            "呢啲實驗產生咗好多複雜嘅函數，"
            "傳統上以為係視覺系統嘅固有特性。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(params_box), FadeIn(params_text), run_time=0.8)
            self.play(FadeIn(method), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_jnd_function(self):
        heading = self.make_heading("剛好可察覺差異 JND")
        jnd_box = self.make_box("JND 函數", C_ORANGE, width=3.5, height=0.8)
        jnd_box.shift(UP * 1.2)
        jnd_desc = self.zh(
            "唔同波長嘅辨別閾值唔一樣，形成複雜嘅曲線",
            font_size=22, color=C_WHITE,
        ).next_to(jnd_box, DOWN, buff=0.4)
        curve = self.zh(
            "波長 → 辨別難度：某啲波長特別敏感，某啲唔係",
            font_size=20, color=C_DIM,
        ).shift(DOWN * 0.3)
        empirical = self.zh(
            "光譜頻率數據可以預測呢個複雜函數",
            font_size=24, color=C_GREEN,
        ).shift(DOWN * 1.2)
        with self.voiceover(
            text="剛好可察覺差異，英文叫 JND。"
            "唔同波長嘅辨別閾值唔一樣，形成複雜嘅曲線。"
            "某啲波長特別敏感，某啲就唔係。"
            "經驗主義嘅解釋係：自然場景嘅光譜頻率數據可以預測呢個複雜函數。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(jnd_box), FadeIn(jnd_desc), run_time=0.8)
            self.play(FadeIn(curve), run_time=0.5)
            self.play(FadeIn(empirical), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_bezold_brucke(self):
        heading = self.make_heading("Bezold-Brücke 效應")
        effect_box = self.make_box("光強度改變色相", C_PINK, width=4.0, height=0.8)
        effect_box.shift(UP * 1.2)
        short_wave = self.zh(
            "短波長：暗嘅時候偏藍，光嘅時候偏綠",
            font_size=22, color=C_CYAN,
        ).next_to(effect_box, DOWN, buff=0.4)
        long_wave = self.zh(
            "長波長：強度變化都會改變感知色相",
            font_size=22, color=C_ORANGE,
        ).next_to(short_wave, DOWN, buff=0.3)
        with self.voiceover(
            text="Bezold-Brücke 效應係指光強度改變色相。"
            "短波長嘅光，暗嘅時候偏藍，光嘅時候偏綠。"
            "長波長嘅光，強度變化都會改變感知色相。"
            "呢個效應傳統上難以解釋，"
            "但光譜共現統計可以預測呢啲心理物理函數。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(effect_box), run_time=0.5)
            self.play(FadeIn(short_wave), run_time=0.5)
            self.play(FadeIn(long_wave), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_empirical_prediction(self):
        heading = self.make_heading("經驗主義預測")
        cooccur = self.make_box("光譜共現", C_GREEN, width=3.5, height=0.8)
        cooccur.shift(UP * 1.0 + LEFT * 2)
        arrow = Arrow(
            cooccur.get_right(), cooccur.get_right() + RIGHT * 2,
            buff=0.2, color=C_WHITE, stroke_width=3,
        )
        predict = self.make_box("預測心理物理函數", C_ORANGE, width=3.5, height=0.8)
        predict.shift(UP * 1.0 + RIGHT * 2)
        key = self.zh(
            "自然場景光譜統計嘅共現頻率 → 感知閾值同色相偏移",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 0.8)
        with self.voiceover(
            text="經驗主義嘅關鍵係：光譜共現嘅頻率可以預測心理物理函數。"
            "自然場景光譜統計嘅共現頻率，"
            "可以預測感知閾值同色相偏移。"
            "JND 同 Bezold-Brücke 效應都唔係視覺系統嘅固有缺陷，"
            "而係經驗累積嘅結果。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(cooccur), GrowArrow(arrow), FadeIn(predict), run_time=0.8)
            self.play(FadeIn(key), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  顏色心理物理學：系統性變化色相、飽和度、明度", font_size=24, color=C_GREEN),
            self.zh("•  JND 函數：波長辨別閾值由光譜頻率預測", font_size=24, color=C_ORANGE),
            self.zh("•  Bezold-Brücke：光強度改變色相，短波長暗藍光綠", font_size=24, color=C_PINK),
            self.zh("•  光譜共現統計可預測複雜心理物理函數", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。顏色心理物理學系統性變化色相、飽和度、明度。"
            "JND 函數嘅波長辨別閾值可以由光譜頻率預測。"
            "Bezold-Brücke 效應係光強度改變色相，短波長暗嘅時候偏藍、光嘅時候偏綠。"
            "光譜共現統計可以預測呢啲複雜嘅心理物理函數。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：運動速度", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講運動速度嘅感知，"
            "包括閃光滯後效應同埋點解物理速度唔能夠直接量度。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
