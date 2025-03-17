import math
# augmented assignment operators
# +=, -=, *=, /=, **=, %=, //=

animals = 0
print(f"{animals} += 2 ->")
animals += 2
print(animals)
print(f"{animals} -= 1 ->")
animals -= 1
print(animals)
print(f"{animals} *= 6 ->")
animals *= 6
print(animals)
print(f"{animals} /= 2 ->")
animals /= 2
print(animals)
print(f"{animals} **= 2 ->")
animals **= 2
print(animals)
print(f"{animals} %= 2 ->")
animals %= 2
print(f"{animals}\n")

# // is the floor division operator which returns the integer part of the division

# aritmetica 2

x = 10
y = 3.1425253
z = -2

print(f"x = {x}, y = {y}, z = {z}")

print(f"round(y, 1) = {round(y, 1)}")
print(f"round(y, 2) = {round(y, 2)}")
print(f"round(y, 3) = {round(y, 3)}")
print(f"y:.1f = {y:.1f}")
print(f"y:.2f = {y:.2f}")
print(f"y:.3f = {y:.3f}")
print(f"abs(z) = {abs(z)}")
print(f"pow(x, 2) = {pow(x, 2)}")
print(f"x**2 = {x**2}")
print(f"max(x, y, z) = {max(x, y, z)}\n")

# math module
print("pi = ", math.pi)
print("e = ", math.e)
print("math.sqrt(25) = ", math.sqrt(25))
print("math.ceil(3.14) = ", math.ceil(3.14))
print("math.floor(3.14) = ", math.floor(3.14))