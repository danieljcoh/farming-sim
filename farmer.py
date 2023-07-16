from crop import Crop
import merchant
from crop import plantable_crops


class Farmer:
    def __init__(self):
        print("A farmer was made!")
        self.name = self.farmer_ask_name()
        self.garden = []  # a list of strings of the names of the crops.
        self.plots = 8
        self.animals = []
        self.inventory = []  # crop needs to be inside inventory to plant. Then remove it from inventory.
        self.turns_before_night = 3  # after every action, goes down by one, then it's nighttime.

    def farmer_next_task(self):
        if self.turns_before_night <= 0:
            self.night_time()
        next_task = input("What do you want to do? (options: plant, visit unc, search, check inventory) ")
        if next_task.lower() == "plant":
            self.farmer_plant()
        elif next_task.lower() == "check":
            self.farmer_check_inventory()

    def farmer_ask_name(self):
        name = input("What's your name: ")
        return name

    def farmer_plant(self):
        crop_name = input("What do you want to plant: ")
        while crop_name not in plantable_crops and crop_name not in self.inventory:
            crop_name = input("What do you want to plant: ")
        crop_to_plant = Crop(crop_name)
        self.garden.append(crop_to_plant.name)  # this is importing the string name, not the object itself.
        self.plots -= 1
        self.inventory.remove(crop_name)
        print(f"{self.name} added {crop_to_plant.name} to their garden!")
        print(f"Garden: {self.garden}")
        print(f"You have {self.plots} plots left.")
        self.turns_before_night -= 1
        print(f"You have {self.turns_before_night} turns before night!")
        self.farmer_next_task()

    def farmer_show_info(self):
        print("Farm Information: ")
        # print(f"\tGarden: {self.farm_name}")
        print(f"\tGarden: {self.garden}")
        print(f"\tPlots Remaining: {self.plots}")
        print(f"\tTurns before night: {self.turns_before_night}")

    def night_time(self):
        # only 1 turn at night
        print("It's night time. Your options are: (merchant / sleep")
        night_activity_choice = input("What do you want to do? ")
        if night_activity_choice.lower() == "merchant":
            self.turns_before_night = 3
            merchant.Merchant.merchant_buy_animal(merchant)
        elif night_activity_choice.lower() == "sleep":
            pass

    def farmer_check_inventory(self):
        print(f"Inventory: {self.inventory}")
        self.farmer_next_task()

    def farmer_search(self):
        pass
        # find some items and plants
