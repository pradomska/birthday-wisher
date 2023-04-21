import smtplib
import datetime as dt
import random
import pandas as pd

MY_EMAIL = "python32day@outlook.com"
PASSWORD = "aiovkjscnxhzujmq"

now = dt.datetime.now()
today_month = now.month
today_day = now.day

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)
if (today_month, today_day) in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    print(file_path)
    name = birthdays_dict[(today_month, today_day)]["name"]
    print(name)
    with open(file_path) as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", name)
        print(letter)
    print(birthdays_dict[(today_month, today_day)]['email'])
    # Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=f"{birthdays_dict[(today_month, today_day)]['email']}",
            msg=f"Subject:Happy Birthday!\n\n{letter}")
