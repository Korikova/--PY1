def get_count_char(str_):
    counter = {} # Словарь для хранения количества вхождения каждого символа в строки
    str_ = str_.lower() # Перевод строки в нижний регистр
    for char in str_:
        if char.isalpha(): # Проверяем, является ли символ буквой
            if char in counter:
                counter[char] = counter[char] + 1 # Такая буква уже есть в словаре counter, поэтому увеличиваем имееющееся значение на 1
            else:
                counter[char] = 1 # Если ещё не встречали такую букву, сохраняем 1
    return counter


def percentage(dictionary):
    total_count = sum(dictionary.values())  # Вычисляем общее количество символов
    percentage_counter = {}  # Создаём новый словарь, чтобы не менять исходный
    for char, amount in dictionary.items():
        percentage_counter[char] = round(amount / total_count * 100.0, 2) # Применим round для округления до сотых
    return percentage_counter


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print((percentage(get_count_char(main_str))))
