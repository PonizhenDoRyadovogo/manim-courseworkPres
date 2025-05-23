from manim import *  # or: from manimlib import *

from manim import MarkupText
from manim_slides.slide import Slide
import random

class FourGridPlotsCustom(Slide):
    def make_axes_group(self, cfg, y_label_text):
        axes = Axes(
            x_range=cfg["x_range"],
            y_range=cfg["y_range"],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        # подписи осей
        x_lab = MathTex("N", color="#343434")\
            .scale(0.75)\
            .next_to(axes.x_axis.get_end(), RIGHT * 0.3 + DOWN * 0.1)
        y_lab = MathTex(y_label_text, color="#343434")\
            .scale(0.75)\
            .next_to(axes.y_axis.get_end(), LEFT * 1.5)
        # метки по Y
        y_ticks = VGroup(*[
            MathTex(f"{v:.1f}", color="#343434").scale(0.75)
                .next_to(axes.c2p(0, v), LEFT * 3, buff=0.05)
            for v in np.arange(*cfg["y_range"])
        ])
        # метки по X
        x_ticks = VGroup(*[
            MathTex(str(int(x)), color="#343434").scale(0.75)
                .next_to(axes.x_axis.n2p(x), DOWN * 3, buff=0.05)
            for x in np.arange(*cfg["x_range"]) if x != 0
        ])
        group = VGroup(axes, x_lab, y_lab, y_ticks, x_ticks)
        return group, axes

    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))

        # 1) Параметры для четырёх графиков
        configs = [
            {"x_range": (0, 1050, 100), "y_range": (23, 26, 0.5)},
            {"x_range": (0, 1050, 100), "y_range": (51, 54, 0.5)},
            {"x_range": (0, 1050, 100), "y_range": (53, 57, 0.5)},
            {"x_range": (0, 1050, 100), "y_range": (66, 70, 0.5)},
        ]
        y_labels = ["\hat{T_1}", "\hat{T_2}", "\hat{T_3}", "\hat{T_4}"]
        x_vals = list(range(50, 1001, 50))
        y_vals_list = [
            [24.3, 24.35, 24.35, 24.5, 24.15, 24.1, 23.9, 24.2,
             24.15, 24.2, 23.9, 24.35, 23.9, 24.05, 23.8, 24.05,
             23.95, 24.15, 24.1, 24.1],
            [52.56, 52.38, 51.98, 52.20, 52.22, 52.28, 51.85, 52.40,
             51.85, 52.22, 52.28, 52.15, 52.23, 52.05, 52.30, 52.30,
             52.15, 52.10, 52.03, 52.02],
            [56.4, 53.85, 55.80, 55.60, 55.20, 54.90, 55.70, 55.70,
             54.85, 55.10, 55.05, 54.95, 55.27, 55.40, 55.35, 55.35,
             55.15, 55.20, 55.10, 55.15],
            [66.75, 69.40, 67.85, 67.70, 68.45, 68.75, 68.55, 68.55,
             69.20, 68.55, 68.75, 68.65, 68.55, 68.45, 68.70, 68.75,
             68.30, 68.30, 68.75, 68.80],
        ]

        # 2) Делаем по 4 группы осей
        axes_groups = []
        axes_objects = []
        for cfg, lab in zip(configs, y_labels):
            group, axes = self.make_axes_group(cfg, lab)
            axes_groups.append(group)
            axes_objects.append(axes)

        # 3) Уменьшаем их и раскладываем в 2×2
        grid = VGroup(*axes_groups)
        grid.scale(0.5).arrange_in_grid(rows=2, cols=2, buff=1.0)
        # сдвигаем левый столбец чуть вправо
        for i in (0, 2):
            grid[i].shift(RIGHT * 0.3)

        # 4) Анимируем появление осей + меток
        self.play(*[Create(g) for g in grid], run_time=2.0)

        title_graph_1 = MarkupText("<i>График зависимости</i>", font_size=15, fill_color="#343434")
        title_graph_1.next_to(grid[0], UP, buff=0).shift(LEFT)
        title_graph_1_t = MathTex(r"\hat{T_1}", fill_color="#343434").scale(0.4).next_to(title_graph_1, RIGHT, buff=0.1)
        title_graph_1_continus = Text("от", font_size=15, fill_color="#343434").next_to(title_graph_1_t, RIGHT,
                                                                                        buff=0.1)
        title_graph_1_n = MathTex(r"N", fill_color="#343434").scale(0.4).next_to(title_graph_1_continus, RIGHT,
                                                                                 buff=0.1)
        title_chart_1 = VGroup(title_graph_1, title_graph_1_t, title_graph_1_n, title_graph_1_continus)

        title_graph_2 = MarkupText("<i>График зависимости</i>", font_size=15, fill_color="#343434")
        title_graph_2.next_to(grid[1], UP, buff=0).shift(LEFT)
        title_graph_2_t = MathTex(r"\hat{T_2}", fill_color="#343434").scale(0.4).next_to(title_graph_2, RIGHT, buff=0.1)
        title_graph_2_continus = Text("от", font_size=15, fill_color="#343434").next_to(title_graph_2_t, RIGHT,
                                                                                        buff=0.1)
        title_graph_2_n = MathTex(r"N", fill_color="#343434").scale(0.4).next_to(title_graph_2_continus, RIGHT,
                                                                                 buff=0.1)
        title_chart_2 = VGroup(title_graph_2, title_graph_2_t, title_graph_2_continus, title_graph_2_n)

        title_graph_3 = MarkupText("<i>График зависимости</i>", font_size=15, fill_color="#343434")
        title_graph_3.next_to(grid[2], UP, buff=0).shift(LEFT)
        title_graph_3_t = MathTex(r"\hat{T_3}", fill_color="#343434").scale(0.4).next_to(title_graph_3, RIGHT, buff=0.1)
        title_graph_3_continus = Text("от", font_size=15, fill_color="#343434").next_to(title_graph_3_t, RIGHT,
                                                                                        buff=0.1)
        title_graph_3_n = MathTex(r"N", fill_color="#343434").scale(0.4).next_to(title_graph_3_continus, RIGHT,
                                                                                 buff=0.1)
        title_chart_3 = VGroup(title_graph_3, title_graph_3_t, title_graph_3_continus, title_graph_3_n)

        title_graph_4 = MarkupText("<i>График зависимости</i>", font_size=15, fill_color="#343434")
        title_graph_4.next_to(grid[3], UP, buff=0).shift(LEFT)
        title_graph_4_t = MathTex(r"\hat{T_4}", fill_color="#343434").scale(0.4).next_to(title_graph_4, RIGHT, buff=0.1)
        title_graph_4_continus = Text("от", font_size=15, fill_color="#343434").next_to(title_graph_4_t, RIGHT,
                                                                                        buff=0.1)
        title_graph_4_n = MathTex(r"N", fill_color="#343434").scale(0.4).next_to(title_graph_4_continus, RIGHT,
                                                                                 buff=0.1)
        title_chart_4 = VGroup(title_graph_4, title_graph_4_t, title_graph_4_continus, title_graph_4_n)

        self.play(Write(title_chart_1), Write(title_chart_2), Write(title_chart_3), Write(title_chart_4), run_time=2)

        # 5) Падающие точки
        all_dots = []
        for axes, y_vals in zip(axes_objects, y_vals_list):
            # для каждой точки рисуем её чуть выше, скрываем, а потом «падаем»
            for x, y in zip(x_vals, y_vals):
                start = axes.c2p(x, y) + UP * 1.2  # точка изначально выше
                dot = Dot(start, radius=0.03, color="#343434")
                dot.set_opacity(0)
                self.add(dot)
                all_dots.append(dot)
                # одновременно делаем видимой и перемещаем на своё место
                self.play(
                    dot.animate.set_opacity(1).move_to(axes.c2p(x, y)),
                    run_time=0.1
                )

        self.wait()
        self.next_slide()

        self.play(
            *[Uncreate(g) for g in grid],  # каждый маленький график «разрисовывается наоборот»
            run_time=0.5
        )
        all_points = VGroup(*all_dots)
        self.play(Uncreate(all_points), run_time=0.5)
        self.play(Unwrite(title_chart_1), Unwrite(title_chart_2), Unwrite(title_chart_3), Unwrite(title_chart_4), run_time=1)

        self.wait()


class Tmp(Slide):
    def make_axes_group(self, cfg, y_label_text):
        axes = Axes(
            x_range=cfg["x_range"],
            y_range=cfg["y_range"],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        # подписи осей
        x_lab = MathTex("N", color="#343434") \
            .scale(0.75) \
            .next_to(axes.x_axis.get_end(), RIGHT * 0.3 + DOWN * 0.1)
        y_lab = MathTex(y_label_text, color="#343434") \
            .scale(0.75) \
            .next_to(axes.y_axis.get_end(), LEFT * 1.5)
        # метки по Y
        y_ticks = VGroup(*[
            MathTex(f"{v:.1f}", color="#343434").scale(0.75)
                         .next_to(axes.c2p(0, v), LEFT * 3, buff=0.05)
            for v in np.arange(*cfg["y_range"])
        ])
        # метки по X
        x_ticks = VGroup(*[
            MathTex(str(int(x)), color="#343434").scale(0.75)
                         .next_to(axes.x_axis.n2p(x), DOWN * 3, buff=0.05)
            for x in np.arange(*cfg["x_range"]) if x != 0
        ])
        group = VGroup(axes, x_lab, y_lab, y_ticks, x_ticks)
        return group, axes

    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))

        # 1) Параметры для четырёх графиков
        configs = [
            {"x_range": (0, 1050, 100), "y_range": (179, 182, 0.5)},
            {"x_range": (0, 1050, 100), "y_range": (3, 5, 0.2)},
            {"x_range": (0, 1050, 100), "y_range": (8, 10, 0.2)},
            {"x_range": (0, 1050, 100), "y_range": (6, 9, 0.5)},
        ]
        y_labels = ["\hat{T_1}", "\hat{T_2}", "\hat{T_3}", "\hat{T_4}"]
        x_vals = list(range(50, 1001, 50))
        y_vals_list = [
            [181.30, 179.90, 180.80, 180.30, 180.25, 180.60, 180.65, 180.70, 180.30, 180.35,
            180.60, 180.60, 180.80, 180.55, 180.55, 180.55, 180.30, 180.30, 180.35, 180.35],
            [3.96, 3.75, 3.58, 3.67, 3.83, 3.75, 3.78, 3.74, 3.75, 3.80,
            3.82, 3.72, 3.63, 3.68, 3.67, 3.75, 3.68, 3.69, 3.75, 3.67],
            [8.38, 8.52, 8.92, 8.56, 8.78, 8.57, 8.63, 8.44, 8.80, 8.72,
            8.75, 8.65, 8.68, 8.61, 8.82, 8.83, 8.75, 8.76, 8.91, 8.88],
            [7.73, 7.01, 6.72, 7.08, 7.08, 6.97, 7.14, 7.15, 7.18, 7.08,
            6.94, 7.02, 6.92, 7.12, 7.06, 7.10, 7.23, 7.11, 7.15, 7.15],
        ]

        # 2) Делаем по 4 группы осей
        axes_groups = []
        axes_objects = []
        for cfg, lab in zip(configs, y_labels):
            group, axes = self.make_axes_group(cfg, lab)
            axes_groups.append(group)
            axes_objects.append(axes)

        # 3) Уменьшаем их и раскладываем в 2×2
        grid = VGroup(*axes_groups)
        grid.scale(0.5).arrange_in_grid(rows=2, cols=2, buff=1.0)
        # сдвигаем левый столбец чуть вправо
        for i in (0, 2):
            grid[i].shift(RIGHT * 0.3)

        # 4) Анимируем появление осей + меток
        self.play(*[Create(g) for g in grid], run_time=2.0)

        title_graph_1 = MarkupText("<i>График зависимости</i>", font_size=15, fill_color="#343434")
        title_graph_1.next_to(grid[0], UP, buff=0).shift(LEFT)
        title_graph_1_t = MathTex(r"\hat{T_1}", fill_color="#343434").scale(0.4).next_to(title_graph_1, RIGHT, buff=0.1)
        title_graph_1_continus = Text("от", font_size=15, fill_color="#343434").next_to(title_graph_1_t, RIGHT,
                                                                                        buff=0.1)
        title_graph_1_n = MathTex(r"N", fill_color="#343434").scale(0.4).next_to(title_graph_1_continus, RIGHT,
                                                                                 buff=0.1)
        title_chart_1 = VGroup(title_graph_1, title_graph_1_t, title_graph_1_n, title_graph_1_continus)

        title_graph_2 = MarkupText("<i>График зависимости</i>", font_size=15, fill_color="#343434")
        title_graph_2.next_to(grid[1], UP, buff=0).shift(LEFT)
        title_graph_2_t = MathTex(r"\hat{T_2}", fill_color="#343434").scale(0.4).next_to(title_graph_2, RIGHT, buff=0.1)
        title_graph_2_continus = Text("от", font_size=15, fill_color="#343434").next_to(title_graph_2_t, RIGHT,
                                                                                        buff=0.1)
        title_graph_2_n = MathTex(r"N", fill_color="#343434").scale(0.4).next_to(title_graph_2_continus, RIGHT,
                                                                                 buff=0.1)
        title_chart_2 = VGroup(title_graph_2, title_graph_2_t, title_graph_2_continus, title_graph_2_n)

        title_graph_3 = MarkupText("<i>График зависимости</i>", font_size=15, fill_color="#343434")
        title_graph_3.next_to(grid[2], UP, buff=0).shift(LEFT)
        title_graph_3_t = MathTex(r"\hat{T_3}", fill_color="#343434").scale(0.4).next_to(title_graph_3, RIGHT, buff=0.1)
        title_graph_3_continus = Text("от", font_size=15, fill_color="#343434").next_to(title_graph_3_t, RIGHT,
                                                                                        buff=0.1)
        title_graph_3_n = MathTex(r"N", fill_color="#343434").scale(0.4).next_to(title_graph_3_continus, RIGHT,
                                                                                 buff=0.1)
        title_chart_3 = VGroup(title_graph_3, title_graph_3_t, title_graph_3_continus, title_graph_3_n)

        title_graph_4 = MarkupText("<i>График зависимости</i>", font_size=15, fill_color="#343434")
        title_graph_4.next_to(grid[3], UP, buff=0).shift(LEFT)
        title_graph_4_t = MathTex(r"\hat{T_4}", fill_color="#343434").scale(0.4).next_to(title_graph_4, RIGHT, buff=0.1)
        title_graph_4_continus = Text("от", font_size=15, fill_color="#343434").next_to(title_graph_4_t, RIGHT,
                                                                                        buff=0.1)
        title_graph_4_n = MathTex(r"N", fill_color="#343434").scale(0.4).next_to(title_graph_4_continus, RIGHT,
                                                                                 buff=0.1)
        title_chart_4 = VGroup(title_graph_4, title_graph_4_t, title_graph_4_continus, title_graph_4_n)

        self.play(Write(title_chart_1), Write(title_chart_2), Write(title_chart_3), Write(title_chart_4), run_time=2)

        # 5) Падающие точки
        all_dots = []
        for axes, y_vals in zip(axes_objects, y_vals_list):
            # для каждой точки рисуем её чуть выше, скрываем, а потом «падаем»
            for x, y in zip(x_vals, y_vals):
                start = axes.c2p(x, y) + UP * 1.2  # точка изначально выше
                dot = Dot(start, radius=0.03, color="#343434")
                dot.set_opacity(0)
                self.add(dot)
                all_dots.append(dot)
                # одновременно делаем видимой и перемещаем на своё место
                self.play(
                    dot.animate.set_opacity(1).move_to(axes.c2p(x, y)),
                    run_time=0.1
                )

        self.wait()
        self.next_slide()

        self.play(
            *[Uncreate(g) for g in grid],  # каждый маленький график «разрисовывается наоборот»
            run_time=0.5
        )
        all_points = VGroup(*all_dots)
        self.play(Uncreate(all_points), run_time=0.5)
        self.play(Unwrite(title_chart_1), Unwrite(title_chart_2), Unwrite(title_chart_3), Unwrite(title_chart_4),
                  run_time=1)

        self.wait()

