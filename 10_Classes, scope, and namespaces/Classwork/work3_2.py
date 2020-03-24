import time


class Services:
    def __init__(self, start=None, finish=None, duration=0,):
        # number is a number of this client in a local DB
        self.time_start = start
        self.time_finish = finish
        self.duration = duration
        self.local = 'ukr'

        def f_duration(self):
            ''' Defines duration by the following logic: If the duration is
                specified directly, the start and end are ignored.
                Otherwise, the difference between end and start is
                returned'''
            if self.duration:
                result = self.duration
                return result
            elif ((self.time_start < self.time_finish)):
                return (self.time_finish - self.time_start)
            else:
                print(self.message('Duration error'))
                self.time_start = self.user_input('time')
                self.time_finish = self.user_input('time')
                return (self.time_finish - self.time_start)
        self.duration = f_duration(self)

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

    def user_input(self, type):
        request = self.message('Input')
        value = self.message(type.capitalize()).lower()
        string = (input(f'{request} {value}: ')).strip()
        self.correct_type(string, type)
        return string

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


s1 = Services(1, 1)
print(s1.duration)
