"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 1: 성적 등급

점수를 입력받아 등급을 출력하세요.
if/elif/else를 사용합니다.

[등급 기준]
90 이상: A 
80 이상: B
70 이상: C
60 이상: D
60 미만: F
"""

# score = int(input("점수를 입력하세요: "))

# 아래에 등급을 판정하여 출력하세요


# "입력" 문구를 띄우고 점수를 입력받으세요.
score = int(input("점수를 입력하세요: "))

if score >= 90:
    grade = "A"

elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"

elif score >= 60:
    grade = "D"

else:
    grade = "F"

print("점수:", score)
print("등급:", grade)

"""
[실행 결과 예시] (입력: 85)
점수: 85
등급: B
"""
