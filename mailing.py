import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup as bs


to_list = ['ilya.tushin.00@mail.ru', 'poselennov.il@ya.ru']


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


for recipient in to_list:
    # ваши учетные данные
    email = "tushin907@gmail.com"
    password = "password"
    # электронная почта отправителя
    FROM = "tushin907@gmail.com"
    # адрес электронной почты получателя
    TO = recipient
    # тема письма (тема)
    subject = "Это пример"

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
    Рассылка для всех - <b>Ура!</b>!
    """
    # делаем текстовую версию HTML
    text = bs(html, "html.parser").text

    text_part = MIMEText(text, "plain")
    html_part = MIMEText(html, "html")
    # прикрепить тело письма к почтовому сообщению
    # сначала прикрепите текстовую версию
    msg.attach(text_part)
    msg.attach(html_part)

    # отправить почту
    send_mail(email, password, FROM, TO, msg)
