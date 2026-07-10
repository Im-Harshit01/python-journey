from random import choice, randint

class Item:
    def __init__(self, name, kind, power, price):
        self.name = name
        self.kind = kind
        self.power = power
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.kind}, +{self.power}) - {self.price} coins"

class Enemy:
    def __init__(self, name, health, attack, reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.reward = reward

    def alive(self):
        return self.health > 0

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.attack = 12
        self.coins = 25
        self.inventory = [Item("Small Potion", "heal", 25, 10), Item("Rusty Sword", "weapon", 5, 15)]
    def alive(self):
        return self.health > 0
    def stats(self):
        print(f"\n{self.name}: {self.health}/{self.max_health} HP")
        print(f"Attack: {self.attack} | Coins: {self.coins}")
    def show_inventory(self):
        print("\nInventory:")
        if not self.inventory:
            print("Empty")
        for i, item in enumerate(self.inventory, 1):
            print(f"{i}. {item}")
    def use_item(self):
        if not self.inventory:
            print("You have no items.")
            return
        self.show_inventory()
        choice_text = input("Choose item number: ")
        if not choice_text.isdigit():
            print("Invalid choice.")
            return
        index = int(choice_text) - 1
        if index < 0 or index >= len(self.inventory):
            print("Invalid choice.")
            return
        item = self.inventory.pop(index)
        if item.kind == "heal":
            self.health = min(self.max_health, self.health + item.power)
            print(f"You used {item.name} and healed {item.power} HP.")
        elif item.kind == "weapon":
            self.attack += item.power
            print(f"You equipped {item.name}. Attack increased by {item.power}.")

def make_enemy():
    enemies = [
        Enemy("Slime", randint(25, 35), randint(5, 8), 12),
        Enemy("Bandit", randint(35, 50), randint(8, 12), 20),
        Enemy("Dark Knight", randint(55, 75), randint(12, 17), 35),
    ]
    return choice(enemies)

def battle(player):
    enemy = make_enemy()
    print(f"\nA wild {enemy.name} appears!")
    while player.alive() and enemy.alive():
        print(f"\n{player.name}: {player.health} HP | {enemy.name}: {enemy.health} HP")
        print("1. Attack\n2. Use item\n3. Run")
        move = input("Choose: ")
        if move == "1":
            damage = randint(player.attack - 3, player.attack + 4)
            enemy.health -= damage
            print(f"You hit {enemy.name} for {damage} damage.")
        elif move == "2":
            player.use_item()
        elif move == "3":
            if randint(1, 2) == 1:
                print("You escaped!")
                return
            print("Escape failed!")
        else:
            print("Invalid move.")
            continue
        if enemy.alive():
            damage = randint(enemy.attack - 2, enemy.attack + 3)
            player.health -= damage
            print(f"{enemy.name} hit you for {damage} damage.")
    if player.alive():
        player.coins += enemy.reward
        print(f"\nYou defeated {enemy.name} and earned {enemy.reward} coins!")
    else:
        print("\nYou were defeated. Game over.")

def shop(player):
    items = [
        Item("Small Potion", "heal", 25, 10),
        Item("Big Potion", "heal", 50, 22),
        Item("Iron Sword", "weapon", 8, 30),
        Item("Steel Sword", "weapon", 14, 55),
    ]
    print("\nShop:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
    print(f"You have {player.coins} coins.")
    choice_text = input("Buy item number, or press Enter to leave: ")
    if choice_text == "":
        return
    if not choice_text.isdigit() or int(choice_text) < 1 or int(choice_text) > len(items):
        print("Invalid choice.")
        return
    item = items[int(choice_text) - 1]
    if player.coins < item.price:
        print("Not enough coins.")
        return
    player.coins -= item.price
    player.inventory.append(item)
    print(f"You bought {item.name}.")

def main():
    print("Text RPG: Inventory Battle")
    player = Player(input("Enter your hero name: ").strip() or "Hero")
    while player.alive():
        print("\n1. Explore\n2. Visit shop\n3. Use item\n4. Show stats\n5. Show inventory\n6. Quit")
        option = input("Choose: ")
        if option == "1":
            battle(player)
        elif option == "2":
            shop(player)
        elif option == "3":
            player.use_item()
        elif option == "4":
            player.stats()
        elif option == "5":
            player.show_inventory()
        elif option == "6":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option.")

main()