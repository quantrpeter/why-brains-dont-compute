"""
Lesson 7 – Learning Empirically
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 7/video"
    manim render -qh scene.py LearningEmpiricallyExplainer
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


class LearningEmpiricallyExplainer(VoiceoverScene):
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
        self.scene_rubiks_cube()
        self.scene_game_complexity()
        self.scene_alphago()
        self.scene_implications()
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
        title = self.zh("經驗學習", font_size=56, color=C_BLUE)
        sub_en = self.en("Learning Empirically", font_size=24, color=C_WHITE).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh("第七課", font_size=36, color=C_ORANGE).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh("制片人：Peter", font_size=24, color=C_DIM).next_to(sub_zh, DOWN, buff=0.7)
        with self.voiceover(
            text="大家好！歡迎嚟到第七課。"
            "今日我哋會睇下遊戲點樣證明經驗學習嘅威力，"
            "從魔方到圍棋，從算法到試錯。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_rubiks_cube(self):
        heading = self.make_heading("魔方：算法嘅勝利")
        cube = self.make_box("魔方 Rubik's Cube", C_ORANGE, width=4.0, height=0.8)
        cube.shift(UP * 1.2)
        states = self.mono("~10¹⁹ 狀態", font_size=24, color=C_CYAN)
        states.next_to(cube, DOWN, buff=0.3)
        algo = self.zh("簡單算法，20 步內解決", font_size=22, color=C_GREEN)
        algo.next_to(states, DOWN, buff=0.4)
        note = self.zh(
            "搜索空間雖然大，但結構簡單，算法可以征服",
            font_size=18, color=C_DIM,
        ).next_to(algo, DOWN, buff=0.4)
        with self.voiceover(
            text="魔方有大約十嘅十九次方個狀態。"
            "聽落好恐怖，但係魔方有一個簡單嘅算法，"
            "可以喺二十步之內解決。"
            "因為魔方嘅結構相對簡單，"
            "搜索空間雖然大，但係算法仍然可以征服。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(cube), run_time=0.5)
            self.play(FadeIn(states), run_time=0.4)
            self.play(FadeIn(algo), run_time=0.5)
            self.play(FadeIn(note), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_game_complexity(self):
        heading = self.make_heading("遊戲樹複雜度")
        games = [
            ("井字棋", "10⁴", C_GREEN),
            ("跳棋", "10²⁰", C_ORANGE),
            ("國際象棋", "10¹²⁰", C_PINK),
            ("圍棋", "10³²⁰", C_RED),
        ]
        rows = VGroup()
        for name, complexity, col in games:
            row = VGroup(
                self.zh(name, font_size=22, color=col),
                self.mono(complexity, font_size=22, color=col),
            ).arrange(RIGHT, buff=1.5)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(UP * 0.3)
        conclusion = self.zh(
            "圍棋嘅搜索空間大過宇宙原子數量",
            font_size=20, color=C_YELLOW,
        ).next_to(rows, DOWN, buff=0.5)
        with self.voiceover(
            text="但係棋類遊戲就唔同喇。"
            "井字棋嘅遊戲樹大約十嘅四次方。"
            "跳棋係十嘅二十次方。"
            "國際象棋係十嘅一百二十次方。"
            "圍棋更加誇張，十嘅三百二十次方。"
            "圍棋嘅搜索空間大過宇宙入面嘅原子數量。"
            "呢啲遊戲，算法根本無法窮舉。"
        ):
            self.play(Write(heading), run_time=0.6)
            for r in rows:
                self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.4)
            self.play(FadeIn(conclusion), run_time=0.5)
        self.wait(0.3)
        self.clear()

    def scene_alphago(self):
        heading = self.make_heading("Deep Blue vs AlphaGo")
        deepblue = self.make_box("Deep Blue (1997)", C_ORANGE, width=3.5, height=0.7)
        deepblue.shift(UP * 1.2 + LEFT * 2.5)
        db_desc = self.zh("暴力搜索 + 專家規則", font_size=18, color=C_DIM).next_to(deepblue, DOWN, buff=0.2)
        alphago = self.make_box("AlphaGo / AlphaZero", C_GREEN, width=3.5, height=0.7)
        alphago.shift(UP * 1.2 + RIGHT * 2.5)
        ag_desc = self.zh("純自我對弈強化學習", font_size=18, color=C_DIM).next_to(alphago, DOWN, buff=0.2)
        contrast = self.zh(
            "AlphaZero：零人類知識，純試錯，打敗所有棋類冠軍",
            font_size=20, color=C_CYAN,
        ).next_to(db_desc, DOWN, buff=0.6)
        with self.voiceover(
            text="一九九七年，Deep Blue 擊敗國際象棋世界冠軍。"
            "Deep Blue 用嘅係暴力搜索加專家規則，"
            "即係人類高手寫嘅評估函數。"
            "但係 AlphaGo 同 AlphaZero 完全唔同。"
            "AlphaZero 用純自我對弈嘅強化學習，"
            "零人類知識，完全靠試錯。"
            "佢唔單止打敗圍棋冠軍，"
            "仲可以學識國際象棋同日本將棋，"
            "打敗所有棋類嘅冠軍。"
            "呢個就係經驗學習嘅威力。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(deepblue), FadeIn(alphago), run_time=0.5)
            self.play(FadeIn(db_desc), FadeIn(ag_desc), run_time=0.4)
            self.play(FadeIn(contrast), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_implications(self):
        heading = self.make_heading("對神經科學嘅啟示")
        impl1 = self.zh("現實世界嘅搜索空間比棋盤大得多", font_size=22, color=C_GREEN)
        impl1.shift(UP * 1.0)
        impl2 = self.zh("大腦面對嘅係感知、決策、語言嘅巨大空間", font_size=22, color=C_ORANGE)
        impl2.next_to(impl1, DOWN, buff=0.4)
        impl3 = self.zh("算法無法處理 → 大腦必須用經驗主義運作", font_size=22, color=C_CYAN)
        impl3.next_to(impl2, DOWN, buff=0.4)
        with self.voiceover(
            text="呢個對神經科學有咩啟示呢？"
            "現實世界嘅搜索空間比棋盤大得多。"
            "大腦面對嘅係感知、決策、語言嘅巨大空間。"
            "呢啲空間算法根本無法處理。"
            "所以大腦必須用經驗主義嚟運作："
            "試錯、學習、適應，而唔係計算。"
            "AI 喺複雜遊戲嘅成功，"
            "正正證明咗經驗學習喺巨大搜索空間嘅優勢。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(impl1), run_time=0.5)
            self.play(FadeIn(impl2), run_time=0.5)
            self.play(FadeIn(impl3), run_time=0.6)
        self.wait(0.3)
        self.clear()

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)
        bullets = VGroup(
            self.zh("•  魔方 ~10¹⁹：算法可解決", font_size=24, color=C_GREEN),
            self.zh("•  棋類：井字 10⁴ → 象棋 10¹²⁰ → 圍棋 10³²⁰", font_size=24, color=C_ORANGE),
            self.zh("•  Deep Blue：暴力 + 專家規則", font_size=24, color=C_PINK),
            self.zh("•  AlphaGo/AlphaZero：純試錯，零人類知識", font_size=24, color=C_CYAN),
            self.zh("•  現實空間更大 → 大腦必須經驗主義", font_size=24, color=C_YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        with self.voiceover(
            text="總結一下。魔方雖然有十嘅十九次方個狀態，但算法可以解決。"
            "棋類遊戲嘅複雜度由井字棋嘅十嘅四次方，"
            "到國際象棋嘅十嘅一百二十次方，"
            "到圍棋嘅十嘅三百二十次方。"
            "Deep Blue 用暴力搜索加專家規則。"
            "AlphaGo 同 AlphaZero 用純試錯，零人類知識。"
            "現實世界嘅搜索空間更大，所以大腦必須用經驗主義運作。"
        ):
            self.play(Write(heading), run_time=0.6)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.clear()

    def scene_outro(self):
        thanks = self.zh("多謝收睇！", font_size=52, color=C_YELLOW)
        next_text = self.zh("下一課：我哋感知啲咩", font_size=28, color=C_CYAN).next_to(thanks, DOWN, buff=0.5)
        with self.voiceover(
            text="多謝收睇！"
            "下一課我哋會進入感知嘅部分，"
            "探討我哋究竟感知啲咩，同點解。"
            "記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)
            self.play(FadeIn(next_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(thanks), FadeOut(next_text), run_time=0.8)
