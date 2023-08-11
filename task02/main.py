# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


class Bankomat:
    def __init__(self):
        self.total_cash = 0
        self.count = 0

    def menu(self):
        print(f"сумма на счете {self.total_cash}")
        print("1 - пополнить")
        print("2 - снять")
        print("0 - выйти")

    def money_in(self, money):
        self.total_cash += money
        self.count += 1
        self._check_account()

    def money_out(self, money):
        self.total_cash -= money
        self.count += 1
        self._check_account()

    def get_money_at_account(self):
        return self.total_cash

    def _check_account(self):
        if self.total_cash > 5_000_000:
            self.total_cash *= 0.9
        if self.count == 3:
            self.total_cash *= 1.03
            self.count = 0

b1 = Bankomat()

while True:
    b1.menu()
    action = input("введите номер операции: ")
    match action:
        case "1":
            add = int(input("внесите сумму кратную 50: "))
            if add % 50 == 0:
                b1.money_in(add)
            else:
                print("неверная сумма")

        case "2":
            take = int(input("введите сумму снятия кратную 50: "))
            if take % 50 == 0:
                percent = take*1.5*0.01
                if percent < 30:
                    percent = 30
                if percent > 600:
                    percent = 600

                if b1.get_money_at_account() < (take+percent):
                    print("недостаточно средств")
                else:
                    b1.money_out(take+percent)
            else:
                print("неверная сумма")

        case "0":
            quit()



# total_cash = 0
# count = 0
# while True:
#
#     if total_cash > 5_000_000:
#         total_cash *= 0.9
#
#     print("сумма на счете ", total_cash)
#
#     print("1 - пополнить")
#     print("2 - снять")
#     print("0 - выйти")
#
#     action = input("введите номер операции: ")
#
#
#     match action:
#         case "1":
#             add = int(input("внесите сумму кратную 50: "))
#             if add % 50 == 0:
#                 total_cash += add
#                 count += 1
#             else:
#                 print("неверная сумма")
#
#         case "2":
#             take = int(input("введите сумму снятия кратную 50: "))
#             if take % 50 == 0:
#                 percent = take*1.5*0.01
#                 if percent < 30:
#                     percent = 30
#                 if percent > 600:
#                     percent = 600
#
#                 if total_cash < (take+percent):
#                     print("недостаточно средств")
#                 else:
#                     total_cash -= (take+percent)
#                     count += 1
#             else:
#                 print("неверная сумма")
#
#         case "0":
#             quit()
#
#     if count == 3:
#         total_cash *= 1.03
#         count = 0