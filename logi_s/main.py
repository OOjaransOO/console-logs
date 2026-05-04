import datetime as d, sys, os, platform as p, psutil as ps,GPUtil as g
import console_functions as c

############################################################

who1="Программа"
who2="Пользователь"
who3="Администратор"
file=open("data/logData.txt", "w")

############################################################

def check(message, who1, who3):
    match message:
        case "/help":
            c.console_print(who1, "/break - Завершение программы")
            c.console_print(who1, "/calculator - Запуск калькулятора")
            c.console_print(who1, "/date - Сегодняшнюю дату")
            c.console_print(who1, "/path - Маршрут к программе")
            c.console_print(who1, "/pc - Характеристики вашего ПК")
            c.console_print(who1, "/rename - Переименовывает пользователя")
        case "/calculator":
            calculator(who3)
        case "/date":
            c.console_print(who1, d.datetime.now().date())
        case "/path":
            c.console_print(who1, sys.path)
        case "/pc":
            pc(who1)
        case "/rename":
            rename(who1, who3)
        case "/-":
            c.console_print(who1, "")
    return None

def rename(who1, who3):
    nameInput = c.console_input(who3, "Введите новое имя: ")
    if nameInput == "/stop":
        c.console_print(who3, "Переименование отменено")
    else:
        infoFile = open("data/infoFile.txt","w+")
        infoFile.write(nameInput)
        c.console_print(who3, "Переименование закончено")
        infoFile.close()
    return None

def pc(who1):
    c.console_print(who1, "=== СИСТЕМА ===")
    c.console_print(who1, p.system()+" "+p.release())

    c.console_print(who1, "===== CPU =====")
    c.console_print(who1, p.processor())

    c.console_print(who1, "===== GPU =====")
    gpus=g.getGPUs()
    if not gpus:
        c.console_print(who1, "Проблема с поиском вашей видеокарты, возможно её нет или это ошибка программы")
    else:
        for gpu in gpus:
            c.console_print(who1, "GPU: "+str(gpu.name))
            c.console_print(who1, "Память: " + str(gpu.memoryTotal) + " MB")

    c.console_print(who1, "===== RAM =====")
    ram=ps.virtual_memory()
    c.console_print(who1, "Всего: " + str(round(ram.total / (1024**3), 2)) + " GB")

    c.console_print(who1, "==== ДИСК ====")
    disk = ps.disk_usage("/")
    c.console_print(who1, "Всего: " + str(round(disk.total / (1024**3), 2)) + " GB")
    return None

def calculator(who3):
    who="Калькулятор"

    c.console_print(who, "Калькулятор запущен")
    c.console_print(who, "Значки действия:")
    c.console_print(who, "+ - сумма")
    c.console_print(who, "- - разность")
    c.console_print(who, "* - умножение")
    c.console_print(who, "/ - деление")
    c.console_print(who, "^ - степень")
    c.console_print(who, "^^ - корень")
    c.console_print(who, "/stop - завершение работы калькулятора")

    while True:
        try:
            x,y=map(float, c.console_input(who3, "Введите 2 числа через пробел: ").split())
        except ValueError:
            c.console_print(who, "Нужно ввести числа")
            continue

        z = c.console_input(who3, "Введите значок действия: ")

        match z:
            case "+":
                res = x+y
            case "-":
                res = x-y
            case "*":
                res = x*y
            case "/":
                if y==0:
                    res = "На 0 делить нельзя"
                else:
                    res = x/y
            case "^":
                res = x**y
            case "^^":
                res = x**(1/y)
            case "/stop":
                c.console_print(who, "Калькулятор выключен!")
                break
            case _:
                res = "Ошибка, значок действия не найден"

        c.console_print(who, res)
    return None


############################################################

timeNow=d.datetime.now().date()
c.console_print(who1,f"Логирование запущено! Сегодня: {timeNow}")

while True:
    message = c.console_input(who3, "")

    check(message, who1, who3)
    if message == "/break":
        break

############################################################

c.console_print(who1,"Логирование завершено.")
file.close()