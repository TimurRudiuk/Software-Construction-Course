class CommandCentre:
    def __init__(self):
        self.runways = []
        self.aircrafts = []

    def register_runway(self, runway):
        self.runways.append(runway)
        runway.command_centre = self

    def register_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)
        aircraft.command_centre = self

    def notify(self, sender, event):
        if isinstance(sender, Aircraft):
            if event == "land":
                available_runway = next((r for r in self.runways if not r.is_busy), None)
                if available_runway:
                    available_runway.is_busy = True
                    print(f"Aircraft {sender.name} is landing on runway {available_runway.id}")
                    return True
                else:
                    print(f"No available runway for aircraft {sender.name}")
                    return False
            elif event == "take_off":
                runway = next((r for r in self.runways if r.is_busy), None)
                if runway:
                    runway.is_busy = False
                    print(f"Aircraft {sender.name} is taking off from runway {runway.id}")
                    return True
                else:
                    print("No aircraft on runway for takeoff")
                    return False

class Aircraft:
    def __init__(self, name):
        self.name = name
        self.command_centre = None

    def land(self):
        print(f"Aircraft {self.name} requesting to land")
        return self.command_centre.notify(self, "land")

    def take_off(self):
        print(f"Aircraft {self.name} requesting to take off")
        return self.command_centre.notify(self, "take_off")

class Runway:
    def __init__(self, id):
        self.id = id
        self.is_busy = False
        self.command_centre = None

def task2_demo():
    command_centre = CommandCentre()

    runway1 = Runway("RWY-09L")
    runway2 = Runway("RWY-27R")
    command_centre.register_runway(runway1)
    command_centre.register_runway(runway2)

    aircraft1 = Aircraft("Boeing 737")
    aircraft2 = Aircraft("Airbus A320")
    command_centre.register_aircraft(aircraft1)
    command_centre.register_aircraft(aircraft2)

    print("\n=== Aircraft Operations ===")
    aircraft1.land()
    aircraft2.land()
    aircraft1.take_off()
    aircraft2.land()
    aircraft2.take_off()

if __name__ == "__main__":
    print("\n=== Task 2: Mediator ===")
    task2_demo()