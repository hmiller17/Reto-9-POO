from . import Class_line, Class_point, Class_shape
import math
import time


class Rectangle(Class_shape.Shape):
    def __init__(self, vertices: list[Class_point.Point]):
        if not self.is_rectangle(vertices):
            #* Se establecen las diagonales del rectángulo, luego se compara si las longitudes de las diagonales son iguales, si no es asi se lanza la excepción.
            raise ValueError("Los vértices no forman un rectángulo ni un cuadrado.")
        
        super().__init__(is_regular=self.is_square(vertices))
        self._vertices = vertices

    def time_execution(func):
        """Decorador para medir el tiempo de ejecución de una función."""
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.6f} segundos")
            return result
        return wrapper
    
    @property
    def vertices(self) -> list[Class_point.Point]:
        return self._vertices

    @property
    def edges(self) -> list[Class_line.Line]:
        return [Class_line.Line(self._vertices[i], self._vertices[(i + 1) % 4]) for i in range(4)]

    @time_execution
    def compute_area(self) -> float:
        time.sleep(2)
        return self.edges[0].length * self.edges[1].length

    def compute_inner_angles(self) -> list[float]:
        return [90.0, 90.0, 90.0, 90.0]

    @staticmethod
    def is_square(vertices: list[Class_point.Point]) -> bool:
        edges = [Class_line.Line(vertices[i], vertices[(i + 1) % 4]) for i in range(4)]
        lengths = [edge.length for edge in edges]
        return all(math.isclose(length, lengths[0]) for length in lengths)

    @staticmethod
    def is_rectangle(vertices: list[Class_point.Point]) -> bool:
        diagonals = [
            Class_line.Line(vertices[0], vertices[2]),
            Class_line.Line(vertices[1], vertices[3])
        ]
        return math.isclose(diagonals[0].length, diagonals[1].length)

# Subclase de Rectangle
class Square(Rectangle):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(vertices)
        if not self.is_square(vertices):
            #* Se compara un lado del cuadrado con los otros para verificar si son iguales, si no se cumple la condición se lanza un error.
            raise ValueError("Los vértices no forman un cuadrado.")
