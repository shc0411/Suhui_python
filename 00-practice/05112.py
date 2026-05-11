scores = [80,90,70],[75,85,95],[60,70,80]
         # 학생 1    # 학생 2    # 학생 3
for idx, student in enumerate(scores):
    total = 0
    for score in student:    # 각 과목 점수
        total += score       # 점수 더하기
    avg = total / len(student) # 총점수 나누기 len = 학생 수(3)
    print(f"학생 {idx}: 평균 {avg:.1f}")  # :.1f -> 소수 첫째자리까지 나타내기