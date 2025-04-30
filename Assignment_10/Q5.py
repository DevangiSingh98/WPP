import numpy as np

arr = np.array(["apple", "banana", "cherry", "mango", "orange"])  

left = np.char.ljust(arr, 15, "_")   
right = np.char.rjust(arr, 15, "_")  
center = np.char.center(arr, 15, "_") 

print("Left Justified:\n", left)
print("\nRight Justified:\n", right)
print("\nCentered:\n", center)
