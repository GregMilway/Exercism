import itertools

class Triangle:
    """Stores and classifies a triangle by side-length.
    Treats degenerate triangles as invalid
    """
    def __init__(self,a,b,c):
        if not self.validate_triag([a,b,c]):
            raise TriangleError('Invalid Triangle')
        self.sides = set([a,b,c])

    def kind(self):
        return self.classification[len(self.sides)]

    def validate_triag(self,triag):
        valid_sides = min(triag) > 0
        valid_length = all(triag[n] < triag[(n+1)%3]+triag[(n+2)%3]
                                                            for n in range(3))
        return valid_sides and valid_length

    classification = {1: 'equilateral', 2: 'isosceles', 3: 'scalene'}

class TriangleError(ValueError):
    """Raised when triangle is impossible"""
    pass
