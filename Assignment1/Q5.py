name = []
max = 15

# Input 
print("Enter the names of 10 students (max 15 characters each):")
for i in range(10):
    name = input(f"Enter name for student {i + 1}: ")
    if len(name) > max:
        name = name[:max]
    name.append(name)

# Reverse name
print("\nReversed names of the students:")
for name in name:
    reverse = name[::-1]  
    print(reverse)
