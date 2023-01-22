class Animal:
    countInstances = 0

    def __init__(self):
        Animal.countInstances += 1

    @staticmethod
    def print_count_instances():
        print(Animal.countInstances)

    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        print('Мяу')


class Dog(Animal):
    def voice(self):
        print('Гав')


class Cow(Animal):
    def voice(self):
        print('Муу')


cat = Cat()
dog = Dog()
cow = Cow()
cat.voice()
dog.voice()
cow.voice()
Animal.print_count_instances()
