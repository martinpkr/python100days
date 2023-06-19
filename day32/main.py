##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random

possible_files = ('letter_1.txt','letter_2.txt','letter_3.txt')
my_email = 'martinkirilov402@gmail.com'
password = 'cuuvwcxxrenfmoqh'
# 1. Update the birthdays.csv
#Making dataframe from csv file
file = pandas.read_csv('birthdays.csv')
df = pandas.DataFrame(file)
dict = df.to_records()
#Taking the current time to see the current date and year
now = dt.datetime.now()
print(dict)
# 2. Check if today matches a birthday in the birthdays.csv
for line in dict:
    name = line[1]
    email = line[2]
    birth_year = line[3]
    birth_month = line[4]
    birth_day = line[5]

    if birth_day == now.day and birth_month == now.month:
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

            with open(f'letter_templates/{random.choice(possible_files)}') as wish:
                text_for_birthay = wish.readlines()
                connection.starttls()
                connection.login(user=my_email, password=password)
                # 4. Send the letter generated in step 3 to that person's email address.

                connection.sendmail(from_addr=my_email, to_addrs=email,
                                    msg=f'Subject:Happy Birthday {name} <3 \n\n{random.choice(text_for_birthay)}');
                connection.close()








