name1 = input ("Enter first name = ")
name2 = input ("Enter second name = ")

name  = name1+name2
name = name.upper()

L = name.count('L')
O = name.count('O')
V = name.count('V')
E = name.count('E')

T = name.count('T')
R = name.count('R')
U = name.count('U')
E = name.count('E')

first = L+O+V+E
second = T+R+U+E

print(f" match count = {first}{second}")
