# for i in range(1, 11):
#     print(i)

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

word = "programming"

vowels = ["a", "e", "i", "o", "u"]

count = 0

for ch in word:
    if ch in vowels:
        count += 1

print("모음 개수:", count)


