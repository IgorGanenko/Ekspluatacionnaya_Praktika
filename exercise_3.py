import tkinter as tk
import math


class SimpleCalculator:
    """Класс, реализующий калькулятор с базовым и обновлённым расширенным функционалом."""

    def __init__(self, master):
        """Инициализация окна калькулятора и его компонентов."""
        self.master = master
        self.master.title("Расширенный калькулятор")
        self.master.geometry("500x400")
        self.master.resizable(False, False)

        self.expression = ""
        self.history = []
        self.advanced_shown = False
        self.exp_notation = False  # Для переключения F-E

        self.create_widgets()

    def create_widgets(self):
        """Создание графического интерфейса калькулятора."""
        self.display = tk.Entry(
            self.master, font=("Arial", 18), justify="right", bd=5, relief="ridge"
        )
        self.display.pack(side="top", fill="x", padx=10, pady=10)

        self.history_label = tk.Label(
            self.master, text="", anchor="e", font=("Arial", 10), fg="gray"
        )
        self.history_label.pack(side="top", fill="x", padx=10)

        button_layout = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "Расширенный"],
        ]

        for row in button_layout:
            frame = tk.Frame(self.master)
            frame.pack(fill="x", pady=2)
            for btn_text in row:
                button = tk.Button(
                    frame,
                    text=btn_text,
                    width=10,
                    height=2,
                    command=lambda txt=btn_text: self.button_click(txt),
                )
                button.pack(side="left", expand=True, padx=2)

        self.advanced_frame = tk.Frame(self.master)
        advanced_buttons = ["F–E", "y√x", "lg10"]
        for btn_text in advanced_buttons:
            button = tk.Button(
                self.advanced_frame,
                text=btn_text,
                width=10,
                height=2,
                command=lambda txt=btn_text: self.button_click(txt),
            )
            button.pack(side="left", expand=True, padx=2, pady=2)

    def button_click(self, button):
        """Обработка нажатий кнопок калькулятора."""
        if button == "=":
            self.evaluate_expression()
        elif button == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif button == "Расширенный":
            self.toggle_advanced()
        elif button in ["F–E", "y√x", "lg10"]:
            self.calculate_advanced(button)
        else:
            self.expression += button
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def evaluate_expression(self):
        """Вычисляет значение введённого выражения."""
        try:
            result = eval(self.expression)
            self.history.append(f"{self.expression} = {result}")
            self.expression = str(result)
            self.display_result(result)
            self.update_history()
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Ошибка")
            self.expression = ""

    def calculate_advanced(self, func):
        """Реализует обновлённые расширенные функции."""
        try:
            value = float(self.display.get())

            if func == "F–E":
                # Переключение между обычным и экспоненциальным представлением
                if self.exp_notation:
                    result = f"{value:.10f}".rstrip("0").rstrip(".")
                else:
                    result = "{:.6e}".format(value)
                self.exp_notation = not self.exp_notation

            elif func == "lg10":
                result = math.log10(value)

            elif func == "y√x":
                # Попросим пользователя ввести значение y
                y_window = tk.Toplevel(self.master)
                y_window.title("Введите значение y")

                label = tk.Label(y_window, text="Степень корня (y):")
                label.pack(pady=5)

                y_entry = tk.Entry(y_window)
                y_entry.pack(pady=5)

                def compute_root():
                    try:
                        y = float(y_entry.get())
                        if y == 0:
                            raise ValueError
                        root = value ** (1 / y)
                        self.display_result(root)
                        y_window.destroy()
                    except Exception:
                        self.display_result("Ошибка")
                        y_window.destroy()

                confirm = tk.Button(y_window, text="OK", command=compute_root)
                confirm.pack(pady=5)
                return  # Ждём подтверждения

            self.display_result(result)
            self.expression = str(result)
        except Exception:
            self.display_result("Ошибка")
            self.expression = ""

    def display_result(self, result):
        """Отображает результат в поле ввода."""
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)

    def toggle_advanced(self):
        """Переключает отображение расширенных функций."""
        if self.advanced_shown:
            self.advanced_frame.pack_forget()
        else:
            self.advanced_frame.pack(fill="x", pady=5)
        self.advanced_shown = not self.advanced_shown

    def update_history(self):
        """Обновляет историю вычислений."""
        self.history_label.config(text=" | ".join(self.history[-3:]))


if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
