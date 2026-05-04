import datetime as d, sys, os, platform as p


############################################################

who1="Программа"
who2="Пользователь"
who3="Администратор"
number=0
file=open("log_data.txt", "w")

############################################################

def console_print(who, message):
    time=d.datetime.now().strftime("%H:%M:%S")
    number = counter()
    log_save(time, who, message, number)
    print(f"{time} <{number}> <{who}> <<{message}>>")

def log_save(time, who, message, number):
    global file
    file.write(f"{time} <{number}> <{who}> <<{message}>>\n")

def counter():
    global number
    number += 1
    return number


def console_input(who3, text):
    number = counter()
    time=d.datetime.now().strftime("%H:%M:%S")
    message=input(f"{time} <{number}> <{who3}> {text}")
    log_save(time, who3, message, number)
    return message

def check(message, who1, who3):
    match message:
        case "/help":
            console_print(who1, "/break - Завершение программы")
            console_print(who1, "/calculator - Запуск калькулятора")
        case "/calculator":
            calculator(who3)
        case "/date":
            console_print(who1, d.datetime.now().date())
        case "/path":
            console_print(who1, sys.path)
        case "/os":
            console_print(who1, p.system())
        case "/-":
            console_print(who1, "")


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