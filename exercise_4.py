import tkinter as tk
from random import randint


class HanoiTowerApp:
    """Графическое приложение для модифицированной задачи о Ханойских башнях."""

    def __init__(self, root):
        """Инициализация главного окна и параметров интерфейса."""
        self.root = root
        self.root.title("Ханойские башни")
        self.root.geometry("1000x550")
        self.root.resizable(False, False)

        self.canvas_width = 1000
        self.canvas_height = 480
        self.disk_thickness = 5
        self.spindles = 8
        self.student_id = "70195323"
        self.percentages = [70, 19, 53, 23]

        self.setup_ui()

    def setup_ui(self):
        """Создание элементов интерфейса приложения."""
        self.canvas = tk.Canvas(
            self.root, width=self.canvas_width, height=self.canvas_height, bg="lightgray"
        )
        self.canvas.pack()

        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=5)

        tk.Button(control_frame, text="Исходное состояние", command=self.show_start).pack(side=tk.LEFT, padx=3)
        tk.Button(control_frame, text="Конечное состояние", command=self.show_end).pack(side=tk.LEFT, padx=3)

        self.iteration_label = tk.Label(control_frame, text="Итерация: 0")
        self.iteration_label.pack(side=tk.LEFT, padx=5)

        self.percent_entries = []
        for i, percent in enumerate(self.percentages):
            percent_var = tk.StringVar(value=str(percent))
            entry = tk.Entry(control_frame, width=4, textvariable=percent_var)
            entry.pack(side=tk.LEFT, padx=2)
            self.percent_entries.append(percent_var)

            tk.Button(
                control_frame, text=f"{percent}%",
                command=lambda idx=i: self.show_iteration(idx)
            ).pack(side=tk.LEFT, padx=2)

        self.show_start()

    def init_spindles(self):
        """Рисует шпиндели для размещения дисков."""
        gap = self.canvas_width // (self.spindles + 1)
        spindle_width = 3
        self.spindle_positions = []

        for i in range(self.spindles):
            x = gap * (i + 1)
            y_top = 50
            y_bottom = self.canvas_height - 20
            self.canvas.create_line(x, y_top, x, y_bottom, width=spindle_width, fill="black")
            self.spindle_positions.append((x, y_bottom))

    def draw_disks(self):
        """Отрисовывает диски на шпинделях в исходном состоянии."""
        max_disk_width = 50
        for spindle_idx in range(self.spindles):
            num_disks = int(self.student_id[-(spindle_idx + 1)])
            x, y_bottom = self.spindle_positions[spindle_idx]

            for disk_num in range(num_disks):
                disk_width = max_disk_width - spindle_idx * 3
                y_top = y_bottom - (disk_num + 1) * (self.disk_thickness + 2)
                color = self.random_color()
                self.canvas.create_rectangle(
                    x - disk_width, y_top,
                    x + disk_width, y_top + self.disk_thickness,
                    fill=color, outline="black"
                )
                self.canvas.create_text(
                    x, y_top + self.disk_thickness / 2,
                    text=str(disk_width), fill="white", font=("Arial", 6)
                )

    def random_color(self):
        """Генерирует случайный цвет."""
        return f'#{randint(50, 200):02x}{randint(50, 200):02x}{randint(50, 200):02x}'

    def show_start(self):
        """Отображает исходное состояние дисков."""
        self.canvas.delete("all")
        self.init_spindles()
        self.draw_disks()
        self.iteration_label.config(text="Итерация: 0")

    def show_end(self):
        """Отображает правильное конечное состояние дисков."""
        self.canvas.delete("all")
        self.init_spindles()

        disks = []
        for spindle_idx in range(self.spindles):
            num_disks = int(self.student_id[-(spindle_idx + 1)])
            disks += [(self.spindles - spindle_idx) * 3] * num_disks

        disks.sort(reverse=True)

        x, y_bottom = self.spindle_positions[0]

        for disk_num, disk_width in enumerate(disks):
            y_top = y_bottom - (disk_num + 1) * (self.disk_thickness + 2)
            color = self.random_color()
            self.canvas.create_rectangle(
                x - disk_width, y_top,
                x + disk_width, y_top + self.disk_thickness,
                fill=color, outline="black"
            )
            self.canvas.create_text(
                x, y_top + self.disk_thickness / 2,
                text=str(disk_width), fill="white", font=("Arial", 6)
            )

        self.iteration_label.config(text=f"Итерация: {self.calculate_iterations()}")

    def show_iteration(self, idx):
        """Отображает количество итераций на основании процента."""
        percent = float(self.percent_entries[idx].get())
        total_iterations = self.calculate_iterations()
        current_iteration = round(total_iterations * percent / 100, 2)
        self.iteration_label.config(text=f"Итерация: {current_iteration}")

    def calculate_iterations(self):
        """Вычисляет общее число дисков (итераций)."""
        return sum(int(digit) for digit in self.student_id[-self.spindles:])


if __name__ == "__main__":
    root = tk.Tk()
    app = HanoiTowerApp(root)
    root.mainloop()
