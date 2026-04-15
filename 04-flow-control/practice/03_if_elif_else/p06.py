"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 6: 요일 판별

숫자(1~7)를 입력받아 요일을 출력하세요.
if/elif/else를 사용합니다.

[요일 기준]
1: 월요일
2: 화요일
3: 수요일
4: 목요일
5: 금요일
6: 토요일
7: 일요일
그 외: "잘못된 입력입니다."
"""

day = int(input("숫자를 입력하세요 (1~7): "))

# 아래에 요일을 판별하여 출력하세요
if day == 1:
    nichi = "월요일"

elif day == 2:
    nichi = "화요일"

elif day == 3:
    nichi = "수요일"
elif day == 4:
    nichi = "목요일"
elif day == 5:
    nichi = "금요일"
elif day == 6:
    nichi = "토요일"
elif day == 7:
    nichi = "일요일"

else:
    nichi = "잘못된 입력입니다."

if 1 <= day <= 7:
    print(f"{day} -> {nichi}")
else:
    print(nichi)

"""
[실행 결과 예시] (입력: 3)
3 → 수요일

[실행 결과 예시] (입력: 9)
잘못된 입력입니다.
"""
