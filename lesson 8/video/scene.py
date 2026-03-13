"""
Lesson 8 – What We Perceive
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 8/video"
    manim render -qh scene.py WhatWePerceiveExplainer
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


class WhatWePerceiveExplainer(VoiceoverScene):
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
        self.traditional_assumptions()
        self.the_dilemma()
        self.empirical_solution()
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
        title = self.zh("我哋感知到啲咩", font_size=56, color=C_BLUE)
        sub_en = self.en("What We Perceive", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第八課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)

        with self.voiceover(
            text="大家好！歡迎嚟到第八課。今日我哋會探討感知嘅本質。"
            "傳統假設話腦會建構物理現實嘅表徵，但係有冇其他可能呢？"
            "我哋會講傳統假設、逆問題嘅困境、同埋經驗主義嘅解決方案。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def traditional_assumptions(self):
        heading = self.make_heading("傳統假設：Marr 嘅計算理論")

        steps = VGroup(
            self.zh("1. 神經檢測 — 視網膜接收光線", font_size=24, color=C_GREEN),
            self.zh("2. 編碼 — 將刺激轉成神經訊號", font_size=24, color=C_ORANGE),
            self.zh("3. 稀疏表徵 — 建構物理現實嘅內部模型", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)

        with self.voiceover(
            text="傳統神經科學假設腦會建構物理現實嘅表徵。"
            "Marr 嘅計算理論話：神經檢測、編碼、然後形成稀疏表徵。"
            "即係話，腦好似電腦咁，會計算出外界嘅真實樣貌。"
        ):
            self.play(Write(heading), run_time=0.6)
            for s in steps:
                self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=0.6)

        self.wait(0.3)
        self.clear()

    def the_dilemma(self):
        heading = self.make_heading("困境：逆問題")

        problem = self.zh(
            "同一種視網膜刺激可以嚟自唔同嘅物理來源",
            font_size=28, color=C_RED,
        ).shift(UP * 0.5)

        consequence = self.zh(
            "刺激特徵無法單獨映射返去現實 — 歧義性無法解決",
            font_size=24, color=C_ORANGE,
        ).shift(DOWN * 0.3)

        with self.voiceover(
            text="但係有個根本問題：逆問題。"
            "同一種視網膜刺激可以嚟自好多唔同嘅物理來源。"
            "刺激嘅特徵無法單獨映射返去現實，歧義性冇辦法用計算解決。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(problem), run_time=0.8)
            self.play(FadeIn(consequence), run_time=0.8)

        self.wait(0.3)
        self.clear()

    def empirical_solution(self):
        heading = self.make_heading("經驗主義嘅解決方案")

        points = VGroup(
            self.zh("•  腦累積經驗，唔係計算物理現實", font_size=26, color=C_GREEN),
            self.zh("•  試錯學習 — 刺激同反應嘅連結隨經驗改進", font_size=26, color=C_ORANGE),
            self.zh("•  感知係基於發生頻率，唔係物理測量", font_size=26, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)

        with self.voiceover(
            text="解決方案係經驗主義。腦唔係計算物理現實，而係累積經驗。"
            "透過試錯學習，刺激同反應嘅連結會隨經驗改進。"
            "感知係基於發生頻率，唔係物理測量。"
        ):
            self.play(Write(heading), run_time=0.6)
            for p in points:
                self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.3)
        self.clear()

    def summary(self):
        heading = self.make_heading("總結", font_size=44)

        bullets = VGroup(
            self.zh("•  傳統假設：腦建構物理現實表徵（Marr）", font_size=24, color=C_GREEN),
            self.zh("•  逆問題：刺激歧義，無法計算還原", font_size=24, color=C_ORANGE),
            self.zh("•  經驗方案：累積經驗、試錯學習", font_size=24, color=C_PINK),
            self.zh("•  注意：由隨機開始，隨經驗改進；分析未必揭示機制", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="總結：傳統假設話腦建構物理現實表徵，但逆問題令呢個假設站唔住腳。"
            "經驗方案話腦累積經驗、試錯學習。"
            "注意：由隨機開始，隨經驗改進；分析未必揭示機制。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.5)
        self.clear()

    def outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)

        with self.voiceover(
            text="多謝收睇！下一課我哋會講空間間距，"
            "探討點解同一視網膜投影可以嚟自唔同嘅物理長度。記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)

        self.wait(1)
        self.play(FadeOut(thanks), run_time=0.8)
