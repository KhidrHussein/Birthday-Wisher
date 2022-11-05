# import smtplib
#
# my_email = "khidrhussein0@gmail.com"
# password = "Hussein_khidr1104"
# #
# # connection = smtplib.SMTP("smtp.gmail.com", 587)
# # connection.starttls()
# # connection.login(user=my_email, password=password)
# # connection.sendmail(from_addr=my_email, to_addrs="husseinkhidr@yahoo.com", msg="Hello")
# # connection.close()
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user="husseinkhidr@yahho.com", password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="Husseinkhidr@yahoo.com", msg="Hello")

import datetime as dt
import random
import smtplib

my_email = "khidrhussein0@gmail.com"
password = "Hussein_khidr1104"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 5:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="husseinkhidr@yahoo.com",
            msg=f"Subject: Friday Motivation \n\n{quote}")
