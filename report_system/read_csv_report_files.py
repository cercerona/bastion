import csv
import pprint

"""Include functions for read csv files with WAB report"""
def read_report(file_obj):
    """
    Function for read report from csv file
    :param file_obj: file to read
    :return: table - report in table with rows of the file
    """
    return [row for row in csv.reader(file_obj)]

if __name__ == '__main__':
    file_name = r'C:\Users\Dmitry Kononov\Documents\Бастион\Python\Отчеты\Примеры выгрузок\БСпб\statistics\srv-wab-dca-2.bankspb.ru_2018-07-20T17_55_s_connections_per_device.csv'
    table = []
    with open(file_name, 'r') as infile:
        table = read_report(infile)

    pprint.pprint(table)
    print('Всего записей: ', len(table))

