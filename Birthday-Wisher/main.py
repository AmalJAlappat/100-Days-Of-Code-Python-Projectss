## ____________ Sending Mail ___________#
# import smtplib

## ____________ Gmail To Yahoo ___________#
# my_email = "amaljalappatttest@gmail.com"
# password = "Super*123"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="amaljalappatt@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

## ____________ Yahoo To Gmail  ___________#
# my_email = "amaljalappatt@yahoo.com"
# password = "fhkzfqzknnjftnsy"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="amaljalappatttest@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")



## ____________ How to use DateTime  ___________#
# import datetime as dt

## ____________ Getting Today's Date  ___________#
# now = dt.datetime.now()
#
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# second = now.second
# day_of_week = now.weekday()

## ____________ Setting A Date  ___________#
# date_of_birth = dt.datetime(year=2000, month=4, day=25)
# print(date_of_birth)


import datetime as dt
import smtplib
import random

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 0:
    with open(file="quotes.txt", mode="r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # ____________ Sending Mail ___________#
    my_email = "amaljalappatttest@gmail.com"
    password = "Super*123"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivational Quotes\n\n{quote}"
                            )









