from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_shape(self, shape_name):
        pass

class VectorRenderer(Renderer):
    def render_shape(self, shape_name):
        return f"Drawing {shape_name} as vector"

class RasterRenderer(Renderer):
    def render_shape(self, shape_name):
        return f"Drawing {shape_name} as pixels"

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
    
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print(self.renderer.render_shape("Circle"))

class Square(Shape):
    def draw(self):
        print(self.renderer.render_shape("Square"))

class Triangle(Shape):
    def draw(self):
        print(self.renderer.render_shape("Triangle"))

def task3_demo():
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()
    
    shapes = [
        Circle(vector_renderer),
        Square(raster_renderer),
        Triangle(vector_renderer),
        Circle(raster_renderer)
    ]
    
    for shape in shapes:
        shape.draw()

if __name__ == "__main__":
    print("\n=== Task 3: Bridge ===")
    task3_demo()