import numpy as np

N = 10  
cartesian = np.random.rand(N, 2) * 10 

r = np.sqrt(cartesian[:, 0]**2 + cartesian[:, 1]**2)  
theta = np.arctan2(cartesian[:, 1], cartesian[:, 0])  

polar = np.column_stack((r, theta)) 

print("Cartesian Coordinates:\n", cartesian)
print("\nPolar Coordinates:\n", polar)
