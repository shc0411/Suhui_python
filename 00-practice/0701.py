# bar = [value for value in range(10, 110, 10)]  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# foo = "hello world"

# # Iteration
# for value in bar:
#     print(value)

# for text in foo:
#     print(text)



# bar = {"a": 10, "b": 20, "c": 30}

# # Iteration for dictionary
# # 1) key : value -> 모든 작업 가능 -> (items)
# for key, value in bar.items():
#     print(f"keys: {key}")
#     print(f"values: {value}")

# # 2) key -> 현재 dict 내 필수키가 있는지 없는지 -> (keys(), in 연산자 기본)
# for key in bar.keys():
#     print(f"keys: {key}")

# # 3) value -> 현 dict 내 값들에 대한 연산 적용 시 -> (value)
# for value in bar.values():
#     print(f"values: {value}")




# # 초기화(생성) + CRUD
# bar = {}
# bar_1 = dict()
# print(type(bar))

# Create ~~ update
# b_dict = {"a": 10}

# f_list = [10]

# # Create in a list
# f_list.append(10)

# print(b_dict.setdefault("a", 20))


# # Create in a dict X -> Update in a dict
# # if "a" not in b_dict:
# #     b_dict["a"] = 10
# #     print("신규생성")


# bar = {"a": 10}

# bar["b"] = 20
# bar["ces"] = "hello"
# bar[200] = True

# print(bar)


# bar = {"a": 10}
# bar.update({"b":20, "c":30})
# bar.update({"b":200, "c":300})
# print(bar)



# bar = {'a': 10, 'b': 200, 'c': 300}

# # bar.clear()
# # print(bar)

# # del bar["f"]
# if bar.pop("b", False):
#     print("삭제 성공")
# print(bar)



bar = {}

# dict -> Element -> key : value
# keys -> ["261", "262", "263"]
# values -> ["김철수", "김영희", "홍길동"]


# a = [1, 2, 3, 4, 5, 6, 7] # 에러 x, 쌍 만든 것까지만 출력
# b = [10, 20, 30, 40]
# c = zip(a, b)

# print(list(c))


std_id = ["261", "262", "263", "264",]
std_name = ["김철수", "김영희", "홍길동",]
std_info = list(zip(std_id, std_name))
dict_std_info = dict(std_info)
print(dict_std_info)