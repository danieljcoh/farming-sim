from animal import Animal
import farmer

# merchants only come out at night?


class Merchant:
    def __init__(self):
        self.names = ["Merchi", "Duncan", "Orgla", "Fiz"]  # different merchants?
        self.level_one_animals = ["pig", "chicken"]

    def merchant_buy_animal(self):
        animal_name__to_purchase = input("What'r'ya buyin'? ")
        while animal_name__to_purchase not in self.level_one_animals:
            animal_name__to_purchase = input("What'r'ya buyin'? ")
        animal = Animal(animal_name__to_purchase)
        farmer.animals.append(animal.name)

