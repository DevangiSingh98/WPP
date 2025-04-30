import math

class Vector2D:
    def __init__(self, x, y):
       
        self.x = x
        self.y = y

    def magnitude(self):  
        
        return math.sqrt(self.x**2 + self.y**2)

    def rotation(self):
        
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def dot_product(self, other):
        """Returns the dot product of two vectors."""
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        
        return self.x * other.y - self.y * other.x

    def __str__(self):
        
        return f"Vector2D({self.x}, {self.y})"


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot_product(self, other):
        
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __str__(self):
        
        return f"Vector3D({self.x}, {self.y}, {self.z})"

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print("2D Vectors:")
print("Magnitude of v1:", v1.magnitude())
print("Rotation of v1:", v1.rotation(), "degrees")
print("Distance between v1 and v2:", v1.distance(v2))
print("Dot Product of v1 and v2:", v1.dot_product(v2))
print("Cross Product of v1 and v2:", v1.cross_product(v2))

v3 = Vector3D(1, 2, 3)
v4 = Vector3D(4, 5, 6)

print("\n3D Vectors:")
print("Magnitude of v3:", v3.magnitude())
print("Dot Product of v3 and v4:", v3.dot_product(v4))
print("Cross Product of v3 and v4:", v3.cross_product(v4))
