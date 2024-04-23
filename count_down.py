# Create in terminal
# python -m venv .venv

# input, goal, waktunya tinggal berapa
# 'str' : 24.02.2024

import datetime

user_input = input("Input your goals and deadline\nex goals:DD.MM.YYYY\n")
goals, date_entry = map(str, user_input.split(':'))
day, month, year = map(int, date_entry.split('.'))
date = datetime.date(year,month,day)
now = datetime.date.today()

print("Goals kamu: ",goals)
print("Sisa waktu: ",date-now)
