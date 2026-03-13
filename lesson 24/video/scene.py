"""
Lesson 24 – Statistical Inference
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 24/video"
    manim render -qh scene.py StatisticalInferenceExplainer
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


class StatisticalInferenceExplainer(VoiceoverScene):
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
        self.scene_statistical_inference()
        self.scene_bayes_theorem()
        self.scene_problems_with_bayes()
        self.scene_empirical_alternative()
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
        title = self.zh("統計推論", font_size=56, color=C_BLUE)
        sub_en = self.en("Statistical Inference", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第二十四課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第二十四課。"
            "今日我哋會評估貝葉斯方法喺感知嘅應用。"
            "同埋點解經驗框架比貝葉斯推論更好。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_statistical_inference(self):
        heading = self.make_heading("統計推論應用於感知")
        infer_box = self.make_box("統計推論", C_GREEN, width=4.0, height=0.8)
        infer_box.shift(UP * 1.2)
        infer_desc = self.zh(
            "用概率推斷刺激最可能嘅來源",
            font_size=22, color=C_WHITE,
        ).next_to(infer_box, DOWN, buff=0.3)
        with self.voiceover(
            text="統計推論應用於感知，係用概率嚟推斷刺激最可能嘅來源。"
            "呢個理論假設腦會做概率計算。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(infer_box), FadeIn(infer_desc), run_time=0.8)
        self.wait(0.3)
        self.clear()

    def scene_bayes_theorem(self):
        heading = self.make_heading("貝葉斯定理")
        prior_box = self.make_box("先驗", C_GREEN, width=2.5, height=0.7)
        prior_box.shift(UP * 1.0 + LEFT * 2)
        like_box = self.make_box("似然", C_ORANGE, width=2.5, height=0.7)
        like_box.shift(UP * 1.0)
        post_box = self.make_box("後驗", C_PINK, width=2.5, height=0.7)
        post_box.shift(UP * 1.0 + RIGHT * 2)
        times = self.zh("×", font_size=36, color=C_WHITE).shift(UP * 1.0 + LEFT * 0.5)
        arrow = self.zh("→", font_size=36, color=C_WHITE).shift(UP * 1.0 + RIGHT * 0.5)
        formula = self.zh("後驗 ∝ 先驗 × 似然", font_size=24, color=C_CYAN).shift(DOWN * 0.5)
        with self.voiceover(
            text="貝葉斯定理：後驗概率等於先驗乘似然。"
            "先驗係事前嘅經驗，似然係數據嘅可能性。"
            "兩者相乘得到後驗嘅估計。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(prior_box), FadeIn(like_box), FadeIn(post_box), run_time=0.6)
            self.play(FadeIn(times), FadeIn(arrow), FadeIn(formula), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_problems_with_bayes(self):
        heading = self.make_heading("貝葉斯方法嘅問題")
        problem_box = self.make_box("先驗係不可知嘅", C_RED, width=4.5, height=0.8)
        problem_box.shift(UP * 1.0)
        problem_desc = self.zh(
            "生物冇辦法知道「真實」嘅先驗，仲假設世界係可計算嘅",
            font_size=22, color=C_WHITE,
        ).next_to(problem_box, DOWN, buff=0.3)
        with self.voiceover(
            text="貝葉斯方法嘅問題係：先驗係不可知嘅。"
            "生物冇辦法知道真實嘅先驗。"
            "而且仲假設世界係可計算嘅。"
            "經驗主義唔需要呢啲假設。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(problem_box), FadeIn(problem_desc), run_time=0.8)
        self.wait(0.3)
        self.clear()

    def scene_empirical_alternative(self):
        heading = self.make_heading("經驗排名 vs 貝葉斯推論")
        emp_box = self.make_box("經驗排名", C_GREEN, width=4.0, height=0.8)
        emp_box.shift(UP * 1.0 + LEFT * 2)
        arrow = Arrow(
            emp_box.get_right(), emp_box.get_right() + RIGHT * 2,
            buff=0.2, color=C_WHITE, stroke_width=3,
        )
        bayes_box = self.make_box("貝葉斯推論", C_ORANGE, width=4.0, height=0.8)
        bayes_box.shift(UP * 1.0 + RIGHT * 2)
        key = self.zh(
            "唔使計算，經驗直接塑造感知，唔需要先驗",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 0.8)
        with self.voiceover(
            text="經驗排名唔使計算。"
            "經驗直接塑造感知，唔需要先驗。"
            "出現頻率嘅排名就夠，唔使貝葉斯推論。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(emp_box), GrowArrow(arrow), FadeIn(bayes_box), run_time=0.8)
            self.play(FadeIn(key), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  統計推論：用概率推斷刺激來源", font_size=24, color=C_GREEN),
            self.zh("•  貝葉斯：先驗 × 似然 → 後驗", font_size=24, color=C_ORANGE),
            self.zh("•  問題：先驗不可知，假設可計算", font_size=24, color=C_PINK),
            self.zh("•  經驗排名：唔使計算，直接塑造感知", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。統計推論係用概率推斷刺激來源。"
            "貝葉斯係先驗乘似然得到後驗。"
            "問題係先驗不可知，仲假設係可計算。"
            "經驗排名唔使計算，直接塑造感知。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：總結", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課係全書總結，"
            "我哋會回顧整個論證：腦唔係計算，係經驗運作。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
