# Legal Services
import time


class Services:
    def __init__(self, number, start=None, finish=None,
                 duration=0, date=time.localtime()[2::-1]):
        # number is a number of this client in a local DB
        self.number = number
        self.time_start = start
        self.time_finish = finish
        self.duration = duration(start, finish, duration)
        self.date = date
        self.price = None
        self.local = 'en'

    def message(self, key):
        messages = {
                    'Duration error': 'Помилка тривалості',
                    'Date': 'Дата',
                    'Time': 'Час',
                    'Duration': 'Тривалість',
                    'Input': 'Введіть'
        }
        if self.local == 'en':
            return self.key
        else:
            return messages[self.key]

    def cost(self):
        price = self.price
        time = self.time_finish - self.time_start
        cost = time * price
        return cost

    def duration(self, start, finish, duration):
        ''' Defines duration by the following logic: If the duration is
        specified directly, the start and end are ignored. Otherwise, the
        difference between end and start is returned'''
        if duration:
            result = self.correct_type(duration, 'duration')
            return result
        elif (
                self.correct_type(start, 'time') and
                self.correct_type(start, 'time') and
                (start < finish)
                ):
            return (finish - start)
        else:
            print(self.message('Duration error'))

    def correct_type(self, value, type):
        if self.type == 'duration':
            try:
                value = float(self.value)
                if value > 0:
                    return value
                else:
                    print(self.message('Duration error'))
                    self.user_input('duration')
            except(TypeError, ValueError) as message:
                print(self.message('Duration error'))
                print(message)
                self.user_input(self.type)
        else:
            if self.type == 'date':
                correct_string = '%d,%m,%y'
            elif self.type == 'time':
                correct_string = '%H:%M'
            try:
                value = time.strptime(self.value, correct_string)
                return value
            except(TypeError, ValueError) as mess:
                print(mess)
                self.user_input(self.type)

        def user_input(self, type):
            request = self.message('Input')
            value = self.message(type.capitalize()).lower()
            string = (input(f'{request} {value}: ')).strip()
            self.correct_type(string, self.type)
            return string


class Consultation(Services):
    def __init__(self, number, start, finish, date):
        super().__init__(number, date)
        self.price = 200
        self.type = 'Консультація'


class Preparation_of_documents(Services):
    def __init__(self, number, start, finish, date):
        super().__init__(number, date)
        self.price = 100
        self.type = 'Підоготовка документів'

# %d%m%y


a = Consultation(1, '21.03.20')
print(a.cost())