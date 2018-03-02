import smtplib, sys, openpyxl

#Excel
wb = openpyxl.load_workbook('c:\\temp\\EmailList.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

#Populate Email Addresses into dictinonary
EmailsToSend = {}
for r in range(2, sheet.max_row -1):
    name = sheet.cell(row=r, column=1).value
    email = sheet.cell(row=r, column=2).value
    PEN = sheet.cell(row=r, column=3).value
    EmailsToSend[name] = {str(email):str(PEN)}

#Send Emails
smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('xxxxxxxxxx@live.com', '*******')
for name, subDict in EmailsToSend.items():
    message = """
    Subject: New PEN. \n
    Dear %s,

    Your new PEN is: %s

    Regards,
    ZR""" % (name, ''.join(list(subDict.values())))

    print('Sending to %s ...' % name)
    smtpObj.sendmail('xxxxxx@live.com',subDict.keys(), message)

smtpObj.quit()
