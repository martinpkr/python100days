import smtplib
my_email = 'martinkirilov402@gmail.com'
password = 'cuuvwcxxrenfmoqh'

class NotificationManager:
    def __init__(self):
        self.notification = str
    def get_notified(self,massage):
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            connection.sendmail(from_addr=my_email, to_addrs='marutinkirilov@abv.bg',
                                msg=f'{massage}');
            connection.close()
    pass