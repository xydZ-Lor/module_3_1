calls = 0 # Переменная для подсчета количества вызовов функций

def count_calls(): # функция увеличивающий глобальный счетчик при использование других функций
    global calls # Обозначаем глобальная переменную
    calls += 1 # Увеличиваем счетчик
    return calls # Возвращаем текущее значение счетчика

def string_info(string): # Возвращает кортеж, содержащий длину строки, строку в нижнем регистре и строку в верхнем регистре.
    count_calls() # Увеличиваем счетчик вызовов
    return (len(string) , string.lower() , string.upper()) # Возвращаем информацию о строке в нижнем и в верхнем регистре

def is_contains(string, listt_to_searh): # Проверяет, содержится ли строка в списке, игнорируя регистр букв.
    count_calls() # Увеличиваем счетчик вызовов
    return string.upper() in [s.upper() for s in listt_to_searh] # Проверяем есть ли строки в списке в верхнем регистре

print(string_info('Capybara')) # должно вывести кол-во символов, нижний регистр и верхний
print(string_info('Armageddon')) # должно вывести кол-во символов, нижний регистр и верхний
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Содержится ли 'Urban' в списке ['ban', 'BaNaN', 'urBAN']
print(is_contains('cycle', ['recycling', 'cyclic'])) # Содержится ли 'cycle' в списке ['recycling', 'cyclic']
print(calls) # Сколько раз вызвали функцию count_calls