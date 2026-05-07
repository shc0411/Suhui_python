# num = int(input())
# reverse = 0

# while num > 0:
#     digit = num & 10
#     reverse = reverse * 10 + digit 
#     num //= 10
# print(f"뒤집은 숫자: {reverse}")


n = int(input())

for i in range(1, n + 1):      
    for j in range(1, i + 1): 
        print(j, end="")
    print()