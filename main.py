import random

class Zoo:
    group = "Birds"
    group = "Mammals"

    def __init__(self, weight, hight, fly, climb, group, type=None):
        self.weight = weight
        self.hight = hight
        self.fly = fly
        self.climb = climb
        self.group = group
        self.type = type


    def __str__(self):
        return f"Hi! I'm {self.type} and i'm {self.weight} kg and my hight is {self.hight} centimeterіs."

    def to_fly(self, fly):
        print(f"{self.type}, Полетіли!")

    def to_climb(self, climb):
        print(f"{self.type}, Поповзли!")

    def climb_or_fly(self):
        live_cube = random.randint(1, 2)
        if live_cube == 1:
            self.to_fly()
        elif live_cube == 2:
            self.to_climb()

        print(self.climb_or_fly)

    def input_(self):
        input("Введіть тварину:")
        if input() == type:
            print(f"{self.type} {self.fly} fly")

    print(input_)


tiger = Zoo(200, 150, "can't", "can't", "Mammals", "tiger")
print(tiger)
monkey = Zoo(30, 80, "can't", "can", "Mammals", "monkey")
print(monkey)
peacocks = Zoo(15, 80, "can", "can't", "Bird", "peacock")
print(peacocks)
flamingo = Zoo(3, 110, "can", "can't", "Bird", "flamingo")
print(flamingo)
