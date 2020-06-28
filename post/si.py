# Написано на Python 3.8, проверялось на Windows 10. Должно работать везде, по идее. #

from tkinter import *
import smtplib
from time import sleep
import datetime
# Определение времени
today = datetime.datetime.today()
# Создание окна
window = Tk()
window.title("Почтовый клиент Si-5 (бета-версия)")
int1 = Label(window, text="Почтовый клиент Si-5 приветствует вас.")  
int1.grid(column=0, row=0)
int2 = Label(window, text="Это бета-версия, поэтому возможны ошибки.")
int2.grid(column=0, row=1)
window.geometry('800x600')
# Размещение кнопок и полей.
email_sm = Label(window, text="Введите SMTP-сервер.")
email_sm.grid(column=0, row=2)
email_smtpk = Entry(window, width=40)
email_smtpk.grid(column=1, row=2)
email_se = Label(window, text="Введите Ваш адрес эл. почты.")
email_se.grid(column=0, row=3)
email_senderk = Entry(window, width=50)
email_senderk.grid(column=1, row=3)
email_p = Label(window, text="Введите Ваш пароль от эл. почты.")
email_p.grid(column=0, row=4)
email_passwordk = Entry(window, width=40)
email_passwordk.grid(column=1, row=4)
email_a = Label(window, text="Введите адрес получателя.")
email_a.grid(column=0, row=5)
email_addressk = Entry(window, width=45)
email_addressk.grid(column=1, row=5)
email_t = Label(window, text="Введите текст письма.")
email_t.grid(column=0, row=6)
email_textk = Text(width=75, height=15)
email_textk.grid(column=1, row=6)
# Да, тут немножко некрасиво, но для получения значений из полей - только так. Над красотой кода поработаю потом.
email_smtp = email_smtpk.get()
email_sender = email_senderk.get()
email_password = email_passwordk.get()
email_address = email_addressk.get()
email_text = email_textk.get("1.0",'end-1c')
# Вынужден поместить тут, т.к. иначе кнопка не будет работать.
def send_email():
    smtpObj = smtplib.SMTP(email_smtp, 587) 
    smtpObj.starttls() # TLS. Можете убрать, если хотите.
    smtpObj.login(email_sender, email_password)
    smtpObj.sendmail(email_sender, email_address, email_text)
    smtpObj.quit() # Всё!
send = Button(window, text="Отправить письмо", command=send_email)
send.grid(column=1,row=7)
logbtn = Button(window, text="Сохранить лог", command=log)
logbtn.grid(column=2,row=7)
# Конец размещения.
window.mainloop()

