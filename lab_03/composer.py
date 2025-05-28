from abc import ABC, abstractmethod

class LightNode(ABC):
    @abstractmethod
    def outer_html(self):
        pass
    
    @abstractmethod
    def inner_html(self):
        pass

class LightTextNode(LightNode):
    def __init__(self, text):
        self.text = text
    
    def outer_html(self):
        return self.text
    
    def inner_html(self):
        return self.text

class LightElementNode(LightNode):
    def __init__(self, tag, display_type, closing_type, css_classes=None):
        self.tag = tag
        self.display_type = display_type
        self.closing_type = closing_type
        self.css_classes = css_classes or []
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def outer_html(self):
        classes = f" class=\"{' '.join(self.css_classes)}\"" if self.css_classes else ""
        opening_tag = f"<{self.tag}{classes}>"
        
        if self.closing_type == "single":
            return opening_tag[:-1] + "/>"
        
        inner = self.inner_html()
        closing_tag = f"</{self.tag}>"
        
        return opening_tag + inner + closing_tag
    
    def inner_html(self):
        return "".join(child.outer_html() for child in self.children)

def task5_demo():
    table = LightElementNode("table", "block", "double", ["table", "table-bordered"])
    
    header_row = LightElementNode("tr", "block", "double")
    headers = ["Name", "Age", "Country"]
    for header in headers:
        th = LightElementNode("th", "block", "double")
        th.add_child(LightTextNode(header))
        header_row.add_child(th)
    table.add_child(header_row)
    
    # Додаємо дані
    data = [
        ["John", "30", "USA"],
        ["Anna", "25", "Germany"],
        ["Peter", "35", "UK"]
    ]
    
    for row_data in data:
        row = LightElementNode("tr", "block", "double")
        for cell_data in row_data:
            td = LightElementNode("td", "block", "double")
            td.add_child(LightTextNode(cell_data))
            row.add_child(td)
        table.add_child(row)
    
    # Виводимо HTML
    print("Generated HTML:")
    print(table.outer_html())

if __name__ == "__main__":
    print("\n=== Task 5: Composite ===")
    task5_demo()