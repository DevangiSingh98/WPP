alphabet = set('abcdefghijklmnopqrstuvwxyz')

s = input("Enter a sentence: ").lower()
set = set(s)  

if alphabet.issubset(set):  
    print("Pangram.")
else:
    print("Not Pangram.")