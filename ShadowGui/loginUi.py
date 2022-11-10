import re
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import loginShadow
import shadow
import Registration_Shadow as Rs
from FaceRecognition import Model_Trainer as Mt

from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime , QDate, Qt 
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from shadowUi import Ui_ShadowUI

class login(QDialog):
    def __init__(self):
        super(login, self).__init__()
        loadUi("ShadowGui/loginUi.ui",self)
        self.warning.setVisible(False)

        # Button
        self.button.clicked.connect(self.buttonclicked)
        self.createAccButton.clicked.connect(self.gotoRegister)

    def buttonclicked(self):
        self.warning.setVisible(False)
        userEmail = self.emailEdit.text().lower().strip() # for login button take name on interface
        if userEmail =='':
                warningmsg = 'Not allow blank string as input'.upper()
                self.warning.setVisible(True)
                self.warning.setText(warningmsg)
        elif re.search(r"[a-zA-z0-9+._%$&]+@[a-zA-z0-9+_%$&]+[.][a-zA-z.0-9]+",userEmail) :
            namelist,nameid,nameEmail = [],[],[]
            with open(r"ShadowGui\FaceRecognition\namelist.txt") as f :
                for i in f:
                    namelist.append(i.split('\n')[0].split('-')[0])
                    nameid.append(i.split('\n')[0].split('-')[1])
                    nameEmail.append(i.split('\n')[0].split('-')[2])
            if userEmail in nameEmail:
                warningmsg = 'press "q" to Exit Camera Screen'.upper()
                self.warning.setVisible(True)
                self.warning.setText(warningmsg)

                index = nameEmail.index(userEmail)
                face_id = nameid[index]
                username = namelist[index]
                print(username,face_id,userEmail)

                authenticate = loginShadow.main_app(username,face_id,userEmail)
                print("Authentication : ",authenticate)
                if authenticate == 'done':
                    MainWindow = Main()
                    widget.addWidget(MainWindow)
                    widget.setFixedHeight(751) # shadow Panel hight
                    widget.setFixedWidth(1168) # shadow Panel width
                    widget.setCurrentIndex(widget.currentIndex()+1)
                else:
                    warningmsg = 'You are not Authenticate person!, check Email id'.upper()
                    self.warning.setVisible(True)
                    self.warning.setText(warningmsg)
                        
            else:
                warningmsg = 'Email Not Matching !!!, Try again With Correct Email'.upper()
                self.warning.setVisible(True)
                self.warning.setText(warningmsg)
                self.emailEdit.setText('')
        else:
            warningmsg = 'Email not valid !'.upper()
            self.warning.setVisible(True)
            self.warning.setText(warningmsg)

    def gotoRegister(self):
        registeruser = Register()
        widget.addWidget(registeruser)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

class Register(QDialog):
    def __init__(self):
        super(Register, self).__init__()
        loadUi("ShadowGui/RegistrationUi.ui",self)
        self.warning.setVisible(False)

        # Button
        self.button.clicked.connect(self.buttonclicked)

    def buttonclicked(self):
        face_id = self.idEdit.text().lower().strip()
        name = self.nameEdit.text().strip()
        emaild = self.emailEdit.text().lower().strip()
        if face_id.startswith('0'):
            face_id = face_id[1:]

        if face_id == '' or name == ''  or emaild == '':
                warningmsg = 'Not allow blank string as input'.upper()
                self.warning.setVisible(True)
                self.warning.setText(warningmsg)

        elif not re.search(r"[a-zA-z0-9+._%$&]+@[a-zA-z0-9+_%$&]+[.][a-zA-z.0-9]+",emaild) :
            warningmsg = 'Email not valid !'.upper()
            self.warning.setVisible(True)
            self.warning.setText(warningmsg)   

        else:         
            f = open(r'ShadowGui\FaceRecognition\namelist.txt')
            value = f.read(1)
            f.close()
            if value  == '':
                with open(r'ShadowGui\FaceRecognition\namelist.txt','a') as f :
                    nameadd = name +"-"+ face_id+'-'+emaild+'\n'
                    f.write(nameadd)
            else:
                with open(r'ShadowGui\FaceRecognition\namelist.txt') as f :
                    namelist,nameid,nameEmail = [],[],[]
                    for i in f:
                            nameid.append(i.split('\n')[0].split('-')[1])
                            nameEmail.append(i.split('\n')[0].split('-')[2])
                    if face_id in nameid:
                        warningmsg = 'Face ID Already In Database. Try again With Other ID'.upper()
                        self.warning.setVisible(True)
                        self.warning.setText(warningmsg)
                        self.idEdit.setText('')
                    elif emaild in nameEmail:
                        warningmsg = 'Email Already In Database. Try again With Other ID'.upper()
                        self.warning.setVisible(True)
                        self.warning.setText(warningmsg)
                        self.emailEdit.setText('')                    
                    else:
                        with open(r'ShadowGui\FaceRecognition\namelist.txt','a') as f :
                            nameadd = name +"-"+ face_id+'-'+emaild+'\n'
                            f.write(nameadd)
                        print('starting Registration...')
                        self.button.setDisabled(True)
                        self.setDisabled(True)
                        
                        Rs.register(name ,face_id,emaild)
                        Mt.starttrainer(name,emaild)
                        Login = login()
                        widget.addWidget(Login)
                        widget.setCurrentIndex(widget.currentIndex()+1)
                            
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShadowUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.starttask)        
        self.ui.pushButton_2.clicked.connect(widget.close)  
        shadow.speak(f'sir, Please click on RUN button to start and  click On EXIT to Stop.')
        
    def starttask(self):
        self.ui.movie = QtGui.QMovie(r"ShadowGui\images\Main.gif")      # path of main bg_image (Labal-1)
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"ShadowGui\images\Initial.gif")      # path of (Labal-2)
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"ShadowGui\images\Shadow.gif")      # path of (Labal-3)
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer= QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        shadow.startExecution.start() #ShadowUI.resize(1168, 751)
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

# main
app = QApplication(sys.argv)
mainwindow = login() # Login Panel 
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(441) # Login Panel height
widget.setFixedWidth(688) # Login Panel width 
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")



