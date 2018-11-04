"""File include the interface function for WAB report processing"""
import tkinter

def init_main_window():
    """Создает и инициирует виджеты главного окна
    :param: нет
    :return: ничего
    """
    global root #создание глобальных виджетов главного окна
    root = tkinter.Tk()
    root.title("WAB reports")

if __name__ == '__main__':
    init_main_window()
    root.mainloop()
