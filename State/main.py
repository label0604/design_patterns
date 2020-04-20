import random
from abc import ABCMeta, abstractmethod
from time import sleep


class State(metaclass=ABCMeta):
    @abstractmethod
    def do_clock(self, context, hour):
        pass

    @abstractmethod
    def do_use(self, context):
        pass

    @abstractmethod
    def do_alarm(self, context):
        pass

    @abstractmethod
    def do_phone(self, context):
        pass


class DayState(State):
    singleton = None

    def __new__(cls):
        if cls.singleton is None:
            cls.singleton = super().__new__(cls)
        return cls.singleton

    def do_clock(self, context, hour):
        if hour < 9 or hour >= 17:
            context.change_state(NightState())

    def do_use(self, context):
        context.record_log('金庫使用（昼間）')

    def do_alarm(self, context):
        context.call_security_center('非常ベル（昼間）')

    def do_phone(self, context):
        context.call_security_center('通常の通話（昼間）')

    def __str__(self):
        return '[昼間]'


class NightState(State):
    singleton = None

    def __new__(cls):
        if cls.singleton is None:
            cls.singleton = super().__new__(cls)
        return cls.singleton

    def do_clock(self, context, hour):
        if hour > 9 and hour <= 17:
            context.change_state(DayState())

    def do_use(self, context):
        context.call_security_center('非常:夜間の金庫使用！')

    def do_alarm(self, context):
        context.call_security_center('非常ベル（夜間）')

    def do_phone(self, context):
        context.record_log('夜間の通話録音')

    def __str__(self):
        return '[夜間]'


class Context(metaclass=ABCMeta):
    @abstractmethod
    def set_clock(self, hour):
        pass

    @abstractmethod
    def change_state(self, state):
        pass

    @abstractmethod
    def call_security_center(self, msg):
        pass

    @abstractmethod
    def record_log(self, msg):
        pass


class SafeFrame(Context):
    def __init__(self):
        self.state = DayState()

    def set_clock(self, hour):
        self.state.do_clock(self, hour)

    def change_state(self, state):
        print('{0}から{1}へ状態が変化しました'.format(self.state, state))
        self.state = state

    def call_security_center(self, msg):
        print('call! ', msg)

    def record_log(self, msg):
        print('record... ', msg)

    def do_use(self):
        self.state.do_use(self)

    def do_alarm(self):
        self.state.do_alarm(self)

    def do_phone(self):
        self.state.do_phone(self)


if __name__ == '__main__':
    frame = SafeFrame()
    for hour in range(0, 23):
        print('---現在時刻: {hour}:00'.format(hour=hour))
        frame.set_clock(hour)
        if random.randint(0, 1):
            frame.do_use()
        if random.randint(0, 1):
            frame.do_alarm()
        if random.randint(0, 1):
            frame.do_phone()
        print()
        sleep(1)
