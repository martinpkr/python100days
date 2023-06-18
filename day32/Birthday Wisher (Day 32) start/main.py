import smtplib
import random
import datetime as dt

my_email = 'martinkirilov402@gmail.com'
password = 'cuuvwcxxrenfmoqh'

# with smtplib.SMTP('smtp.gmail.com',port='587') as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='mkirilov12@yahoo.com',
#                         msg='Subject:Hello\n\nThis is the body of the email.')
#     connection.close()
# with open('animation.gif', 'rb') as attachment:
#     gif = MIMEBase('image', 'gif')
#     gif.set_payload(attachment.read())
#     encoders.encode_base64(gif)
#     gif.add_header('Content-Disposition', 'attachment', filename='animation.gif')
#     message.attach(gif)
WORK_DAYS = [0,1,2,3,4]
with open('quotes.txt','r') as data:
    lines = data.readlines()
    date = dt.datetime.now()
    with smtplib.SMTP(host='smtp.gmail.com',port=587) as connection:
        if date.weekday() in WORK_DAYS:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs='mkirilov12@yahoo.com',msg=random.choice(lines))
            connection.sendmail(from_addr=my_email,to_addrs='Nicolegnaumova@gmail.com',msg=random.choice(lines))
            connection.close()
