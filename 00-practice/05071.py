total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(total)

n = 2025
cnt = 0 
while n > 0:
    n //= 10
    cnt += 1
    print(cnt)

a, b = 48, 18
while b != 0:
    a, b = b, a % b
    print(a)