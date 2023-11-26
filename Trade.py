import json
import random
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Валютний Трейдер")
    parser.add_argument("--cli", action="store_true", help="Запустити командний рядок (CLI)")

class ВалютнийТрейдер:
    def __init__(self):
        self.load_config()
        self.load_state()

    def load_config(self):
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
            self.delta = config["delta"]

    def load_state(self):
        try:
            with open("state.json", "r") as state_file:
                state = json.load(state_file)
                self.rate = state["rate"]
                self.uah_balance = state["uah_balance"]
                self.usd_balance = state["usd_balance"]
        except FileNotFoundError:
            self.rate = 36.00
            self.uah_balance = 10000.00
            self.usd_balance = 0.00
            self.save_state()

    def save_state(self):
        state = {
            "rate": self.rate,
            "uah_balance": self.uah_balance,
            "usd_balance": self.usd_balance
        }
        with open("state.json", "w") as state_file:
            json.dump(state, state_file, indent=2)

    def update_rate(self):
        self.rate = round(random.uniform(self.rate - self.delta, self.rate + self.delta), 2)
        self.save_state()

    def get_rate(self):
        return f"Поточний обмінний курс: {self.rate} UAH/USD"

    def get_balances(self):
        return f"Доступні баланси - USD: {self.usd_balance}, UAH: {self.uah_balance}"

    def buy(self, amount):
        cost = amount * self.rate
        if self.uah_balance >= cost:
            self.usd_balance += amount
            self.uah_balance -= cost
            self.save_state()
            return f"Успішно куплено {amount} USD за {cost:.2f} UAH. Залишок UAH балансу: {self.uah_balance:.2f}"
        else:
            return f"Неможливо виконати покупку. Потрібний баланс: {cost:.2f} UAH, доступний баланс: {self.uah_balance:.2f}"

    def sell(self, amount):
        if self.usd_balance >= amount:
            income = amount * self.rate
            self.usd_balance -= amount
            self.uah_balance += income
            self.save_state()
            return f"Успішно продано {amount} USD за {income:.2f} UAH. Залишок USD балансу: {self.usd_balance}"
        else:
            return f"Неможливо виконати продаж. Потрібний баланс: {amount:.2f} USD, доступний баланс: {self.usd_balance:.2f}"

    def get_commands(self):
        return """
        Список команд:
        NEXT - оновити обмінний курс
        RATE - отримати поточний обмінний курс
        AVAILABLE - отримати залишок балансів
        BUY <сума> - купити долари за вказаною сумою
        SELL <сума> - продати долари за вказаною сумою
        RESTART - перезапустити гру
        EXIT - завершити програму
        COMMANDS - вивести список команд
        """

if __name__ == "__main__":
    print ('''⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈ ⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿ ⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟ ⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠉⠈⠉⠀⠀⢦⡈⢻ ⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷ ⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠃

        ''')
    print("Валютного Трейдер ШРЕК готовий до роботи!")

    print("Для початку роботи введіть будь-який символ.")

    input()

    трейдер = ВалютнийТрейдер()

    print(трейдер.get_commands())

    while True:
        команда = input("\nВведіть команду: ").split()
        дія = команда[0].upper()

        if дія == "EXIT":
            break
        elif дія == "NEXT":
            трейдер.update_rate()
            print(трейдер.get_rate())
        elif дія == "RATE":
            print(трейдер.get_rate())
        elif дія == "AVAILABLE":
            print(трейдер.get_balances())
        elif дія == "BUY":
            if len(команда) == 2:
                try:
                    сума = float(команда[1])
                    print(трейдер.buy(сума))
                except ValueError:
                    print("Невірна сума. Будь ласка, введіть правильне число.")
            else:
                print("Невірна команда. Використовуйте: BUY <сума>")
        elif дія == "SELL":
            if len(команда) == 2:
                try:
                    сума = float(команда[1])
                    print(трейдер.sell(сума))
                except ValueError:
                    print("Невірна сума. Будь ласка, введіть правильне число.")
            else:
                print("Невірна команда. Використовуйте: SELL <сума>")
        elif дія == "RESTART":
            del трейдер
            трейдер = ВалютнийТрейдер()
            print("Гра перезапущена.")
        elif дія == "COMMANDS":
            print(трейдер.get_commands())
        else:
            print("Невірна команда. Введіть 'EXIT', щоб завершити програму.")







############################################################

#             import os

# config_path = os.path.join(script_directory, "config.json")

# with open(config_path, "r") as config_file:
#     config = json.load(config_file)
# https://stackoverflow.com/questions/7783308/os-path-dirname-file-returns-empty
# getcwd()
