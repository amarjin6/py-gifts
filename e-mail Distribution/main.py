import smtplib
from decouple import config


def send(message):
    sender = config('LOGIN')
    password = config('PASSWORD')

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.starttls()

    try:
        mail.login(sender, password)
        mail.sendmail(sender, 'example@gmail.com', f"Subject:VegasML Team: Getting started! \n{message}")
        return 'Success!'

    except Exception as e:
        return f"{e} Check login or password"


if __name__ == '__main__':
    send(str(input('Message: ')))
