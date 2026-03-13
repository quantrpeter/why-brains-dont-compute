"""
Lesson 3 – Algorithms
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 3/video"
    manim render -qh scene.py AlgorithmsExplainer
"""

from manim import *
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


class AlgorithmsExplainer(VoiceoverScene):
    """Single scene explaining algorithmic computation history in Cantonese."""

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
        self.scene_early_machines()
        self.scene_turing_machines()
        self.scene_boolean_algebra()
        self.scene_electronic_computers()
        self.scene_modern_computation()
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
        title = self.zh("演算法", font_size=56, color=C_BLUE)
        sub_en = self.en(
            "Algorithms", font_size=24, color=C_WHITE
        ).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh(
            "第三課", font_size=36, color=C_ORANGE
        ).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh(
            "制片人：Peter", font_size=24, color=C_DIM
        ).next_to(sub_zh, DOWN, buff=0.7)

        with self.voiceover(
            text="大家好！歡迎嚟到第三課。"
            "今日我哋會回顧演算法計算嘅歷史，由算盤到現代電子電腦。"
            "呢個歷史幫我哋理解咩係演算法，同埋電腦點樣運作。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    # ── Scene 2 — Early Machines ────────────────────────────────────────

    def scene_early_machines(self):
        heading = self.make_heading("早期計算機器")

        timeline = [
            ("算盤", "古代", C_GREEN),
            ("Pascal 計算器", "1642", C_ORANGE),
            ("Babbage 差分機", "1822", C_PINK),
            ("Ada Lovelace", "首位程式員", C_PURPLE),
        ]

        items = VGroup()
        for label, year, col in timeline:
            box = RoundedRectangle(
                corner_radius=0.1, width=3.5, height=0.7,
                fill_color=col, fill_opacity=0.2, stroke_color=col,
            )
            txt = VGroup(
                self.zh(label, font_size=22, color=col),
                self.zh(year, font_size=18, color=C_DIM),
            ).arrange(RIGHT, buff=0.4).move_to(box)
            items.add(VGroup(box, txt))
        items.arrange(DOWN, buff=0.3, aligned_edge=LEFT).shift(LEFT * 1.5)

        with self.voiceover(
            text="計算機器嘅歷史好長。"
            "算盤係古代嘅計算工具。"
            "一六四二年，Pascal 發明咗機械計算器。"
            "一八二二年，Babbage 設計差分機，可以計算多項式。"
            "Ada Lovelace 為 Babbage 嘅分析機寫程式，被譽為首位程式員。"
        ):
            self.play(Write(heading), run_time=0.6)
            for item in items:
                self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.7)

        self.wait(0.3)
        self.clear()

    # ── Scene 3 — Turing Machines ────────────────────────────────────────

    def scene_turing_machines(self):
        heading = self.make_heading("Turing 機")

        tape = VGroup(
            *[self.mono("0", font_size=24, color=C_DIM) for _ in range(5)],
            self.mono("1", font_size=24, color=C_YELLOW),
            *[self.mono("0", font_size=24, color=C_DIM) for _ in range(5)],
        ).arrange(RIGHT, buff=0.2).shift(UP * 0.5)

        head = Arrow(UP * 0.3, DOWN * 0.1, buff=0, color=C_RED, stroke_width=4)
        head.next_to(tape[5], UP, buff=0.1)

        turing_box = RoundedRectangle(
            corner_radius=0.15, width=4, height=0.8,
            fill_color=C_BLUE, fill_opacity=0.2, stroke_color=C_BLUE,
        ).shift(DOWN * 0.8)
        turing_text = self.zh(
            "抽象計算模型：讀、寫、移動、狀態轉換",
            font_size=22, color=C_WHITE,
        ).move_to(turing_box)

        universal = self.zh(
            "通用圖靈機 = 可以模擬任何演算法",
            font_size=24, color=C_GREEN,
        ).shift(DOWN * 1.8)

        with self.voiceover(
            text="一九三六年，Alan Turing 提出圖靈機。"
            "圖靈機係一個抽象嘅計算模型：有一條帶、一個讀寫頭、同埋狀態。"
            "佢可以讀、寫、移動、同埋根據規則轉換狀態。"
            "通用圖靈機可以模擬任何演算法，係現代電腦嘅理論基礎。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(tape), run_time=0.8)
            self.play(GrowArrow(head), run_time=0.5)
            self.play(FadeIn(turing_box), FadeIn(turing_text), run_time=0.8)
            self.play(FadeIn(universal), run_time=0.6)

        self.wait(0.3)
        self.clear()

    # ── Scene 4 — Boolean Algebra ───────────────────────────────────────

    def scene_boolean_algebra(self):
        heading = self.make_heading("布林代數")

        bool_box = self.make_box("George Boole", C_PURPLE, width=3.5, height=0.7)
        bool_box.shift(UP * 1.2)
        bool_desc = self.zh("1854 年《思維定律》", font_size=20, color=C_DIM).next_to(bool_box, DOWN, buff=0.2)

        ops = VGroup(
            self.mono("AND: 1∧1=1, 其他=0", font_size=24, color=C_GREEN),
            self.mono("OR:  0∨0=0, 其他=1", font_size=24, color=C_ORANGE),
            self.mono("NOT: ¬1=0, ¬0=1", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.2)

        circuit = self.zh(
            "數位電路嘅邏輯基礎：開關、閘、電晶體",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 1.8)

        with self.voiceover(
            text="George Boole 喺一八五四年發表《思維定律》，建立布林代數。"
            "布林代數用 0 同 1、AND、OR、NOT 嚟表達邏輯。"
            "AND 就係兩個都係 1 先係 1。OR 就係有一個係 1 就係 1。NOT 就係反轉。"
            "呢個係數位電路嘅邏輯基礎，開關、閘、電晶體都係用呢套邏輯。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(bool_box), FadeIn(bool_desc), run_time=0.6)
            for op in ops:
                self.play(FadeIn(op, shift=RIGHT * 0.2), run_time=0.5)
            self.play(FadeIn(circuit), run_time=0.6)

        self.wait(0.3)
        self.clear()

    # ── Scene 5 — Electronic Computers ──────────────────────────────────

    def scene_electronic_computers(self):
        heading = self.make_heading("電子電腦")

        machines = [
            ("Colossus", "1943", "破解密碼", C_GREEN),
            ("ENIAC", "1946", "首部通用電子電腦", C_ORANGE),
            ("電晶體", "1947", "取代真空管", C_PINK),
            ("積體電路", "1958", "摩爾定律開始", C_PURPLE),
        ]

        items = VGroup()
        for name, year, desc, col in machines:
            box = RoundedRectangle(
                corner_radius=0.1, width=4, height=0.9,
                fill_color=col, fill_opacity=0.2, stroke_color=col,
            )
            content = VGroup(
                self.zh(f"{name} ({year})", font_size=22, color=col),
                self.zh(desc, font_size=18, color=C_DIM),
            ).arrange(DOWN, buff=0.1).move_to(box)
            items.add(VGroup(box, content))
        items.arrange(DOWN, buff=0.25, aligned_edge=LEFT).shift(LEFT * 1)

        with self.voiceover(
            text="電子電腦嘅時代嚟喇。"
            "一九四三年，Colossus 用嚟破解密碼。"
            "一九四六年，ENIAC 係首部通用電子電腦。"
            "一九四七年，電晶體發明，取代咗真空管。"
            "一九五八年，積體電路出現，摩爾定律開始。"
        ):
            self.play(Write(heading), run_time=0.6)
            for item in items:
                self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.7)

        self.wait(0.3)
        self.clear()

    # ── Scene 6 — Modern Computation ───────────────────────────────────

    def scene_modern_computation(self):
        heading = self.make_heading("現代計算")

        moore = self.make_box("摩爾定律", C_GREEN, width=4, height=0.7)
        moore.shift(UP * 1.2)
        moore_desc = self.zh(
            "每 18–24 個月晶片密度翻倍",
            font_size=22, color=C_DIM,
        ).next_to(moore, DOWN, buff=0.2)

        milestones = VGroup(
            self.zh("•  PDP-11 小型電腦（1970）", font_size=24, color=C_ORANGE),
            self.zh("•  Cray 超級電腦", font_size=24, color=C_PINK),
            self.zh("•  個人電腦革命", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(DOWN * 0.3)

        with self.voiceover(
            text="現代計算嘅發展好快。"
            "摩爾定律話每十八到二十四個月，晶片密度就會翻倍。"
            "一九七零年代，PDP-11 小型電腦普及。"
            "Cray 超級電腦推動科學計算。"
            "個人電腦革命改變咗全世界。"
            "呢啲全部都係演算法嘅具體實現。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(moore), FadeIn(moore_desc), run_time=0.8)
            for m in milestones:
                self.play(FadeIn(m, shift=RIGHT * 0.3), run_time=0.6)

        self.wait(0.3)
        self.clear()

    # ── Scene 7 — Summary ───────────────────────────────────────────────

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)

        bullets = VGroup(
            self.zh("•  算盤、Pascal、Babbage 係早期計算機器", font_size=26, color=C_GREEN),
            self.zh("•  Turing 機係抽象計算模型", font_size=26, color=C_ORANGE),
            self.zh("•  布林代數係數位電路嘅邏輯基礎", font_size=26, color=C_PINK),
            self.zh("•  Colossus、ENIAC、電晶體、積體電路", font_size=26, color=C_PURPLE),
            self.zh("•  摩爾定律推動現代計算發展", font_size=26, color=C_CYAN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="總結一下今日學咗嘅嘢。"
            "算盤、Pascal、Babbage 係早期計算機器。"
            "Turing 機係抽象計算模型，可以模擬任何演算法。"
            "布林代數係數位電路嘅邏輯基礎。"
            "Colossus、ENIAC、電晶體、積體電路推動電子電腦發展。"
            "摩爾定律繼續推動現代計算。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.5)
        self.clear()

    # ── Scene 8 — Outro ──────────────────────────────────────────────────

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)

        with self.voiceover(
            text="多謝收睇！下一課我哋會講編碼，"
            "對比電腦編碼同神經編碼。記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)

        self.wait(1)
        self.play(FadeOut(thanks), run_time=0.8)