class Begin(Slide):
    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))

        title_introduction = Text("Цель и задачи работы", font_size=36, color="#343434")
        title_introduction.to_edge(UP, buff=0.1)
        title_introduction_ul = Underline(title_introduction, color="#343434")
        self.play(Write(title_introduction), Write(title_introduction_ul))

        target_text = MarkupText(
            "<i><b>Цель</b></i> - построение алгоритма имитационной модели обощенного синхронного\nпотока событий второго порядка с "
            "произвольным числом состояний,\nа также его реализация на языке программирования C++\nдля получения выборки моментов наступления событий",
            font_size=26, color="#343434")
        target_text.to_edge(UP * 1.6 + LEFT)
        self.play(Write(target_text))

        # Список задач
        items = ["Изучить научную литературу по теме исследования", "Построить математическую модель потока",
                 "Построить блок-схему алгоритма", "Реализовать графическую составляющую, то есть написать"
                                                   "GUI-приложение\nс использованием фреймворка Qt на C++"
            , "Провести серию статистических экспериментов"]
        # 1) квадраты
        boxes = VGroup(*[
            Square(side_length=0.4, color="#343434")
                       .set_fill(None, opacity=0)  # пока пустые
            for _ in items
        ])
        # 2) подписи
        labels = VGroup(*[
            Text(text, font_size=26, color="#343434")
            for text in items
        ])
        # 3) сгруппировать пары [квадрат + текст] и расположить вниз
        rows = VGroup(*[
            VGroup(box, lbl).arrange(RIGHT, buff=0.2)
            for box, lbl in zip(boxes, labels)
        ])
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        rows.to_edge(UP * 5 + LEFT)

        # 4 анимация
        self.play(Create(boxes[0]), Write(labels[0]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[1]), Write(labels[1]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[2]), Write(labels[2]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[3]), Write(labels[3]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[4]), Write(labels[4]), run_time=0.5)
        self.wait()

        self.next_slide()
        self.play(Unwrite(title_introduction), Unwrite(title_introduction_ul), Unwrite(target_text), Uncreate(boxes),
                  Unwrite(labels))

class Ending(Slide):
    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))

        end_title = Text("Заключение", fill_color="#343434", font_size=36)
        end_title.to_edge(UP, buff=0.5)
        end_title_ul = Underline(end_title, color="#343434", buff=0.1)
        self.play(Write(end_title), Write(end_title_ul))

        # Список задач
        items = ["Изучена литература по теме исследования", "Построена мат. модель потока", "Выведены формулы, по которым производится моделирование",
                 "Построен алгоритм имитационной модели", "Алгорит имитационной модели реализован на ЯП C++",
                 "Написано GUI-приложение", "Проведена серия статистических экспериментов"]
        # 1) квадраты
        boxes = VGroup(*[
            Square(side_length=0.4, color="#343434")
                       .set_fill(None, opacity=0)  # пока пустые
            for _ in items
        ])
        # 2) подписи
        labels = VGroup(*[
            Text(text, font_size=26, color="#343434")
            for text in items
        ])
        # 3) сгруппировать пары [квадрат + текст] и расположить вниз
        rows = VGroup(*[
            VGroup(box, lbl).arrange(RIGHT, buff=0.2)
            for box, lbl in zip(boxes, labels)
        ])
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        rows.to_edge(UP * 3 + LEFT)

        self.play(
            *[Create(box) for box in boxes],
            *[Write(lbl) for lbl in labels],
            run_time=1
        )

        checks = VGroup(
            *[
                VGroup(
                    # левая ножка галочки
                    Line(
                        box.get_corner(UL) + DOWN * 0.2 + RIGHT * 0.1,
                        box.get_center() + DOWN * 0.1
                    ),
                    # правая ножка
                    Line(
                        box.get_center() + DOWN * 0.1,
                        box.get_corner(UR) + DOWN * 0.1 + LEFT * 0.05
                    ),
                )
                .set_color("#83C167")
                .set_stroke(width=3)
                for box in boxes
            ]
        )

        self.wait()
        self.next_slide()
        self.play(Create(checks[0]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[1]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[2]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[3]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[4]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[5]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[6]), run_time=0.1)

        self.wait()


class Exp3(Slide):
    def construct(self):

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[0.31, 0.32, 0.002],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        axes.y_axis.ticks[-1].set_opacity(0)
        x_label = MathTex("N", color="#343434").next_to(axes.x_axis.get_end(), RIGHT + DOWN, buff=0.2)
        y_label = MathTex(r"\hat{\overline{\tau}}", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        # 2) Метки по Y
        y_values = np.arange(0.31, 0.319, 0.002)  # [23.0, 23.5, …, 25.5]
        y_labels = VGroup(*[
            MathTex(f"{val:.3f}", color="#343434")
                          .scale(0.6)
                          .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in y_values
        ])
        y_labels.set_opacity(1)

        # 3) Падающие точки
        x_vals = list(range(50, 1001, 50))
        y_vals = [
            0.3120, 0.3130, 0.3113, 0.3132, 0.3132, 0.3120, 0.3131, 0.3134, 0.3128, 0.3127,
            0.3133, 0.3124, 0.3132, 0.3127, 0.3123, 0.3130, 0.3122, 0.3134, 0.3128, 0.3129
        ]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        # 4) Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        # 5) Анимация
        self.play(Create(axes), run_time=1)
        self.play(FadeIn(y_label, shift=LEFT), FadeIn(x_label, shift=DOWN))
        self.play(FadeIn(y_labels, shift=LEFT, lag_ratio=0.1), run_time=1)

        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=1
        )
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()

        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=1)
        self.remove(axes, y_labels, x_ticks, x_labels)

        axes = Axes(
            x_range=[0, 550, 50],
            y_range=[0.31, 0.32, 0.002],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        axes.y_axis.ticks[-1].set_opacity(0)
        x_label = MathTex(r"T_m", color="#343434").next_to(axes.x_axis.get_end(), RIGHT + DOWN, buff=0.2)
        y_label = MathTex(r"\hat{\overline{\tau}}", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(0.31, 0.319, 0.002)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.3f}", color="#343434")
                              .scale(0.6)
                              .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 550, 50)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [0.3108, 0.3121, 0.3130, 0.3128, 0.3132, 0.3127, 0.3131, 0.3130, 0.3129, 0.3130]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=1)
        self.play(Write(y_label), Write(x_label), run_time=1)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=1
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=1)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()

class Experiment3(Slide):
    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))
        experiment_3_title = Text("3 статистический эксперимент", font_size=36, fill_color="#343434")
        experiment_3_title.to_edge(UP, buff=0.5)
        experiment_3_title_ul = Underline(experiment_3_title, color="#343434")
        self.play(Write(experiment_3_title), Write(experiment_3_title_ul))

        experiment_3 = Text(
            "Этапы эксперимента:\n1)для фиксированного набора параметров, вероятностей переходов и количества\nитераций N/длительности времени "
            "моделирования реализуется обобщенный синхронный поток событий \nвторого порядка с произвольным кол-ом состояний",
            font_size=20, fill_color="#343434")
        experiment_3.to_edge(UP * 3 + LEFT)
        self.play(Write(experiment_3))
        self.wait()
        self.next_slide()

        experiment_3_1 = MathTex(r"2)\hat{\tau}_j=\frac{1}{k_j}\sum_{i=1}^{k_j}\tau_i^{(j)},j=\overline{1,N}", color="#343434",
                                 font_size=28)
        experiment_3_1.next_to(experiment_3, DOWN)
        experiment_3_1.shift(LEFT * 5.05)
        self.play(Write(experiment_3_1))
        self.wait()
        self.next_slide()

        experiment_3_2 = Text("3) осуществляем повторение N раз шагов 1, 2", font_size=20, fill_color="#343434")
        experiment_3_2.next_to(experiment_3_1, DOWN)
        experiment_3_2.shift(RIGHT * 1.2)
        self.play(Write(experiment_3_2))

        self.wait()
        self.next_slide()

        experiment_3_3 = Text("Вычисляем выборочные средние (оценки) значения длительности интервала между моментами\nнаступления событий в рассматриваемом потоке:",
                              font_size=20, fill_color="#343434")
        experiment_3_3.next_to(experiment_3_2, DOWN, buff=0.2)
        experiment_3_3.shift(RIGHT * 3.25)
        self.play(Write(experiment_3_3))
        self.wait()
        self.next_slide()

        experiment_3_4 = MathTex(r"\hat{\overline{t}}=\frac{1}{N}\sum_{j=1}^N \hat{t}_j", fill_color="#343434")
        experiment_3_4.next_to(experiment_3_3, DOWN, buff=0.5)
        experiment_3_4_rect = SurroundingRectangle(experiment_3_4, color="#343434", buff=0.2)

        self.play(Write(experiment_3_4), Write(experiment_3_4_rect))
        self.wait()
        self.next_slide()

        self.play(Unwrite(experiment_3), Unwrite(experiment_3_1), Unwrite(experiment_3_2), Unwrite(experiment_3_3),
                  Unwrite(experiment_3_4), Unwrite(experiment_3_4_rect))


class Experiment2(Slide):
    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))
        experiment_2_title = Text("2 статистический эксперимент", font_size=36, weight=BOLD, fill_color="#343434")
        experiment_2_title.to_edge(UP, buff=0.1)
        experiment_2_title_ul = Underline(experiment_2_title, color="#343434")
        self.play(Write(experiment_2_title), Write(experiment_2_title_ul))

        experiment_2 = Text(
            "Изменим вероятности переходов по первой и второй случайной величине, \nтак чтобы вероятность оказаться в первом состоянии была максимальна",
            font_size=20, fill_color="#343434")
        experiment_2.to_edge(UP * 2 + LEFT)
        self.play(Write(experiment_2))

        # Заголовок таблицы
        title_1 = Text(
            "Вероятности переходов по первой случайной величине",
            font_size=14,
            color="#343434"
        ).to_edge(UP, buff=0.3)

        table_data_1 = [
            [r"P_1^{(1)}(\lambda_1|\lambda_1)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_2)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_3)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_4)=0.97"],
            [r"P_1^{(1)}(\lambda_2|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_4)=0.01"],
            [r"P_1^{(1)}(\lambda_3|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_4)=0.01"],
            [r"P_1^{(1)}(\lambda_4|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_4)=0.01"],
        ]

        # Подписи столбцов — сразу MathTex
        col_labels_1 = [
            MathTex(r"\lambda_1=4,\ \alpha_1=4", font_size=40, color="#343434"),
            MathTex(r"\lambda_2=2,\ \alpha_2=2", font_size=40, color="#343434"),
            MathTex(r"\lambda_3=1,\ \alpha_3=0.7", font_size=40, color="#343434"),
            MathTex(r"\lambda_4=0.5,\ \alpha_4=1.6", font_size=40, color="#343434"),
        ]

        # Строим таблицу
        table_1 = MathTable(
            table_data_1,
            col_labels=col_labels_1,
            include_outer_lines=True,
            line_config={
                "stroke_color": "#343434",
                "stroke_width": 2,  # при желании можно прописать толщину
            },
            top_left_entry=MathTex("", font_size=40, color="#343434"),
            # оборачивать каждую ячейку в MathTex
            element_to_mobject=MathTex,
            element_to_mobject_config={
                "font_size": 40,
                "color": "#343434",
            },
        )
        table_1.scale(0.35).shift(UP)
        title_1.next_to(table_1, DOWN, buff=0.1)

        self.play(Write(table_1), Write(title_1))

        # Заголовок таблицы
        title_2 = Text(
            "Вероятности переходов по второй случайной величине",
            font_size=14,
            color="#343434"
        ).to_edge(UP, buff=0.3)

        # Данные ячеек — передаём чистые строки,
        #    но Table обернёт их в MathTex:
        table_data_2 = [
            [r"P_1^{(1)}(\lambda_1|\lambda_1)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_2)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_3)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_4)=0.97"],
            [r"P_1^{(1)}(\lambda_2|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_4)=0.01"],
            [r"P_1^{(1)}(\lambda_3|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_4)=0.01"],
            [r"P_1^{(1)}(\lambda_4|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_4)=0.01"],
        ]

        # Подписи столбцов — сразу MathTex
        col_labels_2 = [
            MathTex(r"\lambda_1=4,\ \alpha_1=4", font_size=40, color="#343434"),
            MathTex(r"\lambda_2=2,\ \alpha_2=2", font_size=40, color="#343434"),
            MathTex(r"\lambda_3=1,\ \alpha_3=0.7", font_size=40, color="#343434"),
            MathTex(r"\lambda_4=0.5,\ \alpha_4=1.6", font_size=40, color="#343434"),
        ]

        # Строим таблицу
        table_2 = MathTable(
            table_data_2,
            col_labels=col_labels_2,
            include_outer_lines=True,
            line_config={
                "stroke_color": "#343434",
                "stroke_width": 2,  # при желании можно прописать толщину
            },
            top_left_entry=MathTex("", font_size=40, color="#343434"),
            # оборачивать каждую ячейку в MathTex
            element_to_mobject=MathTex,
            element_to_mobject_config={
                "font_size": 40,
                "color": "#343434",
            },
        )
        table_2.scale(0.35).shift(DOWN * 2)
        title_2.next_to(table_2, DOWN, buff=0.1)
        self.play(Write(table_2), Write(title_2))
        self.wait()
        self.next_slide()

        self.play(Unwrite(title_1), Unwrite(title_2), Unwrite(table_1), Unwrite(table_2), Unwrite(experiment_2_title),Unwrite(experiment_2_title_ul),
                  Unwrite(experiment_2), run_time=2)



