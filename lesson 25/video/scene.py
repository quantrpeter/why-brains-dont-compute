"""
Lesson 25 – Summing Up
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 25/video"
    manim render -qh scene.py SummingUpExplainer
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


class SummingUpExplainer(VoiceoverScene):
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
        self.scene_part_one_recap()
        self.scene_part_two_three_recap()
        self.scene_part_four_recap()
        self.scene_part_five_six_recap()
        self.scene_final_conclusion()
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
        title = self.zh("總結", font_size=56, color=C_BLUE)
        sub_en = self.en("Summing Up", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第二十五課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第二十五課，亦都係最後一課。"
            "今日我哋會總結成本書嘅論證。"
            "腦唔係計算，係經驗運作。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_part_one_recap(self):
        heading = self.make_heading("第一部：唔同現實嘅問題解決")
        part1_items = VGroup(
            self.zh("•  算法 vs 經驗：兩種解決問題嘅方式", font_size=24, color=C_GREEN),
            self.zh("•  客觀現實 vs 主觀經驗：動物冇辦法量度環境", font_size=24, color=C_ORANGE),
            self.zh("•  感知存在喺腦入面，唔喺物理世界", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 0.2)
        with self.voiceover(
            text="第一部講唔同現實嘅問題解決。"
            "算法同經驗係兩種方式。"
            "客觀現實同主觀經驗有差距，動物冇辦法量度環境。"
            "感知存在喺腦入面，唔喺物理世界。"
        ):
            self.play(Write(heading), run_time=0.6)
            for p in part1_items:
                self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_part_two_three_recap(self):
        heading = self.make_heading("第二、三部：算法與神經網絡")
        part23_items = VGroup(
            self.zh("•  算法計算：圖靈機、編碼、電子電腦", font_size=24, color=C_GREEN),
            self.zh("•  神經網絡：試錯學習、反向傳播", font_size=24, color=C_ORANGE),
            self.zh("•  大搜索空間需要經驗策略，唔係算法", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 0.2)
        with self.voiceover(
            text="第二、三部講算法同神經網絡。"
            "算法計算有圖靈機、編碼、電子電腦。"
            "神經網絡用試錯學習、反向傳播。"
            "大搜索空間需要經驗策略，唔係算法。"
        ):
            self.play(Write(heading), run_time=0.6)
            for p in part23_items:
                self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_part_four_recap(self):
        heading = self.make_heading("第四部：感知")
        part4_items = VGroup(
            self.zh("•  刺激係模糊嘅，逆問題冇唯一解", font_size=24, color=C_GREEN),
            self.zh("•  經驗排名：出現頻率決定感知品質", font_size=24, color=C_ORANGE),
            self.zh("•  幾何、亮度、顏色、運動、大小、立體 — 全部經驗預測", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 0.2)
        with self.voiceover(
            text="第四部講感知。"
            "刺激係模糊嘅，逆問題冇唯一解。"
            "經驗排名：出現頻率決定感知品質。"
            "幾何、亮度、顏色、運動、大小、立體，全部可以由經驗預測。"
        ):
            self.play(Write(heading), run_time=0.6)
            for p in part4_items:
                self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_part_five_six_recap(self):
        heading = self.make_heading("第五、六部：連結與其他理論")
        part56_items = VGroup(
            self.zh("•  刺激與行為：進化、學習、文化塑造聯想", font_size=24, color=C_GREEN),
            self.zh("•  機制：可塑性、LTP/LTD、獎賞", font_size=24, color=C_ORANGE),
            self.zh("•  反射、特徵檢測、貝葉斯 — 都有局限，經驗框架更全面", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 0.2)
        with self.voiceover(
            text="第五、六部講連結同其他理論。"
            "刺激與行為由進化、學習、文化塑造。"
            "機制包括可塑性、長期增強抑制、獎賞。"
            "反射、特徵檢測、貝葉斯都有局限，經驗框架更全面。"
        ):
            self.play(Write(heading), run_time=0.6)
            for p in part56_items:
                self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_final_conclusion(self):
        heading = self.make_heading("核心結論")
        main = self.zh("腦唔係計算，係經驗運作", font_size=44, color=C_YELLOW)
        main.shift(UP * 0.5)
        sub_items = VGroup(
            self.zh("•  動物冇辦法量度現實", font_size=24, color=C_GREEN),
            self.zh("•  感知由出現頻率塑造", font_size=24, color=C_ORANGE),
            self.zh("•  對神經科學、AI、心靈哲學都有啟示", font_size=24, color=C_PINK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.8)
        with self.voiceover(
            text="核心結論：腦唔係計算，係經驗運作。"
            "動物冇辦法量度現實。"
            "感知由出現頻率塑造。"
            "呢個對神經科學、人工智能、心靈哲學都有啟示。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(Write(main), run_time=1.2)
            for s in sub_items:
                self.play(FadeIn(s, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        series = self.zh("多謝你哋跟住學晒成個系列", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.4)
        book = self.zh("《Why Brains Don't Compute》", font_size=22, color=C_DIM).next_to(series, DOWN, buff=0.3)
        with self.voiceover(
            text="多謝收睇！"
            "多謝你哋跟住學晒成個系列。"
            "希望呢二十五課幫到你哋理解點解腦唔係計算。"
            "再見！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(series, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(book, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(thanks), FadeOut(series), FadeOut(book), run_time=0.8)
