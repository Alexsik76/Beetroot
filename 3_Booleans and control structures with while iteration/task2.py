# The valid phone number program
phone_num = input('Введите номер телефона: ')
if phone_num.isnumeric() and len(phone_num) == 10:
    print('Спасибо за корректный номер')
elif not phone_num.isnumeric():
    print('Номер содержит не только цифры')
elif not len(phone_num) == 10:
    print('Длина номера отличается от 10')
