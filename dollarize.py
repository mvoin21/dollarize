
class MoneyFmt:
    def __init__(self, money):
        self.money = money

    def update(self, money):
        self.money = money

    def __repr__(self):
        return f'{self.money}'


    def dollarize(self):
        if self.money >= 0:
            return '${:,.2f}'.format(self.money)
        else:
            return '-${:,.2f}'.format(abs(self.money))

    def __str__(self):
        return cash.dollarize()
        

cash = MoneyFmt(12345678.021)
print(cash)

cash.update(100000.4567)
print(cash)

cash.update(-0.3)
print(cash)

print(repr(cash))