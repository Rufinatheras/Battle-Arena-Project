import random

class Fighter:
    def __init__(self, name, max_hp, base_attack):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        self._base_attack = base_attack


    def is_alive(self):
        if self._hp > 0:
            return True
        else:
            return False
        

    def take_damage(self, amount):
        self._hp -= amount
        if self._hp < 0:
            self._hp = 0
        
    
    def reset(self):
        self._hp = self._max_hp

    
    def attack(self, target):
        raise NotImplementedError("Override in subclass")


class Warrior(Fighter):
    def attack(self, target):
        damage = random.randint(self._base_attack - 2, self._base_attack + 2)
        print(self._name, "hits the target for", damage,"!")
        target.take_damage(damage)

class Mage(Fighter):
    def attack(self, target):
        spell = random.randint(0, self._base_attack + 8)
        print(self._name,"casts a spell for", spell,"!")
        target.take_damage(spell)

class Rogue(Fighter):
    def attack(self, target):
        chance = random.randint(1, 3)
        if chance == 1:
            print(self._name, "misses the sneak attack!")
        elif chance == 2:
            sneak_attack=self._base_attack*2
            print(self._name,"lands a CRIT sneak attack for",sneak_attack,"!")
            target.take_damage(sneak_attack)

        else:
            sneak_attack = self._base_attack
            print(self._name,"lands a sneak attack for",sneak_attack,"!")
            target.take_damage(sneak_attack)

       


def run_duel(f1, f2):
    f1.reset()
    f2.reset()

    Fighter_1,Fighter_2= f1,f2

    print("Fight Begins:",f1._name,"vs",f2._name)
    print()
    
    while f1.is_alive() and f2.is_alive():
        f1.attack(f2)
        print(f2._name,"HP:",f2._hp)

        if not f2.is_alive():
            break

        f2.attack(f1)
        print(f1._name,"HP:",f1._hp)
        print()

    if f1.is_alive():
        print(f1._name,"wins!")
    else:
        print(f2._name,"wins!")


def create_fighter():
    name = input("Enter a name:")

    print("Choose class:")
    print("1.Warrior")
    print("2.Mage")
    print("3.Rogue")
    choice = input("Enter your choice:")

    if choice =="1":
        return Warrior(name,50,10)
    elif choice =="2":
        return Mage(name,40,14)
    elif choice =="3":
        return Rogue(name,45,12)
    else:
        print("Invalid choice. Try again.")
        return None


def main():
    fighters = []

    while True:
        print("\n1. Create fighter")
        print("2. List fighters")
        print("3. Start duel")
        print("4. Quit")

        choice = input("> ")

        if choice == "1":
            fighter = create_fighter()
            if fighter:
                fighters.append(fighter)
                print(fighter._name,"was created!")

        elif choice == "2":
            if not fighters:
               print ("No fighters created yet.")
            else:
               for i in range(len(fighters)):
                   f = fighters[i]
                   print(i ,f._name)

        elif choice == "3":
            if len(fighters)<2:
                print("Not enough fighters to start a duel.")
            else:
                run_duel(fighters[-2], fighters[-1])

        elif choice == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

