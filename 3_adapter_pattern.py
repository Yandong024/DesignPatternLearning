"""
适配器方法
（1）类适配器（继承）；
（2）对象适配器（组合）；

本质是如何复用不同程序员写的代码。
"""

from abc import ABCMeta, abstractmethod


class Pay(metaclass=ABCMeta):

    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Pay):

    def pay(self, money):
        print("Alipay: %.02f" % money)


class Wechat(Pay):

    def pay(self, money):
        print("Wechat: %.02f" % money)



# -----------继承---------------------- #

class Huaweipay:
    """
    来了个新程序员把付款方式命名为 cost 函数，和以前的pay功能一致
    但统一调用时会遇到麻烦……
    """

    def cost(self, money):
        print("Huawei: %.02f"%money)

class NewPay(Huaweipay, Pay):

    def pay(self, money):
        self.cost(money)



# -----------组合---------------------- #

class Bankpay:
    """
    来了个新程序员把付款方式命名为 cost 函数，和以前的pay功能一致
    但统一调用时会遇到麻烦……
    """

    def cost(self, money):
        print("Bank: %.02f"%money)

class Xiaomipay:

    def cost(self, money):
        print("Xiaomi: %.02f"%money)


class PayAdapter(Pay):
    """
    (1) init:不同的付款方式
    (2) 实现cost与pay方法的组合
    """

    def __init__(self, pay_method):
        self.pay_method = pay_method

    def pay(self, money):
        # 是否有对抽象类的实现
        self.pay_method.cost(money)


if __name__ == '__main__':

    huawei_pay = NewPay()
    huawei_pay.pay(66.66)
    # -------------- #
    print('---'*20)
    pay_1 = PayAdapter(Xiaomipay())
    pay_1.pay(50.0)

    pay_2 = PayAdapter(Bankpay())
    pay_2.pay(100.0)

