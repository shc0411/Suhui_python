# std_info = {
#             "26001": {"이름": "홍길동",
#             "수강과목" : ["파이썬", "인공지능"],
#             "재적상태" : "재학"},
#             "26002": {"이름": "홍길삼",
#             "수강과목" : ["DL", "AI Agent"],
#             "재적상태" : "휴학"},
#         }

# # 학번, 이름 출력
# print("26001", std_info["26001"]["이름"])  # 26001 홍길동
# print("26002", std_info["26002"]["이름"])  # 26002 홍길삼

# # 학번, 이름, 수강과목 2개 출력
# print(std_info["26001"]["수강과목"][0])  # 파이썬
# print(std_info["26001"]["수강과목"][1])  # 인공지능

# std_id = input("학번을 입력하세요: ")
# # Exception handling(예외처리)
# try:
#     print(std_info[std_id])
# except KeyError:
#     print("유효하지 않음")

# if std_id in std_info:
#     print(std_info[std_id])
# else:
#     print("유효하지 않음")

std_info = {
            "26001": {"이름": "홍길동",
            "수강과목" : ["파이썬", "인공지능"],
            "재적상태" : "재학"},
            "26002": {"이름": "홍길삼",
            "수강과목" : ["DL", "AI Agent"],
            "재적상태" : "휴학"},
        }

std_id = input("학번을 입력하세요: ")

# 이름과 재적상태 출력
# print(std_info.get(std_id, {}))
print(std_info.get(std_id, {}).get("이름", ""))