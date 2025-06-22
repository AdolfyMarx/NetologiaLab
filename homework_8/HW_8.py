# Глобальные переменные
import time

text_template = 'Пользователь {user} {sex}, {age} лет {verb} покупку на {prise} у.е. с {device} из браузера {browser}. Регион, из которого совершалась покупка: {place}'
pass_to_table = 'web_clients_correct.csv'
pass_to_result = 'result_file.txt'
asexual_list = []
unknown_device_list = []


# Метод взаимодействия с файлами
def open_file(path, mode):
    try:
        table = open(path, mode, encoding='utf-8')
    except FileNotFoundError:
        print('Error in opening file ', path)
        return False
    return table


# Метод обработки входных данных
def table_to_text_converter():
    # Вызываем методы чтения/создания файлов
    source_table = open_file(pass_to_table, 'r')
    result_file = open_file(pass_to_result, 'w+')
    # Создаем необходимые переменные
    parsed_line = []
    line_counter = 0
    except_counter = 0
    success_counter = 0
    # Читаем бесполезную строку с заголовками
    line = source_table.readline()
    # Запускаем цикл чтения строк из исходного файла
    while True:
        line = source_table.readline()
        # Проверяем что строка не пустая
        if not line:
            break
        line_counter += 1
        print('строка ', line_counter, end='')
        parsed_line = line.split(',')
        # Идентификация пола
        if parsed_line[3] == 'male':
            sex = 'мужского пола'
            verb = 'совершил'
        elif parsed_line[3] == 'female':
            sex = 'женского пола'
            verb = 'совершила'
        else:
            asexual_list.append(parsed_line[0])
            print('Зверь неведомого пола detected - ', parsed_line[0])
            sex = 'загадочного пола'
            verb = 'совершилО'
        # Идентификация устройства
        if parsed_line[1] == 'mobile':
            device = 'мобильного'
        elif parsed_line[1] == 'tablet':
            device = 'планшетного'
        elif parsed_line[1] == 'desktop':
            device = 'настольного ПК'
        elif parsed_line[1] == 'laptop':
            device = 'носимого ПК'
        else:
            unknown_device_list.append(parsed_line[2])
            print('Неизветсное устройство detected - ', parsed_line[2])
            device = 'помощью голубиной почты'
        # Заполнение шаблона
        result_text = text_template.format(user=parsed_line[0],
                                           sex=sex,
                                           verb=verb,
                                           age=parsed_line[4],
                                           prise=parsed_line[5],
                                           device=device,
                                           browser=parsed_line[2],
                                           place=parsed_line[6])
        # Пытаемся записать в файл с результатом
        print(' - обработана ', end='')
        try:
            result_file.write(result_text + r'\n')
            print('- записана')
            success_counter += 1
        except (IOError, PermissionError, FileNotFoundError, ValueError, UnicodeEncodeError) as exc:
            except_counter += 1
            print('- Ошибка записи строки в файл', exc)
    # Закрываем за собой файлы
    try:
        source_table.close()
        result_file.close()
        print('Файлы за собой закрыли!')
    except (IOError, PermissionError, FileNotFoundError) as exc:
        print('КОШМАР! ФАЙЛЫ СПОРОТИВЛЯЮТСЯ ЗАКРЯТИЮ, НО МЫ ИХ ВСЁ РАВНО ЗАКРОЕМ!!!', exc)
        time.sleep(3)
        source_table.close()
        result_file.close()
    # Симпатичный вывод отчёта об обработке
    return ('\nГотово! ' +
            '\n Обработано строк - ' +
            '\n всего:      ' + str(line_counter) +
            '\n успешно:    ' + str(success_counter) +
            '\n неуспешно:  ' + str(except_counter) +
            '\n список существ неизвестного пола: ' + str(asexual_list) +
            '\n список неизвестных устройств: ' + str(unknown_device_list))


print(table_to_text_converter())
