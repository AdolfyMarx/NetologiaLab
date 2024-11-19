import ast
import csv
import os
from time import sleep


def open_file(path, mode):
    try:
        f = open(path, mode, encoding='utf-8')
    except FileNotFoundError:
        print('Error in opening file ', path)
        return False
    return f

# def create_csv(path, mode, )

def file_comparator():
    visit_file = open_file('visit_log__1___2_.csv', 'r')
    print('Success opened file with structure: ', visit_file.readline())

    purchase_file = open_file('purchase_log.txt', 'r')
    print('Success opened file with structure: ', purchase_file.readline())
    try:
        os.remove('funnel.csv')
    except FileNotFoundError:
        print('ooops')
    print('file funnel.csv erased')

    result_file = open_file('funnel.csv', 'w+')
    writer = csv.writer(result_file, delimiter = ",", lineterminator='\n')
    csv_header = ['user_id','source','category']
    writer.writerow(csv_header)
    print('Success opened file with structure: ' + str(csv_header))
    try:
        while True:
            line = visit_file.readline()
            if not line:
                break
            line_list = line.split(',')
            purchase_file.seek(0)
            while True:
                line_2 = purchase_file.readline()
                if not line_2:
                    break
                line_2_dict = ast.literal_eval(line_2)
                if line_2_dict.get('user_id') == line_list[0]:
                    print(str(line_list[0]) + ' : ' + line_list[1].replace('\n', '') + ' | ' + line_2_dict.get('category'))
                    writer.writerow([line_list[0], line_list[1].replace('\n', ''), line_2_dict.get('category')])
                    print('row was writed')

    except Exception:
        print('something go wrong')

    visit_file.close()
    purchase_file.close()
    result_file.close()
    print('all files successfully closed')


file_comparator()