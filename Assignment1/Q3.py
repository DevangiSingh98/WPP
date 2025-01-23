#user input
feet = float(input("Enter the length in feet: "))
print("Choose a conversion option:")
print("1. Convert to inches")
print("2. Convert to yards")
print("3. Convert to miles")
print("4. Convert to millimeters")
print("5. Convert to centimeters")
print("6. Convert to meters")
print("7. Convert to kilometers")


factors = [12, 0.333333, 0.000189394, 304.8, 30.48, 0.3048, 0.0003048]
units = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]

# Conversion Input
choice = int(input("Enter the number of your choice: "))

if 1 <= choice <= 7:
    convertedvalue = feet * factors[choice - 1]
    print(f"{feet} feet is equal to {convertedvalue:.4f} {units[choice - 1]}")
else:
    print("Invalid choice.")
