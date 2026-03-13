"""
Lesson 2 – Objective and Subjective Reality
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 2/video"
    manim render -qh scene.py ObjectiveSubjectiveReality
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


class ObjectiveSubjectiveReality(VoiceoverScene):
    """Single scene explaining objective vs subjective reality in Cantonese."""

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
        self.scene_newtonian_reality()
        self.scene_biological_measurements()
        self.scene_inverse_problem()
        self.scene_what_we_perceive()
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
        title = self.zh("客觀同主觀現實", font_size=56, color=C_BLUE)
        sub_en = self.en(
            "Objective and Subjective Reality", font_size=24, color=C_WHITE
        ).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh(
            "第二課", font_size=36, color=C_ORANGE
        ).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh(
            "制片人：Peter", font_size=24, color=C_DIM
        ).next_to(sub_zh, DOWN, buff=0.7)

        with self.voiceover(
            text="大家好！歡迎嚟到第二課。"
            "今日我哋會探討物理現實同感知現實之間嘅差距。"
            "牛頓物理學描述嘅係客觀世界，但我哋感知到嘅係主觀經驗。"
            "呢個差距點解會存在？動物點解唔能夠直接量度環境？"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    # ── Scene 2 — Newtonian Reality ──────────────────────────────────────

    def scene_newtonian_reality(self):
        heading = self.make_heading("牛頓物理學嘅客觀現實")

        physics_box = self.make_box("古典物理", C_GREEN, width=4, height=0.9)
        physics_box.shift(UP * 1.0)
        physics_items = VGroup(
            self.zh("•  物質、能量、力、運動", font_size=22, color=C_WHITE),
            self.zh("•  決定論：已知狀態可預測未來", font_size=22, color=C_WHITE),
            self.zh("•  混沌：微小差異可導致巨大變化", font_size=22, color=C_WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(physics_box, DOWN, buff=0.4)

        measure_box = self.make_box("量度", C_ORANGE, width=4, height=0.6)
        measure_box.shift(DOWN * 1.2)
        measure_text = self.zh(
            "科學家用儀器量度：長度、質量、時間、光強度",
            font_size=20, color=C_DIM,
        ).next_to(measure_box, DOWN, buff=0.2)

        with self.voiceover(
            text="牛頓物理學描述嘅係客觀現實。"
            "物質、能量、力、運動，呢啲都係可以量度嘅。"
            "古典物理係決定論嘅，已知狀態可以預測未來。"
            "但混沌理論話我哋知，微小嘅差異可以導致巨大嘅變化。"
            "科學家用儀器量度長度、質量、時間、光強度。"
            "但動物冇呢啲儀器。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(physics_box), run_time=0.6)
            for item in physics_items:
                self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.5)
            self.play(FadeIn(measure_box), FadeIn(measure_text), run_time=0.8)

        self.wait(0.3)
        self.clear()

    # ── Scene 3 — Biological Measurements ────────────────────────────────

    def scene_biological_measurements(self):
        heading = self.make_heading("動物冇量度儀器")

        eye = Circle(radius=0.8, color=C_BLUE, stroke_width=3)
        eye.shift(LEFT * 2 + UP * 0.3)
        eye_label = self.zh("視網膜", font_size=20, color=C_BLUE).next_to(eye, DOWN, buff=0.2)

        arrow = Arrow(
            eye.get_right(), eye.get_right() + RIGHT * 2,
            buff=0.1, color=C_ORANGE, stroke_width=4,
        )
        arrow_label = self.zh(
            "光刺激 → 神經訊號\n唔係直接量度物理量",
            font_size=20, color=C_ORANGE,
        ).next_to(arrow, UP, buff=0.2)

        problem = self.zh(
            "動物只能接收刺激，唔能夠直接知道外界嘅物理真相",
            font_size=24, color=C_RED,
        ).shift(DOWN * 1.8)

        with self.voiceover(
            text="動物冇量度儀器。"
            "視網膜接收光刺激，轉換成神經訊號。"
            "呢個唔係直接量度物理量，而係一種轉換。"
            "動物只能接收刺激，唔能夠直接知道外界嘅物理真相。"
            "呢個就係逆問題嘅根源。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(Create(eye), FadeIn(eye_label), run_time=0.8)
            self.play(GrowArrow(arrow), FadeIn(arrow_label), run_time=1)
            self.play(FadeIn(problem, shift=UP * 0.2), run_time=0.8)

        self.wait(0.3)
        self.clear()

    # ── Scene 4 — Inverse Problem ───────────────────────────────────────

    def scene_inverse_problem(self):
        heading = self.make_heading("逆問題")

        source_box = self.make_box("物理來源", C_GREEN, width=2.5, height=0.8)
        source_box.shift(LEFT * 2.5 + UP * 0.5)
        source_text = self.zh("無數種可能", font_size=18, color=C_DIM).next_to(source_box, DOWN, buff=0.15)

        arrow = Arrow(
            source_box.get_right(), source_box.get_right() + RIGHT * 2,
            buff=0.1, color=C_WHITE, stroke_width=3,
        )
        arrow_label = self.zh("投影", font_size=18, color=C_DIM).next_to(arrow, UP, buff=0.1)

        stim_box = self.make_box("同一刺激", C_ORANGE, width=2.5, height=0.8)
        stim_box.shift(RIGHT * 2.5 + UP * 0.5)
        stim_text = self.zh("同一種投影", font_size=18, color=C_DIM).next_to(stim_box, DOWN, buff=0.15)

        dilemma = self.zh(
            "同一種視網膜投影可以由好多唔同嘅物理來源造成",
            font_size=24, color=C_RED,
        ).shift(DOWN * 1.2)

        example = self.zh(
            "例如：細嘅近物 vs 大嘅遠物 → 投影可以一樣",
            font_size=20, color=C_PURPLE,
        ).shift(DOWN * 1.8)

        with self.voiceover(
            text="逆問題係咁樣嘅。"
            "物理來源有無數種可能，但投影到視網膜嘅刺激可以係同一種。"
            "同一種視網膜投影可以由好多唔同嘅物理來源造成。"
            "例如細嘅近物同大嘅遠物，投影可以完全一樣。"
            "所以單靠刺激，腦唔能夠還原物理真相。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(source_box), FadeIn(source_text), run_time=0.6)
            self.play(GrowArrow(arrow), FadeIn(arrow_label), run_time=0.6)
            self.play(FadeIn(stim_box), FadeIn(stim_text), run_time=0.6)
            self.play(FadeIn(dilemma), run_time=0.8)
            self.play(FadeIn(example), run_time=0.6)

        self.wait(0.3)
        self.clear()

    # ── Scene 5 — What We Perceive ──────────────────────────────────────

    def scene_what_we_perceive(self):
        heading = self.make_heading("感知存在於腦入面")

        berkeley_box = self.make_box("Berkeley 嘅洞見", C_PURPLE, width=5, height=0.8)
        berkeley_box.shift(UP * 1.0)
        berkeley_text = self.zh(
            "感知唔係喺物理世界，而係喺我哋嘅腦入面",
            font_size=24, color=C_WHITE,
        ).next_to(berkeley_box, DOWN, buff=0.3)

        brain_icon = Circle(radius=0.6, color=C_BLUE, fill_opacity=0.2)
        brain_icon.shift(DOWN * 0.3)
        brain_label = self.zh("感知 = 腦嘅建構", font_size=22, color=C_BLUE).next_to(brain_icon, DOWN, buff=0.2)

        mismatch = self.zh(
            "物理量度同感知經常有系統性差異",
            font_size=22, color=C_ORANGE,
        ).shift(DOWN * 1.8)

        with self.voiceover(
            text="十八世紀哲學家 Berkeley 有一個重要洞見。"
            "感知唔係喺物理世界，而係喺我哋嘅腦入面。"
            "感知係腦嘅建構，唔係外界嘅直接複製。"
            "所以物理量度同感知經常有系統性差異。"
            "呢啲差異唔係錯誤，而係腦用經驗嚟解讀刺激嘅結果。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(berkeley_box), FadeIn(berkeley_text), run_time=0.8)
            self.play(Create(brain_icon), FadeIn(brain_label), run_time=0.8)
            self.play(FadeIn(mismatch), run_time=0.6)

        self.wait(0.3)
        self.clear()

    # ── Scene 6 — Summary ───────────────────────────────────────────────

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)

        bullets = VGroup(
            self.zh("•  牛頓物理描述客觀現實，可量度", font_size=26, color=C_GREEN),
            self.zh("•  動物冇儀器，只能接收刺激", font_size=26, color=C_ORANGE),
            self.zh("•  逆問題：同一刺激可來自唔同來源", font_size=26, color=C_PINK),
            self.zh("•  感知存在於腦入面，係建構出嚟嘅", font_size=26, color=C_PURPLE),
            self.zh("•  物理量度同感知有系統性差異", font_size=26, color=C_CYAN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="總結一下今日學咗嘅嘢。"
            "牛頓物理描述客觀現實，可以量度。"
            "動物冇儀器，只能接收刺激。"
            "逆問題話我哋知，同一刺激可以來自唔同嘅物理來源。"
            "感知存在於腦入面，係建構出嚟嘅。"
            "物理量度同感知經常有系統性差異。"
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
            text="多謝收睇！下一課我哋會講演算法嘅歷史，"
            "由算盤到現代電腦。記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)

        self.wait(1)
        self.play(FadeOut(thanks), run_time=0.8)
