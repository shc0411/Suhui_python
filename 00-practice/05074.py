'''
정수를 하나 입력받아 그 숫자의 각 자리 수의 합을 구해 출력하시오
예: 입력이 1234이면 출력은 10 (1+2+3+4)
(힌트: n % 10으로 마지막 자리를 얻고, n //= 10으로 자리를 줄인다)

'''
n = int(input())
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10
print(total)
    