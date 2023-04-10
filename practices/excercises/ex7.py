import decimal

class Calculator:

    PI = "3.14"

    def __init__(self, radius):
        self.radius = radius

    def area_cal(self):
        area = (self.radius**2)*decimal.Decimal(Calculator.PI)
        return area
    
    def circumference(self):
        circ = (2*self.radius)*decimal.Decimal(Calculator.PI)
        return circ

    def volume(self):
        temp = str(4/3)
        vol = decimal.Decimal(temp)*decimal.Decimal(Calculator.PI)*(self.radius**3)
        return vol
    
    def surface_area(self):
        sur = 4*decimal.Decimal(Calculator.PI)*(self.radius**2)
        return sur
    

    
radius = int(input("半径を入力してください: "))
obj = Calculator(radius)

print(obj.area_cal())
print(obj.circumference())
print(obj.volume())
print(obj.surface_area())
