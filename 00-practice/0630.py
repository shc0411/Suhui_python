"""
    26001
        - 이름 : 홍길동
        - 성별 : 남성
        - 이메일 : test1@yju.ac.kr
        - 수강과목
            - 파이썬
                - 학점 : 3학점
                - 점수 : 100
            - 인공지능
                - 학점 : 5학점
                - 점수 : 90
    26002
        - 이름 : 홍길삼
        - 성별 : 여성
        - 이메일 : test2@yju.ac.kr
        - 수강과목
            - DL
                - 학점 : 1학점
                - 점수 : 70
            - AI
                - 학점 : 2학점
                - 점수 : 60

"""

std_info = {
    "26001": {
        "이름": "홍길동",
        "성별": "남성",
        "이메일": "test1@yju.ac.kr",
        "수강과목": {
            "파이썬":{
                "학점":"3학점",
                "점수":"100"
            },
            "인공지능": {
                "학점":"5학점",
                "점수":"90"
            }
        }
    },
    "26002": {
        "이름": "홍길삼",
        "성별": "여성",
        "이메일": "test2@yju.ac.kr",
        "수강과목": {
            "DL": {
                "학점":"1학점", 
                "점수":"70"
            },
            "AI Agent": {
                "학점":"2학점", 
                "점수":"60"
            }
        }
    }
}

# print(std_info["26002"]["수강과목"]["AI Agent"]["점수"])
print(std_info.get("26002", {}).get("수강과목", {}).get("AI Agent", {}).get("점수", 0))



"""
2026-6-1
    - 청소그룹 : 
    - 청소명단 :
        - 홍길동
        - 홍길삼
    - 청소상태 : 양호
2026-6-2
    - 청소그룹 : 2
    - 청소명단 :
        - 김철수
        - 김영희
    - 청소상태 : 불량

"""
clean_info = {
    "2626-6-1": {
        "청소그룹": "1",
        "청소명단": [
            "홍길동", 
            "홍길삼"
        ],
        "청소상태":"양호"
            },
            
    "2626-6-2": {
        "청소그룹": "2",
        "청소명단": [
            "김철수", 
            "김영희"
        ],
        "청소상태":"불량"
            }
    }



print(std_info["26001"]["수강과목"])
print(clean_info["2626-6-2"]["청소명단"])


# # 26001의 이름 출력
# std_id = input("학번 입력: ")
# if std_id in std_info:
#     print(std_info["26001"]["이름"])
# else:
#     print("유효하지 않음")
                
# # 26002의 성별 출력
# std_id = input("학번 입력: ")
# if std_id in std_info:
#     print(std_info["26002"]["성별"])
# else:
#     print("유효하지 않음")

# # 학번, 이름 출력
# print("26001", std_info["26001"]["이름"])  







# dict -> in operator -> default -> key
# foo = {"Bmw x7": 2000, "benz gls": 500, "Tesla X": 300}

# test = ["a", "ab", "abc"]
# pos = {word : len(word) for word in test}
# # print(pos)


# country_code = {"KR": "대한민국", "JP": "일본", "FR": "프랑스"}
# pos = {value : key for key, value in country_code.items()}
# print(pos)























# # iteration : Element -> value
# for value in foo.keys():
#     print(f"value: {value}")

# print(sum(foo.values()))

# pos = {"Bmw x7", "benz gls", "Tesla X", "GV80"}

# foo_keys = foo.keys

# print(foo_keys - pos)
# print(pos - foo_keys)






# # iteraion : Element -> key
# for key in foo:
#     print(f"key: {key}")  

# bar = list(foo.keys())
# print(bar, type(bar))
# print(bar[0])













# # dict -> in operator -> default -> key
# foo = {"Bmw x7": 2000, "benz gls": 500, "Tesla X": 300}


# a, b = (2, 3) # a -> 2, b -> 3


# # iteraion : Element -> key : value
# for key, value in foo.items():
#     print(f"key: {key}, value: {value}")  



# if "Bmw x7" in foo:
#     print("있어")
# else:
#     print("없어")



# bar = [10, 20, 30, 1, 2]

# for value in bar:   # # Iteration: bar에서 순차적으로 꺼내서 value에 담는 것
#     print(value)