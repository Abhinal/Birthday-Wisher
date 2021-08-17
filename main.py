import pandas
import datetime as dt
from random import choice
import smtplib

adminID = input("Enter your Gmail ID: ")
adminPW = input("Enter your Gmail Password: ")

LETTERS_PATH = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

now = dt.datetime.now()
month = now.month
day = now.day

df = pandas.read_csv('birthdays.csv')
code_dict = df.to_dict(orient='records')

for people in code_dict:
    if people['month'] == month and people['day'] == day:
        with open(choice(LETTERS_PATH)) as letter:
            content = letter.read()
            message_body = content.replace('[NAME]', people['name'])
        for _ in range(500):
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(user=adminID, password=adminPW)
                connection.sendmail(from_addr=adminID, to_addrs=people['email'], msg=f'Subject:Happy Birthday\n\n{message_body}')