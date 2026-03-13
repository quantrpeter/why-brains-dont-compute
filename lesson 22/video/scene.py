"""
Lesson 22 – Reflexes
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 22/video"
    manim render -qh scene.py ReflexesExplainer
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


class ReflexesExplainer(VoiceoverScene):
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
        self.scene_reflex_arc()
        self.scene_is_all_behaviour_reflexive()
        self.scene_counterarguments()
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
        title = self.zh("反射", font_size=56, color=C_BLUE)
        sub_en = self.en("Reflexes", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第二十二課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第二十二課。"
            "今日我哋會講反射。"
            "謝靈頓嘅反射弧、係咪所有行為都係反射性嘅、"
            "同埋自由意志同創意嘅反駁。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_reflex_arc(self):
        heading = self.make_heading("謝靈頓嘅反射弧")
        stim_box = self.make_box("刺激", C_GREEN, width=2.0, height=0.7)
        stim_box.shift(UP * 1.0 + LEFT * 2.5)
        proc_box = self.make_box("處理", C_ORANGE, width=2.0, height=0.7)
        proc_box.shift(UP * 1.0)
        resp_box = self.make_box("反應", C_PINK, width=2.0, height=0.7)
        resp_box.shift(UP * 1.0 + RIGHT * 2.5)
        arrow1 = Arrow(stim_box.get_right(), proc_box.get_left(), buff=0.2, color=C_WHITE)
        arrow2 = Arrow(proc_box.get_right(), resp_box.get_left(), buff=0.2, color=C_WHITE)
        sherr = self.zh(
            "刺激 → 神經處理 → 運動輸出",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 0.8)
        with self.voiceover(
            text="謝靈頓提出反射弧嘅概念。"
            "刺激經過神經處理，產生運動輸出。"
            "呢個係最基本嘅刺激反應連結。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(stim_box), FadeIn(proc_box), FadeIn(resp_box), run_time=0.6)
            self.play(GrowArrow(arrow1), GrowArrow(arrow2), run_time=0.5)
            self.play(FadeIn(sherr), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_is_all_behaviour_reflexive(self):
        heading = self.make_heading("係咪所有行為都係反射性嘅？")
        question = self.zh(
            "自願行為、創意、自由意志 — 好似唔係反射？",
            font_size=24, color=C_WHITE,
        ).shift(UP * 0.5)
        complex_box = self.make_box("複雜行為可能係多層反射嘅組合", C_ORANGE, width=5.0, height=0.8)
        complex_box.shift(DOWN * 0.5)
        with self.voiceover(
            text="自願行為、創意、自由意志好似唔係反射。"
            "但複雜行為可能係多層反射嘅組合。"
            "我哋睇吓反駁嘅論點。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(question), run_time=0.6)
            self.play(FadeIn(complex_box), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_counterarguments(self):
        heading = self.make_heading("反駁：決定論嘅基礎")
        counter_items = VGroup(
            self.zh("•  自由意志：可能係複雜因果嘅主觀感受", font_size=22, color=C_GREEN),
            self.zh("•  創意：可能係複雜性，唔係真正嘅新奇", font_size=22, color=C_ORANGE),
            self.zh("•  選擇嘅幻覺：決定性嘅物理基礎", font_size=22, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 0.2)
        determin = self.zh(
            "物理定律係決定性嘅，神經活動都係",
            font_size=20, color=C_DIM,
        ).shift(DOWN * 1.2)
        with self.voiceover(
            text="反駁嘅論點係：自由意志可能係複雜因果嘅主觀感受。"
            "創意可能係複雜性，唔係真正嘅新奇。"
            "物理定律係決定性嘅，神經活動都係。"
            "但呢個唔否定主觀經驗嘅真實性。"
        ):
            self.play(Write(heading), run_time=0.6)
            for c in counter_items:
                self.play(FadeIn(c, shift=RIGHT * 0.2), run_time=0.5)
            self.play(FadeIn(determin), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  謝靈頓反射弧：刺激 → 處理 → 反應", font_size=24, color=C_GREEN),
            self.zh("•  所有行為都係反射？有爭議", font_size=24, color=C_ORANGE),
            self.zh("•  自由意志、創意係反例", font_size=24, color=C_PINK),
            self.zh("•  決定論基礎：物理因果鏈", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。謝靈頓嘅反射弧係刺激、處理、反應。"
            "係咪所有行為都係反射性嘅有爭議。"
            "自由意志同創意係反例。"
            "決定論嘅基礎係物理因果鏈。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：特徵檢測", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講特徵檢測，"
            "包括休伯爾同韋塞爾、面細胞、位置細胞。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
