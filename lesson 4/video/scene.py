"""
Lesson 4 – Coding
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 4/video"
    manim render -qh scene.py CodingExplainer
"""

from manim import *
import numpy as np
from manim_voiceover import VoiceoverScene

from edge_tts_service import EdgeTTSService

# ── colour palette ───────────────────────────────────────────────────────
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


class CodingExplainer(VoiceoverScene):
    """Single scene contrasting computer and neural coding in Cantonese."""

    def construct(self):
        self.set_speech_service(
            EdgeTTSService(voice="zh-HK-HiuMaanNeural", rate="+0%")
        )
        self.camera.background_color = BLACK

        self.bg_image = ImageMobject("wallpaper1.jpg")
        self.bg_image.height = config.frame_height
        self.bg_image.width = config.frame_width
        self.add(self.bg_image)

        self.bg_overlay = Rectangle(
            width=config.frame_width + 0.5,
            height=config.frame_height + 0.5,
            fill_color=BLACK,
            fill_opacity=0.55,
            stroke_width=0,
        )
        self.add(self.bg_overlay)

        self.watermark = self.zh(
            "香港編程學會", font_size=18, color="#9999bb"
        ).to_corner(UL, buff=0.3)
        self.add(self.watermark)

        self.scene_intro()
        self.scene_computer_codes()
        self.scene_programming_languages()
        self.scene_neural_coding()
        self.scene_action_potentials()
        self.scene_summary()
        self.scene_outro()

    # ── text helpers ─────────────────────────────────────────────────────

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
        rect = RoundedRectangle(
            corner_radius=0.15, width=width, height=height,
            fill_color=color, fill_opacity=0.25, stroke_color=color,
        )
        txt = self.zh(label, font_size=24, color=color).move_to(rect)
        return VGroup(rect, txt)

    def make_heading(self, text, color=C_BLUE, font_size=40):
        return self.zh(text, font_size=font_size, color=color).to_edge(UP, buff=0.5)

    # ── Scene 1 — Intro ─────────────────────────────────────────────────

    def scene_intro(self):
        title = self.zh("編碼", font_size=56, color=C_BLUE)
        sub_en = self.en(
            "Coding", font_size=24, color=C_WHITE
        ).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh(
            "第四課", font_size=36, color=C_ORANGE
        ).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh(
            "制片人：Peter", font_size=24, color=C_DIM
        ).next_to(sub_zh, DOWN, buff=0.7)

        with self.voiceover(
            text="大家好！歡迎嚟到第四課。"
            "今日我哋會對比電腦編碼同神經編碼。"
            "電腦用二進制、程式語言。腦用動作電位。"
            "「編碼」呢個概念係咪可以套用到神經系統？"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    # ── Scene 2 — Computer Codes ────────────────────────────────────────

    def scene_computer_codes(self):
        heading = self.make_heading("電腦編碼")

        binary = self.mono("01001000 01100101 01101100 01101100 01101111", font_size=22, color=C_GREEN)
        binary.shift(UP * 1.0)
        binary_label = self.zh("二進制 = Hello", font_size=20, color=C_DIM).next_to(binary, DOWN, buff=0.2)

        media = VGroup(
            self.zh("打孔卡 → 電子開關 → 電壓高低", font_size=24, color=C_ORANGE),
            self.zh("明確對應：每個 bit 有固定意義", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN * 0.5)

        with self.voiceover(
            text="電腦編碼好明確。"
            "二進制，0 同 1，可以表示任何資料。"
            "例如呢串二進制就係 Hello。"
            "打孔卡、電子開關、電壓高低，都係 0 同 1 嘅物理實現。"
            "每個 bit 都有固定意義，可以解碼還原。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(Write(binary), FadeIn(binary_label), run_time=1)
            for m in media:
                self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.6)

        self.wait(0.3)
        self.clear()

    # ── Scene 3 — Programming Languages ──────────────────────────────────

    def scene_programming_languages(self):
        heading = self.make_heading("程式語言")

        langs = [
            ("IBM Short Code", "1949", C_GREEN),
            ("FORTRAN", "1957", C_ORANGE),
            ("BASIC", "1964", C_PINK),
            ("編譯器", "將高階語言變機器碼", C_PURPLE),
        ]

        items = VGroup()
        for name, year, col in langs:
            box = RoundedRectangle(
                corner_radius=0.1, width=4, height=0.7,
                fill_color=col, fill_opacity=0.2, stroke_color=col,
            )
            txt = self.zh(f"{name} — {year}", font_size=22, color=col).move_to(box)
            items.add(VGroup(box, txt))
        items.arrange(DOWN, buff=0.25, aligned_edge=LEFT).shift(LEFT * 0.5)

        arrow = Arrow(LEFT * 2, RIGHT * 2, buff=0.1, color=C_CYAN, stroke_width=3).shift(DOWN * 1.5)
        arrow_label = self.zh("人寫程式 → 編譯器 → 機器執行", font_size=20, color=C_CYAN).next_to(arrow, DOWN, buff=0.2)

        with self.voiceover(
            text="程式語言嘅發展。"
            "一九四九年，IBM Short Code。"
            "一九五七年，FORTRAN，科學計算嘅標準。"
            "一九六四年，BASIC，教育用。"
            "編譯器將高階語言變成機器碼。"
            "人寫程式，編譯器翻譯，機器執行。"
        ):
            self.play(Write(heading), run_time=0.6)
            for item in items:
                self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.6)
            self.play(GrowArrow(arrow), FadeIn(arrow_label), run_time=0.8)

        self.wait(0.3)
        self.clear()

    # ── Scene 4 — Neural Coding ─────────────────────────────────────────

    def scene_neural_coding(self):
        heading = self.make_heading("神經編碼")

        shannon_box = self.make_box("Shannon 資訊論", C_GREEN, width=4, height=0.7)
        shannon_box.shift(UP * 1.0)
        shannon_desc = self.zh(
            "資訊量 vs 訊息意義 — 神經訊號有冇「意義」？",
            font_size=20, color=C_DIM,
        ).next_to(shannon_box, DOWN, buff=0.2)

        barlow = VGroup(
            self.zh("Barlow：稀疏編碼 vs 密集編碼", font_size=24, color=C_ORANGE),
            self.zh("神經元嘅放電模式 ≠ 電腦嘅 0/1", font_size=22, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.5)

        question = self.zh(
            "「編碼」呢個概念係咪適用於神經系統？",
            font_size=24, color=C_YELLOW,
        ).shift(DOWN * 1.6)

        with self.voiceover(
            text="神經編碼係另一回事。"
            "Shannon 資訊論講嘅係資訊量，唔係訊息意義。"
            "神經訊號有冇「意義」？呢個係開放問題。"
            "Barlow 提出稀疏編碼同密集編碼。"
            "但神經元嘅放電模式唔等同電腦嘅 0 同 1。"
            "「編碼」呢個概念係咪適用於神經系統？好多科學家都有爭議。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(shannon_box), FadeIn(shannon_desc), run_time=0.8)
            for b in barlow:
                self.play(FadeIn(b, shift=RIGHT * 0.2), run_time=0.6)
            self.play(FadeIn(question), run_time=0.6)

        self.wait(0.3)
        self.clear()

    # ── Scene 5 — Action Potentials ──────────────────────────────────────

    def scene_action_potentials(self):
        heading = self.make_heading("動作電位")

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[-1, 2, 1],
            x_length=5,
            y_length=2.5,
            axis_config={"color": C_DIM},
        ).shift(UP * 0.2)

        spike_curve = axes.plot(
            lambda x: 1.5 * (np.exp(-((x - 1) ** 2) * 20) + np.exp(-((x - 2) ** 2) * 20) + np.exp(-((x - 3) ** 2) * 20)),
            x_range=[0.5, 3.5],
            color=C_YELLOW,
        )

        coding_types = VGroup(
            self.zh("•  頻率編碼：放電速率表示強度", font_size=22, color=C_GREEN),
            self.zh("•  時間編碼：放電時刻有冇意義？", font_size=22, color=C_ORANGE),
            self.zh("•  群體編碼：好多神經元一齊表示", font_size=22, color=C_PINK),
            self.zh("•  冗餘係好事：抗噪、穩健", font_size=22, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(DOWN * 1.8)

        with self.voiceover(
            text="動作電位係神經元嘅基本訊號。"
            "全有全無，好似數位訊號，但唔係 0 同 1。"
            "頻率編碼：放電速率表示刺激強度。"
            "時間編碼：放電嘅精確時刻有冇意義？仲有爭議。"
            "群體編碼：好多神經元一齊表示一個訊息。"
            "冗餘係好事，可以抗噪、令系統更穩健。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(Create(axes), run_time=0.8)
            self.play(Create(spike_curve), run_time=1)
            for ct in coding_types:
                self.play(FadeIn(ct, shift=RIGHT * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    # ── Scene 6 — Summary ───────────────────────────────────────────────

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)

        bullets = VGroup(
            self.zh("•  電腦編碼：二進制、明確對應", font_size=26, color=C_GREEN),
            self.zh("•  程式語言：FORTRAN、BASIC、編譯器", font_size=26, color=C_ORANGE),
            self.zh("•  神經編碼 ≠ 電腦編碼", font_size=26, color=C_PINK),
            self.zh("•  動作電位：頻率、時間、群體編碼", font_size=26, color=C_PURPLE),
            self.zh("•  冗餘令神經系統更穩健", font_size=26, color=C_CYAN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="總結一下今日學咗嘅嘢。"
            "電腦編碼用二進制，每個 bit 有明確對應。"
            "程式語言由 FORTRAN、BASIC 到編譯器。"
            "神經編碼唔等同電腦編碼，概念唔可以直接套用。"
            "動作電位有頻率編碼、時間編碼、群體編碼。"
            "冗餘令神經系統更穩健。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.5)
        self.clear()

    # ── Scene 7 — Outro ──────────────────────────────────────────────────

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)

        with self.voiceover(
            text="多謝收睇！下一課我哋會講神經網絡，"
            "由 McCulloch 同 Pitts 到感知器。記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)

        self.wait(1)
        self.play(FadeOut(thanks), run_time=0.8)
