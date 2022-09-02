import smtplib

with open('./features/email.txt') as f :
    user_email=f.readline()
    password=f.readline()
    client_email=f.readline()



def sendEmail(subject,content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user_email, password)
        server.sendmail(user_email, client_email,subject, content)
        server.close()
    except Exception as e:
        print(e)

