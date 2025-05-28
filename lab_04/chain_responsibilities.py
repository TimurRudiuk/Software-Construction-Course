from abc import ABC, abstractmethod

class SupportHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, request):
        if self.next_handler:
            return self.next_handler.handle_request(request)
        return None

class TechnicalSupportHandler(SupportHandler):
    def handle_request(self, request):
        if request == "1":
            print("Technical support: Please check if your device is turned on.")
            return "Technical issue resolved"
        else:
            print("Technical support: Unable to help, transferring to billing...")
            return super().handle_request(request)

class BillingSupportHandler(SupportHandler):
    def handle_request(self, request):
        if request == "2":
            print("Billing support: Please check your payment method in account settings.")
            return "Billing issue resolved"
        else:
            print("Billing support: Unable to help, transferring to general...")
            return super().handle_request(request)

class GeneralSupportHandler(SupportHandler):
    def handle_request(self, request):
        if request == "3":
            print("General support: How can I assist you today?")
            return "General inquiry handled"
        else:
            print("General support: Unable to help, transferring to manager...")
            return super().handle_request(request)

class ManagerSupportHandler(SupportHandler):
    def handle_request(self, request):
        if request == "4":
            print("Manager: Let me connect you with a specialist.")
            return "Manager intervention required"
        else:
            print("Manager: Sorry, we couldn't help you. Starting over...")
            return None

def get_user_input(prompt, options):
    while True:
        print("\n" + prompt)
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Your choice: ").strip()
        if choice in options:
            return choice
        print("Invalid choice. Please try again.")

def task1_demo():
    technical = TechnicalSupportHandler()
    billing = BillingSupportHandler()
    general = GeneralSupportHandler()
    manager = ManagerSupportHandler()

    technical.set_next(billing).set_next(general).set_next(manager)

    questions = {
        "1": "Is your issue related to technical problems?",
        "2": "Is your issue related to billing or payments?",
        "3": "Is your issue a general question?",
        "4": "Do you need to speak with a manager?"
    }

    while True:
        print("\n=== Customer Support System ===")
        result = None
        current_handler = technical
        
        while current_handler and not result:
            question = "What type of support do you need?"
            choice = get_user_input(question, questions)
            result = current_handler.handle_request(choice)
            current_handler = current_handler.next_handler if not result else None
        
        if result:
            print(f"\nResult: {result}")
            break
        
        print("We couldn't determine your issue. Let's try again.")

if __name__ == "__main__":
    print("=== Task 1: Chain of Responsibility ===")
    task1_demo()