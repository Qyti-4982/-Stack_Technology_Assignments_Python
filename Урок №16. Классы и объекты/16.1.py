
class Касса:
    def __init__(self, balance = 0):
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным числом!")
        self.balance = balance

    def top_up(self, X):
        self.X = X
        if X <= 0:
            raise ValueError("Сумма для пополнения должна быть положительна!")
        else:
            self.balance += X
            return self.balance
    
    
    def count_1000(self):
        return self.balance // 1000
    
    def take_away(self, X):
        self.X = X
        if X <= 0:
            raise ValueError("Сумма для изъятия должна быть положительной!")
        if X > self.balance:
            raise ValueError("Нельзя вывести больше, чем есть на балансе!")
        if X:
            self.balance -= X
            return self.balance

balance = int(input("Введите баланс денег: "))
касса = Касса(balance) 

action = input("Какую операцию будите совершать?(добавить(добавление суммы к балансу); _1000_(выявить количество тысяч на балансе),вывод(вывод денег с баланса); stop - остановка программы)")
while action != "stop":
    if action == "добавить":
        X = int(input("Введите сумму для добавления к балансу: "))
        _top_up = касса.top_up(X)
        print(_top_up)
    elif action == "_1000_":
        _1000_ = касса.count_1000()
        print(_1000_)
    elif action == "вывод":
        X = int(input("Введите сумму для вывода с баланса: "))
        _take_away = касса.take_away(X)
        print(_take_away)
    else: print("Указанной команды не существует!")
    action = input("Какую операцию будите совершать?(добавить(добавление суммы к балансу); _1000_(выявить количество тысяч на балансе),вывод(вывод денег с баланса); stop - остановка программы)")
