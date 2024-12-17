import re

numbers_list = ['АБОБА777', 'А000АА22', '21А221РР123', 'В333ВК11', 'Ы777ЫЫ123']


# Метод проверки номеров
def car_number_checker(number_list=None):

    if number_list is None:
        number_list = [str]
    # Шаблон
    pattern = r'([АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2})(\d{2,3})'
    # Применяем шаблон
    for number in number_list:
        print('Номер: ', number)
        result = re.fullmatch(pattern, number)
        if result is not None:
            print('Номер ', result[1], ' валиден. Регион: ', result[2], '\n')
        else:
            print('Номер не валиден.\n')

    return 'Список проверен!'

print(car_number_checker(numbers_list))
