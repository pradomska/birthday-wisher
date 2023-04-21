import smtplib
import datetime as dt
import random

MY_EMAIL = "python32day@outlook.com"
PASSWORD = "nqtsxpknskezotcg"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with open("quotes.txt", mode="r") as file:
        list = file.readlines()
        message = random.choice(list)

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="python32day@gmail.com",
            msg=f"Subject:Motivational Quotes\n\n{message}")
