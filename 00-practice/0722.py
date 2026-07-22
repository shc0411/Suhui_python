def check_score(score):
    if score < 0:
        print("잘못된 점수입니다.")
        return
    
    print("점수 확인 완료")
    return score

check_score(-10)



def test():
    print("시작")
    return
    print("이 문장은 실행되지 않음")

test()



def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([3, 1 ,9, 5])
print(result)

low, high = min_max([3, 1, 9, 5])
print(low, high)



def hello(name):
    return f"{name}님, 환영합니다"
print(hello("파이썬"))

def add(a, b):
    return a + b
print(add(3, 5))

def bigger(a, b):
    if a > b:
        return a
    else:
        return b

print(bigger(7, 3))




def calc(a, b):
    return a + b, a - b

result = calc(10, 3)
print(result)
s, d = calc(10, 3)
print(s, d)