class ImitationModeling(Slide):
    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))

        imitation_title = Text("Метод обратных функций", font_size=36, weight=BOLD, fill_color="#343434")
        imitation_title.to_edge(UP, buff=0.1)
        imitation_title_ul = Underline(imitation_title, color="#343434")
        self.play(Write(imitation_title), Write(imitation_title_ul))

        imitation_modeling = Text("Имитационное моделирование представляет собой метод исследования сложных систем путем\nих воспроизведения"
                                  "в виде компьютерных моделей. "
                                  "Имитационное моделирование является\nмощным инструментом анализа сложных систем, позволяя воспроизводить их поведение с учетом\n"
                                  "вероятностных характеристик. Одним из ключевых методов генерации "
                                  "случайных событий в таких\nмоделях является метод обратных функций", font_size=20, fill_color="#343434")
        imitation_modeling.to_edge(UP*2 + LEFT)
        self.play(Write(imitation_modeling))
        self.wait()
        self.next_slide()

        reverse_function = Text("Применение метода обратных функций включает следующие этапы:", font_size=20, fill_color="#343434")
        reverse_function.next_to(imitation_modeling, DOWN, buff=0.1)
        self.play(Write(reverse_function))
        self.wait()
        block_1 = Text("1) Генерация случайного числа U из равномерного распределения [0;1]", font_size=20, fill_color="#343434")
        block_1.next_to(reverse_function, DOWN, buff=0.1)
        block_1.shift(LEFT*2)
        self.play(Write(block_1))
        self.wait()
        self.next_slide()
        block_2 = Text("2) Вычисление значения", font_size=20, fill_color="#343434")
        block_2.next_to(block_1, DOWN, buff=0.1)
        block_2.shift(LEFT*2.9)
        block_2_continius = MathTex(r"X=F^{-1}(U)", fill_color="#343434").scale(0.5)
        block_2_continius.next_to(block_2, RIGHT, buff=0.1)
        self.play(Write(block_2))
        self.play(Write(block_2_continius))
        self.wait()
        self.next_slide()
        block_3 = Text("3) Использование полученного значения X в моделировании системы", font_size=20, fill_color="#343434")
        block_3.next_to(block_2, DOWN, buff=0.1)
        block_3.shift(RIGHT*2.9)
        self.play(Write(block_3))
        self.wait()
        self.next_slide()
        block_4 = Text("Применение метода обратных функций для получения случайной величины, распределенной\nэкспоненциально:", font_size=20, fill_color="#343434")
        block_4.next_to(block_3, DOWN, buff=0.2)
        block_4.shift(RIGHT*1.5)
        self.play(Write(block_4))
        self.wait()
        self.next_slide()
        block_5 = Text("1) Генерируется равномерно распределенное случайное число U на отрезке [0;1)", font_size=20, fill_color="#343434")
        block_5.next_to(block_4, DOWN, buff=0.1)
        block_5.shift(LEFT*0.75)
        self.play(Write(block_5))
        self.wait()
        self.next_slide()
        block_6 = MathTex(r"2) t=F^{-1}(U), t=-\frac{1}{\theta_i}ln(1-U), \theta_i \in \{\lambda_i,\alpha_i\}", fill_color="#343434").scale(0.6)
        block_6.next_to(block_5, DOWN, buff=0.1)
        block_6.shift(LEFT*2.2)
        self.play(Write(block_6))
        self.wait()
        self.next_slide()
        block_7 = Text("Таким образом, получается случайная величина t, распределенная по экспоненциальному закону", font_size=20, fill_color="#343434")
        block_7.next_to(block_6, DOWN, buff=0.2)
        block_7.shift(RIGHT*3.25)
        self.play(Write(block_7))
        self.wait()
        self.next_slide()
        self.play(Unwrite(imitation_title), Unwrite(imitation_title_ul), Unwrite(imitation_modeling), Unwrite(reverse_function),
                  Unwrite(block_1), Unwrite(block_2), Unwrite(block_2_continius),Unwrite(block_3), Unwrite(block_4), Unwrite(block_5), Unwrite(block_6), Unwrite(block_7))
        self.wait()

class Tables(Slide):
    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))

        experiment_1_title = Text("1 статистический эксперимент", font_size=36, weight=BOLD, fill_color="#343434")
        experiment_1_title.to_edge(UP, buff=0.1)
        experiment_1_title_ul = Underline(experiment_1_title, color="#343434")
        self.play(Write(experiment_1_title), Write(experiment_1_title_ul))

        experiment_body_1 = Text(
            "Этапы эксперимента:\n1)для фиксированного набора параметров, вероятностей переходов и длительности\n"
            "времени наблюдения за потоком моделируется обобщенный синхронный поток событий\nвторого порядка с произвольным числом состояний;",
            font_size=20, fill_color="#343434")
        experiment_body_1.to_edge(UP * 2 + LEFT)
        self.play(Write(experiment_body_1))

        self.wait()
        self.next_slide()

        experiment_body_2 = Text("2)осуществляется расчет длительности пребывания процесса в i-ом состоянии системы: ",
                                 font_size=20, fill_color="#343434")
        experiment_body_2.next_to(experiment_body_1, DOWN, buff=0.1)
        experiment_body_2_continius = MathTex(r"T_i^{(j)}, i=\overline{1,n}, j=\overline{1,n}", font_size=22,
                                              color="#343434")
        experiment_body_2_continius.next_to(experiment_body_2, RIGHT, buff=0.1)
        self.play(Write(experiment_body_2))
        self.play(Write(experiment_body_2_continius))

        self.wait()
        self.next_slide()

        experiment_body_3 = Text("3)повторяем N раз шаги 1, 2", font_size=20, fill_color="#343434")
        experiment_body_3.next_to(experiment_body_2, DOWN, buff=0.1)
        experiment_body_3.shift(LEFT * 4)
        self.play(Write(experiment_body_3))

        self.wait()
        self.next_slide()

        experiment_body_4 = Text(
            "Вычисляем выборочные средние (оценки) значения длительностей пребывания процесса\nв i-ом состоянии:",
            font_size=20, fill_color="#343434")
        experiment_body_4.next_to(experiment_body_3, DOWN)
        experiment_body_4.shift(RIGHT * 4.1)
        self.play(Write(experiment_body_4))

        experiment_body_5 = MathTex(r"\hat{T}_i=\frac{1}{N}\sum_{j=1}^{N}T_i^{(j)}, i=\overline{1,n}", font_size=28,
                                    color="#343434")
        experiment_body_5.to_edge(ORIGIN + DOWN * 6)
        experiment_body_5_rect = SurroundingRectangle(experiment_body_5, color="#343434", buff=0.2)
        self.play(Write(experiment_body_5), Create(experiment_body_5_rect))

        self.wait()
        self.next_slide()

        # Заголовок таблицы
        title_1 = Text(
            "Вероятности переходов по первой случайной величине",
            font_size=14,
            color="#343434"
        ).to_edge(UP, buff=0.3)

        # Данные ячеек — передаём чистые строки,
        #    но Table обернёт их в MathTex:
        table_data_1 = [
            [r"P_1^{(1)}(\lambda_1|\lambda_1)=0.5",
             r"P_1^{(1)}(\lambda_1|\lambda_2)=0.4",
             r"P_1^{(1)}(\lambda_1|\lambda_3)=0.1",
             r"P_1^{(1)}(\lambda_1|\lambda_4)=0.3"],
            [r"P_1^{(1)}(\lambda_2|\lambda_1)=0.125",
             r"P_1^{(1)}(\lambda_2|\lambda_2)=0.2",
             r"P_1^{(1)}(\lambda_2|\lambda_3)=0.5",
             r"P_1^{(1)}(\lambda_2|\lambda_4)=0.5"],
            [r"P_1^{(1)}(\lambda_3|\lambda_1)=0.125",
             r"P_1^{(1)}(\lambda_3|\lambda_2)=0.2",
             r"P_1^{(1)}(\lambda_3|\lambda_3)=0.2",
             r"P_1^{(1)}(\lambda_3|\lambda_4)=0.1"],
            [r"P_1^{(1)}(\lambda_4|\lambda_1)=0.25",
             r"P_1^{(1)}(\lambda_4|\lambda_2)=0.2",
             r"P_1^{(1)}(\lambda_4|\lambda_3)=0.2",
             r"P_1^{(1)}(\lambda_4|\lambda_4)=0.1"],
        ]

        # Подписи столбцов — сразу MathTex
        col_labels_1 = [
            MathTex(r"\lambda_1=4,\ \alpha_1=4", font_size=40, color="#343434"),
            MathTex(r"\lambda_2=2,\ \alpha_2=2", font_size=40, color="#343434"),
            MathTex(r"\lambda_3=1,\ \alpha_3=0.7", font_size=40, color="#343434"),
            MathTex(r"\lambda_4=0.5,\ \alpha_4=1.6", font_size=40, color="#343434"),
        ]

        # Строим таблицу
        table_1 = MathTable(
            table_data_1,
            col_labels=col_labels_1,
            include_outer_lines=True,
            line_config={
                "stroke_color": "#343434",
                "stroke_width": 2,  # при желании можно прописать толщину
            },
            top_left_entry=MathTex("", font_size=40, color="#343434"),
            # оборачивать каждую ячейку в MathTex
            element_to_mobject=MathTex,
            element_to_mobject_config={
                "font_size": 40,
                "color": "#343434",
            },
        )
        table_1.scale(0.35).shift(LEFT*3.5 + DOWN*2.5)
        title_1.next_to(table_1, DOWN, buff=0.1)

        # Заголовок таблицы
        title_2 = Text(
            "Вероятности переходов по второй случайной величине",
            font_size=14,
            color="#343434"
        ).to_edge(UP, buff=0.3)

        # Данные ячеек — передаём чистые строки,
        #    но Table обернёт их в MathTex:
        table_data_2 = [
            [r"P_1^{(1)}(\lambda_1|\lambda_1)=0.2",
             r"P_1^{(1)}(\lambda_1|\lambda_2)=0.125",
             r"P_1^{(1)}(\lambda_1|\lambda_3)=0.6",
             r"P_1^{(1)}(\lambda_1|\lambda_4)=0.25"],
            [r"P_1^{(1)}(\lambda_2|\lambda_1)=0.5",
             r"P_1^{(1)}(\lambda_2|\lambda_2)=0.5",
             r"P_1^{(1)}(\lambda_2|\lambda_3)=0.15",
             r"P_1^{(1)}(\lambda_2|\lambda_4)=0.25"],
            [r"P_1^{(1)}(\lambda_3|\lambda_1)=0.15",
             r"P_1^{(1)}(\lambda_3|\lambda_2)=0.125",
             r"P_1^{(1)}(\lambda_3|\lambda_3)=0.15",
             r"P_1^{(1)}(\lambda_3|\lambda_4)=0.125"],
            [r"P_1^{(1)}(\lambda_4|\lambda_1)=0.15",
             r"P_1^{(1)}(\lambda_4|\lambda_2)=0.25",
             r"P_1^{(1)}(\lambda_4|\lambda_3)=0.1",
             r"P_1^{(1)}(\lambda_4|\lambda_4)=0.375"],
        ]

        # Подписи столбцов — сразу MathTex
        col_labels_2 = [
            MathTex(r"\lambda_1=4,\ \alpha_1=4", font_size=40, color="#343434"),
            MathTex(r"\lambda_2=2,\ \alpha_2=2", font_size=40, color="#343434"),
            MathTex(r"\lambda_3=1,\ \alpha_3=0.7", font_size=40, color="#343434"),
            MathTex(r"\lambda_4=0.5,\ \alpha_4=1.6", font_size=40, color="#343434"),
        ]

        # Строим таблицу
        table_2 = MathTable(
            table_data_2,
            col_labels=col_labels_2,
            include_outer_lines=True,
            line_config={
                "stroke_color": "#343434",
                "stroke_width": 2,  # при желании можно прописать толщину
            },
            top_left_entry=MathTex("", font_size=40, color="#343434"),
            # оборачивать каждую ячейку в MathTex
            element_to_mobject=MathTex,
            element_to_mobject_config={
                "font_size": 40,
                "color": "#343434",
            },
        )
        table_2.scale(0.35).shift(RIGHT * 3.5 + DOWN * 2.5)
        title_2.next_to(table_2, DOWN, buff=0.1)

        # Анимация
        self.play(Write(title_1), Write(title_2))
        self.play(Write(table_1), Write(table_2), run_time=3)
        self.wait()

        self.play(Unwrite(experiment_1_title), Unwrite(experiment_1_title_ul), Unwrite(experiment_body_1), Unwrite(experiment_body_2),
                  Unwrite(experiment_body_2_continius),Unwrite(experiment_body_3), Unwrite(experiment_body_4),
                  Unwrite(experiment_body_5), Unwrite(experiment_body_5_rect), Unwrite(title_1),
                  Unwrite(title_2), Unwrite(table_1), Unwrite(table_2))
        self.wait()



