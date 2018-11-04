"""File include the interface function for WAB report processing"""
from read_csv_report_files import *
import tkinter
from tkinter import filedialog as fd

def open_report_file(event):
    """
    Функция открывает файл с отчетом
    """
    table = []
    with open(fd.askopenfilename(filetype = [("Report files", "*.csv")]), 'r') as infile:
        table = read_report(infile)

    pprint.pprint(table)
    print('Всего записей: ', len(table))


def init_main_window():
    """Создает и инициирует виджеты главного окна
    :param: нет
    :return: ничего
    """
    global root, open_file_button, open_file_button #создание глобальных виджетов главного окна и кнопки открытия файла, имя файла отчета
    root = tkinter.Tk()
    root.title("WAB reports")
    open_file_button = tkinter.Button(root, text = 'Open report')
    open_file_button.pack()
    open_file_button.bind('<Button>', open_report_file)

if __name__ == '__main__':
    init_main_window()
    root.mainloop()
