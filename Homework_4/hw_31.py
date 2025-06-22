pins_num = int(input('Введите количество стержней: '))
disks_num = int(input('Введите количество дисков: '))


def upper_disks_list(custom_dict):
    list_of_tops = []
    for pin in range(pins_num):
        print(pin)
        if custom_dict[pin]:
            print('не пусто: ', custom_dict[pin][0])
            list_of_tops.append(custom_dict[pin][0])
        else:
            print('пусто: ', None)
            list_of_tops.append(None)
    return list_of_tops


def do_step(pins_dict, max_disk, target_pin):
    if len(pins_dict[target_pin]) < disks_num:
        to_do_step = try_to_step(pins_dict, max_disk, target_pin)
        disk_to_move = pins_dict.to_do_step[0].pop(0)
        pins_dict.to_do_step[1].insert(0, disk_to_move)
        do_step(pins_dict, to_do_step[2], target_pin)
    else:
        print('Готово: ' + str(pins_dict))


def try_to_step(pins_dict, max_disk, target_pin):
    disks_to_move = upper_disks_list(pins_dict)

    noneless_disc_to_move_list = disks_to_move.copy()
    for elem in noneless_disc_to_move_list:
        print(str(elem))
        if elem is None:
            noneless_disc_to_move_list.remove(elem)
    print(str(noneless_disc_to_move_list))
    largest_disk_to_move = max(noneless_disc_to_move_list)

    sorted_discs_to_move = disks_to_move.copy()
    sorted_discs_to_move.sort(reverse=True)

    if max_disk in disks_to_move:
        print(f'самый целевой диск {max_disk}  доступнен к перемещению')

        if pins_dict[target_pin] in [None, max_disk+1]:
            print(f'есть место для целевого диска {max_disk}, перемещаем на {target_pin}')
            max_disk -= 1
            return disks_to_move.index(max_disk), target_pin, max_disk

    if None in disks_to_move:
        print(f'есть пустое место {disks_to_move.index(None)}, перемещаем туда с {disks_to_move.index(largest_disk_to_move)} самый большой доступный диск')
        return disks_to_move.index(largest_disk_to_move), disks_to_move.index(None)
    else:
        print("И тут начинается крутая рекурсивная логика которую я так и не придумал :'(")
#   Видел предлагаемые нейронками решения, они довольно простые и исключительно однообразные,
#   не стал сюда копипастить, хотел изобрести своё, но так и не сформулировал логику, которая бы в итоге не зацикливалась.



def max_disc_pin(pins_dict, max_disk):
    for pin, discs_list in pins_dict:
        if max_disk in discs_list:
            print('наибольший диск на колке: ' + pin)
            return pin
    else:
        print('что-то пошло не так')
        raise Exception



def hanoi_solver(pins_n, disks_n):
    if pins_n < 3 or disks_n < 1:
        return 'Некорректное условие, в головоломке должно быть не менее трёх стержней и одного диска'

    start_pin_list = list(range(disks_n))
    pins_dict = {0:start_pin_list}
    for i in range(pins_n - 1):
        pins_dict[i + 1] = []

    target_pin = pins_n - 1
    max_disk = disks_n - 1

    do_step(pins_dict, max_disk, target_pin)



hanoi_solver(pins_num, disks_num)