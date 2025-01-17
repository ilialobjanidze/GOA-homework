
a = 10
b = 20

print(a < b)  # True
print(a > b)  # False
print(a == b)  # False

x = 5
y = 15

print(x < 10 and y > 10)  # True
print(x > 10 or y > 10)  # True

c = 30
d = 40

result = (c < d and c > 20) or c == 30
print(result)  # True

result = (a > b) or (x < 10 and y < 20)
print(result)  # True
