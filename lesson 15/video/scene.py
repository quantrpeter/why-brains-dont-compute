"""
Lesson 15 – Motion Speed
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 15/video"
    manim render -qh scene.py MotionSpeedExplainer
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


class MotionSpeedExplainer(VoiceoverScene):
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
        self.scene_physical_motion()
        self.scene_the_problem()
        self.scene_flash_lag_effect()
        self.scene_empirical_explanation()
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
        title = self.zh("運動速度", font_size=56, color=C_BLUE)
        sub_en = self.en("Motion Speed", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第十五課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第十五課。"
            "今日我哋會講運動速度嘅感知。"
            "物理速度同方向喺三維投影到二維嘅時候會混埋一齊，"
            "所以腦唔能夠直接量度物理速度。"
            "我哋會講閃光滯後效應同經驗主義嘅解釋。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_physical_motion(self):
        heading = self.make_heading("物理運動")
        motion_box = self.make_box("速度 + 方向", C_GREEN, width=3.5, height=0.8)
        motion_box.shift(UP * 1.2)
        project = self.zh(
            "3D → 2D 投影：速度同方向混埋一齊",
            font_size=22, color=C_WHITE,
        ).next_to(motion_box, DOWN, buff=0.4)
        range_text = self.zh(
            "可見範圍：約 0.1 至 175 度每秒",
            font_size=20, color=C_DIM,
        ).shift(DOWN * 0.3)
        with self.voiceover(
            text="物理運動有速度同方向。"
            "但係三維空間嘅運動投影到二維視網膜嘅時候，"
            "速度同方向會混埋一齊。"
            "人眼可見嘅運動範圍大約係零點一到一百七十五度每秒。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(motion_box), FadeIn(project), run_time=0.8)
            self.play(FadeIn(range_text), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_the_problem(self):
        heading = self.make_heading("逆問題：同一影像序列")
        source_box = self.make_box("好多唔同 3D 運動", C_GREEN, width=3.5, height=0.8)
        source_box.shift(LEFT * 2.5 + UP * 0.5)
        arrow = Arrow(
            source_box.get_right(), source_box.get_right() + RIGHT * 2,
            buff=0.2, color=C_WHITE, stroke_width=3,
        )
        stim_box = self.make_box("同一視網膜影像序列", C_ORANGE, width=3.5, height=0.8)
        stim_box.shift(RIGHT * 2.5 + UP * 0.5)
        dilemma = self.zh(
            "同一種影像序列可以由好多唔同嘅物理運動造成",
            font_size=22, color=C_RED,
        ).shift(DOWN * 1.2)
        with self.voiceover(
            text="又係逆問題。"
            "好多唔同嘅三維運動可以產生同一種視網膜影像序列。"
            "所以單靠影像，腦唔能夠還原物理速度。"
            "研究用虛擬環境模擬運動物體，"
            "嚟近似影像序列嘅出現頻率。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(source_box), GrowArrow(arrow), FadeIn(stim_box), run_time=0.8)
            self.play(FadeIn(dilemma), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_flash_lag_effect(self):
        heading = self.make_heading("閃光滯後效應 Flash-Lag")
        effect_box = self.make_box("運動物體 + 同時出現嘅閃光", C_PINK, width=5.0, height=0.8)
        effect_box.shift(UP * 1.2)
        observation = self.zh(
            "運動嘅刺激睇落喺閃光前面，速度越快差異越大",
            font_size=22, color=C_WHITE,
        ).next_to(effect_box, DOWN, buff=0.4)
        paradox = self.zh(
            "明明同一位置，點解會覺得運動物體領先？",
            font_size=20, color=C_YELLOW,
        ).shift(DOWN * 0.5)
        with self.voiceover(
            text="閃光滯後效應係一個經典嘅錯覺。"
            "當一個運動嘅物體同一個閃光喺同一位置出現，"
            "人會覺得運動嘅刺激喺閃光前面。"
            "速度越快，差異越大。"
            "明明同一位置，點解會覺得運動物體領先？"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(effect_box), FadeIn(observation), run_time=0.8)
            self.play(FadeIn(paradox), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_empirical_explanation(self):
        heading = self.make_heading("經驗主義解釋")
        freq_box = self.make_box("投影速度嘅出現頻率", C_GREEN, width=4.0, height=0.8)
        freq_box.shift(UP * 1.0 + LEFT * 2)
        arrow = Arrow(
            freq_box.get_right(), freq_box.get_right() + RIGHT * 2,
            buff=0.2, color=C_WHITE, stroke_width=3,
        )
        predict_box = self.make_box("預測心理測量函數", C_ORANGE, width=4.0, height=0.8)
        predict_box.shift(UP * 1.0 + RIGHT * 2)
        key = self.zh(
            "影像序列嘅頻率 → 感知速度、閃光滯後效應",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 0.8)
        with self.voiceover(
            text="經驗主義嘅解釋係：投影速度嘅出現頻率可以預測心理測量函數。"
            "自然場景入面影像序列嘅頻率，"
            "可以預測感知速度同閃光滯後效應。"
            "腦唔係量度物理速度，而係用經驗嚟解讀影像序列。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(freq_box), GrowArrow(arrow), FadeIn(predict_box), run_time=0.8)
            self.play(FadeIn(key), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  3D→2D 投影：速度同方向混埋一齊", font_size=24, color=C_GREEN),
            self.zh("•  同一影像序列可來自好多唔同物理運動", font_size=24, color=C_ORANGE),
            self.zh("•  閃光滯後效應：運動物體睇落喺閃光前面", font_size=24, color=C_PINK),
            self.zh("•  投影速度嘅出現頻率預測心理測量函數", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。三維投影到二維，速度同方向會混埋一齊。"
            "同一影像序列可以來自好多唔同嘅物理運動。"
            "閃光滯後效應係運動物體睇落喺閃光前面。"
            "投影速度嘅出現頻率可以預測心理測量函數。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：運動方向", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講運動方向，"
            "包括孔徑效應、圓形孔徑、垂直狹縫嘅理髮店招牌效應。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
