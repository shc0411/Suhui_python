"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 3: 교통수단 추천

거리(km)를 입력받아 적절한 교통수단을 추천하세요.
if/elif/else를 사용합니다.

[추천 기준]
2km 미만: 도보
2km 이상 5km 미만: 자전거
5km 이상 20km 미만: 버스
20km 이상: 지하철
"""

distance = float(input("거리를 입력하세요 (km): "))

# 아래에 교통수단을 추천하여 출력하세요

if distance < 2:
    norimono = "도보"

elif 2 <= distance < 5:
    norimono = "자전거"

elif 5 <= distance < 20:
    norimono = "버스"

else:
    norimone = "지하철"

print("거리: " + str(distance) + "km")
print("추천 교통수단:", norimono)

"""
[실행 결과 예시] (입력: 8.5)
거리: 8.5km
추천 교통수단: 버스
"""
