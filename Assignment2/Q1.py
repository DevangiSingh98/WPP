str = input("Enter a string: ")

new = ''

for i in range(len(str)):
    if not i %2:
        new = new + str[i].lower()
    else:
        new = new + str[i].upper()
print(new)