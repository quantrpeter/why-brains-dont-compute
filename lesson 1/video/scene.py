"""
Lesson 1 – Solving Problems
Manim CE + Cantonese voiceover (Edge TTS)

Render (1080p):
    cd "lesson 1/video"
    manim render -qh scene.py SolvingProblems
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
C_DIM = "#bbbbbb"
C_CYAN = "#4dd0e1"

FONT = "Songti TC"
MONO = "Menlo"


class SolvingProblems(VoiceoverScene):
    """Single scene explaining problem-solving approaches in Cantonese."""

    def construct(self):
        self.set_speech_service(
            EdgeTTSService(
                voice="zh-HK-WanLungNeural",
                rate="-10%",
                pitch="-5Hz"
            )
        )
        self.camera.background_color = BLACK

        self.bg_image = ImageMobject("wallpaper2.avif")
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
            "香港編程學會", font_size=18, color="#ffffff"
        ).to_corner(UL, buff=0.3)
        self.add(self.watermark)

        self.book_title = self.en(
            "Why Brains Don't Compute", font_size=16, color="#ffffff"
        ).to_corner(UR, buff=0.3)
        self.add(self.book_title)

        self.scene_book_intro()
        self.scene_intro()
        self.scene_two_perspectives()
        self.scene_intelligence()
        self.scene_monty_hall()
        self.scene_artificial_intelligence()
        self.scene_common_ground()
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
        keep = {self.bg_image, self.bg_overlay, self.watermark, self.book_title}
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

    # ── Scene 0 — Book Intro ────────────────────────────────────────────

    def scene_book_intro(self):
        cover = ImageMobject("book.jpeg")
        cover.height = 4.5
        cover.shift(LEFT * 3)

        title = self.en(
            "Why Brains Don't Compute",
            font_size=32, color=C_BLUE,
        ).shift(RIGHT * 2.5 + UP * 1.5)
        author = self.en(
            "Dale Purves", font_size=26, color=C_ORANGE,
        ).next_to(title, DOWN, buff=0.35)
        publisher = self.en(
            "Springer", font_size=20, color=C_DIM,
        ).next_to(author, DOWN, buff=0.25)
        desc = self.zh(
            "呢本書探討點解人腦\n唔係一部電腦",
            font_size=24, color=C_WHITE,
        ).next_to(publisher, DOWN, buff=0.5)

        with self.voiceover(
            text="喺我哋開始之前，我想介紹一下呢個系列嘅教材。"
            "呢本書叫做《Why Brains Don't Compute》，"
            "作者係 Duke 大學嘅神經科學家 Dale Purves。"
            "佢挑戰咗一個好流行嘅假設，就係人腦唔係一部電腦。"
            "我哋會用呢本書做基礎，一課一課咁探討呢個話題。"
        ):
            self.play(FadeIn(cover, shift=RIGHT * 0.3), run_time=1.2)
            self.play(Write(title), run_time=1.0)
            self.play(FadeIn(author, shift=UP * 0.2), run_time=0.6)
            self.play(FadeIn(publisher, shift=UP * 0.2), run_time=0.4)
            self.play(FadeIn(desc, shift=UP * 0.2), run_time=0.8)

        self.wait(0.3)
        self.clear()

    # ── Scene 1 — Intro ─────────────────────────────────────────────────

    def scene_intro(self):
        title = self.zh("解決問題", font_size=56, color=C_BLUE)
        sub_en = self.en(
            "Solving Problems", font_size=24, color=C_WHITE
        ).next_to(title, DOWN, buff=0.4)
        sub_zh = self.zh(
            "第一課", font_size=36, color=C_ORANGE
        ).next_to(sub_en, DOWN, buff=0.3)
        producer = self.zh(
            "制片人：Peter", font_size=24, color=C_DIM
        ).next_to(sub_zh, DOWN, buff=0.7)

        with self.voiceover(
            text="歡迎嚟到《Why Brains Don't Compute》第一課。"
            "今日我哋會探討解決問題嘅兩種方式："
            "用邏輯規則同埋用經驗試錯。"
            "呢個區別會影響我哋點樣理解人工智能同埋生物智慧。"
        ):
            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(sub_en, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(sub_zh, shift=UP * 0.2), run_time=0.8)
            self.play(FadeIn(producer, shift=UP * 0.2), run_time=0.5)

        self.wait(0.3)
        self.clear()

    # ── Scene 2 — Two Perspectives ──────────────────────────────────────

    def scene_two_perspectives(self):
        heading = self.make_heading("解決問題嘅兩種方式")

        algo_box = self.make_box("演算法方式", C_GREEN, width=3.5, height=1.0)
        algo_box.shift(LEFT * 2.5 + UP * 0.5)
        algo_desc = self.zh(
            "跟住規則、邏輯推演\n例如：數學證明、程式編寫",
            font_size=22, color=C_DIM,
        ).next_to(algo_box, DOWN, buff=0.4)

        emp_box = self.make_box("經驗方式", C_ORANGE, width=3.5, height=1.0)
        emp_box.shift(RIGHT * 2.5 + UP * 0.5)
        emp_desc = self.zh(
            "試錯、反覆嘗試\n例如：學行路、識人樣",
            font_size=22, color=C_DIM,
        ).next_to(emp_box, DOWN, buff=0.4)

        vs_label = self.zh("vs", font_size=36, color=C_WHITE).shift(UP * 0.5)

        with self.voiceover(
            text="解決問題有兩種方式。"
            "第一種係演算法方式。跟住規則、用邏輯推演，好似數學證明同程式編寫。"
            "第二種係經驗方式。靠試錯、反覆嘗試，好似學行路、識人樣。"
            "電腦科學家偏向用演算法，神經科學家偏向研究經驗學習。"
            "呢兩種方式其實唔係對立，而係唔同嘅工具。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(DrawBorderThenFill(algo_box), FadeIn(algo_desc, shift=DOWN * 0.2), run_time=1.0)
            self.play(DrawBorderThenFill(emp_box), FadeIn(emp_desc, shift=DOWN * 0.2), run_time=1.0)
            self.play(SpinInFromNothing(vs_label), run_time=0.8)

        self.wait(0.3)
        self.clear()

    # ── Scene 3 — Intelligence ───────────────────────────────────────────

    def scene_intelligence(self):
        heading = self.make_heading("邏輯思考唔係人類強項")

        points = VGroup(
            self.zh("•  人類唔擅長純粹邏輯推理", font_size=26, color=C_GREEN),
            self.zh("•  好多人都會犯系統性錯誤", font_size=26, color=C_ORANGE),
            self.zh("•  例如乘法偏見、概率直覺", font_size=26, color=C_PINK),
            self.zh("•  經驗同直覺往往比邏輯更準", font_size=26, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)

        with self.voiceover(
            text="好多人以為人類好叻邏輯思考，其實唔係。"
            "人類唔擅長純粹邏輯推理，好多人都會犯系統性錯誤。"
            "例如乘法偏見、概率直覺，好多人都會估錯。"
            "反而經驗同直覺，喺好多情況下比邏輯更準。"
            "呢個就係點解 Monty Hall 問題咁難。"
        ):
            self.play(Write(heading), run_time=0.6)
            for p in points:
                self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.3)
        self.clear()

    # ── Scene 4 — Monty Hall ─────────────────────────────────────────────

    def scene_monty_hall(self):
        heading = self.make_heading("Monty Hall 問題")

        doors = VGroup()
        for i, label in enumerate(["門 1", "門 2", "門 3"]):
            rect = RoundedRectangle(
                corner_radius=0.1, width=1.2, height=1.5,
                fill_color=C_DIM, fill_opacity=0.3, stroke_color=C_WHITE,
            ).shift(LEFT * 2.5 + RIGHT * i * 2.5 + DOWN * 0.3)
            txt = self.zh(label, font_size=24).move_to(rect)
            doors.add(VGroup(rect, txt))

        setup = self.zh(
            "三扇門，一扇有車，兩扇有羊。你揀門 1，主持人開咗門 3 係羊。",
            font_size=22, color=C_WHITE,
        ).shift(UP * 1.8)

        question = self.zh(
            "換唔換門？",
            font_size=32, color=C_YELLOW,
        ).shift(DOWN * 1.5)

        answer = self.zh(
            "換！換門贏嘅概率係 2/3，唔換就係 1/3",
            font_size=24, color=C_GREEN,
        ).shift(DOWN * 2.0)

        with self.voiceover(
            text="Monty Hall 問題係經典嘅概率謎題。"
            "三扇門，一扇有車，兩扇有羊。你揀咗門 1，主持人開咗門 3 係羊。"
            "換唔換門？好多人都會話唔換，因為剩低兩扇門好似一樣。"
            "其實換門贏嘅概率係三分之二，唔換就係三分之一。"
            "呢個結果違反直覺，所以好多人都估錯。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(setup), run_time=0.8)
            self.play(
                LaggedStart(*[GrowFromCenter(d) for d in doors], lag_ratio=0.2),
                run_time=1.2
            )
            self.play(Write(question), run_time=0.6)
            self.play(Indicate(question, color=C_RED), run_time=0.8)
            self.play(FadeIn(answer, shift=UP * 0.2), run_time=1)

        self.wait(0.3)
        self.clear()

    # ── Scene 5 — Artificial Intelligence ───────────────────────────────

    def scene_artificial_intelligence(self):
        heading = self.make_heading("人工智能唔等於腦係電腦")

        ai_box = self.make_box("AI 成功", C_GREEN, width=4, height=0.9)
        ai_box.shift(UP * 2.0)
        ai_desc = self.zh(
            "AlphaGo、ChatGPT 好勁，\n但係用嘅係演算法同經驗學習",
            font_size=20, color=C_DIM,
        ).next_to(ai_box, DOWN, buff=0.25)

        brain_box = self.make_box("腦唔係電腦", C_ORANGE, width=4, height=0.9)
        brain_box.shift(DOWN * 2.0)
        brain_desc = self.zh(
            "人腦冇明確目標函數、冇程式碼，\n係靠進化同經驗",
            font_size=20, color=C_DIM,
        ).next_to(brain_box, DOWN, buff=0.25)

        arrow = Arrow(
            ai_desc.get_bottom() + DOWN * 0.1, brain_box.get_top() + UP * 0.1,
            buff=0, color=C_WHITE, stroke_width=3,
        )
        arrow_label = self.zh("唔可以推論", font_size=20, color=C_GREEN).next_to(arrow, RIGHT, buff=0.4)

        with self.voiceover(
            text="AI 成功唔代表腦係電腦。"
            "AlphaGo、ChatGPT 好勁，但佢哋用嘅係演算法同經驗學習嘅結合。"
            "腦係唔同嘅。腦冇明確嘅目標函數、冇程式碼，係靠進化同經驗慢慢形成。"
            "所以唔可以話 AI 成功就證明腦係電腦。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(DrawBorderThenFill(ai_box), FadeIn(ai_desc, shift=DOWN * 0.2), run_time=1.0)
            self.play(GrowArrow(arrow), FadeIn(arrow_label, shift=LEFT * 0.2), run_time=0.8)
            self.play(DrawBorderThenFill(brain_box), FadeIn(brain_desc, shift=UP * 0.2), run_time=1.0)

        self.wait(0.3)
        self.clear()

    # ── Scene 6 — Common Ground ──────────────────────────────────────────

    def scene_common_ground(self):
        heading = self.make_heading("共同嘅定義")

        def_box = self.make_box("問題", C_BLUE, width=5, height=0.8)
        def_box.shift(UP * 0.8)
        def_text = self.zh(
            "要達致嘅目標同埋阻礙嘅因素",
            font_size=22, color=C_WHITE,
        ).next_to(def_box, DOWN, buff=0.25)

        machine_box = self.make_box("機器", C_PURPLE, width=5, height=0.8)
        machine_box.shift(DOWN * 0.8)
        machine_text = self.zh(
            "執行任務嘅系統，唔係一定要係電腦",
            font_size=22, color=C_WHITE,
        ).next_to(machine_box, DOWN, buff=0.25)

        warning = self.zh(
            "小心：唔好將車放喺馬前面 — 唔好假設腦係電腦先",
            font_size=20, color=C_RED,
        ).shift(DOWN * 2.2)

        with self.voiceover(
            text="要搵共同嘅討論基礎，我哋先定義兩個概念。"
            "問題，就係要達致嘅目標同埋阻礙嘅因素。"
            "機器，就係執行任務嘅系統，唔係一定要係電腦。"
            "腦都可以係一種機器。但係要小心，唔好將車放喺馬前面。"
            "唔好假設腦係電腦，然後再去搵證據。"
        ):
            self.play(Write(heading), run_time=0.6)
            self.play(FadeIn(def_box), FadeIn(def_text), run_time=0.8)
            self.play(FadeIn(machine_box), FadeIn(machine_text), run_time=0.8)
            self.play(FadeIn(warning, shift=UP * 0.2), run_time=0.8)

        self.wait(0.3)
        self.clear()

    # ── Scene 7 — Summary ───────────────────────────────────────────────

    def scene_summary(self):
        heading = self.make_heading("總結", font_size=44)

        bullets = VGroup(
            self.zh("•  解決問題有兩種方式：演算法同經驗", font_size=26, color=C_GREEN),
            self.zh("•  人類唔擅長純粹邏輯推理", font_size=26, color=C_ORANGE),
            self.zh("•  Monty Hall 問題顯示直覺會出錯", font_size=26, color=C_PINK),
            self.zh("•  AI 成功唔代表腦係電腦", font_size=26, color=C_PURPLE),
            self.zh("•  要定義清楚「問題」同「機器」先討論", font_size=26, color=C_CYAN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)

        with self.voiceover(
            text="總結一下今日學咗嘅嘢。"
            "解決問題有兩種方式：演算法同經驗。"
            "人類唔擅長純粹邏輯推理，Monty Hall 問題就顯示直覺會出錯。"
            "AI 成功唔代表腦係電腦。"
            "討論之前要定義清楚「問題」同「機器」呢兩個概念。"
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
            text="多謝收睇！下一課我哋會講客觀同主觀現實，"
            "探討物理世界同我哋感知嘅世界有咩唔同。記得繼續跟住學喇！"
        ):
            self.play(Write(thanks), run_time=1)

        self.wait(1)
        self.play(FadeOut(thanks), run_time=0.8)
