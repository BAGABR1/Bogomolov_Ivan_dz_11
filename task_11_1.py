class Date:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def valid(d, m, y):
        if 0 < d < 32 and 0 < m < 13 and 0 < y < 2022:
            print(f'дата {d}-{m}-{y} верна!')
        else:
            print(f'значение даты {d}-{m}-{y} ошибочно!')

    @classmethod
    def int_date(cls, date):
        true_date_list = []
        date_list = date.split('-')
        for i in date_list:
            if i.isdigit():
                true_date_list.append(i)
            else:
                print(f'дата введена ошибочно: {date}!')
                return 0
        a, b, c = map(int, true_date_list)
        return Date.valid(a, b, c)


Date.int_date('38-03-2021')
Date.int_date('u8-03-2021')
Date.int_date('28-03-2021')
