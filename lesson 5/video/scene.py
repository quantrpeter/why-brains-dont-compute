"""
Lesson 5 – Neural Networks
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 5/video"
    manim render -qh scene.py NeuralNetworksExplainer
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


class NeuralNetworksExplainer(VoiceoverScene):
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
        self.scene_history()
        self.scene_key_attributes()
        self.scene_failure_to_take_off()
        self.scene_perceptrons()
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
        title = self.zh("神經網絡", font_size=56, color=C_BLUE)
        sub_en = self.en("Neural Networks", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第五課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第五課。"
            "今日我哋嚟講神經網絡嘅起源同早期發展。"
            "呢個係人工智能同神經科學嘅交界，"
            "亦都係理解大腦係咪計算機嘅關鍵。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_history(self):
        heading = self.make_heading("McCulloch & Pitts (1943)")
        year_box = self.make_box("1943", C_ORANGE, width=2.0, height=0.7)
        year_box.shift(UP * 1.5)
        authors = self.zh("McCulloch & Pitts", font_size=28, color=C_GREEN)
        authors.next_to(year_box, DOWN, buff=0.4)
        idea = self.zh(
            "問題可以透過可修改嘅網絡連接嚟解決",
            font_size=22, color=C_CYAN,
        )
        idea.next_to(authors, DOWN, buff=0.5)
        paper = self.mono(
            "A logical calculus of the ideas immanent in nervous activity",
            font_size=16, color=C_DIM,
        )
        paper.next_to(idea, DOWN, buff=0.4)
        with self.voiceover(
            text="一九四三年，McCulloch 同 Pitts 發表咗一篇劃時代嘅論文。"
            "佢哋提出，好多問題可以透過可修改嘅網絡連接嚟解決。"
            "呢個就係人工神經網絡嘅理論起點。"
            "佢哋用邏輯閘嚟模擬神經元，"
            "證明咗呢啲簡單單元組成嘅網絡可以執行複雜嘅計算。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(year_box), run_time=0.5)
            self.play(FadeIn(authors), run_time=0.5)
            self.play(FadeIn(idea), run_time=0.6)
            self.play(FadeIn(paper), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_key_attributes(self):
        heading = self.make_heading("人工神經網絡嘅關鍵特徵")
        attr1 = self.make_box("試錯學習", C_GREEN, width=4.0, height=0.7)
        attr2 = self.make_box("成功時獲得獎勵", C_ORANGE, width=4.0, height=0.7)
        attr3 = self.make_box("唔需要事先知道答案", C_CYAN, width=4.0, height=0.7)
        attrs = VGroup(attr1, attr2, attr3).arrange(DOWN, buff=0.4).shift(UP * 0.3)
        note = self.zh(
            "呢啲特徵同生物學習好相似",
            font_size=20, color=C_YELLOW,
        ).next_to(attrs, DOWN, buff=0.5)
        with self.voiceover(
            text="人工神經網絡有一個好重要嘅特徵："
            "佢哋透過試錯嚟學習，成功嘅時候會獲得獎勵。"
            "最關鍵嘅係，佢哋唔需要事先知道答案。"
            "呢個同生物嘅學習方式好相似。"
            "動物都係透過嘗試、失敗、再嘗試嚟適應環境，"
            "而唔係用邏輯規則嚟計算。"
        ):
            self.play(Write(heading), run_time=0.6)
            for a in attrs:
                self.play(FadeIn(a, shift=RIGHT * 0.2), run_time=0.5)
            self.play(FadeIn(note), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_failure_to_take_off(self):
        heading = self.make_heading("信用分配問題 Credit Assignment")
        problem_box = self.make_box("點樣提供反饋？", C_RED, width=5.0, height=0.9)
        problem_box.shift(UP * 1.0)
        explain = self.zh(
            "網絡有好多層、好多權重。當輸出錯咗，"
            "點樣知道邊個權重要改？邊個要負責任？",
            font_size=22, color=C_WHITE,
        )
        explain.next_to(problem_box, DOWN, buff=0.5)
        reasons = VGroup(
            self.zh("• 算法計算主導，神經網絡慢、難理解", font_size=20, color=C_DIM),
            self.zh("• 缺乏有效嘅訓練方法", font_size=20, color=C_DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(explain, DOWN, buff=0.5)
        with self.voiceover(
            text="但係人工神經網絡有一個根本問題：信用分配。"
            "當輸出錯咗，點樣知道邊個權重要改？"
            "網絡有好多層、好多連接，邊個要負責任？"
            "因為呢個問題，神經網絡一直冇辦法起飛。"
            "當時算法計算主導，神經網絡又慢又難理解，"
            "而且缺乏有效嘅訓練方法。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(problem_box), run_time=0.5)
            self.play(FadeIn(explain), run_time=0.8)
            for r in reasons:
                self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(0.3)
        self.clear()

    def scene_perceptrons(self):
        heading = self.make_heading("感知器 Perceptron")
        rosenblatt = self.make_box("Rosenblatt (1958)", C_GREEN, width=3.5, height=0.7)
        rosenblatt.shift(UP * 1.5 + LEFT * 2)
        desc = self.zh("兩層分類器", font_size=22, color=C_CYAN).next_to(rosenblatt, DOWN, buff=0.3)
        minsky = self.make_box("Minsky & Papert (1969)", C_RED, width=3.5, height=0.7)
        minsky.shift(UP * 1.5 + RIGHT * 2)
        xor = self.zh("XOR 問題：感知器無法解決", font_size=22, color=C_RED).next_to(minsky, DOWN, buff=0.3)
        xor_diagram = VGroup(
            self.zh("0 ⊕ 0 = 0", font_size=18, color=C_DIM),
            self.zh("0 ⊕ 1 = 1", font_size=18, color=C_DIM),
            self.zh("1 ⊕ 0 = 1", font_size=18, color=C_DIM),
            self.zh("1 ⊕ 1 = 0", font_size=18, color=C_DIM),
        ).arrange(DOWN, buff=0.2).shift(DOWN * 0.5)
        with self.voiceover(
            text="一九五八年，Rosenblatt 發明咗感知器。"
            "感知器係一個兩層嘅分類器，可以學習簡單嘅模式。"
            "但係一九六九年，Minsky 同 Papert 出版咗《感知器》呢本書，"
            "指出感知器有一個致命嘅限制：佢無法解決 XOR 問題。"
            "XOR 即係異或，兩個輸入唔同時輸出 1，相同時輸出 0。"
            "呢個簡單嘅邏輯運算，兩層感知器做唔到。"
            "呢個批評令神經網絡研究進入咗長達十幾年嘅寒冬。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(rosenblatt), FadeIn(minsky), run_time=0.5)
            self.play(FadeIn(desc), FadeIn(xor), run_time=0.5)
            self.play(FadeIn(xor_diagram), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  McCulloch & Pitts (1943)：可修改網絡解決問題", font_size=24, color=C_GREEN),
            self.zh("•  關鍵特徵：試錯學習、獎勵、唔使事先知答案", font_size=24, color=C_ORANGE),
            self.zh("•  信用分配問題：邊個權重要改？", font_size=24, color=C_RED),
            self.zh("•  神經網絡未能起飛：慢、難理解、缺訓練法", font_size=24, color=C_PINK),
            self.zh("•  Rosenblatt 感知器 vs Minsky & Papert XOR 批評", font_size=24, color=C_CYAN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。McCulloch 同 Pitts 提出可修改嘅網絡可以解決問題。"
            "人工神經網絡嘅關鍵特徵係試錯學習、獎勵、唔使事先知答案。"
            "信用分配問題係：當輸出錯咗，邊個權重要改？"
            "神經網絡未能起飛，因為佢哋慢、難理解、缺乏訓練方法。"
            "Rosenblatt 嘅感知器被 Minsky 同 Papert 嘅 XOR 批評打擊，"
            "令神經網絡研究進入寒冬。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：神經網絡嘅復興", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講神經網絡點樣復興，"
            "包括反向傳播、梯度下降、同埋點解大腦可能唔係噉樣運作。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
