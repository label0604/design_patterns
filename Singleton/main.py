class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__':
    print('Start.')
    obj1 = Singleton()
    obj2 = Singleton()
    if obj1 is obj2:
        print('obj1とobj2は同じインスタンスです。')
    else:
        print('obj1とobj2は同じインスタンスではありません。')
    print('End.')
