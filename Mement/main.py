from time import sleep

from game import Gamer

if __name__ == '__main__':
    gamer = Gamer(100)
    mement = gamer.create_mement()
    for i in range(100):
        print('====', i)
        print('現状:', gamer)

        gamer.bet()

        print('所持金は{money}円になりました。'.format(money=gamer.get_money()))

        if gamer.get_money() > mement.get_money():
            print('（だいぶ増えたので、現在の状態を保存しておこう）')
            mement = gamer.create_mement()
        elif gamer.get_money() < mement.get_money() / 2:
            print('（だいぶ減ったので、以前の状態に復帰しよう）')
            gamer.restore_mement(mement)
        sleep(0.5)
