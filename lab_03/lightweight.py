from composer import LightNode, LightTextNode, LightElementNode

class LightHTMLFlyweight:
    _element_cache = {}
    
    @classmethod
    def get_element(cls, tag, display_type, closing_type, css_classes=None):
        key = (tag, display_type, closing_type, tuple(css_classes or []))
        
        if key not in cls._element_cache:
            cls._element_cache[key] = LightElementNode(tag, display_type, closing_type, css_classes)
        
        return cls._element_cache[key]

class LightElementNodeWithFlyweight(LightNode):
    def __init__(self, tag, display_type, closing_type, css_classes=None):
        self.flyweight = LightHTMLFlyweight.get_element(tag, display_type, closing_type, css_classes)
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def outer_html(self):
        if self.flyweight.closing_type == "single":
            return self.flyweight.outer_html()
        
        return self.flyweight.outer_html().replace(
            f"</{self.flyweight.tag}>", 
            self.inner_html() + f"</{self.flyweight.tag}>"
        )
    
    def inner_html(self):
        return "".join(child.outer_html() for child in self.children)

def parse_text_to_html(text):
    lines = text.split('\n')
    root = LightElementNodeWithFlyweight("div", "block", "double")
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        if i == 0:
            element = LightElementNodeWithFlyweight("h1", "block", "double")
        elif len(line) < 20:
            element = LightElementNodeWithFlyweight("h2", "block", "double")
        elif line.startswith(' '):
            element = LightElementNodeWithFlyweight("blockquote", "block", "double")
        else:
            element = LightElementNodeWithFlyweight("p", "block", "double")
        
        element.add_child(LightTextNode(line))
        root.add_child(element)
    
    return root

def get_memory_usage(obj, seen=None):
    if seen is None:
        seen = set()
    
    if id(obj) in seen:
        return 0
    seen.add(id(obj))
    
    size = 0
    try:
        size += obj.__sizeof__()
    except AttributeError:
        pass
    
    if isinstance(obj, dict):
        for k, v in obj.items():
            size += get_memory_usage(k, seen)
            size += get_memory_usage(v, seen)
    elif hasattr(obj, '__dict__'):
        size += get_memory_usage(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        for item in obj:
            size += get_memory_usage(item, seen)
    
    return size

def task6_demo():
    book_text = """The Great Book
Chapter 1
  Once upon a time...
This is a long paragraph that should be rendered as a regular paragraph.
Short line
  Another indented line
End of book"""
    
    html_tree = parse_text_to_html(book_text)
    
    print("Generated HTML:")
    print(html_tree.outer_html())
    
    print("\nMemory usage (bytes):")
    print("Without flyweight:", get_memory_usage(LightElementNode("div", "block", "double")))
    print("With flyweight:", get_memory_usage(LightElementNodeWithFlyweight("div", "block", "double")))

if __name__ == "__main__":
    print("\n=== Task 6: Flyweight ===")
    task6_demo()