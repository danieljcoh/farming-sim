from farmer import Farmer


class Game:
    def __int__(self):
        self.name = "Farming Adventures!"

    def game_introduction(self):
        print("Welcome to Farming Simulator. Let's get started.")

        # Instantiating the player (Farmer)
        player = Farmer()
        farming_name = f"Welcome, Farmer {player.name}."

        print(f"Nice to meetchya {player.name}.")
        print("I'm your Uncle Buf but you can just call me Unc.")

        print()
        print("I'm getting too old to watch over this extra property of mine. So I'm giving it to you.")
        print("This here lovely little plot of land is now yours.")
        print("It has 8 plots and each thing you grow takes up 1 plot. So you dur the math.")
        print("But in the future you might be able to expand it. Let's see how things go.")
        print("Start off small.")
        print()
        print("Here. Take this.")
        print(f"Farmer {player.name} received 3 bundles of corn.")
        player.inventory.append("corn")
        player.inventory.append("corn")
        player.inventory.append("corn")
        print()
        print("If you're gonna plant anything else, you gotta search for it.")
        print("These grounds are ripe for the picking.")
        print("If you need anything come visit me down the street one day. Maybe you can meet some of the neighbors.")
        print("Good luck!")
        print()
        player.farmer_show_info()
        print()
        player.farmer_next_task()

