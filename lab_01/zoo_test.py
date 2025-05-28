from zoo_classes import (
    ZooInventory,
    Employee,
    EmployeePosition,
    Enclosure,
    EnclosureType,
    Food,
    FoodType,
    Animal,
    AnimalType
)

def main():
    zoo = ZooInventory()
    
    print("=== Тестування системи зоопарку ===")
    
    print("\n1. Додаємо співробітників:")
    director = Employee("Олена Іванова", EmployeePosition.DIRECTOR, 30000)
    vet = Employee("Петро Сидоров", EmployeePosition.VETERINARIAN, 20000)
    keeper = Employee("Марія Коваленко", EmployeePosition.KEEPER, 15000)
    
    zoo.add_employee(director)
    zoo.add_employee(vet)
    zoo.add_employee(keeper)
    
    for emp in zoo.employees:
        print(f"- {emp}")
    
    print("\n2. Створюємо вольєри:")
    small_cage = Enclosure(1, EnclosureType.CAGE, 5, 1)
    big_aviary = Enclosure(2, EnclosureType.AVIARY, 30, 3)
    aquarium = Enclosure(3, EnclosureType.AQUARIUM, 15, 2)
    
    zoo.add_enclosure(small_cage)
    zoo.add_enclosure(big_aviary)
    zoo.add_enclosure(aquarium)
    
    for enc in zoo.enclosures:
        print(f"- {enc}")
    
    print("\n3. Поповнюємо запаси корму:")
    zoo.add_food(Food(FoodType.MEAT, 50, "кг"))
    zoo.add_food(Food(FoodType.FRUIT, 30, "кг"))
    zoo.add_food(Food(FoodType.VEGETABLES, 20, "кг"))
    
    for food in zoo.food_supplies.values():
        print(f"- {food}")
    
    print("\n4. Заселяємо тварин:")
    lion = Animal("Король", "Лев", AnimalType.MAMMAL, EnclosureType.CAGE, [FoodType.MEAT])
    parrot = Animal("Ріко", "Ара", AnimalType.BIRD, EnclosureType.AVIARY, [FoodType.FRUIT, FoodType.GRAIN])
    turtle = Animal("Тото", "Черепаха", AnimalType.REPTILE, EnclosureType.TERRARIUM, [FoodType.VEGETABLES])
    
    print(f"Спроба поселити {lion} в маленьку клітку...")
    if zoo.add_animal(lion, small_cage):
        print("Успішно!")
    else:
        print("Не вдалось :(")
    
    print(f"\nСпроба поселити {parrot} в вольєр для птахів...")
    if zoo.add_animal(parrot, big_aviary):
        print("Успішно!")
    else:
        print("Не вдалось :(")
    
    print(f"\nДодаємо {turtle} без вольєра (тимчасово)...")
    zoo.add_animal(turtle)
    
    print("\n5. Тестуємо помилкові сценарії:")
    
    snake = Animal("Зіггі", "Змія", AnimalType.REPTILE, EnclosureType.TERRARIUM, [FoodType.MEAT])
    print(f"Спроба поселити {snake} в акваріум...")
    if zoo.add_animal(snake, aquarium):
        print("Успішно!")
    else:
        print("Помилка: невідповідний тип вольєра!")
    
    another_parrot = Animal("Кікі", "Папуга", AnimalType.BIRD, EnclosureType.AVIARY, [FoodType.FRUIT])
    print(f"\nСпроба додати {another_parrot} до вже заповненого вольєра...")
    if zoo.add_animal(another_parrot, big_aviary):
        print("Успішно!")
    else:
        print("Помилка: вольєр переповнений!")
    
    print("\n=== Підсумкова інформація про зоопарк ===")
    zoo.print_inventory()
    
    print("\n7. Додаткові тести взаємодії:")
    
    print(f"\nВидаляємо {parrot} з вольєра...")
    if big_aviary.remove_animal(parrot):
        print("Успішно видалено!")
        print(f"Тепер у вольєрі {big_aviary.enclosure_id} знаходиться {len(big_aviary.animals)} тварин")
    else:
        print("Помилка при видаленні")
    
    print(f"\nСпроба знову додати {another_parrot} до вольєра...")
    if zoo.add_animal(another_parrot, big_aviary):
        print("Тепер успішно!")
    else:
        print("Знову помилка :(")

if __name__ == "__main__":
    main()