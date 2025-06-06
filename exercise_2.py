import tkinter as tk
from tkinter import scrolledtext


class BankSystem:
    """ Класс содержит выполнение функционала программы """
    def __init__(self):
        # Данные клиента
        self.accounts = {"Ganenko": 70195323 }

    def deposit(self, name, amount):
        # Пополение счета
        self.accounts[name] = self.accounts.get(name, 0) + amount

    def withdraw(self, name, amount):
        # Снятие со счета
        self.accounts[name] = self.accounts.get(name, 0) - amount

    def balance(self, name=None):
        # Неправильный ввод клиента
        return self.accounts.get(name, "Такого клиента нет") if name else self.accounts

    def transfer(self, sender, receiver, amount):
        # Перевод средств на другой счет
        self.accounts[sender] = self.accounts.get(sender, 0) - amount
        self.accounts[receiver] = self.accounts.get(receiver, 0) + amount

    def income(self, percent):
        # Пополнение счета на процент
        for name in self.accounts:
            if self.accounts[name] > 0:
                self.accounts[name] += self.accounts[name] * percent // 100


class BankApp:
    """ Основной класс программы для графического интерфейса"""
    def __init__(self, root):
        # Загрузка компонентов графического интерфейса
        self.bank = BankSystem()
        self.root = root
        self.root.title("Банковская система")

        self.create_widgets()

    def create_widgets(self):
        # Показание графического интерфейса
        tk.Label(self.root, text="Команда:").grid(row=0, column=0, padx=5, pady=5)
        self.input_text = scrolledtext.ScrolledText(self.root, width=40, height=15)
        self.input_text.grid(row=1, column=0, padx=5, pady=5)

        tk.Label(self.root, text="Результат:").grid(row=0, column=1, padx=5, pady=5)
        self.output_text = scrolledtext.ScrolledText(self.root, width=40, height=15, state='disabled')
        self.output_text.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.root, text="Выполнить", command=self.execute_commands).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Очистить", command=self.clear_text).grid(row=2, column=1, padx=5, pady=5)

    def execute_commands(self):
        # Ввод команд и вывод результатов
        results = []
        for command in self.input_text.get("1.0", tk.END).strip().split("\n"):
            parts = command.split()
            if not parts:
                continue
            try:
                cmd, args = parts[0], parts[1:]
                if cmd == "DEPOSIT":
                    self.bank.deposit(args[0], int(args[1]))
                elif cmd == "WITHDRAW":
                    self.bank.withdraw(args[0], int(args[1]))
                elif cmd == "BALANCE":
                    results.append(f"{args[0]}: {self.bank.balance(args[0])}" if args else "\n".join(
                        f"{n}: {b}" for n, b in self.bank.balance().items()))
                elif cmd == "TRANSFER":
                    self.bank.transfer(args[0], args[1], int(args[2]))
                elif cmd == "INCOME":
                    self.bank.income(int(args[0]))
            except:
                results.append(f"Ошибка в команде: {command}")

        self.display_output("\n".join(results))

    def display_output(self, text):
        # Обновление окна
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state='disabled')

    def clear_text(self):
        # Очистка текста
        self.input_text.delete("1.0", tk.END)
        self.display_output("")


if __name__ == "__main__":
    root = tk.Tk()
    BankApp(root)
    root.mainloop()
