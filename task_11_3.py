class MyErr(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


list1 = []
while True:
    a = input('Введите число. Чтобы прекратить ввод-- "stop" ')
    if a == 'stop':
        print(list1)
        break
    else:
        try:
            if not a.isdigit():
                raise MyErr(f'Элемент списка {a} не является числом')
        except ValueError:
            print()
        except MyErr as terr:
            print(terr)
        else:
            list1.append(a)
