import re

class SmartTextReader:
    def read_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        return [list(line.strip()) for line in lines]

class SmartTextChecker:
    def __init__(self, real_reader):
        self.real_reader = real_reader
    
    def read_file(self, filename):
        print(f"Opening file {filename}")
        result = self.real_reader.read_file(filename)
        print(f"Successfully read file {filename}")
        
        lines = len(result)
        chars = sum(len(line) for line in result)
        print(f"Lines: {lines}, Chars: {chars}")
        
        print(f"Closing file {filename}")
        return result

class SmartTextReaderLocker:
    def __init__(self, real_reader, pattern):
        self.real_reader = real_reader
        self.pattern = re.compile(pattern)
    
    def read_file(self, filename):
        if self.pattern.search(filename):
            print("Access denied!")
            return None
        return self.real_reader.read_file(filename)

def task4_demo():
    real_reader = SmartTextReader()
    
    print("=== Testing SmartTextChecker ===")
    checker = SmartTextChecker(real_reader)
    content = checker.read_file("example.txt")
    print("Content:", content[:2], "...") 
    
    print("\n=== Testing SmartTextReaderLocker ===")
    locker = SmartTextReaderLocker(real_reader, r"restricted.*\.txt")
    
    print("Trying to read allowed file:")
    content = locker.read_file("example.txt")
    print("Content:", content[:2] if content else "None", "...")
    
    print("\nTrying to read restricted file:")
    content = locker.read_file("restricted_data.txt")
    print("Content:", content if content else "None")

if __name__ == "__main__":
    print("\n=== Task 4: Proxy ===")
    task4_demo()