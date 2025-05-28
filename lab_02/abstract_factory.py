from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Netbook(ABC):
    @abstractmethod
    def display_info(self):
        pass

class EBook(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Smartphone(ABC):
    @abstractmethod
    def display_info(self):
        pass

class IPhoneLaptop(Laptop):
    def display_info(self):
        return "IPhone Laptop - Thin and Powerful"

class IPhoneNetbook(Netbook):
    def display_info(self):
        return "IPhone Netbook - Compact and Efficient"

class IPhoneEBook(EBook):
    def display_info(self):
        return "IPhone EBook - Easy on Eyes"

class IPhoneSmartphone(Smartphone):
    def display_info(self):
        return "IPhone Smartphone - Innovative Design"

class XiaomiLaptop(Laptop):
    def display_info(self):
        return "Xiaomi Laptop - Affordable Performance"

class XiaomiNetbook(Netbook):
    def display_info(self):
        return "Xiaomi Netbook - Lightweight Companion"

class XiaomiEBook(EBook):
    def display_info(self):
        return "Xiaomi EBook - Long Battery Life"

class XiaomiSmartphone(Smartphone):
    def display_info(self):
        return "Xiaomi Smartphone - Best Value"

class GalaxyLaptop(Laptop):
    def display_info(self):
        return "Galaxy Laptop - Reliable Workhorse"

class GalaxyNetbook(Netbook):
    def display_info(self):
        return "Galaxy Netbook - Durable Design"

class GalaxyEBook(EBook):
    def display_info(self):
        return "Galaxy EBook - Comfortable Reading"

class GalaxySmartphone(Smartphone):
    def display_info(self):
        return "Galaxy Smartphone - User-Friendly"

class TechFactory(ABC):
    @abstractmethod
    def create_laptop(self) -> Laptop:
        pass
    
    @abstractmethod
    def create_netbook(self) -> Netbook:
        pass
    
    @abstractmethod
    def create_ebook(self) -> EBook:
        pass
    
    @abstractmethod
    def create_smartphone(self) -> Smartphone:
        pass

class IProneFactory(TechFactory):
    def create_laptop(self) -> Laptop:
        return IPhoneLaptop()
    
    def create_netbook(self) -> Netbook:
        return IPhoneNetbook()
    
    def create_ebook(self) -> EBook:
        return IPhoneEBook()
    
    def create_smartphone(self) -> Smartphone:
        return IPhoneSmartphone()

class KiaomiFactory(TechFactory):
    def create_laptop(self) -> Laptop:
        return XiaomiLaptop()
    
    def create_netbook(self) -> Netbook:
        return XiaomiNetbook()
    
    def create_ebook(self) -> EBook:
        return XiaomiEBook()
    
    def create_smartphone(self) -> Smartphone:
        return XiaomiSmartphone()

class BalaxyFactory(TechFactory):
    def create_laptop(self) -> Laptop:
        return GalaxyLaptop()
    
    def create_netbook(self) -> Netbook:
        return GalaxyNetbook()
    
    def create_ebook(self) -> EBook:
        return GalaxyEBook()
    
    def create_smartphone(self) -> Smartphone:
        return GalaxySmartphone()

def task2_demo():
    factories = [IProneFactory(), KiaomiFactory(), BalaxyFactory()]
    for factory in factories:
        print(f"\nCreating devices from {factory.__class__.__name__}:")
        devices = [
            factory.create_laptop(),
            factory.create_netbook(),
            factory.create_ebook(),
            factory.create_smartphone()
        ]
        for device in devices:
            print(device.display_info())

if __name__ == "__main__":
    print("\n=== Task 2: Abstract Factory ===")
    task2_demo()