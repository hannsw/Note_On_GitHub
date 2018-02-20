import smtplib

smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)

smtpObj.ehlo()

smtpObj.starttls()

smtpObj.login('dhhh@live.com', 'Vista2048')

message = """From: Daniel Han <dhhh@live.com>
To: Han NSW <han.nsw@live.com>
Subject: Test-Sub2

This is a test e-mail message.
"""

smtpObj.sendmail('dhhh@live.com','han.nsw@live.com', message)

smtpObj.quit()
