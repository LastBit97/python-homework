class Animal:
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
