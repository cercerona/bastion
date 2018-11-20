"""File include the interface function for WAB report processing"""
from read_csv_report_files import read_report
from tkinter import *
from tkinter import filedialog as fd
import pprint
import matplotlib.pyplot as plt


def plot_pie_report(table):
    """
    Рисует круговую диаграмму
    :param table: Таблица с данными. В первой строке содержит подписи, во второй - данные 
    :return: ничего
    """
    # plt.pie(table[1][])


def open_report_file():
    """Функция открывает файл с отчетом"""
    table = []
    with open(fd.askopenfilename(filetypes=[('Report files:', '*.csv')])) as infile:
        table = read_report(infile)

    pprint.pprint(table)
    print('Всего записей: ', len(table))
    print(table[1][0])

    return table


def init_main_window():
    """Создает и инициирует виджеты главного окна"""
    global main_window, main_frame, top_frame, open_file_button, open_file_label, bottom_frame, save_report_button, \
        table_frame, canvas_frame  # создание глобальных виджетов главного окна и кнопки открытия файла, имя файла отчета
    main_window = Tk()  # Создадим главное окно программы
    main_window.title('Программа визуализации отчетов')  # Зададим заголовок главного окна программы
    main_window.geometry('600x300')

    main_frame = Frame(main_window)  # Создадим главный фрейм окна отчета
    main_frame.config(bg='black')
    main_frame.pack(side=TOP, expand=YES, fill=BOTH)  # Растянем фрейм на все пространство главного окна

    top_frame = Frame(main_frame)  # Создадим фрейм для кнопки выбора файла-отчета
    top_frame.config(bg='grey')
    top_frame.pack(side=TOP, fill=X)  # Привяжем фрейм к верхней границе и будем растягивать по стороне X
    open_file_button = Button(top_frame, text='Open report', command=open_report_file)
    open_file_button.pack(side=RIGHT)  # Поместим справа кнопку открытия файла с отчетом
    open_file_label = Label(top_frame, text='Report filename:')
    open_file_label.pack(side=LEFT, expand=YES, fill=X)  # Поместим слева от кнопки надпись

    bottom_frame = Frame(main_frame)  # Создадим фрейм для кнопки сохранения отчета в файле xml
    bottom_frame.config(bg='grey')
    bottom_frame.pack(side=BOTTOM, fill=X)  # Привяжем фрейм к верхней границе и будем растягивать по стороне X
    save_report_button = Button(bottom_frame, text='Save report as XML')
    save_report_button.pack(side=RIGHT)  # Поместим справа кнопку сохранения отчета

    table_frame = Frame(main_frame)  # Создадим фрейм для размещения таблицы с данными
    table_frame.config(bg='grey')
    table_frame.pack(side=LEFT, expand=YES, fill=BOTH)

    canvas_frame = Frame(main_frame)  # Создадим фрейм для размещения графика
    canvas_frame.config(bg='blue')
    canvas_frame.pack(side=RIGHT, expand=YES, fill=BOTH)


if __name__ == '__main__':
    init_main_window()
    main_window.mainloop()
