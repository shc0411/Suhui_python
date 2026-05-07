# n = 10
# while n > 0:
#     print(n)
#     n -= 1


# n = 10
# step = 0
# while n > 0:
#     print(n)
#     n -= step



# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# n = 10
# while n > 0:
#     print(n)
#     n -= 2

# x = 1
# while x < 100:
#     x *= 2
# print(x)

s = "abcd"
while s:
    print(s[0])
    s = s[1:]

n = 20
cnt = 0
while n > 0:
    if n % 2 == 0:
        cnt += 1
    n -= 1
print(cnt)


done = False
i = 0
while not done:
    i += 1
    if i == 3:
        done = True
print(i)