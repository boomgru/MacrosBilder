import os
import time
import pyautogui
import psutil
import random
import colorama
import sys
from colorama import Fore

colorama.init(autoreset=True)


##toexe
def toexe():
    os.system("title Exe Compilator")
    in_path = r"info.txt"
    with open(in_path, 'r') as file:
        file_py = file.read()
        print(Fore.YELLOW + "Компиляция! Атрибуты:")
        print(Fore.YELLOW + "- Один файл")
        print("")
        pyinst_v = f"pyinstaller -F {file_py}"
        os.system(pyinst_v)
        txt()
        print(Fore.YELLOW + ".EXE файл в папке DIST")
        



def txt():
    os.system("title MacrosBuilder ver 1.0")
    if not os.path.exists(r"macros"):
        os.mkdir("macros")
    os.system("cls")
    print(Fore.YELLOW + """
 ____  __  __  ____   __  __    _    ____ ____   ___  
| __ )|  \/  |/ ___| |  \/  |  / \  / ___|  _ \ / _ \ 
|  _ \| |\/| | |  _  | |\/| | / _ \| |   | |_) | | | |
| |_) | |  | | |_| | | |  | |/ ___ \ |___|  _ <| |_| |
|____/|_|  |_|\____| |_|  |_/_/   \_\____|_| \_\\___/ 
    """)
    print(Fore.YELLOW + "Нажмите, для запуска.")
    input("[\]")
    os.system("cls")
    print(Fore.YELLOW + """
 ____  __  __  ____   __  __    _    ____ ____   ___  
| __ )|  \/  |/ ___| |  \/  |  / \  / ___|  _ \ / _ \ 
|  _ \| |\/| | |  _  | |\/| | / _ \| |   | |_) | | | |
| |_) | |  | | |_| | | |  | |/ ___ \ |___|  _ <| |_| |
|____/|_|  |_|\____| |_|  |_/_/   \_\____|_| \_\\___/ 
    """)
    print("")
    print(Fore.RED + "1 - Запустить макрос")
    print("")
    print(Fore.RED + "2 - Создать новый макрос")
    
    funcc = input()
    if funcc == "1":
        start_macros()
    elif funcc == "2":
        create_macros()
    else:
        txt()
  
def start_macros():
    os.system("cls")
    print(Fore.YELLOW + """
 ____  __  __  ____   __  __    _    ____ ____   ___  
| __ )|  \/  |/ ___| |  \/  |  / \  / ___|  _ \ / _ \ 
|  _ \| |\/| | |  _  | |\/| | / _ \| |   | |_) | | | |
| |_) | |  | | |_| | | |  | |/ ___ \ |___|  _ <| |_| |
|____/|_|  |_|\____| |_|  |_/_/   \_\____|_| \_\\___/ 
    """)
    print("")
    print(Fore.RED + "Напишите название макроса")
    start_name = input()
    macro_path = rf"macros\{start_name}.py"
    if os.path.exists(macro_path):
        os.startfile(macro_path)
        txt()
    else:
        print(Fore.RED + "Данного макроса не существует!")
        time.sleep(3)
        txt()
 
def create_macros():
    os.system("cls")
    print(Fore.YELLOW + """
 ____  __  __  ____   __  __    _    ____ ____   ___  
| __ )|  \/  |/ ___| |  \/  |  / \  / ___|  _ \ / _ \ 
|  _ \| |\/| | |  _  | |\/| | / _ \| |   | |_) | | | |
| |_) | |  | | |_| | | |  | |/ ___ \ |___|  _ <| |_| |
|____/|_|  |_|\____| |_|  |_/_/   \_\____|_| \_\\___/ 
    """)
    print("")
    print(Fore.RED + "Напишите название макроса")
    create_name = input()
    macro_path = rf"macros\{create_name}.py"
    info_path = r"info.txt"
    with open(info_path, 'w') as file:
        file.write(macro_path)
    with open(macro_path, 'w', encoding='utf-8') as file:
        file.write("""
import pyautogui
import time
import os
        
#macroBuilder by boomgru
time.sleep(3)
print("Запуск макроса...")
        """)
    cr_ma_w()
def cr_ma_w():
    os.system("cls")
    in_path = r"info.txt"
    with open(in_path, 'r') as file:
        create_name = file.read()
    macro_path = rf"{create_name}"
    with open(macro_path, 'r', encoding='utf-8') as file:
        print(Fore.YELLOW + file.read() )
    print("============================")
    print("")
    print(Fore.YELLOW + "1 - ожидание")
    print("")
    print(Fore.GREEN + "2 - нажатие мыши")
    print("")
    print(Fore.BLUE + "3 - нажатие кнопки")
    print("")
    print(Fore.RED + "4 - перемещение мышки на кординаты")
    print("")
    print(Fore.YELLOW + "5 - компилировать в exe")
    func_wr = input("[\]")
    if func_wr == "1":
        t_sl = input(Fore.GREEN + "Сколько должно быть ожидание (в секундах): ")
        with open(macro_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме дозаписи ('a')
            file.write(f"\ntime.sleep({t_sl})")  # Добавляем новый код в конец файла
        with open(macro_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме дозаписи ('a')
            file.write(f"\n#bmgMacroBilder")  # Добавляем новый код в конец файла
        cr_ma_w()

    elif func_wr == "2": 
        t_sl = input(Fore.GREEN + "Right/left: ")
        with open(macro_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме дозаписи ('a')
            file.write(f"\n#bmgMacroBilder")
        with open(macro_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме дозаписи ('a')
            file.write(f"\npyautogui.mouseDown(button='{t_sl}')")  # Добавляем новый код в конец файла
        with open(macro_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме дозаписи ('a')
            file.write(f"\n#bmgMacroBilder")  # Добавляем новый код в конец файла
        with open(macro_path, 'a', encoding='utf-8') as file:
            file.write(f"\ntime.sleep(0.12)")  # Добавляем новый код в конец файла
        with open(macro_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме дозаписи ('a')
            file.write(f"\npyautogui.mouseUp(button='{t_sl}')")
        with open(macro_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме дозаписи ('a')
            file.write(f"\n#bmgMacroBilder")
        cr_ma_w()
    elif func_wr == "3": 
        butn = input("Кнопка: ")
        with open(macro_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме дозаписи ('a')
            file.write(f"\npyautogui.press('{butn}')")  # Добавляем новый код в конец файла
        with open(macro_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме дозаписи ('a')
            file.write(f"\n#bmgMacroBilder")  # Добавляем новый код в конец файла
        cr_ma_w()
    elif func_wr == "4":
        x = input(Fore.RED + "Кордината X: ")
        y = input(Fore.GREEN + "Кордината Y: ")
        with open(macro_path, 'a', encoding='utf-8') as file:
            file.write(f"\npyautogui.moveTo({x}, {y})")
        with open(macro_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме дозаписи ('a')
            file.write(f"\n#bmgMacroBilder")  # Добавляем новый код в конец файла
        cr_ma_w()
    elif func_wr == "5":
        toexe()





def start():
    os.system("title MacrosBuilder ver 1.0")
    txt()

start()

