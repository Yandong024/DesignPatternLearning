"""
使用了类，继承，编写程序，不意味着程序就有了 object-oriented 的思想
SOLID五个原则，隔离编程
"""

from abc import abstractmethod, ABCMeta


class LandAnimal(metaclass=ABCMeta):

    @abstractmethod
    def walk(self):
        pass


class WaterAnimal(metaclass=ABCMeta):

    @abstractmethod
    def swim(self):
        pass


class SkyAnimal(metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass


class Frog(WaterAnimal, LandAnimal):

    def walk(self):
        print("Frog walks on the land.")

    def swim(self):
        print("Frog swim in the water.")


if __name__ == '__main__':

    frog_1 = Frog()
    frog_1.walk()
    frog_1.swim()


