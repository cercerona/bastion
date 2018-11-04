"""File include the interface function for WAB report processing"""
import tkinter
from tkinter import filedialog as fd

def input_report_filename(event):
    """
    Функция возвращает имя файла с отчетом
    :return: Имя файла с отчетом
    """
    return fd.askopenfilename(filetype = [("Report files", "*.csv")])

def init_main_window():
    """Создает и инициирует виджеты главного окна
    :param: нет
    :return: ничего
    """
    global root, open_file_button #создание глобальных виджетов главного окна и кнопки открытия файла
    root = tkinter.Tk()
    root.title("WAB reports")
    open_file_button = tkinter.Button(root, text = 'Open report')
    open_file_button.pack()
    open_file_button.bind('<Button>', input_report_filename)

if __name__ == '__main__':
    init_main_window()
    root.mainloop()
