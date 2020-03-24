#import datetime
import time


class Services:
    def __init__(self, number, start=None, finish=None,
                 duration=0, date=time.localtime()[2::-1]):
        # number is a number of this client in a local DB
        self.number = number
        self.time_start = start
        self.time_finish = finish
        self.duration = duration
        self.date = date
        self.local = 'en'

        def f_duration(self):
            ''' Defines duration by the following logic: If the duration is
                specified directly, the start and end are ignored.
                Otherwise, the difference between end and start is
                returned'''
            print(correct_type(self, start, 'time'))
            print(correct_type(finish, 'time'))
            print((start < finish))
            if self.duration:
                result = correct_type(self.duration, 'duration')
                print(self.duration)
                return result
            elif (
                    correct_type(self.start, 'time') and
                    correct_type(self.finish, 'time') and
                    (self.start < self.finish)
                    ):
                print('Work')
                return (self.finish - self.start)
            else:
                print(self.message('Duration error'))
        self.duration = f_duration(self)

    def correct_type(self, value, type):
        if type == 'duration':
            try:
                value = float(value)
                if value > 0:
                    return value
                else:
                    print(self.message('Duration error'))
                    self.user_input('duration')
            except(TypeError, ValueError) as message:
                print(self.message('Duration error'))
                print(message)
                self.user_input(type)
        else:
            if type == 'date':
                correct_string = '%d,%m,%y'
            elif type == 'time':
                correct_string = '%H:%M'
            try:
                value = time.strptime(value, correct_string)
                return value
            except(TypeError, ValueError) as mess:
                print(mess)
                self.user_input(type)

    def user_input(self, type):
        request = self.message('Input')
        value = self.message(type.capitalize()).lower()
        string = (input(f'{request} {value}: ')).strip()
        self.correct_type(string, type)
        return string

    def message(self, key):
        messages = {
                    'Duration error': 'Помилка тривалості',
                    'Date': 'Дата',
                    'Time': 'Час',
                    'Duration': 'Тривалість',
                    'Input': 'Введіть'
                    }
        if self.local == 'en':
            return key
        else:
            return messages[key]

    def cost(self):
        price = self.price
        time = self.time_finish - self.time_start
        cost = time * price
        return cost


s1 = Services(1, 6, 8)
print(s1.duration)
