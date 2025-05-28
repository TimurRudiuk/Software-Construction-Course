from abc import ABC, abstractmethod

class Subscription(ABC):
    def __init__(self):
        self.monthly_fee = 0
        self.min_period = 0
        self.channels = []
        self.features = []

    def __str__(self):
        return f"{self.__class__.__name__}: Monthly fee - {self.monthly_fee}$, Min period - {self.min_period} months, Channels - {len(self.channels)}, Features - {', '.join(self.features)}"

class DomesticSubscription(Subscription):
    def __init__(self):
        super().__init__()
        self.monthly_fee = 5
        self.min_period = 1
        self.channels = ["Local News", "Entertainment", "Sports"]
        self.features = ["SD Quality", "Limited Content"]

class EducationalSubscription(Subscription):
    def __init__(self):
        super().__init__()
        self.monthly_fee = 10
        self.min_period = 3
        self.channels = ["Science", "History", "Documentaries"]
        self.features = ["HD Quality", "Educational Content", "No Ads"]

class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__()
        self.monthly_fee = 20
        self.min_period = 6
        self.channels = ["Movies", "Series", "Sports", "News", "Kids"]
        self.features = ["4K Quality", "All Content", "No Ads", "Multi-device"]

class SubscriptionCreator(ABC):
    @abstractmethod
    def create_subscription(self) -> Subscription:
        pass

class WebSite(SubscriptionCreator):
    def create_subscription(self) -> Subscription:
        print("Creating subscription via Website...")
        return PremiumSubscription()

class MobileApp(SubscriptionCreator):
    def create_subscription(self) -> Subscription:
        print("Creating subscription via Mobile App...")
        return DomesticSubscription()

class ManagerCall(SubscriptionCreator):
    def create_subscription(self) -> Subscription:
        print("Creating subscription via Manager Call...")
        return EducationalSubscription()

def task1_demo():
    creators = [WebSite(), MobileApp(), ManagerCall()]
    for creator in creators:
        subscription = creator.create_subscription()
        print(subscription)
        print()

if __name__ == "__main__":
    print("=== Task 1: Factory Method ===")
    task1_demo()