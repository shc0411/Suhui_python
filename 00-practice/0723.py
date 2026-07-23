# def add(a, b):
#     return a + b 

# result_1 = add(2, 3)

# result_2 = add(4, 5)

# print(result_1, result_2)



# def bar(msg):
#     print(f"bar: {msg}")


# def foo(msg):
#     print("foo: {msg}")
#     bar("GSC")
#     print("foo is completed")

# foo("YJU")



# def bar(a, b, c):
#     print(a, b, c)

# bar(1, 2, 3) # 1, 2, 3
# bar(c = 7, a = 6, b = 5)  # 6, 5, 7


# def bar(arg_a):
#     if arg_a % 2 == 0:
#         return "짝수"

#     msg = "홀수 입니다!"

#     return msg

# print(bar(2))
# print(bar(2))



# def bar():
#     print("bar 호출")

# print(bar())



# def bar(value):
#     if value <= 0:
#         return

#     if value % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")

# if bar(-1) == None:
#     print("양의 정수만 입력 하세요")





def get_sum_avg(arg_a, arg_b):
    value_sum = arg_a + arg_b
    value_avg = value_sum / 2

    return value_sum
print(type(get_sum_avg(2, 4)))