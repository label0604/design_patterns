import random
import sys
from abc import ABCMeta, abstractmethod


class Hand:
    HANDVALUE_GUU = 0
    HANDVALUE_CHO = 1
    HANDVALUE_PAA = 2
    hand = []
    name = ['グー', 'チョキ', 'パー']

    def __init__(self, hand_value):
        self.hand_value = hand_value

    @classmethod
    def get_hand(cls, hand_value):
        return Hand.hand[hand_value]

    def is_stronger_than(self, h):
        return self.fight(h) == 1

    def is_weaker_than(self, h):
        return self.fight(h) == -1

    def fight(self, h):
        if self == h:
            return 0
        elif (self.hand_value + 1) % 3 == h.hand_value:
            return 1
        else:
            return -1


# intialize Hand.hand
Hand.hand.append(Hand(Hand.HANDVALUE_GUU))
Hand.hand.append(Hand(Hand.HANDVALUE_CHO))
Hand.hand.append(Hand(Hand.HANDVALUE_PAA))


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def next_hand(self):
        pass

    @abstractmethod
    def study(self, win):
        pass


class WinningStrategy(Strategy):
    def __init__(self, seed):
        self.random = random.Random(seed)
        self.won = False
        self.prev_hand = None

    def next_hand(self):
        if not self.won:
            self.prev_hand = Hand.get_hand(self.random.randint(0, 2))
        return self.prev_hand

    def study(self, win):
        self.won = win


class ProbStrategy(Strategy):
    def __init__(self, seed):
        self.random = random.Random(seed)
        self.prev_hand_value = 0
        self.current_hand_value = 0
        self.history = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]

    def next_hand(self):
        bet = self.random.randint(0, self.get_sum(self.current_hand_value))
        hand_value = 0
        if bet < self.history[self.current_hand_value][0]:
            hand_value = 0
        elif bet < self.history[self.current_hand_value][0] + self.history[self.current_hand_value][1]:
            hand_value = 1
        else:
            hand_value = 2
        self.prev_hand_value = self.current_hand_value
        self.current_hand_value = hand_value
        return Hand.get_hand(hand_value)

    def get_sum(self, hv):
        result = 0
        for i in range(3):
            result += self.history[hv][i]
        return result

    def study(self, win):
        if win:
            self.history[self.prev_hand_value][self.current_hand_value] += 1
        else:
            self.history[self.prev_hand_value][(
                self.current_hand_value + 1) % 3] += 1
            self.history[self.prev_hand_value][(
                self.current_hand_value + 2) % 3] += 1


class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.win_count = 0
        self.lose_count = 0
        self.game_count = 0

    def next_hand(self):
        return self.strategy.next_hand()

    def win(self):
        self.strategy.study(True)
        self.win_count += 1
        self.game_count += 1

    def lose(self):
        self.strategy.study(False)
        self.lose_count += 1
        self.game_count += 1

    def even(self):
        self.game_count += 1

    def __str__(self):
        return '[{name}:{game_count} games, {win_count} win, {lose_count} lose]'.format(
            name=self.name, game_count=self.game_count, win_count=self.win_count, lose_count=self.lose_count
        )


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print('Usage: python main.py randomseed1 randomseed2')
        print('Example: python main.py 314 15')
        sys.exit()

    seed1 = int(args[1])
    seed2 = int(args[2])

    player1 = Player('Taro', WinningStrategy(seed1))
    player2 = Player('Hana', ProbStrategy(seed2))

    for i in range(10000):
        next_hand1 = player1.next_hand()
        next_hand2 = player2.next_hand()
        if next_hand1.is_stronger_than(next_hand2):
            print('Winner: ', player1)
            player1.win()
            player2.lose()
        elif next_hand2.is_stronger_than(next_hand1):
            print('Winner: ', player2)
            player1.lose()
            player2.win()
        else:
            print('Even...')
            player1.even()
            player2.even()
    print('Total result:')
    print(player1)
    print(player2)
