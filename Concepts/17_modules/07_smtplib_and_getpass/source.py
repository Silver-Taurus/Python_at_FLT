#! /usr/bin/env python3

''' Python script to send email '''

# To send emails with python, we need to manually go through the steps of:
#   - Connecting to an email server
#   - Confirming connection
#   - setting a protocol
#   - logging on
# Every major email provider has thier own SMTP (Simple Main Transfer Protocol) Server.

import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_object.ehlo())

# if we have choosen the port 465, then we can skip this step
print(smtp_object.starttls())

# using getpass library to securly enter the password by hiding it on the screen
email = input('Email: ')
password = getpass.getpass('Password please: ')        
print(smtp_object.login(email, password))

from_address = email
to_address = email
subject = input('Enter the subject here: ')
message = input('Enter the body message: ')
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address, to_address, msg)