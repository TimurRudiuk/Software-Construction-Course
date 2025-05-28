from abc import ABC, abstractmethod

class Character:
    def __init__(self):
        self.height = None
        self.build = None
        self.hair_color = None
        self.eye_color = None
        self.clothing = None
        self.inventory = []
        self.special_attributes = []

    def __str__(self):
        return (f"Character: Height - {self.height}, Build - {self.build}, "
                f"Hair Color - {self.hair_color}, Eye Color - {self.eye_color}, "
                f"Clothing - {self.clothing}, Inventory - {self.inventory}, "
                f"Special Attributes - {self.special_attributes}")

class CharacterBuilder(ABC):
    def __init__(self):
        self.character = Character()

    def set_height(self, height):
        self.character.height = height
        return self

    def set_build(self, build):
        self.character.build = build
        return self

    def set_hair_color(self, color):
        self.character.hair_color = color
        return self

    def set_eye_color(self, color):
        self.character.eye_color = color
        return self

    def set_clothing(self, clothing):
        self.character.clothing = clothing
        return self

    def add_to_inventory(self, item):
        self.character.inventory.append(item)
        return self

    @abstractmethod
    def add_special_attribute(self, attribute):
        pass

    def build(self):
        return self.character

class HeroBuilder(CharacterBuilder):
    def add_special_attribute(self, attribute):
        self.character.special_attributes.append(f"Heroic: {attribute}")
        return self

    def add_good_deed(self, deed):
        self.character.special_attributes.append(f"Good Deed: {deed}")
        return self

class EnemyBuilder(CharacterBuilder):
    def add_special_attribute(self, attribute):
        self.character.special_attributes.append(f"Evil: {attribute}")
        return self

    def add_evil_deed(self, deed):
        self.character.special_attributes.append(f"Evil Deed: {deed}")
        return self

class CharacterDirector:
    def __init__(self, builder):
        self.builder = builder

    def create_character(self):
        return self.builder

def task5_demo():
    hero_builder = HeroBuilder()
    director = CharacterDirector(hero_builder)
    hero = (director.create_character()
            .set_height("180 cm")
            .set_build("Athletic")
            .set_hair_color("Blonde")
            .set_eye_color("Blue")
            .set_clothing("Shining Armor")
            .add_to_inventory("Sword")
            .add_to_inventory("Shield")
            .add_special_attribute("Bravery")
            .add_good_deed("Saved the village")
            .build())
    
    print("Hero:")
    print(hero)
    
    enemy_builder = EnemyBuilder()
    director = CharacterDirector(enemy_builder)
    enemy = (director.create_character()
             .set_height("200 cm")
             .set_build("Muscular")
             .set_hair_color("Black")
             .set_eye_color("Red")
             .set_clothing("Dark Robe")
             .add_to_inventory("Dark Magic Staff")
             .add_to_inventory("Poison Dagger")
             .add_special_attribute("Cruelty")
             .add_evil_deed("Burned the village")
             .build())
    
    print("\nEnemy:")
    print(enemy)

if __name__ == "__main__":
    print("\n=== Task 5: Builder ===")
    task5_demo()