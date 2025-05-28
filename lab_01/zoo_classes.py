from enum import Enum
from typing import List, Dict

class AnimalType(Enum):
    MAMMAL = "Ссавець"
    BIRD = "Птах"
    REPTILE = "Рептилія"
    AMPHIBIAN = "Амфібія"
    FISH = "Риба"

class EnclosureType(Enum):
    CAGE = "Клітка"
    AQUARIUM = "Акваріум"
    TERRARIUM = "Тераріум"
    AVIARY = "Вольєр"
    PADDOCK = "Загін"

class FoodType(Enum):
    MEAT = "М'ясо"
    FISH = "Риба"
    FRUIT = "Фрукти"
    VEGETABLES = "Овочі"
    GRAIN = "Зерно"
    INSECTS = "Комахи"

class EmployeePosition(Enum):
    DIRECTOR = "Директор"
    VETERINARIAN = "Ветеринар"
    KEEPER = "Доглядач"
    CLEANER = "Прибиральник"
    SECURITY = "Охорона"

class Animal:
    def __init__(self, name: str, species: str, animal_type: AnimalType, 
                 required_enclosure: EnclosureType, diet: List[FoodType]):
        self.name = name
        self.species = species
        self.animal_type = animal_type
        self.required_enclosure = required_enclosure
        self.diet = diet
        
    def __str__(self):
        return f"{self.name} ({self.species}, {self.animal_type.value})"

class Enclosure:
    def __init__(self, enclosure_id: int, enclosure_type: EnclosureType, 
                 size: float, capacity: int):
        self.enclosure_id = enclosure_id
        self.enclosure_type = enclosure_type
        self.size = size 
        self.capacity = capacity
        self.animals: List[Animal] = []
        
    def add_animal(self, animal: Animal) -> bool:
        if (len(self.animals)) >= self.capacity:
            return False
        if animal.required_enclosure != self.enclosure_type:
            return False
        self.animals.append(animal)
        return True
    
    def remove_animal(self, animal: Animal) -> bool:
        if animal in self.animals:
            self.animals.remove(animal)
            return True
        return False
    
    def __str__(self):
        return (f"Вольєр #{self.enclosure_id} ({self.enclosure_type.value}, "
                f"{self.size} м², місткість: {self.capacity})")

class Food:
    def __init__(self, food_type: FoodType, quantity: float, unit: str):
        self.food_type = food_type
        self.quantity = quantity
        self.unit = unit
        
    def __str__(self):
        return f"{self.food_type.value}: {self.quantity} {self.unit}"

class Employee:
    def __init__(self, name: str, position: EmployeePosition, salary: float):
        self.name = name
        self.position = position
        self.salary = salary
        
    def __str__(self):
        return f"{self.name} ({self.position.value}, зарплата: {self.salary} грн)"

class ZooInventory:
    def __init__(self):
        self.animals: List[Animal] = []
        self.enclosures: List[Enclosure] = []
        self.food_supplies: Dict[FoodType, Food] = {}
        self.employees: List[Employee] = []
        
    def add_animal(self, animal: Animal, enclosure: Enclosure = None) -> bool:
        if enclosure:
            if enclosure.add_animal(animal):
                self.animals.append(animal)
                return True
            return False
        else:
            self.animals.append(animal)
            return True
    
    def add_enclosure(self, enclosure: Enclosure):
        self.enclosures.append(enclosure)
        
    def add_food(self, food: Food):
        if food.food_type in self.food_supplies:
            self.food_supplies[food.food_type].quantity += food.quantity
        else:
            self.food_supplies[food.food_type] = food
    
    def add_employee(self, employee: Employee):
        self.employees.append(employee)
    
    def print_inventory(self):
        print("\n=== Інвентаризація зоопарку ===")
        
        print("\nСпівробітники:")
        for emp in self.employees:
            print(f"- {emp}")
        print(f"Всього співробітників: {len(self.employees)}")
        
        print("\nТварини:")
        for animal in self.animals:
            print(f"- {animal}")
        print(f"Всього тварин: {len(self.animals)}")
        
        print("\nВольєри:")
        for enc in self.enclosures:
            print(f"- {enc}")
            if enc.animals:
                print("  Тварини у вольєрі:")
                for animal in enc.animals:
                    print(f"  - {animal}")
        print(f"Всього вольєрів: {len(self.enclosures)}")
        
        print("\nЗапаси корму:")
        for food in self.food_supplies.values():
            print(f"- {food}")

if __name__ == "__main__":
    zoo = ZooInventory()
    
    zoo.add_employee(Employee("Іван Петренко", EmployeePosition.DIRECTOR, 25000))
    zoo.add_employee(Employee("Марія Сидорова", EmployeePosition.VETERINARIAN, 18000))
    zoo.add_employee(Employee("Олексій Коваль", EmployeePosition.KEEPER, 12000))
    
    cage1 = Enclosure(1, EnclosureType.CAGE, 10, 2)
    aviary1 = Enclosure(2, EnclosureType.AVIARY, 50, 5)
    aquarium1 = Enclosure(3, EnclosureType.AQUARIUM, 20, 3)
    
    zoo.add_enclosure(cage1)
    zoo.add_enclosure(aviary1)
    zoo.add_enclosure(aquarium1)
    
    zoo.add_food(Food(FoodType.MEAT, 50, "кг"))
    zoo.add_food(Food(FoodType.FRUIT, 100, "кг"))
    zoo.add_food(Food(FoodType.GRAIN, 200, "кг"))
    
    lion = Animal("Вовчик", "Лев", AnimalType.MAMMAL, EnclosureType.CAGE, [FoodType.MEAT])
    parrot = Animal("Кеша", "Папуга", AnimalType.BIRD, EnclosureType.AVIARY, [FoodType.FRUIT, FoodType.GRAIN])
    turtle = Animal("Доні", "Черепаха", AnimalType.REPTILE, EnclosureType.TERRARIUM, [FoodType.VEGETABLES])
    
    zoo.add_animal(lion, cage1)
    zoo.add_animal(parrot, aviary1)
    zoo.add_animal(turtle)  
    
    zoo.print_inventory()