# 只有唯一实例,单例模式：文件系统，创建日志……

class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):

    def __init__(self, num):
        self.num = num

if __name__ == '__main__':
    a = MyClass(10)
    b = MyClass(20)

    print(a.num, b.num)
    print(id(a), id(b))
