import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from bs4 import BeautifulSoup as bs

# ваши учетные данные
email = "tushin907@gmail.com"
password = "password"

# электронная почта отправителя
FROM = "tushin907@gmail.com"

# адрес электронной почты получателя
TO = "ilya.tushin.00@mail.ru"

# тема письма (тема)
subject = "Test"

# инициализируем сообщение, которое хотим отправить
msg = MIMEMultipart("alternative")

# установить адрес электронной почты отправителя
msg["From"] = FROM

# установить адрес электронной почты получателя
msg["To"] = TO

# задаем тему
msg["Subject"] = subject

# установить тело письма как HTML
html = """
This email is sent using <b>Python</b>!
"""
# делаем текстовую версию HTML
text = bs(html, "html.parser").text

text_part = MIMEText(text, "plain")
html_part = MIMEText(html, "html")

# прикрепить тело письма к почтовому сообщению
# сначала прикрепите текстовую версию
msg.attach(text_part)
msg.attach(html_part)

print(msg.as_string())


def send_mail(email, password, FROM, TO, msg):
    # инициализировать SMTP-сервер
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # подключиться к SMTP-серверу в режиме TLS (безопасный) и отправить EHLO
    server.starttls()
    # войти в учетную запись, используя учетные данные
    server.login(email, password)
    # отправить электронное письмо
    server.sendmail(FROM, TO, msg.as_string())
    # завершить сеанс SMTP
    server.quit()


send_mail(email, password, FROM, TO, msg)
