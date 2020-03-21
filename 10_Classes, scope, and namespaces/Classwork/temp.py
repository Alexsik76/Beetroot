import json #подключаем библиотеку для работы с json

stroke = '{"food": "banana"}' #json-строка

stroke_s = json.loads(stroke) #загоняем в переменную результат чтения json-строки

print(stroke_s) #выводим результат на экран
