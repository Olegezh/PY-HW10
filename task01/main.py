# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class Animal:
    def __init__(self, name, age, voice='groal'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)


class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    def swim(self):
        print("i'm swimming, oh, it's titan!")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print('Bark!')


class Raven(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = name

    def fly_around_corpse(self):
        print('oooh, meat....')


class AnimalFabric:
    def animal_(self, animal_type, name, age, voice, color = None, breed = None):
        self.animal_type = animal_type
        self.name = name
        self.age = age
        self.voice = voice
        self.color = color
        self.breed = breed

        if animal_type == "fish":
            return Fish(name, age, color, voice)
        elif animal_type == "dog":
            return Dog(name, age, breed, voice)
        elif animal_type == "raven":
            return Raven(name, age, color, voice)
        else:
            raise ValueError("animal ty is not supported")



# fish = Fish('Nemo', 2, 'silver', 'bul-bul')
# dog = Dog('Spark', 5, 'pitbull', 'bark!')
# bird = Raven('Qarasique', 6, 'white', 'bravo!')

animal = AnimalFabric()
fish = animal.animal_('fish', 'Nemo', 2, 'bul-bul', 'silver' )
dog = animal.animal_('dog', 'Spark', 5, 'bark!', 'pitbull', )
bird = animal.animal_('raven', 'Qarasique', 6, 'bravo!', 'white')

animals = [fish, dog, bird]

for i in animals:
    i.make_voice()

fish.swim()
dog.bark()
bird.fly_around_corpse()