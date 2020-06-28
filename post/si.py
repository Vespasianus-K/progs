# Написано на Python 3.8, проверялось на Windows 10. Должно работать везде, по идее. #

import smtplib
smtpObj = smtplib.SMTP('SMTP HERE', 587) # Вставьте SMTP-сервер.
smtpObj.starttls() # TLS. Можете убрать, если хотите.
smtpObj.login('ENTER MAIL HERE','ENTER PASS HERE') # Здесь - ваши логин и пароль к почте.
smtpObj.sendmail("ENTER MAIL HERE","ADDRESS HERE","TEXT HERE") # Последовательно - почта отправки, адресат и текст.
smtpObj.quit() # Всё!
