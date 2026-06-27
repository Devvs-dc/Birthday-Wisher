import random
import smtplib
import pandas as pd
import datetime as dt

import os
user_name=os.environ.get("MY_EMAIL")
pass_word=os.environ.get("MY_PASSWORD")
                         
letters=["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
df=pd.read_csv("birthdays.csv")
bday_months=df["month"].to_list()
today=dt.datetime.now()
bday_row=df[(df.month == today.month) & (df["day"] == today.day)]

if not bday_row.empty:
    for _,row in bday_row.iterrows():
        bday_name=row["name"]
        bday_email=row["email"]
        rndm_letter = random.choice(letters)
        with open(rndm_letter,"r") as file:
            data=file.read()
        bday_letter=data.replace("[NAME]",bday_name)
        with smtplib.SMTP("smtp.mail.com") as connect:
            connect.starttls()
            connect.login(user=user_name,password=pass_word)
            connect.sendmail(
                from_addr=user_name,
                to_addrs=bday_email,
                msg=f"Happy Birthday\n\n{bday_letter}"
            )
else:
    pass
