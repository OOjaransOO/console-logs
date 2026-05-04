import datetime as d, sys, os, platform as p, psutil as ps,GPUtil as g


############################################################

# infoFile = open("data/infoFile.txt","w")
# nameInput = input ()
# infoFile.write(nameInput)
# infoFile.close()

who1="Программа"
who2="Пользователь"
who3="Администратор"
number=0
file=open("data/logData.txt", "w")

############################################################

def console_print(who, message):
    time=d.datetime.now().strftime("%H:%M:%S")
    number = counter()
    log_save(time, who, message, number)
    print(f"{time} <{number}> <{who}> {message}")

def log_save(time, who, message, number):
    global file
    file.write(f"{time} <{number}> <{who}> {message}\n")

def log_save_user(time, number, name, who, message):
    global file
    file.write(f"{time} <{number}> <{who}> <{name}> {message}\n")

def console_input(who3, text):
    number = counter()
    userName=name()
    time=d.datetime.now().strftime("%H:%M:%S")
    message=input(f"{time} <{number}> <{who3}> <{userName}> {text}")
    log_save_user(time, number, userName, who3, message)
    return message

def name():
    infoFile = open("data/infoFile.txt","r")
    userName = infoFile.read()
    infoFile.close()
    return userName

def counter():
    global number
    number += 1
    return number


def check(message, who1, who3):
    match message:
        case "/help":
            console_print(who1, "/break - Завершение программы")
            console_print(who1, "/calculator - Запуск калькулятора")
            console_print(who1, "/date - Сегодняшнюю дату")
            console_print(who1, "/path - Маршрут к программе")
            console_print(who1, "/pc - Характеристики вашего ПК")
        case "/calculator":
            calculator(who3)
        case "/date":
            console_print(who1, d.datetime.now().date())
        case "/path":
            console_print(who1, sys.path)
        case "/pc":
            pc(who1)
        case "/rename":
            rename(who1, who3)
        case "/-":
            console_print(who1, "")
    return None

def rename(who1, who3):
    nameInput = console_input(who3, "Введите новое имя: ")
    if nameInput == "/stop":
        console_print(who3, "Переименование отменено")
    else:
        infoFile = open("data/infoFile.txt","w+")
        infoFile.write(nameInput)
        console_print(who3, "Переименование закончено")
        infoFile.close()
    return None

def pc(who1):
    console_print(who1, "=== СИСТЕМА ===")
    console_print(who1, p.system()+" "+p.release())

    console_print(who1, "===== CPU =====")
    console_print(who1, p.processor())

    console_print(who1, "===== GPU =====")
    gpus=g.getGPUs()
    if not gpus:
        console_print(who1, "Проблема с поиском вашей видеокарты, возможно её нет или это ошибка программы")
    else:
        for gpu in gpus:
            console_print(who1, "GPU: "+str(gpu.name))
            console_print(who1, "Память: " + str(gpu.memoryTotal) + " MB")

    console_print(who1, "===== RAM =====")
    ram=ps.virtual_memory()
    console_print(who1, "Всего: " + str(round(ram.total / (1024**3), 2)) + " GB")

    console_print(who1, "==== ДИСК ====")
    disk = ps.disk_usage("/")
    console_print(who1, "Всего: " + str(round(disk.total / (1024**3), 2)) + " GB")
    return None

def calculator(who3):
    who="Калькулятор"

    console_print(who, "Калькулятор запущен")
    console_print(who, "Значки действия:")
    console_print(who, "+ - сумма")
    console_print(who, "- - разность")
    console_print(who, "* - умножение")
    console_print(who, "/ - деление")
    console_print(who, "^ - степень")
    console_print(who, "^^ - корень")
    console_print(who, "/stop - завершение работы калькулятора")

    while True:
        try:
            x,y=map(float, console_input(who3, "Введите 2 числа через пробел: ").split())
        except ValueError:
            console_print(who, "Нужно ввести числа")
            continue

        z = console_input(who3, "Введите значок действия: ")

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
                console_print(who, "Калькулятор выключен")
                break
            case _:
                res = "Ошибка, значок действия не найден"

        console_print(who, res)
    return None


############################################################

timeNow=d.datetime.now().date()
console_print(who1,f"Логирование запущено! Сегодня: {timeNow}")

while True:
    message = console_input(who3, "")

    check(message, who1, who3)
    if message == "/break":
        break

############################################################

console_print(who1,"Логирование завершено.")
file.close()