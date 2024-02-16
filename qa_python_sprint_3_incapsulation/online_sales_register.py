import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
        
    @property
    def number_items(self):
        return self.__number_items


    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1
    
      
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1
    

    def check_amount(self):
        total = []
        discount = 0.1
        
        for item in self.__name_items:
            total.append(self.__item_price[item])
        
        if len(self.__name_items) > 10:
            return sum(total) * (1 - discount)
        else:
            return sum(total)
    

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        tax = 0.2
        discount = 0.1
        
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)

        for item in twenty_percent_tax:
            total.append(self.__item_price[item])

        if len(self.__name_items) > 10:
            total_sum_tax = sum(total) * (1 - discount) * tax
        else:
            total_sum_tax = sum(total) * tax
        
        return total_sum_tax
    

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        tax = 0.1
        discount = 0.1

        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)

        for item in ten_percent_tax:
            total.append(self.__item_price[item])
    
        if len(self.__name_items) > 10:
            total_sum_tax = sum(total) * (1 - discount) * tax
        else:
            total_sum_tax = sum(total) * tax
        
        return total_sum_tax
    

    def total_tax(self):
        total_sum_tax = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
        return total_sum_tax
    

    @staticmethod    
    def get_telephone_number(telephone_number):
        if type(telephone_number) != int:
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'
        

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]
        for item in date:
            date_and_time.append(f'{item[0]}: {item[1](now)}')
        return date_and_time