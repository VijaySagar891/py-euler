sum = 0
x, y = 1, 2

while x <= 4000000:
    if x%2 ==0:
        sum += x
    x, y = y, x + y

print(sum)
