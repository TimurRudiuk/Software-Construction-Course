# Zoo Management System - Lab 01

## Дотримання принципів програмування

### DRY (Don't Repeat Yourself)
**Пояснення:** Уникається дублювання логіки, наприклад, метод `add_animal` централізує перевірки й додавання тварин.

[`zoo_classes.py`](./zoo_classes.py#L82-L99)

---

### KISS (Keep It Simple, Stupid)
**Пояснення:** Класи мають просту структуру, зрозумілу логіку та обмежену кількість відповідальностей.

[`zoo_classes.py`](./zoo_classes.py#L5-L65)

---

### S – Single Responsibility Principle
**Пояснення:** Кожен клас відповідає за свою частину логіки — тварини, працівники, вольєри тощо.

[`zoo_classes.py`](./zoo_classes.py)

---

### O – Open/Closed Principle
**Пояснення:** Код підтримує додавання нових типів їжі, тварин або вольєрів без зміни існуючого функціоналу.

[`zoo_classes.py`](./zoo_classes.py#L3-L4)

---

### L – Liskov Substitution Principle
**Пояснення:** Теоретично, класи можна розширювати, не ламаючи логіку — наприклад, підкласи тварин.

[`zoo_classes.py`](./zoo_classes.py#L43-L54)

---

### I – Interface Segregation Principle
**Пояснення:** Кожен клас має лише необхідні методи. Наприклад, `Enclosure` має тільки методи роботи з тваринами.

[`zoo_classes.py`](./zoo_classes.py#L66-L81)

---

### D – Dependency Inversion Principle
**Пояснення:** Залежність від абстракцій реалізовано через `enum`, які виступають інтерфейсами для їжі, типів тварин тощо.

[`zoo_classes.py`](./zoo_classes.py#L3-L4)

---

### YAGNI (You Aren’t Gonna Need It)
**Пояснення:** У коді немає зайвих функцій "про запас", тільки необхідна логіка.

[`task2.py`](./task2.py)

---

### Composition Over Inheritance
**Пояснення:** Замість наслідування — використання композиції (наприклад, список тварин усередині `Enclosure`).

[`zoo_classes.py`](./zoo_classes.py#L66-L81)

---

### Program to Interfaces, Not Implementations
**Пояснення:** Абстракції через `enum` дозволяють змінювати реалізації без змін логіки.

[`task2.py`](./zoo_test.py#L43-L55)

---

### Fail Fast
**Пояснення:** Перевірки в `add_animal` одразу зупиняють виконання при помилці — наприклад, несумісний тип вольєра або переповнення.

[`zoo_classes.py`](./zoo_classes.py#L82-L99)


