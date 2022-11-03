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
                warningmsg = 'You are not allow to input any input is blank'
                self.warning.setVisible(True)
                self.warning.setText(warningmsg)
        else:         
            namelist,nameid,nameEmail = [],[],[]
            with open(r"ShadowGui\FaceRecognition\namelist.txt") as f :
                for i in f:
                    namelist.append(i.split('\n')[0].split('-')[0])
                    nameid.append(i.split('\n')[0].split('-')[1])
                    nameEmail.append(i.split('\n')[0].split('-')[2])
            if userEmail in nameEmail:
                index = nameEmail.index(userEmail)
                # print('index',index)
                face_id = nameid[index]
                # print('faceid :',face_id)
                username = namelist[index]
                # print('username :',username)
                print(username,face_id,userEmail)
                loginShadow.main_app(username,face_id,userEmail)
                MainWindow = Main()
                widget.addWidget(MainWindow)
                widget.setFixedHeight(751)
                widget.setFixedWidth(1168)
                widget.setCurrentIndex(widget.currentIndex()+1)
                        
            else:
                warningmsg = 'You Email Not Matching In Ourdata. Try again With Correct Email'
                self.warning.setVisible(True)
                self.warning.setText(warningmsg)
                self.emailEdit.setText('')
    
    def gotoRegister(self):
        registeruser = Register()
        widget.addWidget(registeruser)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

class Register(QDialog):
    def __init__(self):
        super(Register, self).__init__()
        loadUi("ShadowGui/RegistationUi.ui",self)
        self.warning.setVisible(False)

        # Button
        self.button.clicked.connect(self.buttonclicked)

    def buttonclicked(self):
        face_id = self.idEdit.text().lower().strip()
        if face_id.startswith('0'):
            face_id = face_id[1:]
        name = self.nameEdit.text().lower().strip()
        emaild = self.emailEdit.text().lower().strip()

        self.warning.setVisible(False)
        # namelist file management 
        if face_id == '' or name == ''  or emaild == '':
                warningmsg = 'You are not allow to input any input is blank'
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
                            namelist.append(i.split('\n')[0].split('-')[0])
                            nameid.append(i.split('\n')[0].split('-')[1])
                            nameEmail.append(i.split('\n')[0].split('-')[2])
                    if face_id in nameid:
                        warningmsg = 'You Face ID Number Already In Ourdata. Try again With Other ID'
                        self.warning.setVisible(True)
                        self.warning.setText(warningmsg)
                        self.idEdit.setText('')
                    elif name in namelist:
                        warningmsg = 'You Name Already In Ourdata. Try again With Other name'
                        self.warning.setVisible(True)
                        self.warning.setText(warningmsg)
                        self.nameEdit.setText('')                    
                    elif emaild in nameEmail:
                        warningmsg = 'You Email Already In Ourdata. Try again With Other ID'
                        self.warning.setVisible(True)
                        self.warning.setText(warningmsg)
                        self.emailEdit.setText('')                    
                    else:
                        with open(r'ShadowGui\FaceRecognition\namelist.txt','a') as f :
                            nameadd = name +"-"+ face_id+'-'+emaild+'\n'
                            f.write(nameadd)
                        print('start')
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
mainwindow = login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(441)
widget.setFixedWidth(688)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")



