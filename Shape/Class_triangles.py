import math
import time
from . import Class_line, Class_point, Class_shape


# Clase Triangle
class Triangle(Class_shape.Shape):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(is_regular=self.is_equilateral(vertices))
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
        return [Class_line.Line(self._vertices[i], self._vertices[(i + 1) % 3]) for i in range(3)]

    @time_execution
    def compute_area(self) -> float:
        a, b, c = (edge.length for edge in self.edges)
        s = (a + b + c) / 2
        time.sleep(2)
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def compute_inner_angles(self) -> list[float]:
        a, b, c = (edge.length for edge in self.edges)
        angles = [
            math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c))),
            math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))),
            math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        ]
        return angles

    @staticmethod
    def is_equilateral(vertices: list[Class_point.Point]) -> bool:
        edges = [Class_line.Line(vertices[i], vertices[(i + 1) % 3]) for i in range(3)]
        return all(math.isclose(edges[0].length, edge.length) for edge in edges)

# Subclases de Triangle
class Isosceles(Triangle):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(vertices)
        if not self.is_isosceles():
            #* Se establece una variable para cada lado del triángulo, luego se evalua si hay dos lados iguales, 
            #* si no se cumple la condición se lanza un error inidicando que los vértices no forman un triángulo isósceles.
            raise ValueError("Los vértices no forman un triángulo isósceles.")

    def is_isosceles(self) -> bool:
        a, b, c = (edge.length for edge in self.edges)
        return math.isclose(a, b) or math.isclose(a, c) or math.isclose(b, c)

class Equilateral(Triangle):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(vertices)
        if not self.is_equilateral(vertices):
            #* Se compara un lado del triángulo con los otros para verificar si son iguales, si no se cumple la condición se lanza un error.
            raise ValueError("Los vértices no forman un triángulo equilátero.")

class Scalene(Triangle):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(vertices)
        if not self.is_scalene():
            #* Se establece una variable para cada lado del triángulo, luego se evalua si los tres lados son diferentes,
            #* si no se cumple la condición entonces se lanza un error indicando que los vértices no forman un triángulo escaleno.
            raise ValueError("Los vértices no forman un triángulo escaleno.")

    def is_scalene(self) -> bool:
        a, b, c = (edge.length for edge in self.edges)
        return not (math.isclose(a, b) or math.isclose(a, c) or math.isclose(b, c))

class Trirectangle(Triangle):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(vertices)
        if not self.is_right_triangle():
            #* Se establece una variable para cada lado del triángulo, luego se ordenan los lados de menor a mayor,
            #* usando el teorema de Pitágoras se verifica si se cumple la condición de un triángulo rectángulo, si no es así se lanza un error.
            raise ValueError("Los vértices no forman un triángulo rectángulo.")

    def is_right_triangle(self) -> bool:
        a, b, c = sorted(edge.length for edge in self.edges)
        return math.isclose(a**2 + b**2, c**2)