class Introduction(Slide):
    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))

        title_introduction = Text("Цель и задачи работы", font_size=36, color="#343434")
        title_introduction.to_edge(UP, buff=0.1)
        title_introduction_ul = Underline(title_introduction, color="#343434")
        self.play(Write(title_introduction), Write(title_introduction_ul))

        target_text = Text("Цель - построение алгоритма имитационной модели обощенного синхронного\nпотока событий второго порядка с "
                           "произвольным числом состояний,\nа также его реализация на языке программирования C++\nдля получения выборки моментов наступления событий",
                           font_size=26, color="#343434")
        target_text.to_edge(UP*1.6 + LEFT)
        self.play(Write(target_text))

        # Список задач
        items = ["Изучить научную литературу по теме исследования", "Построить математическую модель потока", "Построить блок-схему алгоритма", "Реализовать графическую составляющую, то есть написать"
                                                                                                                                                "GUI-приложение\nс использованием фреймворка Qt на C++"
                 ,"Провести серию статистических экспериментов"]
        # 1) квадраты
        boxes = VGroup(*[
            Square(side_length=0.4, color="#343434")
                       .set_fill(None, opacity=0)  # пока пустые
            for _ in items
        ])
        # 2) подписи
        labels = VGroup(*[
            Text(text, font_size=26, color="#343434")
            for text in items
        ])
        # 3) сгруппировать пары [квадрат + текст] и расположить вниз
        rows = VGroup(*[
            VGroup(box, lbl).arrange(RIGHT, buff=0.2)
            for box, lbl in zip(boxes, labels)
        ])
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        rows.to_edge(UP*5 + LEFT)

        # 4 анимация
        self.play(Create(boxes[0]), Write(labels[0]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[1]), Write(labels[1]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[2]), Write(labels[2]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[3]), Write(labels[3]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[4]), Write(labels[4]), run_time=0.5)
        self.wait()

        self.next_slide()
        self.play(Unwrite(title_introduction), Unwrite(title_introduction_ul), Unwrite(target_text), Uncreate(boxes), Unwrite(labels))



class Graphics(Scene):
    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))
        # 1) Оси (оставим небольшой запас по X, чтобы точка x=1000 не попала в стрелку)

        result_title = Text("График зависимости", font_size=36, color="#343434")
        result_title.to_edge(UP+LEFT*25, buff=0.1)
        result_title_1 = MathTex(r"\hat{T}_1", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        result_title_2 = Text("от значений", font_size=36, color="#343434").next_to(result_title, RIGHT, buff=0.8).shift(UP*0.06)
        result_title_3 = MathTex(r"N", color="#343434").next_to(result_title_2, RIGHT, buff=0.2)
        title = VGroup(result_title, result_title_1, result_title_2, result_title_3)
        result_title_ul = Underline(title, color="#343434")
        self.play(Write(title), Write(result_title_ul))

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[23, 26, 0.5],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        x_label = MathTex("N", color="#343434").next_to(axes.x_axis.get_end(), RIGHT + DOWN, buff=0.2)
        y_label = MathTex("\\hat{T}_1", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        # 2) Метки по Y (до 25.5, чтобы не рисовать 26.0 прямо на стрелке)
        y_values = np.arange(23, 26, 0.5)  # [23.0, 23.5, …, 25.5]
        y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                          .scale(0.6)
                          .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in y_values
        ])
        y_labels.set_opacity(1)

        # 3) Падающие точки
        x_vals = list(range(50, 1001, 50))
        y_vals = [24.3, 24.35, 24.35, 24.5, 24.15, 24.1, 23.9, 24.2,
                  24.15, 24.2, 23.9, 24.35, 23.9, 24.05, 23.8, 24.05,
                  23.95, 24.15, 24.1, 24.1]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        # 4) Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        # 5) Анимация
        self.play(Create(axes), run_time=2)
        self.play(FadeIn(y_label, shift=LEFT), FadeIn(x_label, shift=DOWN))
        self.play(FadeIn(y_labels, shift=LEFT, lag_ratio=0.1), run_time=1)

        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=1
        )
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()

        # результат 2
        new_result_title_1 = MathTex(r"\hat{T}_2", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels), FadeOut(x_label),run_time=1)
        self.play(Transform(result_title_1, new_result_title_1))
        self.remove(axes, y_labels, x_ticks, x_labels)
        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[51, 54, 0.5],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        y_label = MathTex("\\hat{T}_2", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(51, 54, 0.5)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                .scale(0.6)
                .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [52.56, 52.38, 51.98, 52.20, 52.22,  52.28, 51.85, 52.40,  51.85, 52.22, 52.28,52.15,52.23,52.05,52.30,52.30,52.15,52.10,52.03, 52.02]
        points = VGroup(*[
        Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=2)
        self.play(Write(y_label), Write(x_label), run_time=1)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=1
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=1)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()

        # результат 3
        new_result_title_1 = MathTex(r"\hat{T}_3", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=1)
        self.play(Transform(result_title_1, new_result_title_1))
        self.remove(axes, y_labels, x_ticks, x_labels)
        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[53, 57, 0.5],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        y_label = MathTex("\\hat{T}_3", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(53, 57, 0.5)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                              .scale(0.6)
                              .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [56.4, 53.85, 55.80, 55.60, 55.20, 54.90, 55.70, 55.70, 54.85, 55.10, 55.05, 54.95, 55.27, 55.40, 55.35, 55.35, 55.15, 55.20, 55.10, 55.15]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=2)
        self.play(Write(y_label), Write(x_label), run_time=1)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=1
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=1)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()

        # результат 4
        new_result_title_1 = MathTex(r"\hat{T}_4", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=1)
        self.play(Transform(result_title_1, new_result_title_1))
        self.remove(axes, y_labels, x_ticks, x_labels)
        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[66, 70, 0.5],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        y_label = MathTex("\\hat{T}_4", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(66, 70, 0.5)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                              .scale(0.6)
                              .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [
            66.75, 69.40, 67.85, 67.70, 68.45, 68.75, 68.55, 68.55, 69.20, 68.55,
            68.75, 68.65, 68.55, 68.45, 68.70, 68.75, 68.30, 68.30, 68.75, 68.80
        ]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=2)
        self.play(Write(y_label), Write(x_label), run_time=1)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=1
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=1)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()


