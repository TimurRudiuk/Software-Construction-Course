class Logger:
    def log(self, message):
        print(f"\033[92m[LOG] {message}\033[0m")  
    
    def error(self, message):
        print(f"\033[91m[ERROR] {message}\033[0m")  
    
    def warn(self, message):
        print(f"\033[93m[WARN] {message}\033[0m")  

class FileWriter:
    def write(self, text):
        with open("log.txt", "a") as f:
            f.write(text)
    
    def write_line(self, text):
        with open("log.txt", "a") as f:
            f.write(text + "\n")

class FileLoggerAdapter:
    def __init__(self, file_writer):
        self.file_writer = file_writer
    
    def log(self, message):
        self.file_writer.write_line(f"[LOG] {message}")
    
    def error(self, message):
        self.file_writer.write_line(f"[ERROR] {message}")
    
    def warn(self, message):
        self.file_writer.write_line(f"[WARN] {message}")

def task1_demo():
    print("=== Console Logger ===")
    console_logger = Logger()
    console_logger.log("System started")
    console_logger.warn("Low memory")
    console_logger.error("Disk failure")
    
    print("\n=== File Logger (via Adapter) ===")
    file_writer = FileWriter()
    file_logger = FileLoggerAdapter(file_writer)
    file_logger.log("System started")
    file_logger.warn("Low memory")
    file_logger.error("Disk failure")
    
    print("\nCheck 'log.txt' file for results")

if __name__ == "__main__":
    task1_demo()