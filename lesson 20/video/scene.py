"""
Lesson 20 – Associations
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 20/video"
    manim render -qh scene.py AssociationsExplainer
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


class AssociationsExplainer(VoiceoverScene):
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
        self.scene_evolution_associations()
        self.scene_lifetime_learning()
        self.scene_cultural_associations()
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
        title = self.zh("聯想", font_size=56, color=C_BLUE)
        sub_en = self.en("Associations", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第二十課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第二十課。"
            "今日我哋會講聯想點樣塑造刺激同行為嘅連結。"
            "聯想有三種來源：進化、終身學習、同文化。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_evolution_associations(self):
        heading = self.make_heading("進化塑造嘅聯想")
        evo_box = self.make_box("進化聯想", C_GREEN, width=4.0, height=0.8)
        evo_box.shift(UP * 1.2)
        evo_desc = self.zh(
            "先天反應，經過地質時間嘅篩選，物種特定行為",
            font_size=22, color=C_WHITE,
        ).next_to(evo_box, DOWN, buff=0.3)
        innate = self.zh(
            "唔使學，生嚟就有，例如：吸吮、驚嚇、定向",
            font_size=20, color=C_DIM,
        ).shift(DOWN * 0.6)
        with self.voiceover(
            text="進化塑造嘅聯想係先天嘅。"
            "呢啲反應經過地質時間嘅篩選，形成物種特定嘅行為。"
            "吸吮、驚嚇、定向呢啲都係唔使學、生嚟就有嘅。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(evo_box), FadeIn(evo_desc), run_time=0.8)
            self.play(FadeIn(innate), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_lifetime_learning(self):
        heading = self.make_heading("終身學習嘅聯想")
        pavlov_box = self.make_box("巴甫洛夫：古典制約", C_ORANGE, width=4.5, height=0.8)
        pavlov_box.shift(UP * 1.0 + LEFT * 2)
        skinner_box = self.make_box("史金納：操作制約", C_PINK, width=4.5, height=0.8)
        skinner_box.shift(UP * 1.0 + RIGHT * 2)
        practice = self.zh(
            "練習同重複強化刺激反應連結",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 0.5)
        with self.voiceover(
            text="終身學習嘅聯想包括巴甫洛夫嘅古典制約同史金納嘅操作制約。"
            "刺激同反應嘅連結透過練習同重複嚟強化。"
            "呢啲係一生入面不斷累積嘅經驗。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(pavlov_box), FadeIn(skinner_box), run_time=0.8)
            self.play(FadeIn(practice), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_cultural_associations(self):
        heading = self.make_heading("文化塑造嘅聯想")
        culture_items = VGroup(
            self.zh("•  語言：詞彙同概念嘅連結", font_size=24, color=C_GREEN),
            self.zh("•  社會規範：咩可以做、咩唔可以做", font_size=24, color=C_ORANGE),
            self.zh("•  工具：文化傳承嘅技術", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(UP * 0.3)
        rapid = self.zh(
            "文化進化係快速適應，唔使等基因變異",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 1.2)
        with self.voiceover(
            text="文化塑造嘅聯想包括語言、社會規範、工具。"
            "語言建立詞彙同概念嘅連結。"
            "社會規範定義咩可以做、咩唔可以做。"
            "文化進化係快速適應，唔使等基因變異。"
        ):
            self.play(Write(heading), run_time=0.6)
            for c in culture_items:
                self.play(FadeIn(c, shift=RIGHT * 0.2), run_time=0.5)
            self.play(FadeIn(rapid), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  進化聯想：先天反應，物種特定", font_size=24, color=C_GREEN),
            self.zh("•  終身學習：巴甫洛夫、史金納、制約", font_size=24, color=C_ORANGE),
            self.zh("•  文化聯想：語言、規範、工具", font_size=24, color=C_PINK),
            self.zh("•  三種來源一齊塑造刺激同行為嘅連結", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。進化聯想係先天反應，物種特定。"
            "終身學習包括巴甫洛夫、史金納嘅制約。"
            "文化聯想係語言、規範、工具。"
            "三種來源一齊塑造刺激同行為嘅連結。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：機制", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講機制，"
            "包括神經可塑性、短期長期變化、獎賞系統。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
