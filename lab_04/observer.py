class EventListener:
    def __init__(self, event_type, callback):
        self.event_type = event_type
        self.callback = callback

class LightElementNode:
    def __init__(self, tag, display_type, closing_type, css_classes=None):
        self.tag = tag
        self.display_type = display_type
        self.closing_type = closing_type
        self.css_classes = css_classes or []
        self.children = []
        self.event_listeners = []

    def add_event_listener(self, event_type, callback):
        self.event_listeners.append(EventListener(event_type, callback))

    def trigger_event(self, event_type):
        for listener in self.event_listeners:
            if listener.event_type == event_type:
                listener.callback(self)

def click_handler(element):
    print(f"Element {element.tag} was clicked!")

def hover_handler(element):
    print(f"Mouse over element {element.tag}")

button = LightElementNode("button", "inline", "double", ["btn"])
button.add_event_listener("click", click_handler)
button.add_event_listener("mouseover", hover_handler)

button.trigger_event("click")
button.trigger_event("mouseover")