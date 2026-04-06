"""
실습 5: 별 찍기

숫자를 입력받아 아래와 같은 삼각형을 출력하세요.
중첩 for문을 사용합니다.

힌트: print("*", end="")는 줄바꿈 없이 출력합니다.
      print()는 줄바꿈만 합니다.
"""

n = int(input("줄 수를 입력하세요: ")) 

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

# 아래에 별 삼각형을 출력하세요
# for i in range(1, n+1): # 줄 번호
#     for j in range(i):  # 별 개수 반복
#         print("*", end="")   # "*" 별 출력, end="" 줄바꿈 없이 옆으로 계속 출력
#     print()


"""
[실행 결과 예시] (입력: 5)
*
**
***
****
*****
"""
