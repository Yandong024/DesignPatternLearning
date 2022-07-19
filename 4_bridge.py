"""
桥模式：让相关类解耦合
Line -- RedLine 缺点
不同形状，不同颜色
"""

from abc import abstractmethod, ABCMeta


# 抽象接口 Shape，Color
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self):
        pass


# 具体实现形状： Line Rectangle
class Line(Shape):

    name = "直线"

    def __init__(self):
        self.draw()

    def draw(self):
        print("---画出一条直线---")


class Rectangle(Shape):

    name = "长方形"

    def __init__(self):
        self.draw()

    def draw(self):
        print("---画出一个长方形---")


class Red(Color):

    def __init__(self, shape):
        self.shape = shape

    def paint(self):
        print("红色的%s"%self.shape.name)


class Green(Color):

    def __init__(self, shape):
        self.shape = shape

    def paint(self):
        print("绿色的%s" % self.shape.name)



if __name__ == '__main__':

    user_red_line = Red(Line())
    user_red_line.paint()
    print('---'*10)
    user_green_rectangle = Green(Rectangle())
    user_green_rectangle.paint()