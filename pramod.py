

# -------------------------------------------

# x = [[0, 0]]
# a = x + x

# a[0][0] = 100
# print(a)

# --------------------------
# y = ((0, 0))
# b = y + y
# # b[0][0] = 100


# print(b)
# -------------------------------

# y = ([0, 0],)               # Here If I skip the comma (,) then it will be treated as list otherwise it will be treated as Tuple
# # b = y + y

# print(type(y))
# -------------------------------------

# z = tuple((1,2))        
# print(type(z))
# -------------------------------------

# a = 100000
# b = 100000

# print( a is b)
# print(a == b)

# 2. ------------------------
# a = 10
# b = 20

# a = a + 10

# print(id(a))
# print(id(b))

# -------------------------------------------
# -5 and 256 it will return true else false

import math

a = 100000000000000000000000000000000000000000000000000000.5
b = 100000000000000000000000000000000000000000000000000000.5

print(a is b)       # This will compare the memory location of 2 objects
print(a == b)       # This will compare the internal state of 2 objects

print(id(a))
print(id(b))

print("Is Close ",math.isclose(a, b))

# -----------------------
a = [1,2, 3]
b = [1,2, 3]

print(a is b)
print(a == b)

print(id(a))
print(id(b))
