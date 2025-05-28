class TextDocument:
    def __init__(self, content=""):
        self.content = content
    
    def add_text(self, text):
        self.content += text
    
    def delete_text(self, length):
        self.content = self.content[:-length]
    
    def __str__(self):
        return self.content

class TextEditorMemento:
    def __init__(self, content):
        self.content = content

class TextEditor:
    def __init__(self):
        self.document = TextDocument()
        self.history = []
        self.current_state = -1
    
    def add_text(self, text):
        self._save_state()
        self.document.add_text(text)
    
    def delete_text(self, length):
        self._save_state()
        self.document.delete_text(length)
    
    def _save_state(self):
        if self.current_state + 1 < len(self.history):
            self.history = self.history[:self.current_state + 1]
        
        memento = TextEditorMemento(self.document.content)
        self.history.append(memento)
        self.current_state = len(self.history) - 1
    
    def undo(self):
        if self.current_state <= 0:
            print("Nothing to undo")
            return
        
        self.current_state -= 1
        self.document.content = self.history[self.current_state].content
    
    def redo(self):
        if self.current_state >= len(self.history) - 1:
            print("Nothing to redo")
            return
        
        self.current_state += 1
        self.document.content = self.history[self.current_state].content
    
    def show_document(self):
        print(f"Current document: '{self.document}'")

def task5_demo():
    editor = TextEditor()
    
    print("=== Text Editor Demo ===")
    editor.add_text("Hello")
    editor.show_document()
    
    editor.add_text(" World")
    editor.show_document()
    
    editor.add_text("!")
    editor.show_document()
    
    print("\nUndoing last change:")
    editor.undo()
    editor.show_document()
    
    print("\nUndoing one more change:")
    editor.undo()
    editor.show_document()
    
    print("\nRedoing one change:")
    editor.redo()
    editor.show_document()
    
    print("\nAdding new text after undo/redo:")
    editor.add_text(" Python")
    editor.show_document()
    
    print("\nTrying to redo after new change:")
    editor.redo() 
    editor.show_document()

if __name__ == "__main__":
    print("\n=== Task 5: Memento ===")
    task5_demo()