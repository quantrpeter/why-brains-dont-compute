"""
Lesson 21 – Mechanisms
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 21/video"
    manim render -qh scene.py MechanismsExplainer
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


class MechanismsExplainer(VoiceoverScene):
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
        self.scene_neural_plasticity()
        self.scene_short_term_changes()
        self.scene_long_term_changes()
        self.scene_reward_systems()
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
        title = self.zh("機制", font_size=56, color=C_BLUE)
        sub_en = self.en("Mechanisms", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第二十一課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第二十一課。"
            "今日我哋會講經驗學習背後嘅神經機制。"
            "包括神經可塑性、短期長期變化、同獎賞系統。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_neural_plasticity(self):
        heading = self.make_heading("神經可塑性")
        plast_box = self.make_box("神經可塑性", C_GREEN, width=4.0, height=0.8)
        plast_box.shift(UP * 1.2)
        plast_desc = self.zh(
            "神經連接會隨經驗改變，呢個係學習嘅基礎",
            font_size=22, color=C_WHITE,
        ).next_to(plast_box, DOWN, buff=0.3)
        hebb = self.zh(
            "赫布定律：一齊放電嘅神經元，一齊連結",
            font_size=20, color=C_CYAN,
        ).shift(DOWN * 0.6)
        with self.voiceover(
            text="神經可塑性係指神經連接會隨經驗改變。"
            "呢個係學習嘅基礎。"
            "赫布定律話：一齊放電嘅神經元會一齊連結。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(plast_box), FadeIn(plast_desc), run_time=0.8)
            self.play(FadeIn(hebb), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_short_term_changes(self):
        heading = self.make_heading("短期變化")
        short_items = VGroup(
            self.zh("•  易化：突觸傳遞增強", font_size=24, color=C_GREEN),
            self.zh("•  抑制：突觸傳遞減弱", font_size=24, color=C_ORANGE),
            self.zh("•  持續幾毫秒到幾分鐘", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(UP * 0.3)
        with self.voiceover(
            text="短期變化包括易化同抑制。"
            "易化係突觸傳遞增強，抑制係減弱。"
            "呢啲變化持續幾毫秒到幾分鐘。"
        ):
            self.play(Write(heading), run_time=0.6)
            for s in short_items:
                self.play(FadeIn(s, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_long_term_changes(self):
        heading = self.make_heading("長期變化")
        ltp_box = self.make_box("LTP 長期增強", C_GREEN, width=4.0, height=0.8)
        ltp_box.shift(UP * 1.0 + LEFT * 2)
        ltd_box = self.make_box("LTD 長期抑制", C_ORANGE, width=4.0, height=0.8)
        ltd_box.shift(UP * 1.0 + RIGHT * 2)
        struct = self.zh(
            "結構變化：突觸數量、樹突棘嘅改變",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 0.5)
        with self.voiceover(
            text="長期變化包括長期增強同長期抑制。"
            "LTP 係長期增強，LTD 係長期抑制。"
            "仲有結構變化：突觸數量、樹突棘嘅改變。"
            "呢啲係記憶嘅神經基礎。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(ltp_box), FadeIn(ltd_box), run_time=0.8)
            self.play(FadeIn(struct), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_reward_systems(self):
        heading = self.make_heading("獎賞系統")
        dopa_box = self.make_box("多巴胺系統", C_PINK, width=4.0, height=0.8)
        dopa_box.shift(UP * 1.2)
        dopa_desc = self.zh(
            "強化訊號，引導試錯學習，話俾腦知邊啲行為有效",
            font_size=22, color=C_WHITE,
        ).next_to(dopa_box, DOWN, buff=0.3)
        trial = self.zh(
            "試錯學習：獎賞強化成功嘅刺激反應連結",
            font_size=20, color=C_CYAN,
        ).shift(DOWN * 0.8)
        with self.voiceover(
            text="獎賞系統主要由多巴胺驅動。"
            "多巴胺係強化訊號，引導試錯學習。"
            "佢話俾腦知邊啲行為有效。"
            "獎賞會強化成功嘅刺激反應連結。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(dopa_box), FadeIn(dopa_desc), run_time=0.8)
            self.play(FadeIn(trial), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  神經可塑性：連接隨經驗改變", font_size=24, color=C_GREEN),
            self.zh("•  短期：易化、抑制", font_size=24, color=C_ORANGE),
            self.zh("•  長期：LTP、LTD、結構變化", font_size=24, color=C_PINK),
            self.zh("•  獎賞：多巴胺引導試錯學習", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。神經可塑性係連接隨經驗改變。"
            "短期變化係易化同抑制。"
            "長期變化係 LTP、LTD、結構變化。"
            "獎賞系統由多巴胺引導試錯學習。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：反射", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講反射，"
            "探討係咪所有行為都係反射性嘅。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
