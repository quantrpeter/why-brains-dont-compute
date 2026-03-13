"""
Lesson 23 – Feature Detection
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 23/video"
    manim render -qh scene.py FeatureDetectionExplainer
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


class FeatureDetectionExplainer(VoiceoverScene):
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
        self.scene_feature_detection()
        self.scene_specific_neurons()
        self.scene_perception_in_monkeys()
        self.scene_limitations()
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
        title = self.zh("特徵檢測", font_size=56, color=C_BLUE)
        sub_en = self.en("Feature Detection", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第二十三課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第二十三課。"
            "今日我哋會批判性咁檢視特徵檢測理論。"
            "從休伯爾同韋塞爾到祖母細胞。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_feature_detection(self):
        heading = self.make_heading("休伯爾同韋塞爾嘅特徵檢測")
        hw_box = self.make_box("Hubel & Wiesel", C_GREEN, width=4.0, height=0.8)
        hw_box.shift(UP * 1.2)
        features = VGroup(
            self.zh("•  邊緣、方向、運動檢測器", font_size=24, color=C_WHITE),
            self.zh("•  神經元當做特徵偵測器", font_size=24, color=C_DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(hw_box, DOWN, buff=0.3)
        with self.voiceover(
            text="休伯爾同韋塞爾發現視覺皮層有特徵檢測神經元。"
            "邊緣、方向、運動檢測器。"
            "神經元好似當做特徵偵測器咁。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(hw_box), run_time=0.5)
            for f in features:
                self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(0.3)
        self.clear()

    def scene_specific_neurons(self):
        heading = self.make_heading("越嚟越具體嘅神經元")
        specific_items = VGroup(
            self.zh("•  面細胞：對特定面孔有反應", font_size=24, color=C_GREEN),
            self.zh("•  位置細胞：對空間位置有反應", font_size=24, color=C_ORANGE),
            self.zh("•  祖母細胞：極度具體嘅特徵？", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(UP * 0.3)
        with self.voiceover(
            text="之後發現越嚟越具體嘅神經元。"
            "面細胞對特定面孔有反應。"
            "位置細胞對空間位置有反應。"
            "祖母細胞係咪極度具體嘅特徵？有爭議。"
        ):
            self.play(Write(heading), run_time=0.6)
            for s in specific_items:
                self.play(FadeIn(s, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_perception_in_monkeys(self):
        heading = self.make_heading("猴子嘅感知")
        it_box = self.make_box("颞下皮層損傷", C_ORANGE, width=4.0, height=0.8)
        it_box.shift(UP * 1.0)
        it_desc = self.zh(
            "損傷後會損害物體識別，支持特徵檢測嘅角色",
            font_size=22, color=C_WHITE,
        ).next_to(it_box, DOWN, buff=0.3)
        with self.voiceover(
            text="猴子嘅颞下皮層損傷會損害物體識別。"
            "呢個支持特徵檢測喺感知嘅角色。"
            "但特徵檢測唔等於計算。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(it_box), FadeIn(it_desc), run_time=0.8)
        self.wait(0.3)
        self.clear()

    def scene_limitations(self):
        heading = self.make_heading("回到謝靈頓嘅框架")
        limit_box = self.make_box("特徵檢測嘅局限", C_RED, width=4.5, height=0.8)
        limit_box.shift(UP * 1.0)
        limit_desc = self.zh(
            "特徵檢測係現代版嘅反射弧：刺激 → 處理 → 反應",
            font_size=22, color=C_WHITE,
        ).next_to(limit_box, DOWN, buff=0.3)
        inverse = self.zh(
            "逆問題：特徵唔可以映射返去現實",
            font_size=20, color=C_DIM,
        ).shift(DOWN * 0.8)
        with self.voiceover(
            text="特徵檢測其實係現代版嘅反射弧。"
            "刺激、處理、反應。"
            "但逆問題依然存在：特徵唔可以映射返去現實。"
            "經驗框架可以更好咁解釋感知。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(limit_box), FadeIn(limit_desc), run_time=0.8)
            self.play(FadeIn(inverse), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  休伯爾韋塞爾：邊緣、方向、運動檢測", font_size=24, color=C_GREEN),
            self.zh("•  面細胞、位置細胞、祖母細胞", font_size=24, color=C_ORANGE),
            self.zh("•  颞下皮層損傷損害物體識別", font_size=24, color=C_PINK),
            self.zh("•  特徵檢測係現代反射弧，有局限", font_size=24, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。休伯爾韋塞爾發現邊緣、方向、運動檢測。"
            "面細胞、位置細胞、祖母細胞越嚟越具體。"
            "颞下皮層損傷會損害物體識別。"
            "特徵檢測係現代反射弧，但有局限。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：統計推論", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講統計推論，"
            "包括貝葉斯方法同經驗排名嘅比較。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
