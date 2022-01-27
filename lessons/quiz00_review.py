x: str = "goheels"
y: int = 1
z: int = len(x)

y = y ** 2
x = x[z - 1] + x[y] + str(y)

print(x)
print(y % 4)
print(z)