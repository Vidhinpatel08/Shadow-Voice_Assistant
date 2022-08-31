import email
import smtplib

with open('email.text') as f :
    user_email=f.readline()
    password=f.readline()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user_email, password)
    server.sendmail(user_email, to, content)
    server.close()

# sendEmail("vidhin203@gmail.com","hello jarvis sends mail.")
# print("Done")
