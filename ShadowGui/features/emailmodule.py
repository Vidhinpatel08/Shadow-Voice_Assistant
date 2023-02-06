import smtplib

with open(r'ShadowGui\features\email.txt') as f :
    user_email=f.readline()
    password=f.readline()
    client_email=f.readline()

def sendEmail(content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user_email, password)
        server.sendmail(user_email, client_email,content)
        server.close()
    except Exception as e:
        print(e)

if __name__ =='__main__':
    sendEmail("these Test","""Hello Sir, 
    Shadow the Voice Assistent Sends The Email. 
    This is Mail Description""")

