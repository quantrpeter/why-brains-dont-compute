"""
Lesson 18 – Stereopsis
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 18/video"
    manim render -qh scene.py StereopsisExplainer
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


class StereopsisExplainer(VoiceoverScene):
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
        self.scene_correspondence()
        self.scene_binocular_circuitry()
        self.scene_ocular_dominance()
        self.scene_empirical_depth()
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
        title = self.zh("立體視覺", font_size=56, color=C_BLUE)
        sub_en = self.en("Stereopsis", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第十八課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第十八課。"
            "今日我哋會講立體視覺。"
            "傳統理論用影像對應嚟解釋深度感知，"
            "但有一個替代理論用解剖對應。"
            "我哋會講雙眼電路、眼優勢、同經驗主義嘅深度感知。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_correspondence(self):
        heading = self.make_heading("影像對應 vs 解剖對應")
        img_box = self.make_box("影像對應", C_GREEN, width=3.5, height=0.8)
        img_box.shift(UP * 1.0 + LEFT * 2)
        img_desc = self.zh(
            "標準理論：匹配兩眼影像嘅對應點",
            font_size=20, color=C_DIM,
        ).next_to(img_box, DOWN, buff=0.2)
        anat_box = self.make_box("解剖對應", C_ORANGE, width=3.5, height=0.8)
        anat_box.shift(UP * 1.0 + RIGHT * 2)
        anat_desc = self.zh(
            "替代理論：用解剖結構對應",
            font_size=20, color=C_DIM,
        ).next_to(anat_box, DOWN, buff=0.2)
        with self.voiceover(
            text="傳統嘅立體視覺理論用影像對應。"
            "標準理論係匹配兩眼影像嘅對應點，嚟計算深度。"
            "但有一個替代理論用解剖對應。"
            "呢個理論可以更好咁解釋雙眼電路嘅結構。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(img_box), FadeIn(img_desc), run_time=0.6)
            self.play(FadeIn(anat_box), FadeIn(anat_desc), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_binocular_circuitry(self):
        heading = self.make_heading("雙眼電路")
        left_eye = Circle(radius=0.4, color=C_BLUE)
        left_eye.shift(LEFT * 2.5 + UP * 0.5)
        right_eye = Circle(radius=0.4, color=C_BLUE)
        right_eye.shift(RIGHT * 2.5 + UP * 0.5)
        cortex = RoundedRectangle(width=3, height=1.2, color=C_GREEN, corner_radius=0.2)
        cortex.shift(DOWN * 0.8)
        cortex_label = self.zh("視覺皮層", font_size=20, color=C_GREEN).move_to(cortex)
        arrow_l = Arrow(left_eye.get_bottom(), cortex.get_top() + LEFT * 0.5, buff=0.2, color=C_WHITE)
        arrow_r = Arrow(right_eye.get_bottom(), cortex.get_top() + RIGHT * 0.5, buff=0.2, color=C_WHITE)
        evolved = self.zh(
            "進化嘅人工神經網絡可以匹配生物電路結構",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 1.8)
        with self.voiceover(
            text="雙眼電路連接兩眼到視覺皮層。"
            "進化嘅人工神經網絡可以匹配生物電路嘅結構。"
            "呢個支持解剖對應嘅理論。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(Create(left_eye), Create(right_eye), run_time=0.5)
            self.play(GrowArrow(arrow_l), GrowArrow(arrow_r), run_time=0.5)
            self.play(FadeIn(cortex), FadeIn(cortex_label), run_time=0.5)
            self.play(FadeIn(evolved), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_ocular_dominance(self):
        heading = self.make_heading("眼優勢")
        dom_box = self.make_box("雙眼神經元", C_PINK, width=4.0, height=0.8)
        dom_box.shift(UP * 1.2)
        dom_desc = self.zh(
            "多數被一隻眼主導，分離成皮層條紋",
            font_size=22, color=C_WHITE,
        ).next_to(dom_box, DOWN, buff=0.4)
        stripes = self.zh(
            "眼優勢柱：左右眼交替主導嘅皮層區域",
            font_size=20, color=C_DIM,
        ).shift(DOWN * 0.3)
        with self.voiceover(
            text="眼優勢係指雙眼神經元多數被一隻眼主導。"
            "呢啲神經元會分離成皮層條紋，叫做眼優勢柱。"
            "左右眼交替主導唔同嘅皮層區域。"
            "呢個結構同解剖對應理論一致。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(dom_box), FadeIn(dom_desc), run_time=0.8)
            self.play(FadeIn(stripes), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_empirical_depth(self):
        heading = self.make_heading("經驗主義嘅深度感知")
        diff_box = self.make_box("雙眼差異嘅出現頻率", C_GREEN, width=4.5, height=0.8)
        diff_box.shift(UP * 1.0 + LEFT * 2)
        arrow = Arrow(
            diff_box.get_right(), diff_box.get_right() + RIGHT * 2,
            buff=0.2, color=C_WHITE, stroke_width=3,
        )
        depth_box = self.make_box("經驗深度尺度", C_ORANGE, width=4.5, height=0.8)
        depth_box.shift(UP * 1.0 + RIGHT * 2)
        key = self.zh(
            "唔係計算視差，而係用經驗累積嘅頻率",
            font_size=22, color=C_CYAN,
        ).shift(DOWN * 0.8)
        with self.voiceover(
            text="經驗主義嘅深度感知係：雙眼差異嘅出現頻率產生經驗深度尺度。"
            "腦唔係計算視差嚟還原三維，"
            "而係用經驗累積嘅頻率嚟解讀雙眼輸入。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(diff_box), GrowArrow(arrow), FadeIn(depth_box), run_time=0.8)
            self.play(FadeIn(key), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  影像對應 vs 解剖對應：兩種理論", font_size=24, color=C_GREEN),
            self.zh("•  進化神經網絡可匹配生物雙眼電路", font_size=24, color=C_ORANGE),
            self.zh("•  眼優勢：雙眼神經元分離成皮層條紋", font_size=24, color=C_PINK),
            self.zh("•  雙眼差異嘅出現頻率 → 經驗深度尺度", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。影像對應同解剖對應係兩種理論。"
            "進化嘅神經網絡可以匹配生物雙眼電路。"
            "眼優勢係雙眼神經元分離成皮層條紋。"
            "雙眼差異嘅出現頻率產生經驗深度尺度。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：刺激與行為", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講刺激同行為，"
            "探討刺激究竟係咩、生理學家同心理學家嘅觀點、"
            "同埋共同嘅經驗策略。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
