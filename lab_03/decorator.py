class Hero:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def show_stats(self):
        print(f"\nHero: {self.name}")
        print("Inventory:", ", ".join(self.inventory) if self.inventory else "Empty")
        print("Power:", self.power)
        print("Defense:", self.defense)
        print("Magic:", self.magic)

class HeroDecorator:
    def __init__(self, hero):
        self.hero = hero

    def show_stats(self):
        self.hero.show_stats()

    def __getattr__(self, name):
        return getattr(self.hero, name)

class WeaponDecorator(HeroDecorator):
    def __init__(self, hero, weapon):
        super().__init__(hero)
        self.weapon = weapon
        self.hero.inventory.append(weapon)
    
    def show_stats(self):
        if self.weapon == "Sword":
            self.hero.power += 20
        elif self.weapon == "Staff":
            self.hero.magic += 30
        super().show_stats()

class ArmorDecorator(HeroDecorator):
    def __init__(self, hero, armor):
        super().__init__(hero)
        self.armor = armor
        self.hero.inventory.append(armor)
    
    def show_stats(self):
        if self.armor == "Plate Armor":
            self.hero.defense += 40
        elif self.armor == "Robe":
            self.hero.magic += 15
        super().show_stats()

class ArtifactDecorator(HeroDecorator):
    def __init__(self, hero, artifact):
        super().__init__(hero)
        self.artifact = artifact
        self.hero.inventory.append(artifact)
    
    def show_stats(self):
        if self.artifact == "Amulet of Power":
            self.hero.power += 15
            self.hero.magic += 15
        elif self.artifact == "Ring of Protection":
            self.hero.defense += 25
        super().show_stats()

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power = 50
        self.defense = 30
        self.magic = 5

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power = 10
        self.defense = 15
        self.magic = 60

class Paladin(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power = 35
        self.defense = 40
        self.magic = 25

def task2_demo():
    warrior = Warrior("Conan")
    warrior = WeaponDecorator(warrior, "Sword")
    warrior = ArmorDecorator(warrior, "Plate Armor")
    warrior = ArtifactDecorator(warrior, "Amulet of Power")
    warrior.show_stats()
    
    mage = Mage("Gandalf")
    mage = WeaponDecorator(mage, "Staff")
    mage = ArmorDecorator(mage, "Robe")
    mage = ArtifactDecorator(mage, "Ring of Protection")
    mage.show_stats()
    
    paladin = Paladin("Tirion")
    paladin = WeaponDecorator(paladin, "Sword")
    paladin = ArmorDecorator(paladin, "Plate Armor")
    paladin = ArtifactDecorator(paladin, "Ring of Protection")
    paladin.show_stats()

if __name__ == "__main__":
    print("\n=== Task 2: Decorator ===")
    task2_demo()