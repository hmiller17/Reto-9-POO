from . import Class_point, Class_line

# Clase Shape
class Shape:
    def __init__(self, is_regular: bool):
        self.is_regular = is_regular

    def vertices(self) -> list[Class_point.Point]:
        #* Al ser una clase abstracta, se debe implementar en las subclases de acuerdo a los requerimientos de la figura.
        raise NotImplementedError("Este método debe implementarse en las subclases.")

    def edges(self) -> list[Class_line.Line]:
        #* Al ser una clase abstracta, se debe implementar en las subclases de acuerdo a los requerimientos de la figura.
        raise NotImplementedError("Este método debe implementarse en las subclases.")

    def inner_angles(self) -> list[float]:
        #* Al ser una clase abstracta, se debe implementar en las subclases de acuerdo a los requerimientos de la figura.
        return self.compute_inner_angles()

    def compute_area(self) -> float:
        #* Al ser una clase abstracta, se debe implementar en las subclases de acuerdo a los requerimientos de la figura.
        raise NotImplementedError("Este método debe implementarse en las subclases.")

    def compute_perimeter(self) -> float:
        #* Al ser una clase abstracta, se debe implementar en las subclases de acuerdo a los requerimientos de la figura.
        return sum(edge.length for edge in self.edges)

    def compute_inner_angles(self) -> list[float]:
        #* Al ser una clase abstracta, se debe implementar en las subclases de acuerdo a los requerimientos de la figura.
        raise NotImplementedError("Este método debe implementarse en las subclases.")