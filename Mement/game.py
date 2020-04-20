import copy
import random


class Mement:
    def __init__(self, money):
        self.money = money
        self.fruits = []

    def get_money(self):
        return self.money

    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def get_fruits(self):
        return copy.copy(self.fruits)


class Gamer:
    fruitsname = ['リンゴ', 'ぶどう', 'バナナ', 'みかん']

    def __init__(self, money):
        self.money = money
        self.fruits = []
        self.random = random.Random()

    def get_money(self):
        return self.money

    def bet(self):
        dice = self.random.randint(1, 6)
        if dice == 1:
            self.money += 100
            print('所持金が増えました。')
        elif dice == 2:
            self.money /= 2
            print('所持金が半分になりました')
        elif dice == 6:
            f = self.get_fruit()
            print('フルーツ:{fruit}をもらいました。'.format(fruit=f))
            self.fruits.append(f)
        else:
            print('なにも起こりませんでした')

    def create_mement(self):
        m = Mement(self.money)
        for f in self.fruits:
            if f.startswith('おいしい'):
                m.add_fruit(f)
        return m

    def restore_mement(self, mement):
        self.money = mement.money
        self.fruits = mement.get_fruits()

    def __str__(self):
        return '[money = {money}, fruits = {fruits}]'.format(money=self.money, fruits=self.fruits)

    def get_fruit(self):
        prefix = ''
        if self.random.randint(0, 1):
            prefix = 'おいしい'
        return prefix + Gamer.fruitsname[self.random.randint(0, len(Gamer.fruitsname) - 1)]
