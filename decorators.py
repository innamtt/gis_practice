#
# def decorator(func):
#     def decorated(input_text):
#         print('함수 시작')
#         func(input_text)
#         print('함수 끝')
#
#     return decorated


# @decorator
# def hello_world(input_text):
#     print(input_text)

# hello_world('hello')

# def dec(func):
#     def decorated(w,h):
#         if w > 0 and h > 0:
#             func(w,h)
#             print("는 양수")
#         else:
#             func(w,h)
#             print("Error")
#     return decorated
#

# def check_integer(func):
#     def decorated(width, height):
#         if width >= 0 and height >= 0:
#             return func(width, height)
#         else:
#             raise ValueError("에러")
#     return decorated

def check_integer(func):
    def decorated(user, width, height):
        if width >= 0 and height >= 0:
            return func(user, width, height)
        else:
            raise ValueError("에러")
    return decorated


def login_required(func):
    def decorated(user, width, height):
        if user.is_authenticated:
            return func(user, width, height)
        else:
            raise ValueError("에러")
    return decorated


@check_integer
def rect(w,h):
    return w * h


@check_integer
def tri(w,h):
    return w * h / 2

w=1
h=2

print(tri(w,h))
print(rect(w,h))

# User 클래스 작성
# User 클래스 내 is_authenticated 변수 작성
# User 객체를 넓이 함수 인자로 전달
# is_authenticated 변수를 확인하고, True가 아닐경우 Error 발생

#
class User:
    def __init__(self, auth):
        self.is_authenticated = auth


user = User(auth=False)


r = rect(user, 10, 10)
print(r)

t = tri(user, 10, 10)
print(t)