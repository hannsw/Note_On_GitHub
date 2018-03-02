import smtplib

smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)

smtpObj.ehlo()

smtpObj.starttls()

smtpObj.login('xxxx@live.com', 'passssssssss')

message = """From: Daniel H <xxxx@live.com>
To: H  <xxxxx@live.com>
Subject: Test-Sub2

This is a test e-mail message.
"""

smtpObj.sendmail('xxxx@live.com','xxxxw@live.com', message)

smtpObj.quit()
