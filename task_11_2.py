class MyError(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


member_1 = input('Введите делимое ')
member_2 = input('Введите делитель ')
try:
    member_1 = int(member_1)
    member_2 = int(member_2)
    if member_2 == 0:
        raise MyError('Делитель равен нулю')
except MyError as mr:
    print(mr)
except ZeroDivisionError:
    print()
else:
    print(member_1 / member_2)
