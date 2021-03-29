class Storage:
    storage_dict = {}


class Equipment:
    def __init__(self, name, price, weight, con_power):  # модель, цена, вес, потребляемая мощность
        self.name = name
        self.price = price
        self.weight = weight
        self.con_power = con_power

    def forward(self, amount, ship_place):  # оправка на склад другого города: количество, место
        Storage.storage_dict[self.name] = [f'{self.price} рублей', f'{amount} шт', f'отправка в: {ship_place}']

    def valid(self):  # проверка родительских аргументов на соответствие типов
        if type(self.name) != str or type(self.weight) != int or type(self.con_power) != int:
            print('Данные введены неверно!!!')


class Printer(Equipment):
    def __init__(self, name, print_speed, price, weight, con_power):
        Equipment.__init__(self, name, price, weight, con_power)
        if type(print_speed) != int:
            print('Данные введены неверно!!!')
        else:
            self.print_speed = print_speed
        self.valid()


class Scanner(Equipment):
    def __init__(self, name, scan_speed, price, weight, con_power):
        Equipment.__init__(self, name, price, weight, con_power)
        self.scan_speed = scan_speed
        if type(scan_speed) != int:
            print('Данные введены неверно!!!')
        else:
            self.scan_speed = scan_speed
        self.valid()


class Copier(Equipment):
    def __init__(self, name,  price, scan_speed, print_speed, weight, con_power):
        Equipment.__init__(self, name, price, weight, con_power)
        if type(scan_speed) != int or type(print_speed) != int:
            print('Данные введены неверно!!!')
        else:
            self.scan_speed = scan_speed
            self.print_speed = print_speed
        self.valid()


epson = Scanner('Epson model 2021', 10, 4490, 7, 250)
epson.forward(100, 'Msk_storage')
print(Storage.storage_dict)
hp = Copier('hp 2020 station', 15090, 5, 3, 13, 450)
hp.forward(30, 'Spb_storage')
print(Storage.storage_dict)
