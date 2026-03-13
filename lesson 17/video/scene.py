"""
Lesson 17 – Object Size
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 17/video"
    manim render -qh scene.py ObjectSizeExplainer
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


class ObjectSizeExplainer(VoiceoverScene):
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
        self.scene_size_illusions()
        self.scene_distance_cues()
        self.scene_moon_illusion()
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
        title = self.zh("物體大小", font_size=56, color=C_BLUE)
        sub_en = self.en("Object Size", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第十七課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第十七課。"
            "今日我哋會講物體大小嘅感知。"
            "經典嘅大小錯覺、大小距離悖論、"
            "同埋月亮錯覺都可以用經驗主義嚟解釋。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_size_illusions(self):
        heading = self.make_heading("艾賓浩斯效應")
        center = Circle(radius=0.3, color=C_WHITE, fill_opacity=0.8)
        center.shift(UP * 0.5 + LEFT * 2)
        small_surround = VGroup(*[Circle(radius=0.15, color=C_ORANGE) for _ in range(6)])
        small_surround.arrange_in_grid(2, 3, buff=0.2).move_to(center.get_center() + RIGHT * 1.2)
        large_surround = VGroup(*[Circle(radius=0.25, color=C_CYAN) for _ in range(4)])
        large_surround.arrange_in_grid(2, 2, buff=0.3).move_to(center.get_center() + LEFT * 2.5)
        label_small = self.zh("小圓包圍 → 睇落大啲", font_size=20, color=C_ORANGE).shift(DOWN * 1.2 + RIGHT * 1.5)
        label_large = self.zh("大圓包圍 → 睇落細啲", font_size=20, color=C_CYAN).shift(DOWN * 1.2 + LEFT * 1.5)
        same = self.zh("兩個中心圓其實一樣大", font_size=22, color=C_YELLOW).shift(DOWN * 1.8)
        with self.voiceover(
            text="艾賓浩斯效應係經典嘅大小錯覺。"
            "兩個一樣大嘅圓，一個被細圓包圍，一個被大圓包圍。"
            "被細圓包圍嘅睇落大啲，被大圓包圍嘅睇落細啲。"
            "呢個可以由自然場景幾何嘅統計嚟解釋。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(center), run_time=0.5)
            self.play(FadeIn(small_surround), FadeIn(large_surround), run_time=0.8)
            self.play(FadeIn(label_small), FadeIn(label_large), FadeIn(same), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_distance_cues(self):
        heading = self.make_heading("3D 場景嘅大小線索")
        cues = VGroup(
            self.zh("•  透視：近大遠細", font_size=24, color=C_GREEN),
            self.zh("•  遮擋：前面遮後面", font_size=24, color=C_ORANGE),
            self.zh("•  空氣透視：遠嘅模糊", font_size=24, color=C_PINK),
            self.zh("•  運動視差：近嘅動得快", font_size=24, color=C_CYAN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(UP * 0.3)
        paradox_box = self.make_box("大小距離悖論", C_RED, width=4.0, height=0.8)
        paradox_box.shift(DOWN * 1.5)
        paradox_text = self.zh(
            "背景物體物理大小一樣，但睇落大啲，由經驗排名預測",
            font_size=20, color=C_WHITE,
        ).next_to(paradox_box, DOWN, buff=0.3)
        with self.voiceover(
            text="三維場景有好多大小線索。"
            "透視、遮擋、空氣透視、運動視差。"
            "大小距離悖論係：背景嘅物體物理大小一樣，但睇落大啲。"
            "呢個可以由經驗排名嚟預測。"
        ):
            self.play(Write(heading), run_time=0.6)
            for c in cues:
                self.play(FadeIn(c, shift=RIGHT * 0.2), run_time=0.5)
            self.play(FadeIn(paradox_box), FadeIn(paradox_text), run_time=0.8)
        self.wait(0.3)
        self.clear()

    def scene_moon_illusion(self):
        heading = self.make_heading("月亮錯覺")
        horizon = self.zh("地平線月亮", font_size=24, color=C_ORANGE)
        horizon.shift(UP * 0.8 + LEFT * 2)
        zenith = self.zh("天頂月亮", font_size=24, color=C_CYAN)
        zenith.shift(UP * 0.8 + RIGHT * 2)
        observation = self.zh(
            "地平線嘅月亮睇落大過天頂嘅月亮，但物理上一樣大",
            font_size=22, color=C_WHITE,
        ).shift(DOWN * 0.3)
        explanation = self.zh(
            "地平線月亮喺縮細嘅地面投影中排名更高",
            font_size=22, color=C_GREEN,
        ).shift(DOWN * 1.0)
        with self.voiceover(
            text="月亮錯覺係：地平線嘅月亮睇落大過天頂嘅月亮。"
            "但物理上兩個月亮係一樣大嘅。"
            "經驗主義嘅解釋係：地平線月亮喺縮細嘅地面投影中排名更高。"
            "天頂月亮冇地面參照，所以排名唔同。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(horizon), FadeIn(zenith), run_time=0.6)
            self.play(FadeIn(observation), run_time=0.6)
            self.play(FadeIn(explanation), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  艾賓浩斯效應：周圍物體改變感知大小", font_size=24, color=C_GREEN),
            self.zh("•  透視、遮擋、空氣透視、運動視差係 3D 線索", font_size=24, color=C_ORANGE),
            self.zh("•  大小距離悖論：背景物體睇落大啲", font_size=24, color=C_PINK),
            self.zh("•  月亮錯覺：地平線月亮排名更高", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。艾賓浩斯效應係周圍物體會改變感知大小。"
            "透視、遮擋、空氣透視、運動視差係三維場景嘅線索。"
            "大小距離悖論係背景物體睇落大啲。"
            "月亮錯覺係地平線月亮喺縮細投影中排名更高。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：立體視覺", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講立體視覺，"
            "包括影像對應同解剖對應、雙眼電路、眼優勢。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
