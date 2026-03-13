"""
Lesson 19 – Stimuli and Behavior
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 19/video"
    manim render -qh scene.py StimuliAndBehaviorExplainer
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


class StimuliAndBehaviorExplainer(VoiceoverScene):
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
        self.scene_what_are_stimuli()
        self.scene_physiologist_view()
        self.scene_psychologist_view()
        self.scene_common_strategy()
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
        title = self.zh("刺激與行為", font_size=56, color=C_BLUE)
        sub_en = self.en("Stimuli and Behavior", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第十九課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第十九課。"
            "今日我哋會重新思考刺激究竟係咩，"
            "同埋生理學家同心理學家點樣唔同咁理解刺激同行為嘅關係。"
            "兩邊其實有一個共同嘅經驗策略。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_what_are_stimuli(self):
        heading = self.make_heading("刺激究竟係咩？")
        filter_box = self.make_box("神經前濾波", C_GREEN, width=3.5, height=0.8)
        filter_box.shift(UP * 1.2)
        filter_desc = self.zh(
            "能量經過濾波先到達感受器，改變咗原始輸入",
            font_size=22, color=C_WHITE,
        ).next_to(filter_box, DOWN, buff=0.3)
        higher = self.zh(
            "高階處理有反饋迴路，刺激唔係單純嘅物理量",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 0.5)
        with self.voiceover(
            text="刺激究竟係咩？"
            "能量會經過神經前濾波先到達感受器，改變咗原始輸入。"
            "高階處理有反饋迴路，刺激唔係單純嘅物理量。"
            "所以刺激係經過多層轉換嘅，唔係外界嘅直接複製。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(filter_box), FadeIn(filter_desc), run_time=0.8)
            self.play(FadeIn(higher), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_physiologist_view(self):
        heading = self.make_heading("生理學家嘅觀點")
        phys_box = self.make_box("生理學", C_GREEN, width=4.0, height=0.8)
        phys_box.shift(UP * 1.0 + LEFT * 2)
        phys_items = VGroup(
            self.zh("•  神經機制、反射、運動控制", font_size=20, color=C_WHITE),
            self.zh("•  關注輸入點樣轉成輸出", font_size=20, color=C_DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(phys_box, DOWN, buff=0.3)
        with self.voiceover(
            text="生理學家理解行為嘅時候，關注神經機制。"
            "反射、運動控制、輸入點樣轉成輸出。"
            "佢哋用細胞、電路、突觸嚟解釋行為。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(phys_box), run_time=0.5)
            for p in phys_items:
                self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(0.3)
        self.clear()

    def scene_psychologist_view(self):
        heading = self.make_heading("心理學家嘅觀點")
        psych_box = self.make_box("心理學", C_ORANGE, width=4.0, height=0.8)
        psych_box.shift(UP * 1.0 + RIGHT * 2)
        psych_items = VGroup(
            self.zh("•  主觀報告、心理物理學、認知", font_size=20, color=C_WHITE),
            self.zh("•  關注感知、決策、意識", font_size=20, color=C_DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(psych_box, DOWN, buff=0.3)
        with self.voiceover(
            text="心理學家理解行為嘅時候，關注主觀報告。"
            "心理物理學、認知、感知、決策、意識。"
            "佢哋用刺激同反應嘅關係嚟量度感知。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(psych_box), run_time=0.5)
            for p in psych_items:
                self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(0.3)
        self.clear()

    def scene_common_strategy(self):
        heading = self.make_heading("共同嘅經驗策略")
        stim_box = self.make_box("刺激", C_GREEN, width=2.5, height=0.8)
        stim_box.shift(UP * 1.0 + LEFT * 2.5)
        arrow = Arrow(
            stim_box.get_right(), stim_box.get_right() + RIGHT * 2,
            buff=0.2, color=C_WHITE, stroke_width=3,
        )
        resp_box = self.make_box("反應", C_ORANGE, width=2.5, height=0.8)
        resp_box.shift(UP * 1.0 + RIGHT * 2.5)
        unify = self.zh(
            "兩邊都尋求刺激同反應嘅連結，經驗框架可以統一",
            font_size=24, color=C_CYAN,
        ).shift(DOWN * 0.8)
        with self.voiceover(
            text="生理學家同心理學家有一個共同策略。"
            "兩邊都尋求刺激同反應嘅連結。"
            "經驗框架可以統一呢兩個領域。"
            "刺激唔係物理量，反應唔係計算結果，"
            "而係經驗累積形成嘅連結。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(stim_box), GrowArrow(arrow), FadeIn(resp_box), run_time=0.8)
            self.play(FadeIn(unify), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  刺激經過濾波同反饋，唔係單純物理量", font_size=24, color=C_GREEN),
            self.zh("•  生理學：神經機制、反射、運動控制", font_size=24, color=C_ORANGE),
            self.zh("•  心理學：主觀報告、心理物理學、認知", font_size=24, color=C_PINK),
            self.zh("•  共同策略：連結刺激同反應，經驗框架統一", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。刺激經過濾波同反饋，唔係單純嘅物理量。"
            "生理學關注神經機制、反射、運動控制。"
            "心理學關注主觀報告、心理物理學、認知。"
            "兩邊嘅共同策略係連結刺激同反應，經驗框架可以統一。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：聯想", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講聯想，"
            "包括進化、終身學習、文化點樣塑造刺激同行為嘅連結。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
