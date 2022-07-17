"""
接口：抽象方法的集合
接口的好处：屏蔽了底层逻辑
（1）抽象 pay 方法，作为接口
（2）现实 pay 方法，ali_pay，wechat_pay
"""

from abc import ABCMeta, abstractmethod


class Pay(metaclass=ABCMeta):

    @abstractmethod
    def pay(self, momey):
        pass


class Alipay(Pay):

    def pay(self, momey):
        print("Alipay: %.02f"%momey)


class Wechat(Pay):

    def pay(self, momey):
        print("Wechat: %.02f"%momey)


if __name__ == '__main__':
    a_pay = Alipay()
    a_pay.pay(61.18)

