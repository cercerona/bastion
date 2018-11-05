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
    global root, open_file_button, open_file_label #создание глобальных виджетов главного окна и кнопки открытия файла, имя файла отчета
    root = tkinter.Tk()
    root.grid_rowconfigure(0, weight=1)
    root.title("WAB reports")
    open_file_button = tkinter.Button(root, text = 'Open report')
    open_file_button.grid(row = 0, column = 3, sticky = 'nw')
    open_file_button.bind('<Button>', open_report_file)

    open_file_label = tkinter.Label(root, text = 'Report filename:')
    open_file_label.grid(row = 0, column = 0, columnspan = 2, sticky = 'ne')

if __name__ == '__main__':
    init_main_window()
    root.mainloop()
