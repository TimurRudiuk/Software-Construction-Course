import copy

class Virus:
    def __init__(self, weight, age, name, species):
        self.weight = weight
        self.age = age
        self.name = name
        self.species = species
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def clone(self):
        return copy.deepcopy(self)

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}Name: {self.name}, Species: {self.species}, Age: {self.age}, Weight: {self.weight}")
        for child in self.children:
            child.display(level + 1)

def task4_demo():
    grandparent = Virus(50, 10, "GrandVirus", "Alpha")
    
    parent1 = Virus(30, 5, "ParentVirus1", "Beta")
    parent2 = Virus(35, 6, "ParentVirus2", "Beta")
    
    child1 = Virus(15, 2, "ChildVirus1", "Gamma")
    child2 = Virus(18, 3, "ChildVirus2", "Gamma")
    child3 = Virus(20, 1, "ChildVirus3", "Gamma")
    
    grandparent.add_child(parent1)
    grandparent.add_child(parent2)
    
    parent1.add_child(child1)
    parent1.add_child(child2)
    parent2.add_child(child3)
    
    print("Original Virus Family:")
    grandparent.display()
    
    cloned_virus = grandparent.clone()
    cloned_virus.name = "ClonedGrandVirus"
    cloned_virus.children[0].name = "ClonedParentVirus1"
    cloned_virus.children[0].children[0].name = "ClonedChildVirus1"
    
    print("\nCloned Virus Family (with some name changes):")
    cloned_virus.display()
    
    print("\nOriginal Virus Family (should remain unchanged):")
    grandparent.display()

if __name__ == "__main__":
    print("\n=== Task 4: Prototype ===")
    task4_demo()