class Presentation(Slide):
    def construct(self):
        box_backgrund = Square(color="#ece6e2", fill_opacity=1).scale(10)
        self.play(Write(box_backgrund))

        header_text = (
            "Статистические эксперименты на имитационной\nмодели обобщенного синхронного потока событий\n"
            "второго порядка с произвольным числом состояний"
        )
        header = Text(header_text, fill_color="#343434", weight=BOLD, font_size=36)
        # Размещаем заголовок в верхней части экрана
        header.to_edge(UP, buff=0.5)

        # Создаем линию под заголовком с помощью функции Underline
        underline = Underline(header, color="#343434")
        underline_bk = Rectangle(width=header.width, height=header.height * 1.6) \
            .next_to(underline, DOWN, buff=0) \
            .set_style(fill_opacity=1, stroke_width=0, fill_color="#ece6e2")
        vg_title = VGroup(underline_bk, underline)

        # Создаем информационные надписи без параметра align
        supervisor_info1 = Text(
            "Руководитель работы д-р физ.-мат. наук, профессор:",
            font_size=20,
            fill_color="#343434"
        )
        supervisor_info2 = Text(
            "Л.А. Нежельская",
            font_size=20,
            fill_color="#343434"
        )
        author_info1 = Text(
            "Автор работы студент гр.932221:",
            font_size=20,
            fill_color="#343434"
        )
        author_info2 = Text(
            "А.С. Иванов",
            font_size=20,
            fill_color="#343434"
        )

        # Группируем и выравниваем по правому краю
        info_group = VGroup(supervisor_info1, supervisor_info2, author_info1, author_info2).arrange(DOWN,
                                                                                                    aligned_edge=RIGHT)
        info_group.to_corner(DR, buff=0.5)

        # Линия справа внизу
        vertical_bar = Rectangle(width=info_group.width * 0.009, height=info_group.height) \
            .next_to(info_group, RIGHT, buff=0.1) \
            .set_style(fill_color="#343434", fill_opacity=1, stroke_width=0)

        vertical_bar_bk = Rectangle(width=info_group.width, height=info_group.height) \
            .next_to(info_group, RIGHT, buff=0) \
            .set_style(fill_opacity=1, stroke_width=0, fill_color="#ece6e2")
        vg_info_group = VGroup(vertical_bar_bk, vertical_bar)

        # Добавляем все объекты на сцену
        self.play(Write(header))
        self.play(Write(info_group))

        # Ждем, чтобы зритель увидел первый слайд
        self.wait()
        self.next_slide()

        self.play(GrowFromCenter(underline), Write(vertical_bar))
        self.add(vg_title, vg_info_group)
        self.play(vg_title.animate.shift(UP * underline_bk.height),
                  vg_info_group.animate.shift(LEFT * info_group.width))
        self.play(ShrinkToCenter(underline), ShrinkToCenter(vertical_bar))
        self.remove(vg_title, header, info_group, vg_info_group)

        # 2 слайд
        introduction_title = Text("Введение", font_size=36, weight=BOLD, fill_color="#343434")
        introduction_title.to_edge(UP, buff=0.75)
        introduction_title_ul = Underline(introduction_title, color="#343434")
        body_text_1 = (
            "• В начале 20-го века в связи с бурным развитием \nтелекоммуникационных сетей возникла такая дисциплина \nкак теория массового обслуживания (ТМО)"
        )
        body_1 = Text(body_text_1, font_size=28, fill_color="#343434")
        body_1.move_to(ORIGIN + UP*1.25 + LEFT*0.75)

        body_text_2 = (
            "• Первыми работами в этой области стали труды \nдатского инженера и математика А. К. Эрланга"
        )
        body_2 = Text(body_text_2, font_size=28, fill_color="#343434")
        body_2.move_to(ORIGIN + DOWN+0.9 + LEFT*2.7)

        body_text_3 = (
            "• Цифровые сети интегрального обслуживания, сокращенно ЦСИО"
        )
        body_3 = Text(body_text_3, font_size=28, fill_color="#343434")
        body_3.move_to(ORIGIN + DOWN*1.25 + LEFT*0.1)


        slide_1 = Text("1", font_size=20, fill_color="#343434")
        slide_1.to_corner(DR, buff=0.1)
        self.play(Write(introduction_title), Write(introduction_title_ul), Write(slide_1))
        self.play(Write(body_1))

        self.wait()
        self.next_slide()

        self.play(Write(body_2))

        self.wait()
        self.next_slide()
        self.play(Write(body_3))

        self.wait()
        self.next_slide()
        self.play(Unwrite(introduction_title), Unwrite(introduction_title_ul), Unwrite(body_1), Unwrite(body_2),
                  Unwrite(body_3))
        slide_2 = Text("2", font_size=20, fill_color="#343434")
        slide_2.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_2))

        title_introduction = Text("Цель и задачи работы", font_size=36, color="#343434")
        title_introduction.to_edge(UP, buff=0.1)
        title_introduction_ul = Underline(title_introduction, color="#343434")
        self.play(Write(title_introduction), Write(title_introduction_ul))

        target_text = Text(
            "Цель - построение алгоритма имитационной модели обощенного синхронного\nпотока событий второго порядка с "
            "произвольным числом состояний,\nа также его реализация на языке программирования C++\nдля получения выборки моментов наступления событий",
            font_size=26, color="#343434")
        target_text.to_edge(UP * 1.6 + LEFT)
        self.play(Write(target_text))

        # Список задач
        items = ["Изучить научную литературу по теме исследования", "Построить математическую модель потока",
                 "Построить блок-схему алгоритма", "Реализовать графическую составляющую, то есть написать"
                                                   "GUI-приложение\nс использованием фреймворка Qt на C++"
            , "Провести серию статистических экспериментов"]
        # 1) квадраты
        boxes = VGroup(*[
            Square(side_length=0.4, color="#343434")
                       .set_fill(None, opacity=0)  # пока пустые
            for _ in items
        ])
        # 2) подписи
        labels = VGroup(*[
            Text(text, font_size=26, color="#343434")
            for text in items
        ])
        # 3) сгруппировать пары [квадрат + текст] и расположить вниз
        rows = VGroup(*[
            VGroup(box, lbl).arrange(RIGHT, buff=0.2)
            for box, lbl in zip(boxes, labels)
        ])
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        rows.to_edge(UP * 5 + LEFT)

        # 4 анимация
        self.play(Create(boxes[0]), Write(labels[0]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[1]), Write(labels[1]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[2]), Write(labels[2]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[3]), Write(labels[3]), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(Create(boxes[4]), Write(labels[4]), run_time=0.5)
        self.wait()

        self.next_slide()
        self.play(Unwrite(title_introduction), Unwrite(title_introduction_ul), Unwrite(target_text), Uncreate(boxes),
                  Unwrite(labels))

        slide_3 = Text("3", font_size=20, fill_color="#343434")
        slide_3.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_3))

        model_title = Text("Математическая модель", font_size=36, weight=BOLD, fill_color="#343434")
        model_title.to_edge(UP, buff=1)
        model_title_ul = Underline(model_title, color="#343434")

        self.play(Write(model_title), Write(model_title_ul))
        model_text_1 = MathTex( r"\lambda(t) ", color="#343434")
        model_text_1.to_edge(UP*4 + LEFT*0.75)
        model_text_1_continius = Text("– кусочно-постоянный процесс с n состояниями:", font_size=28, fill_color="#343434")
        model_text_1_continius.next_to(model_text_1, RIGHT, buff=0.1)
        state_text = MathTex("S_1, S_2, ..., S_n", color="#343434")
        state_text.next_to(model_text_1_continius, RIGHT,buff=0.1)
        self.play(Write(model_text_1), Write(model_text_1_continius))
        self.play(Write(state_text))

        self.wait()
        self.next_slide()

        lambda_text_1 = Text("Если ", font_size=28, fill_color="#343434")
        lambda_text_1.to_edge(UP*6 + LEFT*0.75)
        self.play(Write(lambda_text_1))
        lambda_text_2 = MathTex(r"\lambda(t)=\lambda_i,", color="#343434")
        lambda_text_2.next_to(lambda_text_1, RIGHT, buff=0.1)
        lambda_text_3 = Text("то имеет место i-ое состояние процесса ", font_size=28, fill_color="#343434")
        lambda_text_3.next_to(lambda_text_2, RIGHT, buff=0.1)
        self.play(Write(lambda_text_2))
        self.play(Write(lambda_text_3))

        self.wait()
        self.next_slide()

        lambda_text_4 = MathTex(r"\lambda(t), i = 1,2,...,n; \lambda_1>\lambda_2>...>\lambda_n", color="#343434")
        lambda_text_4.to_edge(DOWN*7.5 + LEFT*0.75)
        self.play(Write(lambda_text_4))

        self.wait()
        self.next_slide()

        lambda_text_5 = MathTex(r"F_i^{(1)}(t) = 1-e^{-\lambda_it}, F_i^{(2)}(t)=1-e^{-\alpha_it}", color="#343434")
        lambda_text_5.to_edge(DOWN*5.75 + LEFT*0.75)
        self.play(Write(lambda_text_5))

        self.wait()
        self.next_slide()

        lambda_text_6 = MathTex(r"P_1^{(1)}(\lambda_j|\lambda_i), P_1^{(2)}(\lambda_j|\lambda_i), i,j=\overline{1,n}", color="#343434")
        lambda_text_6.to_edge(DOWN*4 + LEFT*0.75)
        self.play(Write(lambda_text_6))

        self.wait()
        self.next_slide()

        lambda_text_7 = MathTex(r"\sum_{i=1}^nP_1^{(1)}(\lambda_j|\lambda_i)=1, j=\overline{1,n}; \sum_{i=1}^nP_1^{(2)}(\lambda_j|\lambda_i)=1, j=\overline{1,n}",
                                 color="#343434")
        lambda_text_7.to_edge(DOWN + LEFT*0.75)
        self.play(Write(lambda_text_7))

        self.wait()
        self.next_slide()

        self.play(Unwrite(model_title), Unwrite(model_title_ul), Unwrite(model_text_1), Unwrite(model_text_1_continius),
                  Unwrite(state_text), Unwrite(lambda_text_1), Unwrite(lambda_text_2), Unwrite(lambda_text_3), Unwrite(lambda_text_4),
                  Unwrite(lambda_text_5), Unwrite(lambda_text_6), Unwrite(lambda_text_7))

        slide_4 = Text("4", font_size=20, fill_color="#343434")
        slide_4.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_4))

        imitation_title = Text("Метод обратных функций", font_size=36, weight=BOLD, fill_color="#343434")
        imitation_title.to_edge(UP, buff=0.1)
        imitation_title_ul = Underline(imitation_title, color="#343434")
        self.play(Write(imitation_title), Write(imitation_title_ul))

        imitation_modeling = Text(
            "Имитационное моделирование представляет собой метод исследования сложных систем путем\nих воспроизведения"
            "в виде компьютерных моделей. "
            "Имитационное моделирование является\nмощным инструментом анализа сложных систем, позволяя воспроизводить их поведение с учетом\n"
            "вероятностных характеристик. Одним из ключевых методов генерации "
            "случайных событий в таких\nмоделях является метод обратных функций", font_size=20, fill_color="#343434")
        imitation_modeling.to_edge(UP * 2 + LEFT)
        self.play(Write(imitation_modeling))
        self.wait()
        self.next_slide()

        reverse_function = Text("Применение метода обратных функций включает следующие этапы:", font_size=20,
                                fill_color="#343434")
        reverse_function.next_to(imitation_modeling, DOWN, buff=0.1)
        self.play(Write(reverse_function))
        self.wait()
        block_1 = Text("1) Генерация случайного числа U из равномерного распределения [0;1]", font_size=20,
                       fill_color="#343434")
        block_1.next_to(reverse_function, DOWN, buff=0.1)
        block_1.shift(LEFT * 2)
        self.play(Write(block_1))
        self.wait()
        self.next_slide()
        block_2 = Text("2) Вычисление значения", font_size=20, fill_color="#343434")
        block_2.next_to(block_1, DOWN, buff=0.1)
        block_2.shift(LEFT * 2.9)
        block_2_continius = MathTex(r"X=F^{-1}(U)", fill_color="#343434").scale(0.5)
        block_2_continius.next_to(block_2, RIGHT, buff=0.1)
        self.play(Write(block_2))
        self.play(Write(block_2_continius))
        self.wait()
        self.next_slide()
        block_3 = Text("3) Использование полученного значения X в моделировании системы", font_size=20,
                       fill_color="#343434")
        block_3.next_to(block_2, DOWN, buff=0.1)
        block_3.shift(RIGHT * 2.9)
        self.play(Write(block_3))
        self.wait()
        self.next_slide()
        block_4 = Text(
            "Применение метода обратных функций для получения случайной величины, распределенной\nэкспоненциально:",
            font_size=20, fill_color="#343434")
        block_4.next_to(block_3, DOWN, buff=0.2)
        block_4.shift(RIGHT * 1.5)
        self.play(Write(block_4))
        self.wait()
        self.next_slide()
        block_5 = Text("1) Генерируется равномерно распределенное случайное число U на отрезке [0;1)", font_size=20,
                       fill_color="#343434")
        block_5.next_to(block_4, DOWN, buff=0.1)
        block_5.shift(LEFT * 0.75)
        self.play(Write(block_5))
        self.wait()
        self.next_slide()
        block_6 = MathTex(r"2) t=F^{-1}(U), t=-\frac{1}{\theta_i}ln(1-U), \theta_i \in \{\lambda_i,\alpha_i\}",
                          fill_color="#343434").scale(0.6)
        block_6.next_to(block_5, DOWN, buff=0.1)
        block_6.shift(LEFT * 2.2)
        self.play(Write(block_6))
        self.wait()
        self.next_slide()
        block_7 = Text("Таким образом, получается случайная величина t, распределенная по экспоненциальному закону",
                       font_size=20, fill_color="#343434")
        block_7.next_to(block_6, DOWN, buff=0.2)
        block_7.shift(RIGHT * 3.25)
        self.play(Write(block_7))
        self.wait()
        self.next_slide()
        self.play(Unwrite(imitation_title), Unwrite(imitation_title_ul), Unwrite(imitation_modeling),
                  Unwrite(reverse_function),
                  Unwrite(block_1), Unwrite(block_2), Unwrite(block_2_continius), Unwrite(block_3), Unwrite(block_4),
                  Unwrite(block_5), Unwrite(block_6), Unwrite(block_7))

        slide_5 = Text("5", font_size=20, fill_color="#343434")
        slide_5.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_5))

        stream_title = Text("Формирование наблюдаемого потока событий", font_size=36, weight=BOLD, fill_color="#343434")
        stream_title.to_edge(UP, buff=0.5)
        stream_title_ul = Underline(stream_title, color="#343434")
        self.play(Write(stream_title), Write(stream_title_ul))

        axes = Axes(
            x_range=[0, 12],
            y_range=[0, 6],
            x_length=10,
            y_length=5,
            axis_config={"include_ticks": False, "color": BLACK},
        )

        self.play(Create(axes), run_time=2)

        x_ticks = [2, 3.6, 5, 6.5, 8, 9.7]
        y_ticks = [4.5, 3, 1]

        x_tick_marks = VGroup()
        for i in x_ticks:
            x_tick_marks.add(axes.get_x_axis().get_tick(i))

        x_labels = VGroup()
        for j in range(len(x_ticks)):
            x_labels.add(MathTex(f"t_{j + 1}", color=BLACK).next_to(axes.c2p(x_ticks[j], 0), DOWN, buff=0.2))

        y_tick_marks = VGroup()
        for i in y_ticks:
            y_tick_marks.add(axes.get_y_axis().get_tick(i))

        y_labels = VGroup()
        for j in range(len(y_ticks)):
            y_labels.add(
                MathTex(r"\lambda_" + str(j + 1), color=BLACK).next_to(axes.c2p(0, y_ticks[j]), LEFT, buff=0.2))

        self.play(Create(y_tick_marks), Write(y_labels), run_time=2)

        horizontal_line = VGroup(Line(axes.c2p(0, y_ticks[0]), axes.c2p(x_ticks[0], y_ticks[0]),
                                      color=BLACK, stroke_width=4))
        vertical_line = VGroup(DashedLine(axes.c2p(x_ticks[0], 0), axes.c2p(x_ticks[0], y_ticks[0]),
                                          color=BLACK, dashed_ratio=0.5, stroke_width=2))

        self.wait()
        self.next_slide()
        self.play(y_labels[0].animate.scale(1.5), run_time=0.5)
        self.play(y_labels[0].animate.scale(1/1.5), run_time=0.5)

        rand_x = MathTex(r"x_1=rand[0;1), x_2=rand[0;1)", color="#343434")
        rand_x.to_edge(UP*3 + RIGHT)
        text_eta_1 = MathTex(r"\eta^{(1)}=-\frac{1}{\lambda_1}ln(1-x_1)", color="#343434")
        text_eta_1.to_edge(UP*4.5 + RIGHT)
        text_eta_2 = MathTex(r"\eta^{(2)}=-\frac{1}{\alpha_1}ln(1-x_2)", color="#343434")
        text_eta_2.to_edge(UP*7 + RIGHT)
        self.play(Write(rand_x), Write(text_eta_1), Write(text_eta_2))

        self.wait()
        self.next_slide()

        self.play(Unwrite(rand_x), Unwrite(text_eta_1), Unwrite(text_eta_2))
        text_eta = MathTex(r"\eta=", color="#343434")
        text_eta.to_edge(UP*3 + RIGHT*7)
        text_eta_continius = MathTex(r"min(\eta^{(1)},\eta{(2)})", color="#343434")
        text_eta_continius.to_edge(UP*2.5 + RIGHT*0.5)
        self.play(Write(text_eta), Write(text_eta_continius))
        text_eta_transform = MathTex(r"\eta^{(1)}", color="#343434")
        text_eta_transform.to_edge(UP*2.5 + RIGHT*5)
        self.wait()
        self.next_slide()
        self.play(Transform(text_eta_continius, text_eta_transform))

        self.play(Create(horizontal_line), Create(vertical_line))
        self.play(Create(x_tick_marks[0]), Write(x_labels[0]))
        brace = Brace(horizontal_line, direction=UP, color=BLACK, buff=0.1)
        label = brace.get_text(r"$\eta$").set_color(BLACK)

        self.play(GrowFromCenter(brace), Write(label))

        self.wait()
        self.next_slide()

        self.play(ShrinkToCenter(brace), Unwrite(label), Unwrite(text_eta), Unwrite(text_eta_continius))


        count_duplicate_state = 0
        tmp = 0
        y_current = y_ticks[0]
        y_for_check = random.choice(y_ticks)

        transition_text = VGroup(MathTex(r"P_1^{(1)}(\lambda_" + str(y_ticks.index(y_for_check) + 1) + r"|\lambda_1)", color="#343434").scale(0.55))
        transition_text[0].next_to(vertical_line[0].get_end(), UP, buff=0.1)
        self.play(Write(transition_text[0]))
        self.wait()
        self.next_slide()

        for j in range(len(x_ticks)):
            if j == 0:
                continue

            y_next = y_for_check
            horizontal_line_for = Line(axes.c2p(x_ticks[tmp], y_next), axes.c2p(x_ticks[j], y_next),
                                       color=BLACK, stroke_width=4)
            horizontal_line.add(horizontal_line_for)
            self.play(Create(horizontal_line_for))
            if y_next > y_current:
                vertical_line_2 = DashedLine(axes.c2p(x_ticks[tmp], 0), axes.c2p(x_ticks[tmp], y_next),
                                             color=BLACK, dashed_ratio=0.5, stroke_width=2)
                vertical_line.add(vertical_line_2)
                self.play(Create(vertical_line_2))
                self.play(Create(x_tick_marks[tmp]), Write(x_labels[tmp]))

                y_for_check = random.choice(y_ticks)
                if y_for_check == y_next:
                    count_duplicate_state += 1
                    if count_duplicate_state == 3:
                        while y_for_check == y_next:
                            y_for_check = random.choice(y_ticks)
                        count_duplicate_state = 0

                transition_text.add(MathTex(r"P_1^{(" + str(random.randint(1,2)) + r")}(\lambda_" + str(y_ticks.index(y_next) + 1)
                                            + r"|\lambda_" + str(y_ticks.index(y_current) + 1) + ")", color="#343434").scale(0.5))
                if(j == 2):
                    transition_text[-1].scale(0.9)

                transition_text[-1].next_to(horizontal_line[j-1].get_end(), RIGHT, buff=0)
                self.play(Write(transition_text[-1]))

                if (y_for_check <= y_next) or (j == len(x_ticks) - 1):
                    vertical_line_1 = DashedLine(axes.c2p(x_ticks[j], 0), axes.c2p(x_ticks[j], y_next),
                                                 color=BLACK, dashed_ratio=0.5, stroke_width=2)
                    vertical_line.add(vertical_line_1)
                    self.play(Create(vertical_line_1))
                    self.play(Create(x_tick_marks[j]), Write(x_labels[j]))

                    transition_text.add(MathTex(r"P_1^{(" + str(random.randint(1,2)) + r")}(\lambda_" + str(y_ticks.index(y_for_check) + 1)
                                                + r"|\lambda_" + str(y_ticks.index(y_next) + 1) + ")",
                                                color="#343434").scale(0.5))
                    transition_text[-1].next_to(vertical_line[-1].get_end(), UP, buff=0.1)
                    if (j != (len(x_ticks) - 1)):
                        self.play(Write(transition_text[-1]))
            else:
                y_for_check = random.choice(y_ticks)
                if y_for_check == y_next:
                    count_duplicate_state += 1
                    if count_duplicate_state == 3:
                        while y_for_check == y_next:
                            y_for_check = random.choice(y_ticks)
                        count_duplicate_state = 0

                if (y_for_check <= y_next) or (j == len(x_ticks) - 1):
                    vertical_line_1 = DashedLine(axes.c2p(x_ticks[j], 0), axes.c2p(x_ticks[j], y_next),
                                                 color=BLACK, dashed_ratio=0.5, stroke_width=2)
                    vertical_line.add(vertical_line_1)
                    self.play(Create(vertical_line_1))
                    self.play(Create(x_tick_marks[j]), Write(x_labels[j]))

                    transition_text.add(MathTex(r"P_1^{(" + str(random.randint(1,2)) + r")}(\lambda_" + str(y_ticks.index(y_for_check) + 1)
                                                + r"|\lambda_" + str(y_ticks.index(y_next) + 1) + ")",
                                                color="#343434").scale(0.5))
                    transition_text[-1].next_to(vertical_line[-1].get_end(), UP, buff=0.1)
                    if (j != (len(x_ticks) - 1)):
                        self.play(Write(transition_text[-1]))
            y_current = y_next
            tmp = j

        self.wait()
        self.next_slide()

        slide_6 = Text("6", font_size=20, fill_color="#343434")
        slide_6.to_corner(DR, buff=0.1)
        self.play(Uncreate(vertical_line), Uncreate(horizontal_line), Uncreate(x_tick_marks), Uncreate(y_tick_marks),
                  Unwrite(x_labels), Unwrite(y_labels), Unwrite(axes), Unwrite(transition_text), Transform(slide_1, slide_6))

        stream_img = ImageMobject("img/streamExample.jpg").scale(2)
        stream_img_rect = SurroundingRectangle(stream_img, color="#343434", buff=0.2)
        self.play(FadeIn(stream_img), Create(stream_img_rect))

        self.wait()
        self.next_slide()

        slide_7 = Text("7", font_size=20, fill_color="#343434")
        slide_7.to_corner(DR, buff=0.1)

        self.play(Unwrite(stream_title), Unwrite(stream_title_ul), Transform(slide_1, slide_7), FadeOut(stream_img), Uncreate(stream_img_rect))

        schem_title = Text("Блок-схема имитацинной модели", font_size=36, weight=BOLD, fill_color="#343434")
        schem_title.to_edge(UP, buff=0.1)
        schem_title_ul = Underline(schem_title, color="#343434")

        self.play(Write(schem_title), Write(schem_title_ul))

        schem_img = ImageMobject("img/schem.png").scale(0.65).shift(DOWN*0.4)


        self.play(FadeIn(schem_img))

        self.wait()
        self.next_slide()

        slide_8 = Text("8", font_size=20, fill_color="#343434")
        slide_8.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_8))

        self.play(FadeOut(schem_img))

        schem_img_1 = ImageMobject("img/schem_1.png").scale(2)

        self.play(FadeIn(schem_img_1))

        self.wait()
        self.next_slide()
        self.play(FadeOut(schem_img_1))

        slide_9 = Text("7", font_size=20, fill_color="#343434")
        slide_9.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_9))

        schem_img_2 = ImageMobject("img/schem_2.png").scale(1.75)

        self.play(FadeIn(schem_img_2))

        self.wait()
        self.next_slide()
        self.play(FadeOut(schem_img_2))

        slide_10 = Text("10", font_size=20, fill_color="#343434")
        slide_10.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_10))

        schem_img_3 = ImageMobject("img/schem_3.png").scale(1.75)

        self.play(FadeIn(schem_img_3))
        self.wait()
        self.next_slide()

        self.play(FadeOut(schem_img_3))

        slide_11 = Text("11", font_size=20, fill_color="#343434")
        slide_11.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_11))

        schem_img_4 = ImageMobject("img/schem_4.png").scale(1.75)

        self.play(FadeIn(schem_img_4))

        self.wait()
        self.next_slide()
        self.play(FadeOut(schem_img_4))

        slide_12 = Text("12", font_size=20, fill_color="#343434")
        slide_12.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_12))

        schem_img_5 = ImageMobject("img/schem_5.png")

        self.play(FadeIn(schem_img_5))
        self.wait()
        self.next_slide()

        self.play(FadeOut(schem_img_5), Unwrite(schem_title), Unwrite(schem_title_ul))
        self.wait()

        gui_app_title = Text("GUI-приложение имитационной модели", font_size=36, weight=BOLD, fill_color="#343434")
        gui_app_title.to_edge(UP, buff=0.1)
        gui_app_title_ul = Underline(gui_app_title, color="#343434")
        self.play(Write(gui_app_title), Write(gui_app_title_ul))

        slide_13 = Text("13", font_size=20, fill_color="#343434")
        slide_13.to_corner(DR, buff=0.1)

        self.play(Transform(slide_1, slide_13))

        win_img = ImageMobject("img/win.png").scale(0.75).shift(DOWN*0.25)
        win_img_rect = SurroundingRectangle(win_img, color="#343434", buff=0.2)
        self.play(FadeIn(win_img), Create(win_img_rect))

        self.wait()
        self.next_slide()

        self.play(FadeOut(win_img), Uncreate(win_img_rect))

        slide_14 = Text("14", font_size=20, fill_color="#343434")
        slide_14.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_14))

        example_img = ImageMobject("img/example.png").scale(0.85).shift(DOWN*0.5)
        example_img_rect = SurroundingRectangle(example_img, color="#343434", buff=0.2)
        self.play(FadeIn(example_img), Create(example_img_rect))

        self.wait()
        self.next_slide()

        self.play(FadeOut(example_img), Uncreate(example_img_rect), Unwrite(gui_app_title), Unwrite(gui_app_title_ul))

        slide_15 = Text("15", font_size=20, fill_color="#343434")
        slide_15.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_15))

        experiment_1_title = Text("1 статистический эксперимент", font_size=36, weight=BOLD, fill_color="#343434")
        experiment_1_title.to_edge(UP, buff=0.1)
        experiment_1_title_ul = Underline(experiment_1_title, color="#343434")
        self.play(Write(experiment_1_title), Write(experiment_1_title_ul))

        experiment_body_1 = Text(
            "Этапы эксперимента:\n1)для фиксированного набора параметров, вероятностей переходов и длительности\n"
            "времени наблюдения за потоком моделируется обобщенный синхронный поток событий\nвторого порядка с произвольным числом состояний;",
            font_size=20, fill_color="#343434")
        experiment_body_1.to_edge(UP * 2 + LEFT)
        self.play(Write(experiment_body_1))

        self.wait()
        self.next_slide()

        experiment_body_2 = Text("2)осуществляется расчет длительности пребывания процесса в i-ом состоянии системы: ",
                                 font_size=20, fill_color="#343434")
        experiment_body_2.next_to(experiment_body_1, DOWN, buff=0.1)
        experiment_body_2_continius = MathTex(r"T_i^{(j)}, i=\overline{1,n}, j=\overline{1,n}", font_size=22,
                                              color="#343434")
        experiment_body_2_continius.next_to(experiment_body_2, RIGHT, buff=0.1)
        self.play(Write(experiment_body_2))
        self.play(Write(experiment_body_2_continius))

        self.wait()
        self.next_slide()

        experiment_body_3 = Text("3)повторяем N раз шаги 1, 2", font_size=20, fill_color="#343434")
        experiment_body_3.next_to(experiment_body_2, DOWN, buff=0.1)
        experiment_body_3.shift(LEFT * 4)
        self.play(Write(experiment_body_3))

        self.wait()
        self.next_slide()

        experiment_body_4 = Text(
            "Вычисляем выборочные средние (оценки) значения длительностей пребывания процесса\nв i-ом состоянии:",
            font_size=20, fill_color="#343434")
        experiment_body_4.next_to(experiment_body_3, DOWN)
        experiment_body_4.shift(RIGHT * 4.1)
        self.play(Write(experiment_body_4))

        experiment_body_5 = MathTex(r"\hat{T}_i=\frac{1}{N}\sum_{j=1}^{N}T_i^{(j)}, i=\overline{1,n}", font_size=28,
                                    color="#343434")
        experiment_body_5.to_edge(ORIGIN + DOWN * 6)
        experiment_body_5_rect = SurroundingRectangle(experiment_body_5, color="#343434", buff=0.2)
        self.play(Write(experiment_body_5), Create(experiment_body_5_rect))

        self.wait()
        self.next_slide()

        # Заголовок таблицы
        title_1 = Text(
            "Вероятности переходов по первой случайной величине",
            font_size=14,
            color="#343434"
        ).to_edge(UP, buff=0.3)

        # Данные ячеек — передаём чистые строки,
        #    но Table обернёт их в MathTex:
        table_data_1 = [
            [r"P_1^{(1)}(\lambda_1|\lambda_1)=0.5",
             r"P_1^{(1)}(\lambda_1|\lambda_2)=0.4",
             r"P_1^{(1)}(\lambda_1|\lambda_3)=0.1",
             r"P_1^{(1)}(\lambda_1|\lambda_4)=0.3"],
            [r"P_1^{(1)}(\lambda_2|\lambda_1)=0.125",
             r"P_1^{(1)}(\lambda_2|\lambda_2)=0.2",
             r"P_1^{(1)}(\lambda_2|\lambda_3)=0.5",
             r"P_1^{(1)}(\lambda_2|\lambda_4)=0.5"],
            [r"P_1^{(1)}(\lambda_3|\lambda_1)=0.125",
             r"P_1^{(1)}(\lambda_3|\lambda_2)=0.2",
             r"P_1^{(1)}(\lambda_3|\lambda_3)=0.2",
             r"P_1^{(1)}(\lambda_3|\lambda_4)=0.1"],
            [r"P_1^{(1)}(\lambda_4|\lambda_1)=0.25",
             r"P_1^{(1)}(\lambda_4|\lambda_2)=0.2",
             r"P_1^{(1)}(\lambda_4|\lambda_3)=0.2",
             r"P_1^{(1)}(\lambda_4|\lambda_4)=0.1"],
        ]

        # Подписи столбцов — сразу MathTex
        col_labels_1 = [
            MathTex(r"\lambda_1=4,\ \alpha_1=4", font_size=40, color="#343434"),
            MathTex(r"\lambda_2=2,\ \alpha_2=2", font_size=40, color="#343434"),
            MathTex(r"\lambda_3=1,\ \alpha_3=0.7", font_size=40, color="#343434"),
            MathTex(r"\lambda_4=0.5,\ \alpha_4=1.6", font_size=40, color="#343434"),
        ]

        # Строим таблицу
        table_1 = MathTable(
            table_data_1,
            col_labels=col_labels_1,
            include_outer_lines=True,
            line_config={
                "stroke_color": "#343434",
                "stroke_width": 2,  # при желании можно прописать толщину
            },
            top_left_entry=MathTex("", font_size=40, color="#343434"),
            # оборачивать каждую ячейку в MathTex
            element_to_mobject=MathTex,
            element_to_mobject_config={
                "font_size": 40,
                "color": "#343434",
            },
        )
        table_1.scale(0.35).shift(LEFT * 3.5 + DOWN * 2.5)
        title_1.next_to(table_1, DOWN, buff=0.1)

        # Заголовок таблицы
        title_2 = Text(
            "Вероятности переходов по второй случайной величине",
            font_size=14,
            color="#343434"
        ).to_edge(UP, buff=0.3)

        # Данные ячеек — передаём чистые строки,
        #    но Table обернёт их в MathTex:
        table_data_2 = [
            [r"P_1^{(1)}(\lambda_1|\lambda_1)=0.2",
             r"P_1^{(1)}(\lambda_1|\lambda_2)=0.125",
             r"P_1^{(1)}(\lambda_1|\lambda_3)=0.6",
             r"P_1^{(1)}(\lambda_1|\lambda_4)=0.25"],
            [r"P_1^{(1)}(\lambda_2|\lambda_1)=0.5",
             r"P_1^{(1)}(\lambda_2|\lambda_2)=0.5",
             r"P_1^{(1)}(\lambda_2|\lambda_3)=0.15",
             r"P_1^{(1)}(\lambda_2|\lambda_4)=0.25"],
            [r"P_1^{(1)}(\lambda_3|\lambda_1)=0.15",
             r"P_1^{(1)}(\lambda_3|\lambda_2)=0.125",
             r"P_1^{(1)}(\lambda_3|\lambda_3)=0.15",
             r"P_1^{(1)}(\lambda_3|\lambda_4)=0.125"],
            [r"P_1^{(1)}(\lambda_4|\lambda_1)=0.15",
             r"P_1^{(1)}(\lambda_4|\lambda_2)=0.25",
             r"P_1^{(1)}(\lambda_4|\lambda_3)=0.1",
             r"P_1^{(1)}(\lambda_4|\lambda_4)=0.375"],
        ]

        # Подписи столбцов — сразу MathTex
        col_labels_2 = [
            MathTex(r"\lambda_1=4,\ \alpha_1=4", font_size=40, color="#343434"),
            MathTex(r"\lambda_2=2,\ \alpha_2=2", font_size=40, color="#343434"),
            MathTex(r"\lambda_3=1,\ \alpha_3=0.7", font_size=40, color="#343434"),
            MathTex(r"\lambda_4=0.5,\ \alpha_4=1.6", font_size=40, color="#343434"),
        ]

        # Строим таблицу
        table_2 = MathTable(
            table_data_2,
            col_labels=col_labels_2,
            include_outer_lines=True,
            line_config={
                "stroke_color": "#343434",
                "stroke_width": 2,  # при желании можно прописать толщину
            },
            top_left_entry=MathTex("", font_size=40, color="#343434"),
            # оборачивать каждую ячейку в MathTex
            element_to_mobject=MathTex,
            element_to_mobject_config={
                "font_size": 40,
                "color": "#343434",
            },
        )
        table_2.scale(0.35).shift(RIGHT * 3.5 + DOWN * 2.5)
        title_2.next_to(table_2, DOWN, buff=0.1)

        # Анимация
        self.play(Write(title_1), Write(title_2))
        self.play(Write(table_1), Write(table_2), run_time=3)
        self.wait()
        self.next_slide()

        self.play(Unwrite(experiment_1_title), Unwrite(experiment_1_title_ul), Unwrite(experiment_body_1),
                  Unwrite(experiment_body_2),
                  Unwrite(experiment_body_2_continius), Unwrite(experiment_body_3), Unwrite(experiment_body_4),
                  Unwrite(experiment_body_5), Unwrite(experiment_body_5_rect), Unwrite(title_1),
                  Unwrite(title_2), Unwrite(table_1), Unwrite(table_2))

        slide_16 = Text("16", font_size=20, fill_color="#343434")
        slide_16.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_16))

        result_title = Text("График зависимости", font_size=36, color="#343434")
        result_title.to_edge(UP + LEFT * 25, buff=0.1)
        result_title_1 = MathTex(r"\hat{T}_1", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        result_title_2 = Text("от значений", font_size=36, color="#343434").next_to(result_title, RIGHT,
                                                                                    buff=0.8).shift(UP * 0.06)
        result_title_3 = MathTex(r"N", color="#343434").next_to(result_title_2, RIGHT, buff=0.2)
        title = VGroup(result_title, result_title_1, result_title_2, result_title_3)
        result_title_ul = Underline(title, color="#343434")
        self.play(Write(title), Write(result_title_ul))

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[23, 26, 0.5],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        x_label = MathTex("N", color="#343434").next_to(axes.x_axis.get_end(), RIGHT + DOWN, buff=0.2)
        y_label = MathTex("\\hat{T}_1", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        # 2) Метки по Y (до 25.5, чтобы не рисовать 26.0 прямо на стрелке)
        y_values = np.arange(23, 26, 0.5)  # [23.0, 23.5, …, 25.5]
        y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                          .scale(0.6)
                          .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in y_values
        ])
        y_labels.set_opacity(1)

        # 3) Падающие точки
        x_vals = list(range(50, 1001, 50))
        y_vals = [24.3, 24.35, 24.35, 24.5, 24.15, 24.1, 23.9, 24.2,
                  24.15, 24.2, 23.9, 24.35, 23.9, 24.05, 23.8, 24.05,
                  23.95, 24.15, 24.1, 24.1]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        # 4) Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        # 5) Анимация
        self.play(Create(axes), run_time=1)
        self.play(FadeIn(y_label, shift=LEFT), FadeIn(x_label, shift=DOWN), run_time=1)
        self.play(FadeIn(y_labels, shift=LEFT, lag_ratio=0.1), run_time=1)

        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=0.5
        )
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()


        # результат 2
        new_result_title_1 = MathTex(r"\hat{T}_2", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=0.5)
        self.play(Transform(result_title_1, new_result_title_1))
        self.remove(axes, y_labels, x_ticks, x_labels)

        slide_17 = Text("17", font_size=20, fill_color="#343434")
        slide_17.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_17))

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[51, 54, 0.5],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        y_label = MathTex("\\hat{T}_2", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(51, 54, 0.5)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                              .scale(0.6)
                              .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [52.56, 52.38, 51.98, 52.20, 52.22, 52.28, 51.85, 52.40, 51.85, 52.22, 52.28, 52.15, 52.23, 52.05,
                  52.30, 52.30, 52.15, 52.10, 52.03, 52.02]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=1)
        self.play(Write(y_label), Write(x_label), run_time=0.5)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=0.5)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()

        # 3 результат
        new_result_title_1 = MathTex(r"\hat{T}_3", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=0.5)
        self.play(Transform(result_title_1, new_result_title_1))
        self.remove(axes, y_labels, x_ticks, x_labels)

        slide_18 = Text("18", font_size=20, fill_color="#343434")
        slide_18.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_18))

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[53, 57, 0.5],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        y_label = MathTex("\\hat{T}_3", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(53, 57, 0.5)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                              .scale(0.6)
                              .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [56.4, 53.85, 55.80, 55.60, 55.20, 54.90, 55.70, 55.70, 54.85, 55.10, 55.05, 54.95, 55.27, 55.40,
                  55.35, 55.35, 55.15, 55.20, 55.10, 55.15]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=1)
        self.play(Write(y_label), Write(x_label), run_time=0.5)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=0.5)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()


        # 4 результат
        new_result_title_1 = MathTex(r"\hat{T}_4", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=0.5)
        self.play(Transform(result_title_1, new_result_title_1))
        self.remove(axes, y_labels, x_ticks, x_labels)

        slide_19 = Text("19", font_size=20, fill_color="#343434")
        slide_19.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_19))

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[66, 70, 0.5],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        y_label = MathTex("\\hat{T}_4", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(66, 70, 0.5)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                              .scale(0.6)
                              .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [
            66.75, 69.40, 67.85, 67.70, 68.45, 68.75, 68.55, 68.55, 69.20, 68.55,
            68.75, 68.65, 68.55, 68.45, 68.70, 68.75, 68.30, 68.30, 68.75, 68.80
        ]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=1)
        self.play(Write(y_label), Write(x_label), run_time=0.5)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=0.5)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()

        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=0.5)
        self.remove(axes, y_labels, x_ticks, x_labels)
        self.play(Unwrite(title), Unwrite(result_title_ul))

        slide_20 = Text("20", font_size=20, fill_color="#343434")
        slide_20.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_20))

        experiment_2_title = Text("2 статистический эксперимент", font_size=36, weight=BOLD, fill_color="#343434")
        experiment_2_title.to_edge(UP, buff=0.1)
        experiment_2_title_ul = Underline(experiment_2_title, color="#343434")
        self.play(Write(experiment_2_title), Write(experiment_2_title_ul))

        experiment_2 = Text(
            "Изменим вероятности переходов по первой и второй случайной величине, \nтак чтобы вероятность оказаться в первом состоянии была максимальна",
            font_size=20, fill_color="#343434")
        experiment_2.to_edge(UP * 2 + LEFT)
        self.play(Write(experiment_2))
        self.wait()
        self.next_slide()

        # Заголовок таблицы
        title_1 = Text(
            "Вероятности переходов по первой случайной величине",
            font_size=14,
            color="#343434"
        ).to_edge(UP, buff=0.3)

        table_data_1 = [
            [r"P_1^{(1)}(\lambda_1|\lambda_1)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_2)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_3)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_4)=0.97"],
            [r"P_1^{(1)}(\lambda_2|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_4)=0.01"],
            [r"P_1^{(1)}(\lambda_3|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_4)=0.01"],
            [r"P_1^{(1)}(\lambda_4|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_4)=0.01"],
        ]

        # Подписи столбцов — сразу MathTex
        col_labels_1 = [
            MathTex(r"\lambda_1=4,\ \alpha_1=4", font_size=40, color="#343434"),
            MathTex(r"\lambda_2=2,\ \alpha_2=2", font_size=40, color="#343434"),
            MathTex(r"\lambda_3=1,\ \alpha_3=0.7", font_size=40, color="#343434"),
            MathTex(r"\lambda_4=0.5,\ \alpha_4=1.6", font_size=40, color="#343434"),
        ]

        # Строим таблицу
        table_1 = MathTable(
            table_data_1,
            col_labels=col_labels_1,
            include_outer_lines=True,
            line_config={
                "stroke_color": "#343434",
                "stroke_width": 2,  # при желании можно прописать толщину
            },
            top_left_entry=MathTex("", font_size=40, color="#343434"),
            # оборачивать каждую ячейку в MathTex
            element_to_mobject=MathTex,
            element_to_mobject_config={
                "font_size": 40,
                "color": "#343434",
            },
        )
        table_1.scale(0.35).shift(UP)
        title_1.next_to(table_1, DOWN, buff=0.1)

        self.play(Write(table_1), Write(title_1))

        # Заголовок таблицы
        title_2 = Text(
            "Вероятности переходов по второй случайной величине",
            font_size=14,
            color="#343434"
        ).to_edge(UP, buff=0.3)

        # Данные ячеек — передаём чистые строки,
        #    но Table обернёт их в MathTex:
        table_data_2 = [
            [r"P_1^{(1)}(\lambda_1|\lambda_1)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_2)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_3)=0.97",
             r"P_1^{(1)}(\lambda_1|\lambda_4)=0.97"],
            [r"P_1^{(1)}(\lambda_2|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_2|\lambda_4)=0.01"],
            [r"P_1^{(1)}(\lambda_3|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_3|\lambda_4)=0.01"],
            [r"P_1^{(1)}(\lambda_4|\lambda_1)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_2)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_3)=0.01",
             r"P_1^{(1)}(\lambda_4|\lambda_4)=0.01"],
        ]

        # Подписи столбцов — сразу MathTex
        col_labels_2 = [
            MathTex(r"\lambda_1=4,\ \alpha_1=4", font_size=40, color="#343434"),
            MathTex(r"\lambda_2=2,\ \alpha_2=2", font_size=40, color="#343434"),
            MathTex(r"\lambda_3=1,\ \alpha_3=0.7", font_size=40, color="#343434"),
            MathTex(r"\lambda_4=0.5,\ \alpha_4=1.6", font_size=40, color="#343434"),
        ]

        # Строим таблицу
        table_2 = MathTable(
            table_data_2,
            col_labels=col_labels_2,
            include_outer_lines=True,
            line_config={
                "stroke_color": "#343434",
                "stroke_width": 2,  # при желании можно прописать толщину
            },
            top_left_entry=MathTex("", font_size=40, color="#343434"),
            # оборачивать каждую ячейку в MathTex
            element_to_mobject=MathTex,
            element_to_mobject_config={
                "font_size": 40,
                "color": "#343434",
            },
        )
        table_2.scale(0.35).shift(DOWN * 2)
        title_2.next_to(table_2, DOWN, buff=0.1)
        self.play(Write(table_2), Write(title_2))
        self.wait()
        self.next_slide()

        self.play(Unwrite(title_1), Unwrite(title_2), Unwrite(table_1), Unwrite(table_2), Unwrite(experiment_2_title),
                  Unwrite(experiment_2_title_ul),
                  Unwrite(experiment_2), run_time=2)

        slide_21 = Text("21", font_size=20, fill_color="#343434")
        slide_21.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_21))

        result_title = Text("График зависимости", font_size=36, color="#343434")
        result_title.to_edge(UP + LEFT * 25, buff=0.1)
        result_title_1 = MathTex(r"\hat{T}_1", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        result_title_2 = Text("от значений", font_size=36, color="#343434").next_to(result_title, RIGHT,
                                                                                    buff=0.8).shift(UP * 0.06)
        result_title_3 = MathTex(r"N", color="#343434").next_to(result_title_2, RIGHT, buff=0.2)
        title = VGroup(result_title, result_title_1, result_title_2, result_title_3)
        result_title_ul = Underline(title, color="#343434")
        self.play(Write(title), Write(result_title_ul))

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[179, 182, 0.5],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        x_label = MathTex("N", color="#343434").next_to(axes.x_axis.get_end(), RIGHT + DOWN, buff=0.2)
        y_label = MathTex("\\hat{T}_1", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        # 2) Метки по Y (до 25.5, чтобы не рисовать 26.0 прямо на стрелке)
        y_values = np.arange(179, 182, 0.5)
        y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                          .scale(0.6)
                          .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in y_values
        ])
        y_labels.set_opacity(1)

        # 3) Падающие точки
        x_vals = list(range(50, 1001, 50))
        y_vals = [
            181.30, 179.90, 180.80, 180.30, 180.25, 180.60, 180.65, 180.70, 180.30, 180.35,
            180.60, 180.60, 180.80, 180.55, 180.55, 180.55, 180.30, 180.30, 180.35, 180.35
        ]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        # 4) Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        # 5) Анимация
        self.play(Create(axes), run_time=1)
        self.play(FadeIn(y_label, shift=LEFT), FadeIn(x_label, shift=DOWN), run_time=0.5)
        self.play(FadeIn(y_labels, shift=LEFT, lag_ratio=0.1), run_time=0.5)

        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=0.5
        )
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()

        # результат 2
        new_result_title_1 = MathTex(r"\hat{T}_2", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=0.5)
        self.play(Transform(result_title_1, new_result_title_1))
        self.remove(axes, y_labels, x_ticks, x_labels)

        slide_22 = Text("22", font_size=20, fill_color="#343434")
        slide_22.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_22))

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[3, 5, 0.2],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        y_label = MathTex("\\hat{T}_2", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(3, 5, 0.2)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                              .scale(0.6)
                              .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [
            3.96, 3.75, 3.58, 3.67, 3.83, 3.75, 3.78, 3.74, 3.75, 3.80,
            3.82, 3.72, 3.63, 3.68, 3.67, 3.75, 3.68, 3.69, 3.75, 3.67
        ]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=1)
        self.play(Write(y_label), Write(x_label), run_time=0.5)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=0.5)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()

        # 3 результат
        new_result_title_1 = MathTex(r"\hat{T}_3", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=0.5)
        self.play(Transform(result_title_1, new_result_title_1))
        self.remove(axes, y_labels, x_ticks, x_labels)

        slide_23 = Text("23", font_size=20, fill_color="#343434")
        slide_23.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_23))

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[8, 10, 0.2],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        y_label = MathTex("\\hat{T}_3", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(8, 10, 0.2)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                              .scale(0.6)
                              .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [
            8.38, 8.52, 8.92, 8.56, 8.78, 8.57, 8.63, 8.44, 8.80, 8.72,
            8.75, 8.65, 8.68, 8.61, 8.82, 8.83, 8.75, 8.76, 8.91, 8.88
        ]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=1)
        self.play(Write(y_label), Write(x_label), run_time=0.5)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=0.5)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()

        # 4 результат
        new_result_title_1 = MathTex(r"\hat{T}_4", color="#343434").next_to(result_title, RIGHT, buff=0.2)
        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=1)
        self.play(Transform(result_title_1, new_result_title_1))
        self.remove(axes, y_labels, x_ticks, x_labels)

        slide_24 = Text("24", font_size=20, fill_color="#343434")
        slide_24.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_24))

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[6, 9, 0.5],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        y_label = MathTex("\\hat{T}_4", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(6, 9, 0.5)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.1f}", color="#343434")
                              .scale(0.6)
                              .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [
            7.73, 7.01, 6.72, 7.08, 7.08, 6.97, 7.14, 7.15, 7.18, 7.08,
            6.94, 7.02, 6.92, 7.12, 7.06, 7.10, 7.23, 7.11, 7.15, 7.15
        ]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=1)
        self.play(Write(y_label), Write(x_label), run_time=0.5)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=0.5)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()

        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=0.5)
        self.remove(axes, y_labels, x_ticks, x_labels)
        self.play(Unwrite(title), Unwrite(result_title_ul))

        slide_25 = Text("25", font_size=20, fill_color="#343434")
        slide_25.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_25))

        experiment_3_title = Text("3 статистический эксперимент", font_size=36, fill_color="#343434")
        experiment_3_title.to_edge(UP, buff=0.5)
        experiment_3_title_ul = Underline(experiment_3_title, color="#343434")
        self.play(Write(experiment_3_title), Write(experiment_3_title_ul))

        experiment_3 = Text(
            "Этапы эксперимента:\n1)для фиксированного набора параметров, вероятностей переходов и количества\nитераций N/длительности времени "
            "моделирования реализуется обобщенный синхронный поток событий \nвторого порядка с произвольным кол-ом состояний",
            font_size=20, fill_color="#343434")
        experiment_3.to_edge(UP * 3 + LEFT)
        self.play(Write(experiment_3))
        self.wait()
        self.next_slide()

        experiment_3_1 = MathTex(r"2)\hat{\tau}_j=\frac{1}{k_j}\sum_{i=1}^{k_j}\tau_i^{(j)},j=\overline{1,N}",
                                 color="#343434",
                                 font_size=28)
        experiment_3_1.next_to(experiment_3, DOWN)
        experiment_3_1.shift(LEFT * 5.05)
        self.play(Write(experiment_3_1))
        self.wait()
        self.next_slide()

        experiment_3_2 = Text("3) осуществляем повторение N раз шагов 1, 2", font_size=20, fill_color="#343434")
        experiment_3_2.next_to(experiment_3_1, DOWN)
        experiment_3_2.shift(RIGHT * 1.2)
        self.play(Write(experiment_3_2))

        self.wait()
        self.next_slide()

        experiment_3_3 = Text(
            "Вычисляем выборочные средние (оценки) значения длительности интервала между моментами\nнаступления событий в рассматриваемом потоке:",
            font_size=20, fill_color="#343434")
        experiment_3_3.next_to(experiment_3_2, DOWN, buff=0.2)
        experiment_3_3.shift(RIGHT * 3.25)
        self.play(Write(experiment_3_3))
        self.wait()
        self.next_slide()

        experiment_3_4 = MathTex(r"\hat{\overline{\tau}}=\frac{1}{N}\sum_{j=1}^N \hat{\tau}_j", fill_color="#343434")
        experiment_3_4.next_to(experiment_3_3, DOWN, buff=0.5)
        experiment_3_4_rect = SurroundingRectangle(experiment_3_4, color="#343434", buff=0.2)

        self.play(Write(experiment_3_4), Write(experiment_3_4_rect))
        self.wait()
        self.next_slide()

        self.play(Unwrite(experiment_3_title), Unwrite(experiment_3_title_ul), Unwrite(experiment_3), Unwrite(experiment_3_1), Unwrite(experiment_3_2), Unwrite(experiment_3_3),
                  Unwrite(experiment_3_4), Unwrite(experiment_3_4_rect))

        slide_26 = Text("26", font_size=20, fill_color="#343434")
        slide_26.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_26))

        title_3 = Text("График зависимости", fill_color="#343434", font_size=36)
        title_3.to_edge(UP + LEFT * 15, buff=0.2)
        title_3_1 = MathTex(r"\hat{\overline{\tau}}", fill_color="#343434")
        title_3_1.next_to(title_3, RIGHT, buff=0.2)
        title_3_2 = Text("от значений", fill_color="#343434", font_size=36)
        title_3_2.next_to(title_3, RIGHT, buff=0.7).shift(UP * 0.06)
        title_3_3 = MathTex(r"N", fill_color="#343434")
        title_3_3.next_to(title_3_2, RIGHT, buff=0.2)
        tl = VGroup(title_3, title_3_1, title_3_2, title_3_3)
        tl_ul = Underline(tl, color="#343434", buff=0.1)
        self.play(Write(tl), Write(tl_ul))

        axes = Axes(
            x_range=[0, 1050, 100],
            y_range=[0.31, 0.32, 0.002],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        axes.y_axis.ticks[-1].set_opacity(0)
        x_label = MathTex("N", color="#343434").next_to(axes.x_axis.get_end(), RIGHT + DOWN, buff=0.2)
        y_label = MathTex(r"\hat{\overline{\tau}}", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        # 2) Метки по Y
        y_values = np.arange(0.31, 0.319, 0.002)  # [23.0, 23.5, …, 25.5]
        y_labels = VGroup(*[
            MathTex(f"{val:.3f}", color="#343434")
                          .scale(0.6)
                          .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in y_values
        ])
        y_labels.set_opacity(1)

        # 3) Падающие точки
        x_vals = list(range(50, 1001, 50))
        y_vals = [
            0.3120, 0.3130, 0.3113, 0.3132, 0.3132, 0.3120, 0.3131, 0.3134, 0.3128, 0.3127,
            0.3133, 0.3124, 0.3132, 0.3127, 0.3123, 0.3130, 0.3122, 0.3134, 0.3128, 0.3129
        ]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        # 4) Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 1001, 100)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        # 5) Анимация
        self.play(Create(axes), run_time=1)
        self.play(FadeIn(y_label, shift=LEFT), FadeIn(x_label, shift=DOWN))
        self.play(FadeIn(y_labels, shift=LEFT, lag_ratio=0.1), run_time=1)

        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=1
        )
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()


        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(Unwrite(tl), Unwrite(tl_ul), FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks), FadeOut(x_labels),
                  FadeOut(x_label), run_time=1)
        self.remove(axes, y_labels, x_ticks, x_labels)

        slide_27 = Text("27", font_size=20, fill_color="#343434")
        slide_27.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_27))

        title_3 = Text("График зависимости", fill_color="#343434", font_size=30)
        title_3.to_edge(UP + LEFT * 12, buff=0.2)
        title_3_1 = MathTex(r"\hat{\overline{\tau}}", fill_color="#343434")
        title_3_1.next_to(title_3, RIGHT, buff=0.2)
        title_3_2 = Text("от времени моделирования", fill_color="#343434", font_size=30)
        title_3_2.next_to(title_3, RIGHT, buff=0.7).shift(DOWN * 0.06)
        title_3_3 = MathTex(r"T_m", fill_color="#343434")
        title_3_3.next_to(title_3_2, RIGHT, buff=0.2)
        tl = VGroup(title_3, title_3_1, title_3_2, title_3_3)
        tl_ul = Underline(tl, color="#343434", buff=0.1)
        self.play(Write(tl), Write(tl_ul))

        axes = Axes(
            x_range=[0, 550, 50],
            y_range=[0.31, 0.32, 0.002],
            axis_config={"include_tip": True, "color": "#343434"},
        )
        axes.y_axis.ticks[-1].set_opacity(0)
        x_label = MathTex(r"T_m", color="#343434").next_to(axes.x_axis.get_end(), RIGHT + DOWN, buff=0.2)
        y_label = MathTex(r"\hat{\overline{\tau}}", color="#343434").next_to(axes.y_axis.get_end(), UP + LEFT, buff=0.2)

        new_y_values = np.arange(0.31, 0.319, 0.002)
        new_y_labels = VGroup(*[
            MathTex(f"{val:.3f}", color="#343434")
                              .scale(0.6)
                              .next_to(axes.c2p(0, val), LEFT, buff=0.2)
            for val in new_y_values
        ])
        new_y_labels.set_opacity(1)

        # Засечки и подписи по X
        x_ticks = axes.x_axis.ticks.copy()
        x_ticks.set_opacity(0)

        tick_vals = np.arange(0, 550, 50)  # 0,100,200,…1000
        x_labels = VGroup(*[
            MathTex(str(int(val)), color="#343434")
                          .scale(0.5)
                          # ставим ТОЛЬКО там, где действительно лежит ось:
                          .next_to(axes.x_axis.n2p(val), DOWN, buff=0.2)
            for val in tick_vals if val != 0
        ])
        x_labels.set_opacity(1)

        y_vals = [0.3108, 0.3121, 0.3130, 0.3128, 0.3132, 0.3127, 0.3131, 0.3130, 0.3129, 0.3130]
        points = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.07, color="#343434")
                        .save_state()
                        .shift(UP * 3)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(Create(axes), run_time=1)
        self.play(Write(y_label), Write(x_label), run_time=1)
        # показываем засечки и их подписи
        self.play(
            FadeIn(x_ticks, shift=DOWN, lag_ratio=0.1),
            FadeIn(x_labels, shift=DOWN, lag_ratio=0.1),
            run_time=1
        )
        self.play(Write(new_y_labels, lag_ratio=0.1), run_time=1)
        y_labels = new_y_labels
        # падают точки по одной
        for pt in points:
            self.play(Restore(pt), run_time=0.15)
        self.wait()
        self.next_slide()

        self.play(FadeOut(points), run_time=1)
        self.remove(points)
        self.play(Unwrite(tl), Unwrite(tl_ul), FadeOut(axes), FadeOut(y_label), FadeOut(y_labels), FadeOut(x_ticks),
                  FadeOut(x_labels), FadeOut(x_label), run_time=1)
        self.remove(axes, y_labels, x_ticks, x_labels, x_label, y_label)

        slide_28 = Text("28", font_size=20, fill_color="#343434")
        slide_28.to_corner(DR, buff=0.1)
        self.play(Transform(slide_1, slide_28))

        end_title = Text("Заключение", fill_color="#343434", font_size=36)
        end_title.to_edge(UP, buff=0.5)
        end_title_ul = Underline(end_title, color="#343434", buff=0.1)
        self.play(Write(end_title), Write(end_title_ul))

        # Список задач
        items = ["Изучена литература по теме исследования", "Построена мат. модель потока",
                 "Выведены формулы, по которым производится моделирование",
                 "Построен алгоритм имитационной модели", "Алгорит имитационной модели реализован на ЯП C++",
                 "Написано GUI-приложение", "Проведена серия статистических экспериментов"]
        # 1) квадраты
        boxes = VGroup(*[
            Square(side_length=0.4, color="#343434")
                       .set_fill(None, opacity=0)  # пока пустые
            for _ in items
        ])
        # 2) подписи
        labels = VGroup(*[
            Text(text, font_size=26, color="#343434")
            for text in items
        ])
        # 3) сгруппировать пары [квадрат + текст] и расположить вниз
        rows = VGroup(*[
            VGroup(box, lbl).arrange(RIGHT, buff=0.2)
            for box, lbl in zip(boxes, labels)
        ])
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        rows.to_edge(UP * 3 + LEFT)

        self.play(
            *[Create(box) for box in boxes],
            *[Write(lbl) for lbl in labels],
            run_time=1
        )

        checks = VGroup(
            *[
                VGroup(
                    # левая ножка галочки
                    Line(
                        box.get_corner(UL) + DOWN * 0.2 + RIGHT * 0.1,
                        box.get_center() + DOWN * 0.1
                    ),
                    # правая ножка
                    Line(
                        box.get_center() + DOWN * 0.1,
                        box.get_corner(UR) + DOWN * 0.1 + LEFT * 0.05
                    ),
                )
                .set_color("#83C167")
                .set_stroke(width=3)
                for box in boxes
            ]
        )

        self.wait()
        self.next_slide()
        self.play(Create(checks[0]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[1]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[2]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[3]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[4]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[5]), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(Create(checks[6]), run_time=0.5)


