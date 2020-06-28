import smtplib
smtpObj = smtplib.SMTP('SMTP HERE', 587) # Вставьте SMTP-сервер.
smtpObj.starttls()
smtpObj.login('ENTER MAIL HERE','ENTER PASS HERE') # Здесь - ваши логин и пароль к почте.
smtpObj.sendmail("ENTER MAIL HERE","ADDRESS HERE","TEXT HERE") # Последовательно - почта отправки, адресат и текст.
smtpObj.quit() # Всё!
