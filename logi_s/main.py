import datetime as d, sys, os, platform as p, psutil as ps,GPUtil as g
import console_functions as c
import comands as com

############################################################

who1="Программа"
who2="Пользователь"
who3="Администратор"
file=open("data/logData.txt", "w")

############################################################

def check(message, who1, who3):
    match message:
        case "/help":
            com.helpC(who1)
        case "/calculator":
            com.calculator(who3)
        case "/date":
            com.date(who1)
        case "/path":
            com.path(who1)
        case "/pc":
            com.pc(who1)
        case "/rename":
            com.rename(who1, who3)
        case "/-":
            c.console_print(who1, "")
    return None

############################################################

timeNow=d.datetime.now().date()
c.console_print(who1,f"Логирование запущено! Сегодня: {timeNow}")
c.console_print(who1,"Чтобы узнать о доступнах командах напишите /help")

while True:
    message = c.console_input(who3, "")

    check(message, who1, who3)
    if message == "/break":
        break

############################################################

c.console_print(who1,"Логирование завершено.")
file.close()