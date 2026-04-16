wind = float(input("풍속(m/s) 입력: "))

if wind < 4:
    print("약풍")

elif 4 <= wind < 9:
    print("보통")

elif 9 <= wind < 14:
    print("강풍")

else:
    print("폭풍 경보")