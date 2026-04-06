# "국어 점수" 문구를 띄우고 정수로 점수를 입력받으세요
korean = int(input("국어 점수: "))

# "영어 점수" 문구를 띄우고 정수로 점수를 입력받으세요
english = int(input("영어 점수: "))

# "수학 점수" 문구를 띄우고 정수로 점수를 입력받으세요
math = int(input("수학 점수: "))

# 다중 대입을 사용해 "국어", "수학", "영어"를 저장하세요
sub1, sub2, sub3 = "국어", "영어", "수학"

# 과목: 국어 영어 수학 을 출력하세요
print("과목:", sub1, sub2, sub3)

# 국어: [입력받은 점수] 출력 
print(sub1 + ":", korean)

# 영어: [입력받은 점수] 출력
print(sub2 + ":", english)

# 수학: [입력받은 점수] 출력
print(sub3 + ":", math)

# 총점은 total = 0으로 시작하세요
total = 0

# 점수를 하나씩 누적하세요
total += korean       # total = total + 10 -> total = 10
total += english      # total = total + 20 -> total = 30
total += math         # total = total + 30 -> total = 60

# 총점: total 출력
print("총점:", total)

# 평균: total / 3 출력
print(f"평균: {total / 3}")
