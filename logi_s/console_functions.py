import datetime as d

number=0

def numberZero():
    global number
    number=0
    return None

def counter():
    global number
    number += 1
    return number

def console_print(who, message):
    time=d.datetime.now().strftime("%H:%M:%S")
    number = counter()
    log_save(time, who, message, number)
    print(f"{time} <{number}> <{who}> {message}")

def log_save(time, who, message, number):
    file=open("data/logData.txt", "a")
    file.write(f"{time} <{number}> <{who}> {message}\n")
    file.close()

def log_save_user(time, number, name, who, message):
    file=open("data/logData.txt", "a")
    file.write(f"{time} <{number}> <{who}> <{name}> {message}\n")
    file.close()

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