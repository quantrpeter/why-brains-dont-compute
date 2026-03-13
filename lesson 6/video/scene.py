"""
Lesson 6 – Resurrection of Neural Networks
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 6/video"
    manim render -qh scene.py ResurrectionExplainer
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


class ResurrectionExplainer(VoiceoverScene):
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
        self.scene_back_propagation()
        self.scene_gradient_descent()
        self.scene_biological_implausibility()
        self.scene_unsupervised_credit()
        self.scene_search_spaces()
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
        title = self.zh("神經網絡嘅復興", font_size=56, color=C_BLUE)
        sub_en = self.en("Resurrection of Neural Networks", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第六課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第六課。"
            "上課講咗神經網絡點樣陷入寒冬。"
            "今日我哋會講佢哋點樣復興，"
            "同埋呢個復興對理解大腦有咩啟示。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_back_propagation(self):
        heading = self.make_heading("反向傳播 Backpropagation")
        werbos = self.make_box("Werbos 1974", C_GREEN, width=3.0, height=0.7)
        werbos.shift(UP * 1.2 + LEFT * 2.5)
        rumelhart = self.make_box("Rumelhart & McClelland 1986", C_ORANGE, width=4.0, height=0.7)
        rumelhart.shift(UP * 1.2 + RIGHT * 2.5)
        desc = self.zh(
            "透過鏈式法則，將誤差從輸出層反向傳播到每一層",
            font_size=20, color=C_CYAN,
        )
        desc.next_to(rumelhart, DOWN, buff=0.6)
        book = self.mono("Parallel Distributed Processing", font_size=16, color=C_DIM).next_to(desc, DOWN, buff=0.3)
        with self.voiceover(
            text="神經網絡復興嘅關鍵係反向傳播算法。"
            "一九七四年，Werbos 喺博士論文入面已經提出咗呢個概念。"
            "但係真正令佢普及嘅係一九八六年 Rumelhart 同 McClelland 嘅著作"
            "《並行分佈處理》。"
            "反向傳播透過鏈式法則，將輸出層嘅誤差一路傳返去每一層，"
            "令我哋知道每個權重要點樣調整。"
            "呢個就解決咗信用分配問題。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(werbos), FadeIn(rumelhart), run_time=0.6)
            self.play(FadeIn(desc), run_time=0.6)
            self.play(FadeIn(book), run_time=0.4)
        self.wait(0.3)
        self.clear()

    def scene_gradient_descent(self):
        heading = self.make_heading("梯度下降 Gradient Descent")
        flow = VGroup(
            self.make_box("計算誤差", C_RED, width=3.5, height=0.6),
            self.make_box("反向傳播梯度", C_ORANGE, width=3.5, height=0.6),
            self.make_box("更新權重", C_GREEN, width=3.5, height=0.6),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.5)
        arrows = VGroup()
        for i in range(len(flow) - 1):
            a = Arrow(flow[i].get_bottom(), flow[i + 1].get_top(), buff=0.1, color=C_WHITE, stroke_width=2)
            arrows.add(a)
        note = self.zh(
            "沿住梯度下降方向，逐步減少誤差",
            font_size=20, color=C_YELLOW,
        ).next_to(flow, DOWN, buff=0.5)
        with self.voiceover(
            text="梯度下降係反向傳播嘅核心。"
            "首先計算輸出同目標之間嘅誤差。"
            "然後反向傳播，計算每個權重對誤差嘅貢獻。"
            "最後沿住梯度下降嘅方向更新權重。"
            "每一步都令誤差減少少少，"
            "重複好多遍之後，網絡就會學到正確嘅映射。"
        ):
            self.play(Write(heading), run_time=0.6)
            for i, f in enumerate(flow):
                self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.4)
                if i < len(arrows):
                    self.play(GrowArrow(arrows[i]), run_time=0.25)
            self.play(FadeIn(note), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_biological_implausibility(self):
        heading = self.make_heading("生物學上嘅不可信")
        req1 = self.make_box("需要已知答案（監督學習）", C_RED, width=5.0, height=0.7)
        req1.shift(UP * 1.0)
        req2 = self.make_box("需要精確嘅權重反向規格", C_RED, width=5.0, height=0.7)
        req2.next_to(req1, DOWN, buff=0.4)
        conclusion = self.zh(
            "大腦冇標籤數據，亦冇反向傳播嘅神經機制",
            font_size=22, color=C_YELLOW,
        ).next_to(req2, DOWN, buff=0.5)
        with self.voiceover(
            text="但係反向傳播有一個好大嘅問題：佢生物學上唔可信。"
            "第一，反向傳播需要已知嘅正確答案，即係監督學習。"
            "但係大腦學習嘅時候，邊個嚟提供標籤？"
            "第二，反向傳播需要精確嘅權重反向規格，"
            "即係每個突觸都要知道佢對輸出嘅貢獻。"
            "神經科學到而家都未發現大腦有呢種機制。"
            "所以，就算人工神經網絡好成功，"
            "都唔代表大腦係噉樣運作嘅。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(req1), run_time=0.5)
            self.play(FadeIn(req2), run_time=0.5)
            self.play(FadeIn(conclusion), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_unsupervised_credit(self):
        heading = self.make_heading("無監督嘅信用分配")
        evolution = self.make_box("進化 = 監督者", C_GREEN, width=4.0, height=0.8)
        evolution.shift(UP * 1.2)
        reward = self.zh("生存、繁殖 = 獎勵信號", font_size=22, color=C_ORANGE)
        reward.next_to(evolution, DOWN, buff=0.4)
        genetic = self.zh("遺傳算法、強化學習：試錯 + 獎勵", font_size=20, color=C_CYAN)
        genetic.next_to(reward, DOWN, buff=0.4)
        with self.voiceover(
            text="咁大腦點樣學習呢？"
            "答案可能係：進化就係監督者。"
            "生存同繁殖就係獎勵信號。"
            "唔使有人話你知答案係咩，"
            "只要試錯、成功嘅話就繁殖多啲，失敗就少啲。"
            "遺傳算法同強化學習都係呢個思路："
            "試錯加獎勵，唔使標籤數據。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(evolution), run_time=0.5)
            self.play(FadeIn(reward), run_time=0.5)
            self.play(FadeIn(genetic), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_search_spaces(self):
        heading = self.make_heading("搜索空間 Search Spaces")
        small = self.make_box("細空間 ~10¹⁰", C_GREEN, width=3.5, height=0.7)
        small.shift(UP * 1.0 + LEFT * 2.5)
        small_note = self.zh("適合算法", font_size=18, color=C_DIM).next_to(small, DOWN, buff=0.2)
        large = self.make_box("大空間 ~10¹⁰⁰⁺", C_RED, width=3.5, height=0.7)
        large.shift(UP * 1.0 + RIGHT * 2.5)
        large_note = self.zh("需要經驗主義", font_size=18, color=C_DIM).next_to(large, DOWN, buff=0.2)
        conclusion = self.zh(
            "現實世界嘅搜索空間巨大，算法無法窮舉，必須試錯",
            font_size=20, color=C_YELLOW,
        ).next_to(small_note, DOWN, buff=0.8)
        with self.voiceover(
            text="最後講下搜索空間。"
            "當搜索空間比較細，例如十嘅十次方，"
            "算法可以窮舉或者用規則嚟解決。"
            "但係當搜索空間好大，例如十嘅一百次方或者更大，"
            "算法就做唔到喇。"
            "呢啲巨大嘅空間必須用經驗主義：試錯、學習、適應。"
            "現實世界嘅問題，搜索空間往往係天文數字，"
            "所以大腦同成功嘅 AI 都係用試錯，而唔係算法。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(small), FadeIn(large), run_time=0.5)
            self.play(FadeIn(small_note), FadeIn(large_note), run_time=0.4)
            self.play(FadeIn(conclusion), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  反向傳播：Werbos 1974，Rumelhart 1986", font_size=24, color=C_GREEN),
            self.zh("•  梯度下降：誤差 → 反向傳播 → 更新權重", font_size=24, color=C_ORANGE),
            self.zh("•  生物學不可信：要已知答案、要權重反向規格", font_size=24, color=C_RED),
            self.zh("•  無監督信用：進化 = 監督，生存 = 獎勵", font_size=24, color=C_PINK),
            self.zh("•  大搜索空間必須用經驗主義、試錯", font_size=24, color=C_CYAN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。反向傳播由 Werbos 同 Rumelhart 等人普及。"
            "梯度下降透過誤差、反向傳播、更新權重嚟訓練網絡。"
            "但係反向傳播生物學上不可信，需要已知答案同權重反向規格。"
            "大腦可能用無監督嘅方式：進化做監督，生存做獎勵。"
            "當搜索空間好大，必須用經驗主義、試錯，而唔係算法。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：經驗學習", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會講經驗學習，"
            "從魔方到 AlphaGo，睇下試錯點樣戰勝算法。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
