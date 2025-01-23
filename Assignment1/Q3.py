options = [1,2,3,4,5,6,7]

ft = int(input("Enter length in feet: "))

print("\n1. inches\
      2. yards\
      3. miles\
      4. milimeters\
      5. centimeters\
      6. meters\
      7. kilometres ")
convert = int(input("Choose option to convert into: "))

for i in options:
      if convert == options[i]:
            continue
      else:
            print("Invalid option")
            break