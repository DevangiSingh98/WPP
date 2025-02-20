class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()

        self.to_meters = {
            "inches": 0.0254,
            "feet": 0.3048,
            "yards": 0.9144,
            "miles": 1609.34,
            "kilometers": 1000,
            "meters": 1,
            "centimeters": 0.01,
            "millimeters": 0.001
        }

        if self.unit not in self.to_meters:
            print("Invalid unit")
            self.valid = False
        else:
            self.valid = True

    def to_base_meters(self):
        
        return self.length * self.to_meters[self.unit]

    def convert_to(self, targetunit):
        
        return self.to_base_meters() / self.to_meters[targetunit]

length = float(input("Enter the length: "))
unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").lower()

converter = Converter(length, unit)

if converter.valid:
    print("\nConverted values:")
    for i in converter.to_meters:
        print(f"{i.capitalize()}: {converter.convert_to(i)}")
