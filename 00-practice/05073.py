'''
사용자로부터 문자열을 계속 입력받다가 "quit"이 입력되면 종료하시오.
종료한 뒤, 그동안 입력된 문자열의 개수를 출력하시오
(힌트: "quit"은 개수에 포함하지 않음)
'''

user_input = input()
count = 0
while True:
    user_input = input()
    if user_input == "quit":
        break
    count += 1
print(count)
    