import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

print("Upper case:\n", s.str.upper())
print("Lower case:\n", s.str.lower())
print("Length of string values:\n", s.str.len())
