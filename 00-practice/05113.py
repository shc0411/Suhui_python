# for i in range(5):
#     if i == 3:
#         break
#     print(i, end="")

# # 정답: 012


# for i in range(5):
#     if i % 2 == 0:
#         continue
#     print(i, end=" ")

# 정답: 3


s = 0
for i in range(1, 10):
    s += 1
    if s > 15:
        break
print(s,i)

# 답: 9 9
