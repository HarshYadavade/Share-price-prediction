from multiprocessing import Process
import threading
import pandas as pd
import sys
import time
# from urllib.request import urlopen
import requests
import yfinance as yf
import allimgs
import requests
from bs4 import BeautifulSoup
import Connectionpro as cp
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import math
import random
import smtplib
import yfinance as yf
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from sklearn.preprocessing import MinMaxScaler
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential


class WelcomeScreen(QMainWindow):

    def __init__(self):
        super(WelcomeScreen , self).__init__()
        loadUi("welcome.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.Loginbut.clicked.connect(self.gotologin)
        self.Signupbut.clicked.connect(self.gotosignup)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

    def closeEvent(self, event):
                event.accept()
                global started
                started = False  
                global intche
                intche = False  
    
    def gotologin(self):
        login.show()
        welcome.close()
        
    def gotosignup(self):
        signup.show()
        welcome.close()

    def totclose(self):
        welcome.close()
        global started
        started = False

class LoginScreen(QDialog):

    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("LoginScreen.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.Loginbutton.clicked.connect(self.login)
        self.hmbu.clicked.connect(self.back_WelcomeScreen)
        self.createaccbut.clicked.connect(self.gotosignup)
        self.frgbur.clicked.connect(self.forgotpass)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        # t34 = threading.Thread(target=self.internet_on , args=())
        # t34.start()

    # def internet_on(self):
    #     global intche
    #     while intche :
    #         try:
    #             urlopen('https://www.google.co.in/', timeout=1)
    #         except:
    #             background-color: rgb(255, 255, 255);
    
    def closeEvent(self, event):
            event.accept()
            global started
            started = False
            global intche
            intche = False 

    def forgotpass(self):
        frgot.show()
        login.close()
    
    def back_WelcomeScreen(self):
        welcome.show()
        login.close()
           
    def gotosignup(self):
        signup.show()
        login.close()

    def login(self):
        un = self.un.text()
        pa = self.pa.text()
        
        if len(un) == 0:
                err = QMessageBox()
                err.setIcon(QMessageBox.Critical)
                err.setText("ERROR!!Fields cannot be empty...")
                err.setWindowTitle("Warning")
                err.setStandardButtons(QMessageBox.Ok)
                retval = err.exec_() 
        
        elif len(pa) == 0:    
                err = QMessageBox()
                err.setIcon(QMessageBox.Critical)
                err.setText("ERROR!!! Fields cannot be empty...")
                err.setWindowTitle("Warning")
                err.setStandardButtons(QMessageBox.Ok)
                retval = err.exec_() 
        else:   
                username_login = ""
                password_login = ""
                cp.cursor.execute("Select * from profile where username='"+ un +"'")
                result = cp.cursor.fetchall() 
                for row in result:
                    user_Name = row[0]
                    username_login = row[3] 
                    password_login = row[4]
                
                if un == username_login and pa == password_login:
                    ug.show()
                    ug.label_11.setText(user_Name)
                    ug.username_ug.setText(un)
                    login.close()
                    global started
                    started = True
                    t1 = threading.Thread(target= ug.sen, args=())
                    t1.start()
                    t2 = threading.Thread(target=ug.nifty, args= ())
                    t2.start()
                    t3 = threading.Thread(target=ug.sensex_ch_rs, args=())
                    t3.start()
                    t4 = threading.Thread(target=ug.nifty_ch_rs,args=())
                    t4.start()
                    t5 = threading.Thread(target=ug.timeeee,args=())
                    t5.start()
                    t6 = threading.Thread(target=ug.timeeeenif,args=())
                    t6.start()
                    t7 = threading.Thread(target=ug.sensex_ch_per,args=())
                    t7.start()
                    t8 = threading.Thread(target=ug.nifty_ch_per,args=())
                    t8.start()
                else:   
                    err = QMessageBox()
                    err.setIcon(QMessageBox.Critical)
                    err.setText("Invalid login details")
                    err.setWindowTitle("Warning")
                    err.setStandardButtons(QMessageBox.Ok)
                    retval = err.exec_() 

class SignupScreen(QDialog):
    
    def __init__(self):
        super(SignupScreen, self).__init__()
        loadUi("SignupScreen.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.Signupbut.clicked.connect(self.creator)
        self.Backbut.clicked.connect(self.back_WelcomeScreen)
        self.verify.clicked.connect(self.verifier)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
   
    def closeEvent(self, event):
                event.accept()
                global started
                started = False
                global intche
                intche = False 

    def verifier(self):
        
        emailver = self.Email.text()
        self.OTPve = ""
        digits = "0123456789"
              
        for i in range(6) :
                self.OTPve += digits[math.floor(random.random() * 10)]

        text = "Hii User, \r\nThank you for choosing AMJH Stock Predictor \r\nWelcome to AMJH Services and start your financestic journey with us \r\nPlease find the One Time Password(OTP) attached with the email \r\nYour OTP is:"+self.OTPve+"\r\nThank You, \r\nTeam AMJH"
        
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("amjh32255@gmail.com","klwmihjqxbmiiqja")

        SUBJECT = "NEW REGISTRATION"
        TEXT = text
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        try:
            server.sendmail("amjh32255@gmail.com",emailver,message)
            print("success")
            self.cont.setText("We've sent an verification code to your email")
        
        except smtplib.SMTPRecipientsRefused:
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("ERROR!! Invalid Email Address...")
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_() 
        finally:
            server.quit()

    def creator(self):
        name_1 = self.Name.text()
        name_2 = self.Name_2.text()
        name_3 = self.Name_3.text()
        name = name_1+" "+name_2+" "+name_3 
        mobile = self.Mobile.text()
        email = self.Email.text()
        username = self.Username.text()
        password = self.Password.text()
        ren = self.Reenter.text()
        birthdate = self.birth.date().toString()
        gender = self.gender.currentText()
        otpsu = self.otpfile.text()

        if len(name_1)==0 or len(name_2)==0 or len(name_3)==0 or len(mobile)==0 or len(email)==0 or len(username)==0 or len(password)==0 or len(ren)==0 or len(gender)==0 or len(otpsu)==0:
                err = QMessageBox()
                err.setIcon(QMessageBox.Critical)
                err.setText("ERROR!! Fields cannot be empty...")
                err.setWindowTitle("Warning")
                err.setStandardButtons(QMessageBox.Ok)
                retval = err.exec_() 

        elif self.tandc.isChecked():
        
            if otpsu == self.OTPve:

                cp.cursor.execute("Select(EXISTS(Select username from profile where username='"+username+"'))::int")
                result = cp.cursor.fetchone()
                if name_1.isalpha() == False:
                            err = QMessageBox()
                            err.setIcon(QMessageBox.Critical)
                            err.setText("ERROR!! Invalid Name format") 
                            err.setWindowTitle("Warning")
                            err.setStandardButtons(QMessageBox.Ok)
                            retval = err.exec_()
                elif name_2.isalpha() == False:
                            err = QMessageBox()
                            err.setIcon(QMessageBox.Critical)
                            err.setText("ERROR!! Invalid Name format") 
                            err.setWindowTitle("Warning")
                            err.setStandardButtons(QMessageBox.Ok)
                            retval = err.exec_()
                elif name_3.isalpha() == False:
                            err = QMessageBox()
                            err.setIcon(QMessageBox.Critical)
                            err.setText("ERROR!! Invalid Name format") 
                            err.setWindowTitle("Warning")
                            err.setStandardButtons(QMessageBox.Ok)
                            retval = err.exec_()
                elif len(mobile) < 10 or len(mobile) > 10:
                            err = QMessageBox()
                            err.setIcon(QMessageBox.Critical)
                            err.setText("ERROR!! Invalid Mobile Number") 
                            err.setWindowTitle("Warning")
                            err.setStandardButtons(QMessageBox.Ok)
                            retval = err.exec_()
                elif mobile.isdecimal() == False:
                            err = QMessageBox()
                            err.setIcon(QMessageBox.Critical)
                            err.setText("ERROR!! Invalid Mobile No. format") 
                            err.setWindowTitle("Warning")
                            err.setStandardButtons(QMessageBox.Ok)
                            retval = err.exec_()  
                elif otpsu.isdecimal() == False:
                            err = QMessageBox()
                            err.setIcon(QMessageBox.Critical)
                            err.setText("ERROR!! Invalid OTP format") 
                            err.setWindowTitle("Warning")
                            err.setStandardButtons(QMessageBox.Ok)
                            retval = err.exec_()
                elif result[0] == 1:
                            err = QMessageBox()
                            err.setIcon(QMessageBox.Critical)
                            err.setText("Username already exists !!")
                            err.setWindowTitle("Warning")
                            err.setStandardButtons(QMessageBox.Ok)
                            retval = err.exec_()
                elif password == ren:
                    sql = """INSERT INTO profile (name, mobile, email, username, password, birthdate, gender) Values(%s,%s,%s,%s,%s,%s,%s) """
                    val = (name,mobile,email,username,password,birthdate,gender)
                    cp.cursor.execute(sql,val)
                    cp.connection.commit()
                    err = QMessageBox()
                    err.setIcon(QMessageBox.Information)
                    err.setText("HURRAH!! Sign Up Successful")
                    err.setWindowTitle("Success")
                    err.setStandardButtons(QMessageBox.Ok)
                    retval = err.exec_()
                    login.show()
                    signup.close()
                    self.Name.setText("")
                    self.Name_2.setText("")
                    self.Name_3.setText("")
                    self.Mobile.setText("")
                    self.Email.setText("")
                    self.Username.setText("")
                    self.Password.setText("")
                    self.Reenter.setText("")
                    self.birth.date()
                    self.gender.currentText()
                    self.otpfile.setText("")

                else:
                    err = QMessageBox()
                    err.setIcon(QMessageBox.Critical)
                    err.setText("ERROR!! Password fields do not Match") 
                    err.setWindowTitle("Warning")
                    err.setStandardButtons(QMessageBox.Ok)
                    retval = err.exec_()
            else:
                err = QMessageBox()
                err.setIcon(QMessageBox.Critical)
                err.setText("OTP verification failed!!!") 
                err.setWindowTitle("Warning")
                err.setStandardButtons(QMessageBox.Ok)
                retval = err.exec_()

        else:
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("Please check the T&C checkbox !!!") 
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_()

    def back_WelcomeScreen(self):
        welcome.show()
        signup.close()

class Forgetpassword(QDialog):

        def __init__(self):
            super(Forgetpassword , self).__init__()
            loadUi("Forgetpassword.ui",self)
            self.setWindowTitle('AMJH_SPP')
            self.setWindowIcon(QIcon('120.jpeg'))
            self.enter_forgetpass.clicked.connect(self.forgetmail)
            self.submit_Forgetpassword.clicked.connect(self.actofotpver)
            self.resend.clicked.connect(self.forgetmail)
            self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        
        def closeEvent(self, event):
                    event.accept()
                    global started
                    started = False
                    global intche
                    intche = False  

        def forgetmail(self):
            self.efield = self.emailfield.text()
            if len(self.efield) == 0 :
                err = QMessageBox()
                err.setIcon(QMessageBox.Critical)
                err.setText("ERROR!!Fields cannot be empty...")
                err.setWindowTitle("Warning")
                err.setStandardButtons(QMessageBox.Ok)
                retval = err.exec_() 
            else:
                
                cp.cursor.execute("Select(EXISTS(Select name from profile where email = '"+self.efield+"'))::int")
                result = cp.cursor.fetchone()
                if result[0] == 0:
                    err = QMessageBox()
                    err.setIcon(QMessageBox.Critical)
                    err.setText("ERROR!! No data found...")
                    err.setWindowTitle("Warning")
                    err.setStandardButtons(QMessageBox.Ok)
                    retval = err.exec_() 
                else:
                    self.OTPver = ""
                    cp.cursor.execute("Select name from profile where email = '"+self.efield+"'")
                    result = cp.cursor.fetchone()
                    digits = "0123456789"

                    for i in range(6) :
                            self.OTPver += digits[math.floor(random.random() * 10)]

                    text = "Hii"+result[0]+", \r\nYou recently requested to Reset the password for your account. \r\nPlease Find the One Time Password (OTP) attached with the email. \r\nIf you did not request a password reset, reply to let us know .\r\nYour OTP : "+self.OTPver+"\r\nThank You,\r\nTeam AMJH"

                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    server.login("amjh32255@gmail.com","klwmihjqxbmiiqja")

                    SUBJECT = "FORGOT PASSWORD"
                    TEXT = text
                    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

                    try:
                        server.sendmail("amjh32255@gmail.com",self.efield ,message)
                        print("success")
                        self.label_5.setText("We've sent an verification code to your email")
                    
                    except smtplib.SMTPRecipientsRefused:
                        err = QMessageBox()
                        err.setIcon(QMessageBox.Critical)
                        err.setText("ERROR!! Invalid Email Address...")
                        err.setWindowTitle("Warning")
                        err.setStandardButtons(QMessageBox.Ok)
                        retval = err.exec_() 
                    finally:
                        server.quit()
                        
        def actofotpver(self):

            if self.OTPver == self.otpfield.text():
                frgpasss.show()
                frgot.close()
                frgpasss.invisible.setText(self.efield)

            else:
                err = QMessageBox()
                err.setIcon(QMessageBox.Critical)
                err.setText("Invalid details!!")
                err.setWindowTitle("Warning")
                err.setStandardButtons(QMessageBox.Ok)
                retval = err.exec_()

class Changepassfor(QDialog):
    
        def __init__(self):
            super(Changepassfor , self).__init__()
            loadUi("Changepasswordfor.ui",self)
            self.setWindowTitle('AMJH_SPP')
            self.setWindowIcon(QIcon('120.jpeg'))
            self.submitchangepassfor.clicked.connect(self.changepass)
            self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        def closeEvent(self, event):
                    event.accept()
                    global started
                    started = False
                    global intche
                    intche = False 
        
        def changepass(self):
            newpass = self.newpassfor_newpass.text()
            newpassre = self.newpassfor_reenter.text()
            efield = self.invisible.text()
            if len(newpass) == 0 or len(newpassre)==0:
                err = QMessageBox()
                err.setIcon(QMessageBox.Critical)
                err.setText("ERROR!!Fields cannot be empty...")
                err.setWindowTitle("Warning")
                err.setStandardButtons(QMessageBox.Ok)
                retval = err.exec_() 
            
            elif newpass == newpassre:
                import Connectionpro as cp
                cp.cursor.execute("Update profile Set password='"+newpass+"'where email ='"+efield +"'")
                cp.connection.commit()
                err = QMessageBox()
                err.setIcon(QMessageBox.Information)
                err.setText("Password change successful")
                err.setWindowTitle("Success")
                err.setStandardButtons(QMessageBox.Ok)
                retval = err.exec_()
                login.show()
                frgpasss.close()
           
            def closeEvent(self, event):
                global started
                started = False   
                event.accept()

class UserPage(QDialog):
    
    def __init__(self):
        super(UserPage , self).__init__()
        loadUi("UserPage.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.Logout.clicked.connect(self.logout)
        self.radioButton.toggled.connect(self.onclick)
        self.radioButton.toggled.connect(self.onclick)
        self.fav.clicked.connect(self.favo)
        self.supp.clicked.connect(self.suppo)
        self.hist.clicked.connect(self.histoo)
        self.port.clicked.connect(self.portf)
        self.sett.clicked.connect(self.prosett)
        self.search.clicked.connect(self.searchee)
        self.radioButton.setChecked(True)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
    
    def closeEvent(self, event):
            event.accept()
            global started
            started = False
            global intche
            intche = False 

    def favo(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select stockname from wishlist where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        f.tableWidget.setColumnCount(1)
        f.tableWidget.setHorizontalHeaderLabels([""])
        f.tableWidget.setColumnWidth(0,1011)
        f.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            f.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        f.username_ug.setText(unam)
        f.show()
        ug.close()
        global started
        started = False

    def histoo(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select tickname from search_hist where username='"+unam+"'")
        res = cp.cursor.fetchall()
        his.tableWidget.setColumnCount(1)
        his.tableWidget.setHorizontalHeaderLabels([""])
        his.tableWidget.setColumnWidth(0,1011)
        his.tableWidget.setRowCount(len(res))
        i = 0 
        for row in res:
            his.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        his.username_ug.setText(unam)
        his.show()
        ug.close()
        global started
        started = False

    def portf(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select stockname from portfolio where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        por.tableWidget.setColumnCount(1)
        por.tableWidget.setHorizontalHeaderLabels([""])
        por.tableWidget.setColumnWidth(0,1011)
        por.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            por.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        por.username_ug.setText(unam)
        por.show()
        ug.close()
        global started
        started = False

    def prosett(self):
        unam = self.username_ug.text()
        se.username_ug.setText(unam)
        se.show()
        ug.close()
        global started
        started = False

    def suppo(self):
        unam = self.username_ug.text()
        sup.username_ug.setText(unam)
        sup.show()
        ug.close()
        global started
        started = False

    def logout(self):
        login.show()
        global started 
        started = False
        login.un.setText("")
        login.pa.setText("")
        ug.close()
    
    def onclick(self):
        if self.radioButton.isChecked():
            vbox = QVBoxLayout()
            names = ['Arex Industries Ltd.', 'Adinath Textiles Ltd', 'D. B. Corp Limited', 'Bharat Heavy Electricals Ltd.', 'IRB Infrastructure Developers Limited', 'New Delhi Television Limited', 'Ishita Drugs & Industries Ltd', 'Gateway Distriparks Limited', 'DLF Limited', 'Deepak Spinners Limited', 'Danlaw Technologies India Limited', 'Vipul Dye Chem Ltd.', 'Vadilal Dairy International Ltd.', 'Trimurthi Limited', 'Thakkers Developers Ltd', 'TATA MOTORS LTD - DVR', 'SUPERSTAR DISTILLERIES & FOODS', 'Shri Dinesh Mills Limited', 'Radhe Developers (India) Ltd.', 'Proto Developers & Technologies Limited', 'ND Metal Industries Ltd', 'MODERN DENIM LTD.', 'Mangalam Drugs & Organics Limited', 'Interworld Digital Ltd.', 'Indian Toners & Developers Ltd.', 'India Lease Development Limited', 'Housing Development & Infrastructure Limited', 'Housing Development Finance Corporation Limited', 'Golkunda Diamonds & Jewellery Limited', 'Ess Dee Aluminium Limited', 'E.I.D.- Parry (India) Limited', 'Keltech Energies Limited', 'Eastern Silk Industries Ltd.', 'Sterling International Enterprises Ltd.', 'Sequel e-Routers Ltd.', 'M.K. Exim (India) Limited', 'Jaybharat Textiles And Real Estate Limited', 'Indiabulls Real Estate Limited', 'Emmessar Biotech & Nutrition Limited', 'E.com Infotech India Ltd.', 'Bharat Electronics Limited', 'Zicom Electronic Security Systems Limited', 'Anukaran Commercial Enterprises Ltd.', 'Fortune Financial Services (India) Limited', 'Sundram Fasteners Limited', 'Sundaram Finance Limited', 'Relaxo Footwears Limited', 'Rashtriya Chemicals And Fertilizers Limited', 'Nikki Global Finance Limited', 'KZ Leasing & Finance Ltd.', 'Integrated Financial Services Limited', 'Hindustan Foods Limited', 'Hilton Metal Forging Limitied', 'Gowra Leasing & Finance Ltd.', 'Geefcee Finance Limited', 'Force Motors Ltd.', 'Foods & Inns Ltd.', 'Filmcity Media Ltd.', 'Foundry Fuel Products Ltd.', 'Arora Fibres', 'Ajwa Fun World & Resort Ltd', 'Ad-Manum Finance Ltd', 'Subway Finance & Investment Co., Ltd.', 'SIYARAM PODDAR FINANCE & TRADI', 'SHERATON PROPERTIES & FINANCE', 'SAMPARK TRADING & FINANCE LTD.', 'Nivedita Mercantile & Financing Ltd.', 'Wall Street Finance Ltd.', 'WEIZMANN FOREX LTD.', 'Wallfort Financial Services Limited', 'Voith Paper Fabrics India Limited', 'VBC Ferro Alloys Limited', 'Vax Housing Finance Corporation Ltd.', 'Upasana Finance Ltd', 'Tirupati Foam Limited', 'Gayatri Projects Limited', 'TAJGVK Hotels & Resorts Limited', 'Oil and Natural Gas Corp. Ltd.', 'Huhtamaki PPL Limited', 'International Travel House Limited', 'Hester Biosciences Ltd', 'Hindustan Construction Company Limited', 'Gujarat Hotels Ltd.', 'Graviss Hospitality Limited', 'Benares Hotels Limited', 'Zenith Healthcare Ltd', 'WONDERLA HOLIDAYS LTD', 'WH Brady & Company Limited', 'THE BYKE HOSPITALITY LTD.', 'Sunil Hitech Engineers Ltd.', 'STERLINH6.BO', 'Sterling Holiday Resorts (India) Limited', 'Shree Hari Chemicals Export Limited', 'Shree Ganesh Jewellery House (I) Limited', 'Royal Orchid Hotels Limited', 'J.Kumar Infraprojects Limited', 'JVL Agro Industries Ltd', 'Jai Balaji Industries Ltd.', 'State Bank of Bikaner & Jaipur', 'Jyoti Ltd.', 'Jubilant FoodWorks Limited', 'JSW STEEL LTD.', 'JSW Energy Limited', 'JPT Securities Ltd.', 'Jaiprakash Power Ventures Limited', 'Jaypee Infratech Limited', 'Jetking Infotrain Limited', 'Jet Airways (India) Ltd.', 'JCT Ltd.', 'JAMES WARREN TEA LTD', 'Jagsonpal Finance & Leasing Ltd', 'Divya Jyoti Industries Ltd', 'B.J.DUPLEX BOARDS LTD.', 'JAI MATA INDUSTRIES LTD.', 'Jyoti Resins & Adhesives Ltd.', 'JUPITER INFOMEDIA LTD.', 'JENSON & NICHOLSON (INDIA) LTD', 'JKLAKSHMI*', 'Kintech Renewables Limited', 'JAY ENERGY AND S.ENERGIES LTD.', 'Jayatma Spinners Limited', 'Jayant Mercantile Co. Ltd.', 'R J BIO-TECH LTD', 'JINDAL WORLDWIDE LTD.', 'JINDAL STEEL & POWER LTD.', 'JINDAL POLY FILMS LTD.', 'JAIPRAKASH ASSOCIATES LTD.', 'Kashyap Tele-Medicines Limited', 'VERONICA PRODUCTION LTD', 'JAIN IRRIGATION SYSTEMS LTD.', 'JPASSOCIAT6.BO', 'Jeevan Scientific Technology L', 'Florence Investech Limited', 'James Hotels Ltd', 'Jet Infraventure Limited', 'JINDAL SAW LTD.', 'Jenburkt Pharmaceuticals Ltd.', 'C.J. Gelatine Products Ltd.', 'J. L. Morison (India) Limited', 'JATTASHANKAR INDUSTIES LTD.', 'JAYKAY ENTERPRISES LTD.', 'Jindal Stainless Limited', 'Jaysynth Dyestuff India Ltd.', 'JMC PROJECTS (INDIA) LTD.', 'JTL INFRA LTD.', 'Narbada Gems And Jewellery Ltd', 'Jay Ushin Limited', 'JUMBO BAG LTD.', 'SAI JEEVADHARA FINANCE LIMITED', 'JUMBO FINANCE LTD.', 'JBF Industries Limited', 'Jindal Hotels Ltd', 'JSL6.BO', 'Jagson Airlines Ltd.', 'JAICORPLTD6.BO', 'A.J.BROTHERS LTD.', 'JIK INDUSTRIES LTD.', 'LYPSA GEMS & JEWELLERY LTD', 'Josts Engineering Company Ltd', 'Jaihind Synthetics Limited', 'ATLAS JEWELLERY INDIA LIMITED', 'JK TYRE & INDUSTRIES LTD.', 'JAGSONPAL PHARMACEUTICALS LTD.', 'JMD Ventures Limited', 'JAY BHARAT MARUTI LTD.', 'JAGDAMD.BO', 'Joy Realty Ltd', 'JMP CASTINGS LTD.', 'PC JEWELLER LTD.', 'JK PAPER LTD.', 'JMDE PACKAGING & REALTIES LTD.', 'Jai Mata Glass Ltd.', 'JINDAL PHOTO LTD.', 'JK Lakshmi Cement Limited', 'J. TAPARIA PROJECTS LTD', 'JOLLY RIDES LTD.', 'Jiya Eco-Products Limited', 'JISLJALEQS6.BO', 'Shree Jagdambe Paper Mills Ltd.', 'KM Sugar Mills Ltd.', 'Shree Krishna Paper Mills & Industries Ltd.', 'Konark Synthetic, Ltd.', 'SONA KOYO STEERING SYSTEMS LTD', 'Shree Karthik Papers Ltd.', 'Kuwer Industries Limited', 'Kunststoffe Industries', 'Karnataka Bank Ltd.', 'KSK Energy Ventures Limited', 'Kaveri Seed Company Limited', 'Krebs Biochemicals & Industries Ltd', 'Kothari Products Ltd', 'Kotak Mahindra Bank Limited', 'Kopran Limited', 'Koffee Break Pictures Limited', 'KOA Tools India Limited', 'KNR Constructions Limited.', 'KNITWORTH EXPORTS LTD.', 'KLK Electrical Ltd', 'Kirloskar Pneumatic Company Ltd', 'KIRAN SYNTEX LTD.', 'Kilpest India Ltd.', 'Kilburn Office Automation Ltd.', 'Khoday India Limited', 'Khandwala Securities Limited', 'Khaitan (India) Ltd.', 'Kennametal India Limited', 'KENGOLD (INDIA) LTD.', 'Kemp & Co. Ltd', 'KDDL Limited', 'The KCP Limited', 'Kaycee Industries Ltd.', 'Shri Keshav Cements and Infra Limited', 'Katare Spinning Mills Ltd.', 'G.K. Consultants Limited', "Eskay K'n'IT (India) Limited", 'Dai-Ichi Karkaria Limited', 'ABM Knowledgeware Limited', 'Kriti Industries (India) Ltd.', 'KIC Metaliks Ltd.', 'KSL and Industries Ltd', 'CONSORTEX KARL DOELITZCH (INDI', 'Kilburn Chemicals Limited', 'Kaira Can Company Limited', 'KUSHAL TRADELINK LTD', 'KANEL INDUSTRIES LIMITED', 'KANDAGIRI SPINNING MILLS LTD.', 'SpiceJet Limited', 'Reliance Power Limited', 'Warner Multimedia Ltd.', 'Walchand Peoplefirst Limited', 'Transport Corp. of India Ltd.', 'Stanpacks (India) Limited', 'Shree Renuka Sugars Limited', 'Reliance Capital Limited', 'Rain Industries Limited', 'Pratibha Industries Ltd.', 'Polygenta Technologies Limited', 'Olympic Oil Industries Ltd.', 'MPIL Corporation Limited', 'Infosys Limited', 'Indraprastha Medical Corp. Ltd.', 'Zydus Wellness Limited', 'Zenotech Laboratories Limited', 'Yash Papers Limited', 'Wipro Ltd.', 'AYM Syntex Limited', 'Vishal Malleables Ltd.', 'Vardhaman Laboratories Ltd.', 'Vantage Corporate Services Ltd.', 'UT Ltd.', 'Unistar Multimedia Limited', 'Triton Valves Ltd', 'Tricom India Limited', 'Tata Chemicals Limited', 'Sudev Industries Ltd.', 'Sturdy Industries Ltd', 'Spice Islands Apparels Ltd.', 'Softsol India Ltd.', 'Sky Industries Limited', 'Shukra Bullions Ltd.', 'Simplex Projects Ltd.', 'SHUKUN CONSTRUCTION LTD.', 'Shree Cement Limited', 'Radha Madhav Corp. Ltd.', 'Muthoot Capital Services Ltd.', 'MPHASIS6.BO', 'MosChip Semiconductor Technology Limited', 'MCLEOD RUSSEL INDIA LTD.', 'Mafatlal Industries Limited', 'Raj Television Network Ltd.', 'Nile Ltd.', 'Nettlinx Ltd', 'National Peroxide Limited', 'NEW SAGAR TRADING CO.LTD.', 'Sun TV Network Ltd', 'Sri Nachammai Cotton Mills Limited', 'Smartlink Network Systems Limited', 'Pritish Nandy Communications Ltd.', 'NTPC Ltd.', 'Npr Finance Ltd.', 'Nova Iron & Steel Ltd.', 'N2N TECHNOLOGIES LIMITED', 'Nitin Spinners Ltd.', 'Nitco Limited', 'Nirlon Ltd.', 'Niraj Cement Structurals Ltd', 'Nila Infrastructures Ltd', 'NIJJER AGRO FOODS LTD.', 'NIIT Technologies Limited', 'Nihar Info Global Ltd', 'Nidhi Granites Limited', 'N.G. Industries Limited', 'National Fertilizers Ltd.', 'Neyveli Lignite Corporation Limited', 'Monarch Networth Capital Limited', 'Nelcast Limited', 'Neelkanth Rockminerals Ltd.', 'Neelamalai Agro Industries Ltd.', 'Steel Authority of India Limited', 'Unique Organics Ltd.', 'The Tinplate Company Of India Limited', 'Store One Retail India Ltd', 'The Shipping Corporation of India Limited', 'Raj Oil Mills Limited', 'Oxford Industries Ltd', 'OVOBEL FOODS LTD.', 'Oscar Investments Ltd.', 'ORIENT PRESS LTD.', 'ORIENT BELL LIMITED', 'Organic Coatings Ltd.', 'Orchid Pharma Limited', 'Omnitech Infosolutions Limited', 'OMKAR SPECIALITY CHEMICALS LTD', 'Omkar Overseas Ltd', 'Omaxe Ltd.', 'OK Play India Limited', 'Oil India Limited', 'OCL India Limited', 'MARUTI ORGANICS LTD.', 'Lahoti Overseas Limited', 'Indian Oil Corporation Limited', 'Indian Overseas Bank', 'GKB Ophthalmics Ltd', 'Central Bank of India', 'Bang Overseas Ltd.', 'Aksh Optifibre Limited', 'Automobile Corp. of Goa Ltd.', 'Ocean Agro (India) Limited', 'Optimus Finance Limited', 'OXIDES & SPECIALITIES LTD.', 'GULF OIL LUBRICANTS INDIA LTD', 'MCX6.BO', 'ORIENT PAPER & INDUSTRIES LTD.', 'ORNTSYN.BO', 'SBT6.BO', 'ORBIT MULTIMEDIA LTD.', 'BANK OF BARODA', 'MANSINGHKA OIL PRODUCTS LTD.', 'CONCOR4.BO', 'Sahara One Media and Entertainment Limited', 'OPTIEMUS INFRACOM LTD', 'SVOGL Oil Gas And Energy Limit', 'TUBEINVEST6.BO', 'DOLPHIN OFFSHORE ENTERPRISES (', 'Union Quality Plastics Limited', 'Quintegra Solutions Limited', 'QUASAR INDIA LTD', 'QUANTUM BUILD-TECH LTD', 'Quantum Digital Vision India Ltd.', 'Quantum Mutual Fund - Quantum Index Fund', 'QPRO INFOTECH LTD.', 'Quick Heal Technologies Limite', 'Quantum Mutual Fund - Quantum Gold Fund', 'QUADRANT TELEVENTURES LIMITED', 'QUEST SOFTECH (INDIA) LTD', 'Ruchi Strips & Alloys Ltd.', 'Ritesh Properties and Industries Ltd.', 'RFL International Ltd', 'Rapicut Carbides Ltd.', 'Coastal Roadways Limited', 'BSEL Infrastructure Realty Limited', 'SVC Resources Ltd.', 'Sunteck Realty Limited', 'Shree Steel Wire Ropes Ltd.', 'Shree Rajasthan Syntex Ltd.', 'Samkrg Pistons and Rings Limited', 'Ushdev International Limited', 'UPL*', 'Universal Starch Chem Allied Ltd.', 'Universal Prime Aluminium Ltd.', 'Universal Arts Ltd.', 'United Textiles Limited', 'Uni Abex Alloy Products Ltd.', 'Sinnar Bidi Udyog Ltd.', 'Carborundum Universal Limited', 'Vybra Automet Ltd.', 'Vyapar Industries Ltd.', 'VOLTAS6.BO', 'Voltas Ltd.', 'Vivid Global Industries Limited', 'Visagar Polytex Ltd.', 'Virtualsoft Systems Ltd', 'Vinyoflex Ltd.', 'Vijay Solvex Ltd', 'Vesuvius India Limited', 'Venlon Enterprises Limited', 'Venkat Pharma Ltd', 'Veer Energy & Infrastructure Ltd', 'Vardhman Industries Limited', 'Valuemart Info Technologies Ltd.', 'Swasti Vinayaka Synthetics Limited', 'SHIVANI VANASPATI LTD.', 'Royal Cushion Vinyl Products', 'The Lakshmi Vilas Bank Limited', 'IPRU2296.BO', 'Hotel Leelaventure Limited', 'GeeCee Ventures Ltd', 'Barak Valley Cement Ltd.', 'VISHVPRABHA TRADING LTD.', 'Virat Leasing Limited', 'Silicon Valley Infotech Limited', 'Siddha Ventures Ltd', 'JYOTI POLY VINYL LTD.', 'Vikas Granaries Ltd', 'VARDHMAN TEXTILES LIMTED', 'VKJ INFRADEVELOPERS LTD', 'VSF Projects Limited', 'VRL Logistics Limited', 'VIDARBHA IRON & STEEL CORPORAT', 'VINDHYA TELELINKS LTD.', 'VISHVAKIRTI INVESTMENT LTD.', 'Calcom Visions Ltd.', 'VINADITYA TRADING CO.LTD.', 'VST INDUSTRIES LTD.', 'SHREE VINDHYA PAPER MILLS LTD.', 'The Victoria Mills Limited', 'VCU DATA MANAGEMENT LTD', 'HOTELEELA6.BO', 'VBC Industries Ltd.', 'AXONFIN.BO', 'VAIBHAV GLOBAL LTD', 'Vama Industries Ltd.', 'UTTAM VALUE STEELS LTD.', 'VERONICA LABORATORIES LTD.', 'Morgan Ventures Limited', 'VCCL Ltd.', 'Virat Crane Industries Ltd.', 'VXL INSTRUMENTS LTD.', 'VINAYAK VANIJYA LTD.', 'VIMTA LABS LTD.', 'Vaghani Techno-Build Limited', 'VOLGA AIR TECHNICS LTD.', 'VIRALSYN.BO', 'SHREEASHTA6.BO', 'Viaan Industries Limited', 'VIRINCHI PP', 'VORA CONSTRUCTIONS LTD.', 'V2 RETAIL LTD.', 'CHAKAN VEGOILS LTD.', 'Vikram Thermo (India) Ltd', 'TECHNVISION VENTURES LTD.', 'VISION ORGANICS LTD.', 'VENMAX DRUGS AND PHARMACEUTICA', 'VIPCORP.BO', 'DOON VALLEY RICE LTD.', 'AADHAAR VENTURES INDIA LTD.', 'Vippy Spinpro Ltd.', 'VOGUE TEXTILES LTD.', 'Vamshi Rubber Limited', 'VMS INDUSTRIES LTD.', 'VINYL CHEMICALS (INDIA) LTD.', 'VATSA EDUCATIONS LTD.', 'V-Guard Industries Limited', 'VISESH INFOTECNICS LTD.', 'VELVETTE INTERNATIONAL PHARMA', 'SWASTI VINAYAKA ART AND HERITA', 'VHCL INDUSTRIES LTD.', 'VANTEL TECHNOLOGIES LTD.', 'IPRU8496.BO', 'VIMAL OIL & FOODS LTD.', 'VARDHMAN SPECIAL STEELS LTD.', 'VATSA MUSIC LTD.', 'AVTIL ENTERPRISE LTD', 'SOFTRAK VENTURE INVESTMENT LTD', 'PVP Ventures Ltd', 'Tatia Global Venture Ltd.', 'Welcast Steels Ltd.', 'WPIL Limited', 'Wisec Global Limited', 'Winsome Textile Industries Ltd.', 'WINRO COMMERCIAL (INDIA) LTD.', 'Wheels India Limited', 'Welterman International Limited', 'Welspun India Ltd.', 'WABCO INDIA LTD.', 'T Spiritual World Ltd', 'Ram Ratna Wires Ltd', 'India Steel Works Limited', 'Inox Wind Limited', 'Hindustan Tin Works Ltd.', 'First Winner Industries Limited', 'Borosil Glass Works Limited', 'ATLANTSP.BO', 'W W TECHNOLOGY HOLDINGS LTD.', 'WILLIAMSON MAGOR & COMPANY LTD', 'CREATIVE WORLD TELEFILMS LTD.', 'GG Dandekar Machine Works Ltd.', 'WESTERN INDIA COTTONS LTD.', 'Ozone World Limited', 'KRISHNA ENGINEERING WORKS LTD.', 'NEWEVER TRADE WINGS LTD', 'Lakshmi Automatic Loom Works Limited', 'WATERBASE LTD.', 'Hindustan Wires Limited', 'WINY COMMERCIAL AND FISCAL SER', 'WAGEND INFRA VENTURE LIMITED', 'Whirlpool of India Limited', 'WIM PLAST LTD.', 'WEST LEISURE RESORTS LTD', 'WINMORE SILK MILLS LTD.', 'Wintac Ltd.', 'WEIZMANN LTD.', 'WHITE HALL COMMERCIAL CO.LTD.', 'ADOR WELDING LTD.', 'KHATAU MAKANJI SPG.& WVG.CO.LT', 'Wires & Fabriks (S.A.) Limited', 'ACE TOURS WORLDWIDE LTD', 'Welcure Drugs & Pharmaceuticals Ltd.', 'Bombay Talkies Ltd', 'STEEL STRIPS WHEELS LTD.', 'TITAGARH WAGONS LTD.', 'ENKEI WHEELS (INDIA) LTD.', "Today's Writing Instruments Limited", 'WOOLWAYS (INDIA) LTD.', 'Modella Woollens Limited', 'Wanbury Ltd.', 'Winsome Breweries Limited', 'WOPOLIN PLASTICS LTD.', 'Vikas WSP Limited', 'Shalimar Wires Industries Ltd', 'WELSPUN ENTERPRISES LIMTED', 'DOWELLS ELEKTRO WERKE LTD.', 'XPRO INDIA LTD.', 'Excel Glasses Limited', 'FIVE X FINANCE & INVESTMENT LT', 'Saral Mining Limited', 'XCHANGING SOLUTIONS LTD.', 'XL ENERGY LTD.', 'Yuken India Limited', 'Yogi Infra Projects Limited', 'Yes Bank Limited', 'Yashraj Containeurs Ltd', 'Citizen Yarns Limited', 'Andrew Yule & Company Ltd.', 'YURANUS INFRASTRUCTURE LTD', 'YKM INDUSTRIES LTD.', 'Sharad Fibres and Yarn Processors Limited', 'Rishab Special Yarns Limited', 'YAMINI INVESTMENTS COMPANY LTD', 'CT COTTON YARN LTD.', 'YORK EXPORTS LTD.', 'Yash Management and Satellite Ltd.', 'YANTRA NATURAL RESOURCES LTD.', 'YULE FINANCING & LEASING CO.LT', 'Yarn Syndicate Limited', 'YENEPOYA MINERALS & GRANITES L', 'YASH TRADING & FINANCE LTD.', 'SHREE YAAX PHARMA & COSMETICS', 'YESBANK4.BO', 'WINSOME YARNS LTD.', 'Oswal Yarns Ltd.', 'YUVRAJ INTERNATIONAL LTD.', 'YOGI POLYESTERS LTD.', 'YUVRAAJ HYGIENE PRODUCTS LTD.', 'Yogya Enterprises Limited', 'Padam Cotton Yarns Limited', 'Zylog Systems Limited', 'S.V.TRADING & AGENCIES LTD.', 'SARASWATI COMMERCIAL (INDIA) L', 'INDUCON INDIA LTD.', 'ZIGMA SOFTWARE LTD.', 'Binayak Tex Processors Limited', 'SVARAJ TRADING & AGENCIES LTD.', 'SURYODAYA INVESTMENT & TRADING', 'Dhanvantri Jeevan Rekha Ltd', 'Khandelwal Extractions Ltd.', 'GOLD ROCK INVESTMENTS LTD.', 'SOMESHWARA CEMENTS & CHEMICALS', 'ZENITH INFOTECH LTD.', 'ZUARI AGRO CHEMICALS LTD.', 'SATYAM SILK MILLS LTD.', 'Hindustan Zinc Ltd.', 'ZEEMEDIA6.BO', 'ZODIAC-JRD-MKJ LTD.', 'ZILLION PHARMACHEM LTD.', 'ZENTECH*', 'BHILAI ENGINEERING CORPORATION', 'BIHAR AIR PRODUCTS LTD.', 'ZHINDBRE.BO', 'HINDUSTAN HOUSING CO.LTD.', 'SAMPADA CHEMICALS LTD.', 'TRIBHOVANDAS BHIMJI ZAVERI LTD', 'KOVALAM INVESTMENT & TRADING C', 'ROSE ZINC LTD.', 'GAEKWAR MILLS LTD.', 'SWASTIK SAFE DEPOSIT & INVESTM', 'ZENSAR TECHNOLOGIES LTD.', 'ZODIAC CLOTHING CO.LTD.', 'GOLKONDA ENGINEERING ENTERPRIS', 'HINDZINC4.BO', 'Mewat Zinc Ltd.', 'ZENITH COMPUTERS LTD.', 'VVN MFG.& INVESTA LTD.', 'ZENITH EXPORTS LTD.', 'Z.F.STEERING GEAR (INDIA) LTD.', 'MANSOON TRADING CO.LTD.', 'SANCHANA TRADING & FINANCE LTD', 'ZUARI GLOBAL LTD.', 'HEM HOLDINGS & TRADING LTD.', 'ARDI INVESTMENT & TRADING LTD.', 'MULTIPURPOSE TRADING & AGENCIE', 'Zyden Gentec Ltd.', 'JEET MACHINE TOOLS LTD.', 'ZEE ENT*', 'PRABHU STEEL INDUSTRIES LTD.', 'SNEH CONSTRUCTION LTD.', 'Exdon Trading Company Limited', 'ZEE LEARN LTD.', 'CHANAKYA INVESTMENTS LTD.', 'SANMITRA COMMERCIAL LTD.', 'DIGITAL ELECTRONICS LTD.', 'SPEEDAGE COMMERCIALS LTD.', 'BALGOPAL HOLDING & TRADERS LTD', 'ARCO LEASING LTD.', 'SOMAIYA ORGANICS (INDIA) LTD.', 'PARASRAMPURIA POLYAMIDES LTD.', 'ZEE MEDIA CORPORATION LIMITED', 'NIVI TRADING LTD.', 'NILKANTH ENGINEERING LTD.', 'MILGRAY FINANCE & INVESTMENT L', 'AMBIKA SILK MILLS LTD.', 'HIMATSINGKA MOTOR WORKS LTD.', 'SRI CHAKRA FINANCIAL SERVICES', 'ZODIAC VENTURES LIMITED', 'KHATAU EXIM LTD.', 'WARDEN CONSTRUCTION & FINANCE', 'BHAVI INVESTMENTS LTD.', 'GOVIND POY OXYGEN LTD.', 'SOUTHERN GAS LTD.', 'LEENA CONSULTANCY LTD.', 'SARVAMANGAL MERCANTILE CO.LTD.', 'DOLPHIN INVESTMENTS LTD.', 'ZYDUSWELL6.BO', "Planter's Polysacks Limited", 'ZENERGY LTD.', 'ZENITH CAPITALS LTD.', 'Zen Technologies Ltd.', 'ZANDU REALTY LIMITED', 'ZEE ENTERTAINMENT ENTERPRISES', 'SUNRISE ZINC LTD.', 'Zenith Fibres Ltd.', 'HINDUSTHAN UDYOG LTD.', 'SAM-TUL INVESTMENTS LTD.', 'ZEN TECH*', 'ZENITH BIRLA (INDIA) LTD.', 'Parichay Investments Limited', 'SIMCO TRADING & FINANCE CO.LTD', 'ZENITHSTL.BO', 'PESTICIDES & BREWERIES LTD.', 'AARTI DRUGS LTD.', 'AAKAR ENGINEERING & MANUFACTUR', 'CMM BROADCASTING NETWORK LTD.', 'AAGAM CAPITAL LTD.', 'Jainex Aamcol Ltd.', 'AARYA GLOBAL SHARES AND SECURI', 'AASWA TRADING & EXPORTS LTD.', 'AASHEE INFOTECH LTD.', 'Aayush Food And Herbs Limited', 'AAR COMMERCIAL COMPANY LIMITED', 'Aananda Lakshmi Spinning Mills', 'AARTI INDUSTRIES LTD.', 'Aarey Drugs & Pharmaceuticals Ltd.', 'AASHEESH SECURITIES LTD.', 'Aadi Industries Limited', 'AARVEE DENIMS & EXPORTS LTD.', 'Aanchal Ispat Limited', 'ABC Gas (International) Ltd.', 'Aditya Birla Chemicals (India) Limited', 'ABB4.BO', 'ABB India Limited', 'ADITYA BIRLA NUVO LTD.', 'ORIENT ABRASIVES LTD.', 'ABAN OFFSHORE LTD.', 'Starlog Enterprises Limited', 'ABC India Limited', 'VALLEY ABRASIVES LTD.', 'Abirami Financial Services India Ltd', 'ABHISHEK CORPORATION LTD.', 'Abhishek Infraventures Limited', 'ABL Bio-Technologies Ltd.', 'ABC Bearings Ltd.', 'ABACUS COMPUTERS LTD.', 'Abhinav Capital Services Ltd', 'Abhishek Finlease limited', 'Abhinav Leasing & Finance Limi', 'Abhijit Trading Co. Ltd.', 'ABBOTT INDIA LTD.', 'ABG Shipyard Limited', 'ABEE INFO-CONSUMABLES LTD.', 'Aditya Birla Fashion and Retai', 'Acrysil Ltd.', 'EVINIX ACCESSORIES LTD.', 'Action Financial Services India Ltd', 'ACIL Cotton Industries Ltd', 'ACI Infocom Ltd', 'Accurate Transformers Ltd.', 'ACC Limited', 'Allied Computers International (Asia) Ltd.', 'ACE EDUTREND LTD.', 'ACCLAIM INDUSTRIES LIMITED', 'INDIAN ACRYLICS LTD.', 'Acknit Industries Limited', 'ORION ACIDS & CHEMICALS LTD.', 'TREE HOUSE EDUCATION & ACCESSO', 'ACCELYA KALE SOLUTIONS LIMITD', 'Accel Transmatic Ltd.', 'Ace Software Exports Limited', 'AMRAPALI CAPITAL AND FINANCE S', 'ACHAL INVESTMENTS LTD', 'Accentia Technologies, Ltd.', 'Accel Frontline Limited', 'NATAUTO.BO', 'SHREE ACIDS & CHEMICALS LTD.', 'Pasupati Acrylon Ltd.', 'ACC4.BO', 'ACROPETAL TECHNOLOGIES LTD.', 'Action Construction Equipment Ltd', 'ACE MEN ENGG WORKS LIMITED', 'India Motor Parts and Accessories Limited', 'Acrow India Ltd.', 'Acme Resources Limited', 'Adinath Bio-labs Ltd.', 'Hindustan Adhesives Limited', 'ADVANCE METERING TECHNOLOGY LT', 'Advance Petrochemicals Ltd.', 'Advent Computer Services Ltd.', 'Ahluwalia Contracts (India) Limited', 'Adi Rasayan Limited', 'Adarsh Plant Protect Ltd.', 'ADANI ENTERPRISES LTD.', 'MAHAVIR ADVANCED REMEDIES LTD.', 'ADVANCE LIFESTYLES LTD.', 'Adani Transmission Limited', 'SANGAM ADVISORS LTD.', 'SRI ADHIKARI BROTHERS TELEVISI', 'ADCC Infocad Limited', 'ADANIPORTS6.BO', 'Sonal Adhesives Ltd', 'Adhbhut Infrastructure Ltd.', 'NEW MARKETS ADVISORY LTD.', 'ADITYA INFO-SOFT LTD.', 'ADITYA BIRLA MONEY LTD.', 'Advance Powerinfra Tech Ltd', 'ALLIEDDIG*', 'Ador Multiproducts Ltd', 'Adlabs Entertainment Limited', 'ADHARSHILA CAPITAL SERVICES LI', 'PRESSMAN ADVERTISING LIMITED', 'Aditya Forge Ltd', 'Advik Laboratories Ltd.', 'Aditya Spinners Limited', 'ADAM COMSOF LTD.', 'Nikhil Adhesives Ltd.', 'ADARSH MERCANTILE LTD', 'Advanta Limited', 'Adani Power Limited', 'ADD-LIFE PHARMA LTD.', 'GCM CAPITAL ADVISORS LTD', 'ADI FINECHEM LTD.', 'ONELIFE CAPITAL ADVISORS LTD.', 'Adhunik Metaliks Limited', 'ADANI PORTS AND SPECIAL ECONOM', 'ADVANCE MULTITECH LTD.', 'Advanced Micronic Devices Ltd.', 'KJMC CORPORATE ADVISORS (INDIA', 'Adinath Exim Resources Ltd', 'Addi Industries Limited', 'ADVIK INDUSTRIES LIMITED', 'Allied Digital Services Ltd.', 'ADHUNIK INDUSTRIES LTD', 'ADITYPL.BO', 'Navigant Corporate Advisors Li', 'INTELLIVATE CAPITAL ADVISORS L', 'ADF FOODS LTD.', 'Aegis Logistics Limited', 'AEONIAN INVESTMENTS CO.LTD.', 'Taneja Aerospace and Aviation Limited', 'AEGIS LOGIS', 'AEGIS LOGIS*', 'Amba Enterprises Ltd.', 'AEC ENTERPRISES LTD.', 'AFTEK6.BO', 'A.F. ENTERPRISES LTD', 'AFTEK LTD.', 'Basant Agro Tech (India) Limited', 'Teesta Agro Industries Ltd.', 'Prima Agro Limited', 'NAISARGIK AGRITECH (INDIA) LTD', 'Hatsun Agro Product Limited', "Dr. Agarwal's Eye Hospital Limited", 'Amraworld Agrico Ltd.', 'Nagarjuna Agri Tech Ltd', 'Rashel Agrotech Limited', 'AKASH AGENCIES LTD.', 'AGI Infra Limited', 'CRYPTOGEN AGRO INDUSTRIES LTD.', 'NATIONAL STEEL & AGRO INDUSTRI', 'Bell Agromachina Ltd.', 'RATNAMANI AGRO INDUSTRIES LTD', 'Raghuvansh Agrofarms Limited', 'MONESHI AGRO INDUSTRIES LTD.', 'AGRI- TECH (INDIA) LTD', 'Piccadily Agro Industries Limited', 'GRANDMA TRADING & AGENCIES LTD', 'INDOBRIT.BO', 'RAVINDRA TRADING & AGENCIES LT', 'NR Agarwal Industries Ltd', 'Raj Agro Mills Ltd.', 'REI AGRO LTD.', 'SANJIVANI AGRO INDUSTRIES LTD.', 'OSWAL AGRO MILLS LTD.', 'IFB AGRO INDUSTRIES LTD.', 'Bombay Cycle & Motor Agency Ltd.', 'GENERA AGRI CORP LTD.', 'Sanwaria Agro Oils Limited', 'VARUNA AGROPROTEINS LTD.', 'AGRIMONY COMMODITIES LTD', 'TRANS AGRO TECH LTD.', 'NOEL AGRITECH LTD.', 'JAYANT AGRO-ORGANICS LTD.', 'Bambino Agro Industries Ltd.', 'REIAGROLTD6.BO', 'Mukta Agriculture Limited', 'USHER AGRO LTD.', 'AGRI-MARINE EXPORTS LTD.', 'HINDUSTAN AGRIGENETICS LTD.', 'Shri Mahalaxmi Agricultural De', 'GREEN FIRE AGRI COMMODITIES LT', 'SYP AGRO FOODS LTD.', 'Omega Ag-Seeds (Punjab) Ltd.', 'SC Agrotech Limited', 'Dhanuka Agritech Ltd', 'Aries Agro Limited', 'CIAN AGRO IND & INFRA LTD', 'AMBICA AGARBATHIES & AROMA IND', 'Elegant Floriculture & Agrotech (India) Limited', 'BHARAT AGRI FERT & REALTY LTD.', 'AGRO DUTCH INDUSTRIES LTD.', 'AGC NETWORKS LIMITED', 'MUDUNURU LIMITED', 'GALAXY AGRICO EXPORTS LTD.', 'Nagarjuna Agrichem Limited', 'BIRDHI CHAND PANNALAL AGENCIES', 'Parker Agrochem Exports Ltd.', 'SATGURU AGRO INDUSTRIES LTD.', 'Sunil Agro Foods Ltd', 'BHASKAR AGROCHEMICALS LTD.', 'DHARNENDRA AGRO FOOD INDUSTRIE', 'SOUTH EAST AGRO INDUSTRIES LTD', 'AGS INFOTECH LIMITED', 'SHIVA GLOBAL AGRO INDUSTRIES L', 'UNIQUE AGRO PROCESSORS (INDIA)', 'G.D.TRADING & AGENCIES LTD.', 'Gokul Agro Resources Ltd', 'SWARNAJYOTHI AGROTECH & POWER', 'MAYA AGRO PRODUCTS LTD.', 'Pioneer Agro Extracts Ltd', 'Agio Paper & Industries Ltd', 'Saptarishi Agro Industries Limited', 'M. P. Agro Industries Ltd', 'COROMANDEL AGRO PRODUCTS & OIL', 'SC Agrotech Limited', 'Ashiana Agro Industries Ltd.', 'AGRO TECH FOODS LTD.', 'RKB AGRO INDUSTRIES LIMITED', 'NEPC AGRO FOODS LTD.', 'TWIN ROSES TRADES & AGENCIES L', 'VITAN AGRO INDUSTRIES LTD', 'Agarwal Industrial Corporation Ltd', 'KGN AGRO INTERNATIONALS LTD.', 'Naturite Agro Products Limited', 'Simplex Trading & Agencies Ltd.', 'SHRI ANJANEY AGRO FOODS LTD.', 'Archon Industries Limited', 'Ahluwalia Contracts (India) Limited', 'AHURA WELDING ELECTRODE MANUFA', 'ASIAN HOTELS (WEST) LTD.', 'ASIAN HOTELS (EAST) LTD.', 'Ahmedabad Steelcraft Ltd.', 'AIML*', 'ASHAPURA INTIMATES FASHION LTD', 'AIA Engineering Ltd.', 'AIMCO PESTICIDES LTD.', 'A Infrastructure Limited', 'KFA6.BO', 'SUPERIA.BO', 'Kingfisher Airlines Limited', 'Authum Investment & Infrastruc', 'Anubhav Industrial Resources L', 'BHARTIARTL6.BO', 'Patels Airtemp (India) Limited', 'Bharti Airtel Limited', 'ALLIANCE INTEGRATED METALIKS L', 'AIPCL', 'AIL6.BO', 'AI CHAMPDANY INDUSTRIES LTD.', 'Aishwarya Technologies and Telecom Limited', 'Ajmera Realty & Infra India Limited', 'Ajanta Soya Limited', 'Ajel Limited', 'Ajcon Global Services Ltd.', 'Shree Ajit Pulp & Paper limited', 'Shree Ajit Pulp And Paper Ltd.', 'AJANTA PHARMA LTD.', 'Akar Tools Ltd.', 'AKZO NOBEL INDIA LIMITED', 'Akme Star Housing Finance Limi', 'AKZOINDIA6.BO', 'A. K. Capital Services Limited', 'AKAR LAMINATORS LTD.', 'AksharChem India Ltd', 'A.K. Spintex Ltd.', 'AKASHDEEP METAL INDUSTRIES LIM', 'Alpa Laboratories Ltd', 'Alkali Metals Ltd.', 'SHAH ALLOYS LTD.', 'S.A.L. Steel Limited', 'Indian Metals & Ferro Alloys Limited', 'Gujarat Alkalies and Chemicals Limited', 'Ferro Alloys Corp. Ltd.', 'Facor Alloys Ltd.', 'Balasore Alloys Limited', 'Associated Alcohols & Breweries Limited', 'Allsec Technologies Limited', 'Allcargo Logistics Limited', 'Alka Diamond Industries Limited', 'Alfa ICA (India) Ltd.', 'Alembic Ltd.', 'Alchemist Corporation Limited', 'ALLSOFT CORPORATION LTD.', 'Alan Scott Industries Ltd.', 'ALICON CASTALLOY LIMITED', 'Hind Aluminium Industries Ltd', 'ALEMBIC PHARMACEUTICALS LTD.', 'ALSA MARINE & HARVESTS LTD.', 'Bhoruka Aluminium Limited', 'UNI-METAL ALLOYS LTD.', 'Rishabh Digha Steel & Allied Products Ltd.', 'Punjab Alkalies and Chemicals Ltd.', 'ASIAN ALLOYS LTD.', 'ALPICFIN.BO', 'MAAN ALUMINIUM LTD.', 'GYSCOAL ALLOYS LTD.', 'Ashok Alco-Chem Ltd', 'Alfavision Overseas (India) Limited', 'ALLAHABAD BANK', 'NATIONAL ALUMINIUM CO.LTD.', 'BELLARY STEELS & ALLOYS LTD.', 'MAX ALERT SYSTEMS LTD.', 'Alkem Laboratories Limited', 'Tuticorin Alkali Chemicals and Fertilisers Limited', 'ALACRITY HOUSING LTD.', 'KUTCH SALT & ALLIED INDUSTRIES', 'ALPS INFOSYS LTD.', 'ALNA TRADING & EXPORTS LTD.', 'ALLCARGOLO*', 'HARYANA STEEL & ALLOYS LTD.', 'PADMANABH ALLOYS & POLYMERS LT', 'Avonmore Capital & Management Services Limited', 'Alphageo (India) Limited', 'Shri Bajrang Alloys Ltd.', 'ALCHEMIST LTD.', 'RMG ALLOY STEEL LIMITED', 'MAITHAN ALLOYS LTD.', 'ALOK INDUSTRIES LTD.', 'Alora Trading Company Limited', 'Alufluoride Ltd', 'Nicco Uco Alliance Credit Limited', 'ALKYL AMINES CHEMICALS LTD.', 'Nitin Alloys Global Ltd.', 'EUROPEAN SOFTWARE ALLIANCES LT', 'ALANKIT', 'Alka India Ltd.', 'Alka Securities Ltd.', 'CHEMFAB ALKALIS LTD.', 'ALPINE CAPITAL SERVICES LTD.', 'ALPINE HOUSING DEVELOPMENT COR', 'METKORE ALLOYS & INDUSTRIES LT', 'SHRI GANG INDUSTRIES AND ALLIE', 'Camphor & Allied Products Ltd.', 'Golkonda Aluminium Extrusions Limited', 'Alfa Transformers Limited', 'ALPINE INDUSTRIES LTD.', 'Alstone Textiles (India) Ltd', 'Parth Alluminium Limited', 'Sree Rayalaseema Alkalies & Allied Chemicals Ltd.', 'ALBK6.BO', 'Lords Chloro Alkali Limited', 'ALL METAL PROCESS INDUSTRIES L', 'Golkonda Aluminium Extrusions', 'ALOKTEXT6.BO', 'NATIONALUM6.BO', 'ESSDEE6.BO', 'Alpha Graphic India Ltd.', 'ALANG MARINE LTD.', 'ALACRITY SECURITIES LTD', 'Alpha Hi-Tech Fuel Ltd.', 'Piccadily Sugar & Allied Industries Limited', 'ALACRITY ELECTRONICS LTD.', 'Manaksia Aluminium Company Ltd', 'ALEXCON FOAMCAST LTD.', 'Alang Industrial Gases Limited', 'Ranjeev Alloys Ltd', 'ALPS MOTOR FINANCE LTD', 'Allied Herbals Limited', 'SHREE POMANI METALS & ALLOYS L', 'ALPS INDUSTRIES LTD.', 'ALEMBIC LTD*', 'SHREE NARMADA ALUMINIUM INDUST', 'Alchemist Realty Limited', 'CENTRON INDUSTRIAL ALLIANCE LT', 'Albert David Limited', 'GIRDHARILAL SUGAR & ALLIED IND', 'PENNAR ALUMINIUM CO.LTD.', 'KARNAVATI ALFA INTERNATIONAL L', 'SURYODAYA ALLO-METAL POWDERS L', 'ALCOBEX METALS LTD.', 'Parekh Aluminex Limited', 'Deepti Alloy Steel Limited', 'ALERT PETROGAS LTD.', 'BOTHRA METALS & ALLOYS LTD.', 'Alfred Herbert India Ltd.', 'Gujarat Ambuja Exports Limited', 'Amrit Corp. Ltd', 'Ambika Cotton Mills Ltd.', 'Ambalal Sarabhai Enterprises Ltd.', 'AMAR REMEDIES LTD.', 'Amulya Leasing & Finance Ltd.', 'AMALGAMATED ELECTRICITY CO.LTD', 'AMBJELE.BO', 'Amines & Plasticizers Ltd.', 'Amal Ltd', 'Amsons Apparels Limited', 'Appu Marketing & Manufacturing', 'AMRUTANJAN HEALTH CARE LTD.', 'Amradeep Industries Ltd', 'BALAJI AMINES LTD.', 'Ambitious Plastomac Co. Ltd.', 'AMTEKAUTO4.BO', 'Amit Securities Limited', 'Amani Trading & Exports Ltd.', 'SRI AMARNATH FINANCE LIMITED', 'AMIT SPINNING INDUSTRIES LTD.', 'BANNARI AMMAN SUGARS LTD.', 'Amco India Ltd.', 'Amrapali Industries Ltd.', 'AMARAJABAT6.BO', 'Amforge Industries Limited', 'AMBUJA CEMENTS LTD.', 'AMTEKAUTO*', 'SHREE AMBESHWAR PAPER MILLS LT', 'Ambar Protein Industries Limit', 'Amtek Auto Ltd.', 'BANNARI AMMAN SPINNING MILLS L', 'AMARNATH SECURITIES LTD', 'AMARJOTHI SPINNING MILLS LTD.', 'AMARA RAJA BATTERIES LTD.', 'AMI COMPUTERS (I) LTD.', 'APTE AMALGAMATIONS LTD.', 'AMAR6.BO', 'Ambition Mica Limited', 'AMD INDUSTRIES LTD.', 'Indo Amines Ltd.', 'Amrapali Fincap Limited', 'AMISON FOODS LTD.', 'Amit International Ltd.', 'Anuh Pharma Ltd.', 'PUNJAB CHEMICALS AND CROP PROT', 'Pal Credit & Capital Limited', 'Anjani Portland Cement Limited', 'ANSALAPI6.BO', 'Universal Credit and Securities Limited', 'BCL Industries and Infrastruct', 'PINE ANIMATION LIMITED', 'CARE Ratings Limited', 'Indo-Asian Foods and Commodities Limited', 'Premier Energy and Infrastructure Limited', 'SHARANAM INFRAPROJECT AND TRAD', 'Oriental Carbon & Chemicals Limited', 'GOLDEN TOURIST RESORTS AND DEV', 'Ameya Laboratories Ltd', 'Majestic Research Services and', 'Ansal Housing & Construction Ltd.', 'ANSALH*', 'CONFIDENCE FINANCE AND TRADING', 'POOJA ENTERTAINMENT AND FILMS', 'PRISM MEDICO AND PHARMACY LTD.', 'PIPAVAVDOC6.BO', 'Bharati Defence and Infrastruc', 'PANACHE INNOVATIONS LIMITED', 'Southern Magnesium and Chemicals Limited', 'MANGAL CREDIT AND FINCORP LTD.', 'OCL IRON AND STEEL LTD.', 'Poddar Housing and Development', 'RELIANCE DEFENCE AND ENGINEERIN', 'ONGC4.BO', 'ANDHRA CEMENTS LTD.', 'Asahi Infrastructure & Projects Ltd.', 'INTEGRA GARMENTS AND TEXTILES', 'Anant Raj Limited', 'ANANT ROTOSPIN LTD.', 'ANDHRA PETROCHEMICALS LTD.', 'Northlink Fiscal And Capital S', 'JINDAL POLY INVESTMENT AND FIN', 'Rajputana Investment and Finan', 'PECOS Hotels And Pubs Limited', 'PARTH HOUSING AND ESTATE DEVEL', 'Anka India Ltd', 'Crest Animation Studios Limited', 'Anjani Synthetics Ltd.', 'Ansal Buildwell Ltd.', 'ANDHRA SUGARS LTD.', 'VETO SWITCHGEARS AND CABLES LI', 'IL&FS ENGINEERING AND CONSTRUC', 'Lotus Eye Hospital and Institute Limited', 'Nishtha Finance And Investment', 'DALMIA BHARAT SUGAR AND INDUST', 'Mangalore Refinery and Petrochemicals Limited', 'HITACHI HOME AND LIFE SOLUTION', 'B L Kashyap & Sons Limited', 'STANDARD SHOE SOLE AND MOULD (', 'Corporate Courier and Cargo Ltd', 'SHUBHRA LEASING FINANCE AND IN', 'SANGHVI FORGING AND ENGINEERIN', 'Shivkrupa Machineries and Engi', 'SURANA TELECOM AND POWER LIMIT', 'Kashiram Jain and Company Limi', 'TGBHOTELS6.BO', 'The Sandur Manganese & Iron Ores Limited', 'Anjani Finance Ltd.', 'P.C.I.CHEMICALS AND PHARMACEUT', 'CHOLAMANDALAM INVESTMENT AND F', 'Krishna Capital And Securities', 'Andhra Bank', 'TINNA RUBBER AND INFRASTRUCTUR', 'MISHKA FINANCE AND TRADING LTD', 'Lynx Machinery & Commercials Ltd', 'ANKIT METAL & POWER LTD.', 'Junction Fabrics and Apparels', 'Eldeco Housing and Industries Limited', 'STAR FERRO AND CEMENT LTD', 'ANS INDUSTRIES LTD', 'Geetanjali Credit And Capital', 'ANDHRA PRADESH TANNERIES LTD.', 'Anshuni Commercials Limited', 'Fraser And Company Limited', 'ANAND PROJECTS LTD', 'RAM MINERALS AND CHEMICALS LIM', 'S H Kelkar and Company Limited', 'Anna Infrastructure Ltd', 'SAI BABA INVESTMENT AND COMMER', 'Anubhav Infrastructure Limited', 'WINSOME DIAMONDS AND JEWELLERY', 'ANUGRAHA JEWELLERS LTD.', 'NEXTGEN ANIMATION MEDIAA LTD.', 'ANGELS ENTERPRISES LTD', 'CYBERTECH SYSTEMS AND SOFTWARE', 'SOUTHERN ISPAT AND ENERGY LTD', 'Kothari Fermentation & Biochem Limited', 'CITADEL REALTY AND DEVELOPERS', 'ATLANTA INFRASTRUCTURE AND FIN', 'ANSAL PROPERTIES & INFRASTRUCT', 'RAGHAVA ESTATES AND PROPERTIES', 'ANAND CREDIT LTD.', 'Sutlej Textiles and Industries Ltd.', 'Anil Special Steel Industries Ltd.', 'Shri Niwas Leasing and Finance', 'WELSPUN INVESTMENTS AND COMMER', 'ANKUR DRUGS & PHARMA LTD.', 'KOTIA ENTERPRISES LTD', 'Ankush Finstock Ltd.', 'KDJ HOLIDAYSCAPES AND RESORTS', 'ANUP MALLEABLE LTD.', 'Boston Leasing and Finance Ltd', 'LLOYDS METALS AND ENERGY LTD.', 'SUN AND SHINE WORLDWIDE LTD.', 'ANSHUS CLOTHING LTD.', 'Decorous Investment and Tradin', 'ANISHA IMPEX LTD', 'ANG INDUSTRIES LIMITED', 'TECHNO ELECTRIC AND ENGINEERIN', 'INDAGE RESTAURANTS AND LEISURE', 'ANAR INDUSTRIES LTD.', 'COUNTRY CLUB HOSPITALITY AND H', 'Filtra Consultants and Enginee', 'ANANTHI CONSTRUCTIONS LTD.', 'ANIL LTD.', 'TGB BANQUETS AND HOTELS LTD.', 'Devki Leasing & Finance Ltd', 'Anik Industries Limited', 'BOSTON EDUCATION AND SOFTWARE', 'APTECH LTD.', 'APOLLOHOSP4.BO', 'Partani Appliances Limited', 'Apoorva Leasing Finance & Inve', 'PHELIX APPLIANCES LTD.', 'APAR INDUSTRIES LTD.', 'SHIVAM APPERALS EXPORT LTD.', 'APL APOLLO TUBES LTD.', 'APOLLOTYRE*', 'Apollo Hospitals Enterprise Ltd.', 'APLAB Ltd.', 'GUJARAT APOLLO INDUSTRIES LTD.', 'APPLE CREDIT CORPORATION LTD.', 'INTERNATIONAL PAPER APPM LIMIT', 'APTECHT6.BO', 'Apple Finance Limited', 'APCOTEX INDUSTRIES LTD.', 'APIS INDIA LTD.', 'APT PACKAGING LTD.', 'APTECHLTD*', 'Apollo Tyres Ltd.', 'Apunka Invest Commercial Limit', 'Aplaya Creations Limited', 'Ras Resorts & Apart Hotels Ltd', 'APEX INTERTECH LTD.', 'GUJARAT APOLLO INDUSTRIES LTD.', 'APCOTEX IND*', 'HARIA APPARELS LTD', 'BUTTERFLY GANDHIMATHI APPLIANC', 'APM Industries', 'HINDUSTAN APPLIANCES LTD.', 'Panasonic Appliances India Company Limited', 'OXEMBERG APPARELS LTD.', 'Apollo Finvest (India) Limited', 'E-Land Apparel Limited', 'MAHA RASHTRA APEX CORPORATION', 'Datasoft Application Software India Ltd.', 'AQUA LOGISTICS LTD', 'RUIA AQUACULTURE FARMS LTD.', 'TKNOMIN.BO', 'SUVARNA AQUA FARM & EXPORTS LT', 'GUJARAT AQUA INDUSTRIES LTD.', 'SHANTANU SHEOREY AQUAKULT LTD.', 'AQUA PUMPS INFRA VENTURES LTD', 'AQUA6.BO', 'Baba Arts Ltd.', 'Arvind Remedies Ltd', 'Arshiya Ltd', 'Arrow Textiles Ltd.', 'Aroni Commercials Limited', 'Arms Paper Ltd', 'Archies Ltd.', 'Archidply Industries Limited', 'Arcee Industries Ltd.', 'ARNAV CORPORATION LTD.', 'Artefact Projects Ltd', 'Aryaman Financial Services Limited', 'ARCHIT ORGANOSYS LTD.', 'Arcotech Ltd', 'ARIHANT TOURNESOL LTD.', 'ARO GRANITE INDUSTRIES LTD.', 'ARNOLD HOLDINGS LTD', 'ARIHANT THREADS LTD.', 'AROMA ENTERPRISES (INDIA) LTD.', 'Arrow Greentech Limited', 'ARO GRANITE*', 'Arcuttipore Tea Co Ltd', 'ARAMUSK INFRASTRUCTURE INVESTM', 'ARIHANT6.BO', 'ARVIND SMARTSPACES LTD', 'ARIHANT MANGAL GROWTH SCHEME-C', 'AROCHEM SILVASSA LTD.', 'ARIHANT INDUSTRIES LTD.', 'ARSS Infrastructure Projects Limited', 'ARUN PROCESSORS LTD.', 'Arihant Capital Markets Limited', 'Arvind Limited', 'Arman Financial Services Ltd', 'Artson Engineering Ltd.', 'ARUNA HOTELS LTD.', 'MUKTA ART PP', 'EMKAY AROMATICS LTD.', 'Mukta Arts Ltd', 'ARCHIES6.BO', 'Artech Power & Trading Limited', 'THIRU AROORAN SUGARS LTD.', 'ARIHANTCOT.BO', 'INTELLECT DESIGN ARENA LIMITED', 'ARLABS(80NC)', 'ARTILLEGENCE BIO-INNOVATIONS L', 'ARCHANA S PP', 'Arihant Avenues & Credit Limited', 'ARIHANT FOUNDATIONS & HOUSING', 'dynamic Archistructures Limite', 'Aryaman Capital Markets Limite', 'ARUNODAY MILLS LTD.', 'Arfin India Limited', 'Arvind International Ltd.', 'Aravali Securities & Finance Ltd.', 'GILLANDERS ARBUTHNOT & CO.LTD.', 'ARIHANT SUPERSTRUCTURES LIMITE', 'RAJDARSHAN INDUSTRIES LTD.', 'ARLABS.BO', 'ARHAT INDUSTRIES LTD.', 'GUJARAT ARTH LTD.', "Arihant's Securities Limited", 'ARMAN HOLDINGS LTD', 'SRI ARUMUGA ENTERPRISE LIMITED', 'ARCHANA SOFTWARE LTD.', 'ARIS INTERNATIONAL LTD.', 'ARNMNTX.BO', 'ASIS LOGISTICS LIMITED', 'Shriram Asset Management Company Ltd', 'Indo Asia Finance Limited', 'AstraZeneca Pharma India Limited', 'Asian Paints Limited', 'Tridev InfraEstates Ltd', 'Ashirwad Steels & Industries Ltd.', 'Ashok Leyland Limited', 'Ashish Polyplast Ltd', 'Ashiana Ispat Ltd', 'Automotive Stampings & Assemblies Ltd.', 'Bengal & Assam Company Ltd.', 'Asian Petroproducts & Exports Limited', 'ASYA INFOSOFT LIMITED', 'ASBUSIN.BO', 'ASHIKA CREDIT CAPITAL LTD.', 'Ashnoor Textile Mills Ltd.', 'ASSAMBROOK LTD.', 'Asit C Mehta Financial Services Limited', 'Asian Granito India Limited', 'Asian Tea & Exports Ltd.', 'ASSAM PETROCHEMICALS LTD.', 'ASTRA MICROWAVE PRODUCTS LTD.', 'ASIA PACK LTD.', 'ASHAPURA MINECHEM LTD.', 'Ashram Online.com Ltd.', 'ASIAN FERTILIZERS LTD.', 'Assam Company India Ltd', 'Ashirwad Capital Limited', 'Astral Poly Technik Limited', 'GOYAL ASSOCIATES LTD.', 'Astec LifeSciences Limited', 'ASCENT EXIM (INDIA) LTD.', 'ASIAN VEGPRO INDUSTRIES LTD.', 'EURO ASIA EXPORTS LTD.', 'SHRI ASTER SILICATES LIMITED', 'ASSOCIATED MARMO & GRANITES LT', 'ASHIMA LTD.', 'ASSOCIATED CERAMICS LTD.', 'ASEEM GLOBAL LTD.', 'ASHOKLEY4.BO', 'ASEAN INDUSTRIAL STRUCTURES LT', 'EIH ASSOCIATED HOTELS LTD.', 'SUNRISE ASIAN LIMITED', 'ASAHI SONGWON COLORS LTD.', 'ASIA CAPITAL LIMITED', 'ASIAN ELECTRONICS LTD.', 'ASIAN FOOD PRODUCTS LTD.', 'Ashoka Refineries Limited', 'Associated Stone Industries (Kotah) Ltd.', 'Trans Asia Corporation Ltd', 'ASAHI INDIA GLASS LTD.', 'ASHCO NIULAB INDUSTRIES LTD.', 'OJAS ASSET RECONSTRUCTION COMP', 'ASHOKA BUILDCON LTD.', 'ASIAN FLORA LTD.', 'SHREE ASHTAVINAYAK CINE VISION', 'ASHIANA HOUSING LTD.', 'SOUTH ASIAN MUSHROOMS LTD.', 'ASIAN FILMS PRODUCTION & DISTR', 'ASM Technologies Ltd.', 'ASAHI INDUSTRIES LIMITED', 'ASAHIINDIA6.BO', 'ASIAN HOTELS (NORTH) LIMITED', 'South Asian Enterprises Limited', 'ASUTOSH ENTERPRISES LTD.', 'ASIAN BEARINGS LTD.', 'ASHOKA COTSEEDS LTD.', 'Asian Oilfield Services Ltd.', 'Asian Star Company Limited', 'SANGHVI ASBESTOS CEMENTS LTD.', 'ATV Projects India, Ltd.', 'Atharv Enterprises Limited', 'ATN INTERNATIONAL LTD.', 'Atishay Limited', 'Athena Constructions Limited', 'ATHENA FINANCIAL SERVICES LTD.', 'Atlanta Ltd.', 'ATLAS CYCLES (HARYANA) LTD.', 'Atul Auto Limited', 'ATCOM TECHNOLOGIES LTD.', 'Athena Global Technologies Limited', 'ATUL LTD.', 'ATLANTA DEVCON LIMITED', 'Athena Global Technologies Lim', 'Automotive Axles Ltd.', 'Porwal Auto Components Ltd', 'Lumax Auto Technologies Limited', 'Aurangabad Paper Mills Limited', 'PPAP Automotive Limited', 'HIRA AUTOMOBILES LTD.', 'GS Auto International Limited', 'Kailash Auto Finance Ltd', 'AUTOPAL IND', 'AUTORIDERS INTERNATIONAL LTD.', 'Brakes Auto (India) Limited', 'SWARAJ AUTOMOTIVES LIMITED', 'AUTOLITE (INDIA) LTD.', 'Avantel Ltd', 'Avance Technologies Limited', 'Available Finance Ltd', 'Avon Corporation Ltd', 'AVANTI FEEDS LTD.', 'AVI Photochem Ltd', 'AVANTEL*', 'AVON INDUSTRIES LTD.', 'InterGlobe Aviation Limited', 'Aviva Industries Limited', 'AVT Natural Products Limited', 'Avon Lifesciences Limited', 'AVINASH INFORMATION TECHNOLOGI', 'AVON MERCANTILE LTD.', 'AVONMORE CAPITAL & MANAGEMENT', 'Avon Lifesciences Limited', 'Avi Polymers Ltd.', 'AVANTE LTD*', 'Axtel Industries Ltd', 'Axel Polymers Ltd', 'Wheel & Axle Textiles Ltd', 'AXIS MUTUAL FUND - AXIS GOLD E', 'AXISCADES', 'Elixir Capital Limited', "Omni Ax's Software Limited", 'AXIS RAIL INDIA LTD', 'AXIS Bank Limited', 'Axon Ventures Limited', 'AYM Syntex Limited', 'Kerala Ayurveda Ltd.', 'AYEPEE LAMITUBES LTD.', 'AYOKI MERCANTILE LTD.', 'AZURE EXIM SERVICES LTD.', 'IDBI Bank Limited', 'Bartronics India Limited', 'Bajaj Corp Limited', 'Ind. Bank Housing Ltd', 'Balmer Lawrie Investments Limited', 'Batliboi Ltd.', 'BASF India Limited', 'Banswara Syntex Ltd.', 'Balurghat Technologies Ltd.', 'Balrampur Chini Mills Limited', 'Bala Techno Global Ltd.', 'Bagadia Colourchem Ltd.', 'Corporation Bank', 'MYSOREBANK6.BO', 'State Bank of Travancore', 'FEDERALBNK6.BO', 'Rathi Bars Limited', 'BALRAMCHIN6.BO', 'BANK OF INDIA', 'BASF6.BO', 'Baid Leasing & Finance Co Ltd', 'BANSAL ROOFING PRODUCTS LTD', 'BANARAS BEADS LTD.', 'BALAJI INDUSTRIAL CORPORATION', 'IDFC Bank Limited', 'BALKRISHNA INDUSTRIES LTD.', 'Indian Bank', 'BAFNA SPINNING MILLS & EXPORTS', 'BANSISONS TEA INDUSTRIES LTD.', 'Goldman Sachs Mutual Fund - Goldman Sachs Banking Index Exchange Traded Scheme', 'Bampsl Securities Ltd.', 'Bharat Bijlee Limited', 'BOMBAY BURMAH TRADING CORP.LTD', 'B&B REALTY LIMITED', 'BCL FORGINGS LTD.', 'BCL Enterprises Limited', 'Hemang Resources Limited', 'B.C. POWER CONTROLS LTD', 'BHANOT CONSTRUCTION & HOUSING', 'PYXIS FINVEST LIMITED', 'BALRAMCHIN*', 'Bcc Fuba India Ltd', 'BDH Industries Ltd.', 'Somi Conveyor Beltings Ltd.', 'SNL Bearings Ltd.', 'Gajra Bevel Gears Ltd.', 'Fag Bearings India Ltd.', 'Deccan Bearings Ltd', 'BESCO LTD.', 'Beryl Drugs Ltd.', 'Berger Paints India Limited', 'Bhansali Engineering Polymers Ltd.', 'BEML Limited', 'Bemco Hydraulics Ltd.', 'Beckons Industries Ltd.', 'Beeyu Overseas Ltd.', 'BETEX INDIA LTD.', 'Ganesh Benzoplast', 'TATAGLOBAL4.BO', 'Beekay Niryat Limited', 'BELAPUR INDUSTRIES LTD.', 'ARAMBHAN HOSPITALITY SERVICES L', 'Menon Bearings Ltd.', 'UNION BEARINGS (INDIA) LTD.', 'BEE ELECTRONIC MACHINES LTD.', 'Manpasand Beverages Limited', 'BENTLEY COMMERCIAL ENTERPRISES', 'Bimetal Bearings Limited', 'NRB INDUSTRIAL BEARINGS LTD.', 'Benzo Petro International Ltd.', 'Beekay Steel Industries Ltd.', 'SHRAM BEARIN', 'BETA-KAPPA INVESTMENTS LTD.', 'GRAPHIC CHARTS LTD.', 'TALWALKARS BETTER VALUE FITNES', 'Bengal Tea & Fabrics Ltd.', 'BEDMUTHA INDUSTRIES LTD.', 'NRB BEARINGS LTD.', 'TATA GLOBAL BEVERAGES LIMITED', 'SHREE BENZOPHEN INDUSTRIES LTD', 'SHRIRAM BEARINGS LTD.', 'Best Eastern Hotels Ltd.', 'BETALA GLOBAL SECURITIES LTD.', 'Bella Casa Fashion & Retail Li', 'BENGAL STEEL INDUSTRIES LTD.', 'BFL Developers Limited.', 'Bangalore Fort Farms Limited', 'BF INVESTMENT LTD.', 'BF UTILITIES LTD.', 'BHARATIYA GLOBAL INFOMEDIA LTD', 'BGR Energy Systems Limited', 'Bgil Films & Technologies Limited', 'BIO GREEN PAPERS LTD', 'Bhagwati Autocast Ltd.', 'Bharat Petroleum Corp. Ltd.', 'Bhartiya International Ltd.', 'Bhilwara Tex-Fin Ltd.', 'Bhilwara Spinners Ltd.', 'Bheema Cements Ltd', 'Bharat Seats Ltd.', 'Bhandari Hosiery Exports Ltd.', 'Bhageria Industries Limited', 'BHAGHEERATHA ENGINEERING LTD.', 'MCNALLY BHARAT ENGINEERING COM', 'Shri Bholanath Carpets Limited', 'Bhagyashree Leasing & Finance Ltd', 'Hathway Bhawani Cabletel and Datacom Ltd.', 'BHAGYANAGAR INDIA LTD.', 'BHOR INDUSTRIES LTD.', 'BHARTI INFRATEL LTD.', 'BHAGYODAYA INFRASTRUCTURE DEVE', 'Shree Bhavya Fabrics Limited', 'BHARAT LINE LTD.', 'DALMIA BHARAT LTD.', 'BHARAT RASAYAN LTD.', 'BHANDERI INFRACON LTD', 'BHAGWATI OXYGEN LTD.', 'Bhageria Industries Limited', 'NAVA BHARAT VENTURES LTD.', 'Bharat Bhushan Finance & Commodity Brokers Ltd.', 'Bhagawati Gas Ltd', 'Shree Bhawani Paper Mills Ltd.', 'BHAGWATI COTTONS LTD.', 'Tamilnadu Jai Bharath Mills Ltd.', 'Bhagwandas Metals Ltd.', 'BHEL6.BO', 'BHARTISHIP.BO', 'HATHWAY BHAWANI CABLETEL & DAT', 'BHARAT TEXTILES & PROOFING IND', 'BHUSHAN STEEL LTD.', 'SHRI BHAGAVATI BRIGHT BARS LTD', 'BHAGYA INL*', 'BHUVAN TRIPURA INDUSTRIES LTD.', 'Bhuwalka Steel Industries Limited', 'Bharat Wire Ropes Limited', 'Bharat Immunologicals & Biologicals Corp. Ltd.', 'Bhagiradha Chemicals & Industries Ltd.', 'BHARAT GEARS LTD.', 'BILCONTI.BO', 'Bhilwara Technical Textiles Ltd', 'BHUPENDRAIND', 'Bharat Forge Limited', 'BHUSANSTL6.BO', 'Shivalik Bimetal Controls Limited', 'Birla Cotsyn (India) Limited', 'TRINITY BIO-TECH LTD.', 'Transgene Biotek Ltd.', 'Tasty Bite Eatables Ltd.', 'Sterling Biotech Limited', 'Sharon Bio Medicine Limited', 'Saamya Biotech (India) Limited', 'Panacea Biotec Ltd.', 'Hindustan Bio Sciences Ltd.', 'Gufic Biosciences Ltd.', 'BIRMINGHAM THERMOTECH LTD.', 'Biopac India Corp. Ltd.', 'Birla Sun Life Mutual Fund', 'BLUE BIRD (INDIA) LTD.', 'Bisil Plast Limited', 'BILCARE6.BO', 'INDO BIOTECH FOODS LTD.', 'BIL ENERGY SYSTEMS LTD.', 'Indrayani Biotech Limited', 'GENOMICS BIOTECH LTD.', 'Titan Biotech Limited', 'Birla Sun Life Mutual Fund', 'HPC BIOSCIENCES LTD.', 'BIHAR FOUNDRY & CASTINGS LTD.', 'BIRLA SUN LIFE MUTUAL FUND- BI', 'SOCRUS BIO SCIENCES LIMITED', 'Birla Transasia Carpets Limited', 'Binny Limited', 'Medicamen Biotech Ltd.', 'BIRLA PACIFIC MEDSPA LTD.', 'ESTEEM BIO ORGANIC FOOD PROCES', 'PANACEA BIO*', 'Birla Sun Life Mutual Fund', 'Oswal Greentech Limited', 'CITURGIA BIOCHEMICALS LTD.', 'JUPITER BIOSCIENCE LTD.', 'BIRLA SUN LIFE MUTUAL FUND- BI', 'Gujarat Themis Biosyn Ltd.', 'BIRLA SUN LIFE MUTUAL FUND- B', 'Birla Sun Life Mutual Fund', 'SHEETAL BIO-AGRO TECH LTD.', 'Birla Sun Life Mutual Fund', 'BIOFIL CHEMICALS & PHARMACEUTI', 'BIRLA SUN LIFE MUTUAL FUND- B', 'BIRLA SUN LIFE MUTUAL FUND- BI', 'VIVO BIO TECH LTD.', 'Birla Precision Technologies Ltd', 'KDL BIOTECH LTD.', 'Birla Sun Life Mutual Fund', 'KOLAR BIOTECH LTD.', 'BIRLA CORPORATION LTD.', 'BINNY MILLS LTD.', 'Birla Sun Life Mutual Fund', 'BIJOY HANS LTD.', 'Birla Sun Life Mutual Fund', 'SHREEKRISHNA BIOTECH LTD.', 'Birla Sun Life Mutual Fund', 'Birla Shloka Edutech Ltd', 'BIOWIN.BO', 'Birla Power Solutions Limited', 'BOSTON BIO SYSTEMS LTD.', 'CHEMCEL BIO-TECH LTD.', 'Synergy Bizcon Limited', 'Birla Sun Life Mutual Fund', 'Birla Sun Life Mutual Fund', 'Birla Sun Life Mutual Fund', 'BIL INDUSTRIES LTD.', 'Riddhi Siddhi Gluco Biols Limited', 'TULASEE BIO-ETHANOL LTD.', 'Brawn Biotech Limited', 'OCEANAA BIOTEK INDUSTRIES LTD', 'Birla Capital & Financial Services Limited', 'Camson Bio Technologies Limited', 'BONANZA BIOTECH LTD.', 'Celestial Biolabs Ltd.', 'Birla Sun Life Mutual Fund', 'Mavens Biotech Limited', 'BRONZE INFRA-TECH LTD.', 'BILATI (ORISSA) LTD.', 'Birla Sun Life Mutual Fund', 'Bits Ltd.', 'BIJLEE TEXTILES LTD.', 'GBL INDUSTRIES LIMITED', 'Biocon Limited', 'INDO-FRENCH BIOTECH ENTERPRISE', 'Bilcare Ltd.', 'Birla Sun Life Mutual Fund', 'SBBJ6.BO', 'Birla Sun Life Mutual Fund', 'BILPOWER LTD.', 'NATH BIO-GENES (INDIA) LTD', 'GENOMIC VALLEY BIOTECH LIMITED', 'Bihar Sponge Iron Ltd.', 'BIRLA SUN LIFE MUTUAL FUND - B', 'VALPLUS BIOTECH LTD.', 'BIRLA SUN LIFE MUTUAL FUND- BI', 'Vivanza Biosciences Limited', 'Shree Ganesh Biotech (India) L', 'Southern Online Bio Technologies Ltd.', 'BINANI INDUSTRIES LTD.', 'CLASSIC BIOTECH & EXPORTS LTD.', 'Gayatri BioOrganics Limited', 'BIRLA SUN LIFE MUTUAL FUND - B', 'DSQ BIOTECH LTD.', 'BINACA SYNTHETIC RESINS LTD.', 'DOCTORS BIOTECH INDIA LTD.', 'BIRLA SUN LIFE MUTUAL FUND - B', 'B.K.DUPLEX BOARD LTD.', 'BKV Industries Ltd.', 'Bliss Gvs Pharma Limited', 'Blue Chip Tex Industries Ltd', 'Blue Blends (India) Ltd.', 'BLS Infotech Ltd.', 'BLCISER6.BO', 'BLUE CIRCLE SERVICES LTD.', 'BLUE PEARL TEXSPIN LIMITED', 'DSP BlackRock Mutual Fund', 'BLUBLEND IND', 'BLUE BLENDS', 'DSP BlackRock Mutual Fund', 'Bloom Dekor Limited', 'Blue Cloud Softech Solutions L', 'DSP BlackRock Mutual Fund', 'Bluechip Stockspin Ltd.', 'BLAZON MARBLES LIMITED', 'BALAJI GALVANISING INDUSTRIES', 'BLUE COAST HOTELS LTD.', 'Bloom Industries Limited', 'DSP BlackRock Mutual Fund', 'BLUE BLENDS', 'Black Rose Industries Ltd', 'BLUE STAR LTD.', 'BLUESTARCO6.BO', 'Blue Dart Express Ltd.', 'Blueblood Ventures Limited', 'BLUE CHIP INDIA LTD.', 'PHILLIPS CARBON BLACK LTD.', 'BLB LTD.', 'NCC BLUE WATER PRODUCTS LTD.', 'Blue Star Infotech Ltd.', 'BLUEDART6.BO', 'SHREE SALASAR INVESTMENT LTD.', 'BMB Music & Magnetics Limited', 'BNK Capital Markets Ltd.', 'B.nanji Enterprises Ltd', 'BNR Udyog Ltd.', 'BN Rathi Securities Ltd.', 'B&A Ltd.', 'GEOJIT BNP PARIBAS FINANCIAL S', 'Bombay Rayon Fashion Limited', 'Borax Morarji Limited', 'SAURASHTRA PAPER & BOARD MILLS', 'BOSCH LTD.', 'BOSCHLTD4.BO', 'CREWBOS6.BO', 'UV Boards Ltd.', 'VICTORY PAPER & BOARDS (INDIA)', 'Crew B.O.S. Products Limited', 'Bombay Swadeshi Stores Ltd.', 'Indo Borax & Chemicals Ltd.', 'Indo Bonito Multinational Ltd.', 'BOSCH LTD*', 'Bodal Chemicals Ltd.', 'BOSTON TEKNOWSYS (INDIA) LTD', 'Bonanza Industries Limited', 'Gujarat Borosil Limited', 'SESHASAYEE PAPER & BOARDS LTD.', 'BOROSIL*', 'Bodhtree Consulting Limited', 'Prag Bosimi Synthetics Ltd.', 'BOMBAY POTTERIES & TILES LTD.', 'NEPC PAPER & BOARD LTD.', 'BOBSHELL ELECTRODES LTD.', 'GENUS PAPER & BOARDS LIMITED', 'BOMBAY DYEING & MFG.CO.LTD.', 'BOMBAY WIRE ROPES LTD.', 'COMMERCIAL ENGINEERS & BODY BU', 'BRFL6.BO', 'Bombay Oxygen Corporation Limited', 'BPL Limited', 'B. P. CAPITAL LTD', 'Broadcast Initiatives Ltd.', 'Brigade Enterprises Ltd.', 'Bridge Securities Limited', 'Brady & Morris Engineering Company Limited', 'INDIAN BRIGHT STEEL CO.LTD.', 'GM Breweries Ltd', 'UBL6.BO', 'BRITANNIA6.BO', 'UNITED BREWERIES (HOLDINGS) LT', 'SUNBRIGHT STOCK BROKING LTD.', 'TV18 BROADCAST LTD.', 'KIRLOSKAR BROTHERS LTD.', 'CHASE BRIGHT STEEL LTD.', 'Brahmanand Himghar Ltd.', 'GLOBAL FILMS & BROADCASTING LT', 'Kohinoor Broadcasting Corporation Ltd.', 'SBI ETF BSE 100 ETF', 'BSL Limited', 'BS LTD.', 'BSI LTD.', 'Martin Burn Ltd', 'BUDGE BUDGE COMPANY LIMITED', 'NBCC (India) Limited', 'GUJARAT BULK PACKS LTD.', 'KMF Builders & Developers Ltd', 'BURR BROWN I', 'GYAN DEVELOPERS & BUILDERS LTD', 'DHENU BUILDCON INFRA LTD.', 'Vijay Shanthi Builders Limited', 'Navkar Builders Ltd.', 'Goenka Business & Finance Limi', 'EAST BUILDTECH LTD.', 'Inanna Fashion and Trends Limited', 'Pennar Engineered Building Sys', 'Sawaca Business Machines Limited', 'SIDDARTH BUSINESSES LTD', 'ERA BUILDSYS LIMITED', 'PATIDAR BUILDCON LIMITED', 'Burnpur Cement Ltd.', 'BWL LTD.', 'S P Capital Financing Ltd.', 'Solid Carbide Tools Ltd', 'SMIFS Capital Markets Limited', 'Marvel Capital & Finance (India) Ltd.', 'Indo Credit Capital Ltd', 'Gogia Capital Services Ltd.', 'EXCEL CASTRONICS LIMITED', 'Emgee Cables & Communications Ltd', 'Dhruva Capital Services Ltd.', 'Centrum Capital Limited', 'Cat Technologies Ltd.', 'Carnation Industries Limited', 'CAPRICORN SYSTEMS GLOBAL SOLUT', 'Caplin Point Laboratories Ltd', 'Capital Trust Ltd.', 'Cairn India Limited', 'KOKUYO CAMLIN LTD.', 'Nahar Capital and Financial Services Limited', 'SANGAM HEALTH CARE PRODUCTS LT', 'KM CAPITAL LTD.', 'Gujarat Carbon & Industries Ltd.', 'CAPITAL FIRST LTD.', 'CCL PRODUCTS (INDIA) LTD.', 'CCL International Limited', 'Consolidated Construction Consortium Limited', 'CCS Infotech Ltd.', 'CLASSIC GLOBAL FINANCE & CAPIT', 'CDI International Limited', 'CDR MEDICAL INDUSTRIES LTD.', 'CDR HEALTH CARE LTD.', 'Prism Cement Limited', 'ITD Cementation India Limited', 'Idea Cellular Ltd.', 'Panyam Cements & Mineral Industries Ltd.', 'The Central Provinces Railways Company Limited', 'Celebrity Fashions Limited', 'Ceejay Finance Ltd.', 'UDAIPUR CEMENT WORKS LTD.', 'KAJARIA CERAMICS LTD.', 'MANGALAM CEMENT LTD.', 'SOMANI CEMENT COMPANY LTD.', 'PANCHAMAHAL CEMENT LTD.', 'GUJARAT SIDHEE CEMENT LTD.', 'Century Textiles and Industries Limited', 'Euro Ceramics Ltd.', 'TRINETRA CEMENT LTD.', 'CENTURY PLYBOARDS (I) LTD.', 'CEETA INDUSTRIES LTD.', 'Shiva Cement Ltd.', 'KOVAI MEDICAL CENTER & HOSPITA', 'Arunjyoti Bio Ventures Limited', 'IDEA6.BO', 'CENTERAC TECHNOLOGIES LTD.', 'CENTURY EXTRUSIONS LTD.', 'CEAT LTD.', 'LAKSHMI CEMENT & CERAMICS LTD.', 'Cenlub Industries Limited', 'JKLAKSHMI6.BO', 'India Cements Capital Ltd.', 'CEREBRA INTEGRATED TECHNOLOGIE', 'Centenial Surgical Suture, Ltd.', 'Restile Ceramics Ltd.', 'CEATFIN.BO', 'Noida Medicare Centre Ltd', 'ULTRATECH CEMENT LTD.', 'GANGOTRI CEMENT LTD.', 'SOMANY CERAMICS LTD.', 'CERA SANITARYWARE LTD.', 'SPARTEK CERAMICS INDIA LTD.', 'NIRMAN CEMENTS LTD.', 'THE RAMCO CEMENTS LIMITED', 'REGENCY CERAMICS LTD.', 'Decolight Ceramics Ltd.', 'Ceenik Exports (India) Ltd.', 'Kalyanpur Cements Ltd.', 'P.R.CEMENTS LTD.', 'Saurashtra Cement Ltd.', 'SAGAR CEMENTS LTD.', 'KAKATIYA CEMENT SUGAR & INDUST', 'CESC Limited', 'MAHENDRA CEMENTS LTD.', 'Centum Electronics Limited', 'SUN EARTH CERAMICS LTD.', 'Shyam Century Ferrous Limited', 'Pee Cee Cosma Sope Ltd.', 'TWENTYFIRST CENTURY MANAGEMENT', 'CES LIMITED', 'The India Cements Limited', 'CETHAR INDUSTRIES LTD.', 'CESC4.BO', 'HEMADRI CEMENTS LTD.', 'PRAKASH CERAMICS LTD.', 'Vaishno Cement Company Limited', 'Sri Chakra Cement Limited', 'RCC CEMENTS LTD.', 'CELLULOSE PRODUCTS OF INDIA LT', 'SHREE DIGVIJAY CEMENT CO.LTD.', 'ORIENT CEMENT LTD', 'Century Enka Ltd.', 'MODERN CEMENT INDUSTRIES LTD.', 'Deccan Cements Ltd.', 'MURUDESHWAR CERAMICS LTD.', 'CG-VAK Software and Exports Limited', 'C.G.IMPEX LTD.', 'CAPRI GLOBAL CAPITAL LIMITED', 'Link Pharma Chem Ltd.', 'Sunitee Chemicals Ltd.', 'Sukhjit Starch & Chemicals Ltd.', 'Sikozy Realtors Ltd', 'Refnol Resins & Chemicals Ltd.', 'Lotus Chocolate Company Limited', 'The Indian Link Chain Manufactures Ltd.', 'Haryana Leather Chemicals, Ltd.', 'Fischer Chemic Ltd.', 'Diamines & Chemicals Ltd', 'Dharamsi Morarji Chemical Co. Ltd.', 'Chordia Food Products Limited', 'Chokhani Securities Ltd.', 'Chartered Logistics Ltd.', 'Chitradurga Spintex Limited', 'Cheviot Co. Ltd.', 'CHD Developers Limited', 'Chaman Lal Setia Exports Ltd.', 'CHAIN IMPEX LTD.', 'GARODIA CHEMICALS LTD.', 'Chemo Pharma Laboratories Ltd.', 'CHOKSI TUBE CO.LTD.', 'Chemiesynth (Vapi) Limited', 'CHANDNI TEXTILES ENGINEERING I', 'Chembond Chemicals Ltd.', 'SARANG CHEMICALS LTD.', 'BARIUM CHEMICALS LTD.', 'DHARANI SUGARS & CHEMICALS LTD', 'CHPL Industries Ltd.', 'ISHAN DYES & CHEMICALS LTD.', 'Daikaffil Chemicals India Limited', 'SUMEX CHEMICALS LTD.', 'CHICAGO SOFTWARE INDUSTRIES LT', 'CHROMATIC INDIA LTD.', 'Caprolactam Chemicals Limited', 'CHENNPETRO6.BO', 'MANGALORE CHEMICALS & FERTILIZ', 'Lime Chemicals Limited', 'Choksi Laboratories Ltd', 'KEDIA CHEMICAL INDUSTRIES LTD.', 'INDIAN ELECTRO CHEMICALS LTD.', 'FUTURISTIC OFFSHORE SERVICES &', 'CHETAK SPINTEX LTD.', 'CHD Chemicals Limited', 'EMPEE SUGARS & CHEMICALS LTD.', 'CHEMXSC.BO', 'CHOKHANI INTERNATIONAL LTD.', 'HARSHVARDHAN CHEMICALS & MINER', 'CHENNAI FERROUS INDUSTRIES LIM', 'Choice International Limited', 'CHOWGULE STEAMSHIPS LTD.', 'DECCAN CHR*', 'TAI CHONBANG TEXTILE INDUSTRIE', 'THIRUMALAI CHEMICALS LTD.', 'CHHABRA SPINNERS LTD.', 'Pratiksha Chemicals Limited', 'IOL CHEMICALS & PHARMACEUTICAL', 'REGENT CHEMICALS LTD.', 'SHRISHMA FINE CHEMICALS & PHAR', 'CHEMTECH INDUSTRIAL VALVES LTD', 'NARIMAN POINT CHEMICAL INDUSTR', 'DCHL6.BO', 'Cimmco Ltd', 'Fine-Line Circuits Limited', 'CIPLA6.BO', 'Cipla Limited', 'Cindrella Hotels Ltd.', 'CIL Securities Limited', 'Consecutive Investments & Trad', 'Circuit Systems India Ltd', 'MAHINDRA CIE AUTOMOTIVE LIMITE', 'CIFCO FINANCE LTD.', 'OPTO CIRCUITS (INDIA) LTD.', 'SHRIRAM CITY UNION FINANCE LTD', 'Citizen Infoline Ltd.', 'Cindrella Financial Services Ltd', 'City Online Services Limited', 'CUB6.BO', 'Gala Print City Limited', 'Citi Port Financial Services Limited', 'Cityman Ltd', 'VISION CINEMAS LTD.', 'CIL NOVA PETROCHEMICALS LTD.', 'CITY UNION BANK LTD.', 'CINELINE INDIA LIMITED', 'CITY LIFTS (INDIA) LTD.', 'TARRIF CINE & FINANCE LTD.', 'MADRAS HI-TECH CIRCUITS LTD.', 'Cinerad Communications Ltd.', 'CIGNITI TECHNOLOGIES LTD.', 'OPTOCIRCUI6.BO', 'CINEVISTA LTD.', 'Cistro Telelink Ltd', 'Clio Infotech Limited', 'SONELL CLOCKS & GIFTS LTD.', 'RELIANCE CLOSE ENDED EQUITY FU', 'Kewal Kiran Clothing Limited', 'INDIAN CARD CLOTHING CO.LTD.', 'CLASSIC PRESS (INTERNATIONAL)', 'CLARICH.BO', 'Kumar Wire Cloth Manufacturing Co. Ltd.', 'RELIANCE CLOSE ENDED EQUITY FU', 'CLARIANT CHEMICALS (INDIA) LTD', 'Crescent Leasing Limited', 'CLARO INDIA LTD.', 'CLASSIC ELECTRICALS LTD.', 'CLUTCH AUTO LTD.', 'CLASSIC DIAMONDS (INDIA) LTD.', 'RELIANCE CLOSE ENDED EQUITY FU', 'CLARIS LIFESCIENCES LTD.', 'RELIANCE CLOSE ENDED EQUITY FU', 'CMI Limited', 'CMI FPE Ltd', 'CREATIVE MERCHANTS LTD', 'Chennai Meenakshi Multispeciality Hospital Ltd.', 'C. MAHENDRA EXPORTS LTD.', 'CMC Limited', 'CMS INFOTECH LTD.', 'CMAHENDRA6.BO', 'CSL Finance Limited', 'CNI Research Ltd', 'Goldman Sachs Mutual Fund - Goldman Sachs CNX Nifty Shariah Index Exchange Traded Scheme', 'TAMO.BO', 'CONSOL SEC*', 'HDBK.BO', 'i-NAV RELIANCE CNX100', 'CAPTAIN POLYPLAST LTD', 'CPSE ETF', 'CPEC LTD.', 'Cressanda Solutions Ltd.', 'CONCRETE CREDIT LIMITED', 'HARIG CRANKSHAFTS LTD.', 'CRANESSOFT6.BO', 'Finalysis Credit & Guarantee Co. Ltd.', 'CRISIL*', 'CRISIL6.BO', 'SMC CREDITS LTD.', 'CRB SHARE CUSTODIAN SERVICES L', 'CRIMSON METAL ENGINEERING COMP', 'Jayabharat Credit Ltd', 'Morganite Crucible India Ltd', 'PARNAMI CREDITS LTD', 'CROWN TOURS LTD', 'Super Crop Safe Ltd', 'Octal Credit Capital Ltd.', 'Creative Eye Ltd.', 'CREST', 'SARLA CREDIT & SECURITIES LTD.', 'CREDENCE SOUND & VISION LTD.', 'VINTAGE CARDS & CREATIONS LTD.', 'Cranex Limited', 'CREDENTIAL FINANCE LTD.', 'CREDENTI FIN', 'SATIN CREDITCARE NETWORK LIMIT', 'CRANES SOFTWARE INTERNATIONAL', 'Crane Infrastructure Limited', 'CRYSTAL SOFTWARE SOLUTIONS LTD', 'Oracle Credit Limited', 'Hind Securities & Credits Limi', 'Kwality Credit & Leasing Ltd', 'CREATIVE EYE LTD.', 'Crestchem Limited', 'Sharda Cropchem Limited', 'EXCEL CROP CARE LTD.', 'CG POWER AND INDUSTRIAL SOLNS L', 'BAYER CROPSCIENCE LTD.', 'Crazy Infotech Ltd.', 'CROMPGREAV6.BO', 'Scintilla Commercial & Credit', 'Gujarat Credit Corporation Limited', 'United Credit Ltd', 'BAYERCROP6.BO', 'CRISIL Limited', 'CANARA ROBECO MUTUAL FUND - CA', 'GUJ CREDITPP', 'BEST & CROMPTON ENGG.LTD.', 'LAKSHMI TRADE CREDITS LTD.', 'CROMPTONGRE*', 'Gujarat Craft Industries Ltd.', 'Jhaveri Credits & Capital Ltd.', 'Market Creators Limited', 'Cravatex Limited', 'CROMAKEM LTD.', 'KWALITY CREDIT & LEASING LTD.', 'COSYN Limited', 'CSJ TECHNOLOGIES LTD.', 'Continental Securities Limited', 'CSL Finance Limited', 'CAPITAL TRADE LINKS LTD', 'CTIL LTD.', 'Cambridge Technology Enterprises Limited', 'CUMMINS INDIA LTD.', 'EDDY CURRENT CONTROLS (I) LTD.', 'CUBEX TUBINGS LTD.', 'Cupid Trades & Finance Ltd.', 'CURA TECHNOLOGIES LTD.', 'KPIT4.BO', 'Cubical Financial Services Ltd.', 'FIRST CUSTODIAN FUND (INDIA) L', 'CURE SPECTS LASERS LTD.', 'Cupid Ltd.', 'CVIL INFRA LTD.', 'Cybele Industries Ltd', 'Everest Kanto Cylinder Limited', 'CybermateInfotek Limited', 'Cyberscape Multimedia Ltd.', 'CYIENT LIMITED', 'Cyber Media (India) Ltd.', 'CYBERSPACE INFOSYS LTD.', 'MILLENNIUM CYBERTECH LTD.', 'GUJARAT CYPROMET LTD.', 'Rajasthan Cylinders & Containe', 'Dabur India Ltd.', 'DALMIA INDUSTRIES LTD.', 'DATAPRO INFORMATION TECHNOLOGY', 'Dazzel Confindive Ltd.', 'Prabhat Dairy Limited', 'DATAMATICS GLOBAL SERVICES LTD', 'Darjeeling Ropeway Company Lim', 'Sugal & Damani Share Brokers Ltd', 'International Data Management Ltd', 'LT Foods Limited', 'DAMODAR INDUSTRIES LTD.', 'Umang Dairies Ltd', 'Dalal Street Investments Limited', 'Modern Dairies Limited', 'DATAR SWITCHGEAR LTD.', 'DARSHAN OILS LTD.', 'Som Datt Finance Corp Ltd', 'Coffee Day Enterprises Limited', 'Poona Dal & Oil Industries Ltd.', 'DATABASE FINANCE LTD.', 'DAEWOO MOTORS (INDIA) LTD.', 'Daulat Securities Ltd', 'DAI ICH KAR*', 'DSJ COMMUNICATIONS LTD.', 'SHUKLA DATA TECHNICS LTD.', 'DB (INTERNATIONAL) STOCK BROKE', 'DBREALTY6.BO', 'DB Realty Ltd', 'DCMSL*', 'Deccan Chronicle Holdings Limited', 'DCM SHRIRAM INDUSTRIES LTD.', 'DCM TOYOTA N', 'DCM FINANCIAL SERVICES LTD.', 'DCM SHRIRAM LIMITED', 'DCB BANK LIMITED', 'DCBBANK6.BO', 'DCM Ltd.', 'DCW Limited', 'Deep Diamond India Limited', 'Devine Impex Limited', 'Dharti Proteins Ltd', 'De Nora India Limited', 'Deltron Ltd.', 'DELMA INFRASTRUCTURE LIMITED', 'Deccan Polypacks Ltd.', 'Deccan Gold Mines Ltd', 'Deepak Fertilisers And Petrochemicals Corporation Limited', 'Pan India Resort and Land Development Limited', 'GLOBUS CONSTRUCTORS & DEVELOPE', 'Tulive Developers Ltd.', 'DEWAN TYRES LTD.', 'Mitshi India Limited', 'Indtradeco Limited', 'Decillion Finance Ltd.', 'DFM Foods Limited', 'DFL INFRASTRUCTURE FINANCE LTD', 'Dhanlaxmi Fabrics Ltd.', 'Dhanlaxmi Cotex Ltd.', 'Dhunseri Tea & Industries Ltd', 'DHAR TEXTILE MILLS LTD.', 'DHAMPUR SUGAR (KASHIPUR) LTD.', 'Dhampure Speciality Sugars Ltd.', 'DHAMPUR SUGAR MILLS LTD.', 'DEWAN HOUSING FINANCE CORPORAT', 'DHYANA FINSTOCK LTD', 'DHARNENDRA INDUSTRIES LTD.', 'DHUNSERI INVESTMENTS LTD.', 'DHANLEELA INVESTMENTS & TRADIN', 'Dharani Finance Ltd.', 'D&H INDIA LTD', 'Dhanlaxmi Bank Limited', 'DHANADA CORPORATION LTD.', 'Dhruv Estates Ltd.', 'Dhanalaxmi Roto Spinners Ltd', 'Dhanus Technologies Limited', 'Dhoot Industries Ltd.', 'DHP India Ltd', 'DHANUKA COMMERCIAL LTD', 'DHATU FORGE LTD.', 'Dhabriya Polywood Limited', 'Dhoot Industrial Finance Ltd.', 'DIVINE MULTIMEDIA (INDIA) LTD.', 'Disa India Ltd', 'DIGITAL MULTIFORMS LTD.', 'Diana Tea Company Limited', 'TRILOGIC DIGITAL MEDIA LTD.', 'Medinova Diagnostic Services Limited', 'Span Divergent Limited', 'Digjam Ltd', 'Empee Distilleries Limited', 'Mini Diamonds (India) Limited', 'Laser Diamonds Ltd', 'GOENKA DIAMOND & JEWELS LTD.', 'DIVINE ENTERTAINMENT LTD', 'DISHTV6.BO', 'JUST DIAL LTD.', "Divi's Laboratories Limited", 'PIONEER DISTILLERIES LTD.', 'DINA IRON & STEEL LTD.', 'DIC INDIA LTD.', 'DION GLOBAL SOLUTIONS LTD.', 'Sovereign Diamonds Ltd', 'Sheetal Diamonds Ltd', 'CHAM BR DIST', 'Dishman Pharmaceuticals and Chemicals Ltd.', 'PAREKH DISTRIBUTORS LTD.', 'DIAMOND POWER INFRASTRUCTURE L', 'GDL6.BO', 'DIAMANT INFRASTRUCTURE LIMITED', 'FLAWLESS DIAMOND (INDIA) LTD.', 'Chambal Breweries & Distilleries Ltd', 'INTERNATIONAL DIAMOND SERVICES', 'Dil Ltd.', 'SOM DISTILLERIES & BREWERIES L', 'Gujchem Distillers India Ltd', 'PROFESSIONAL DIAMONDS LTD.', 'INTERGRATED DIGITAL INFO SERVI', 'Dish TV India Limited', 'DIVISLAB4.BO', 'White Diamond Industries Ltd.', 'DIVINUS FABRICS LTD', 'VARAHI DIAMONDS & FINANCE LTD.', 'Divyashakti Granites Ltd.', 'KINGS CHEMICALS & DISTILLERIES', 'DILIGENT INDUSTRIES LTD.', 'RAVI KUMAR DISTILLERIES LTD.', 'DIAMOND INFOSYSTEMS LTD.', 'Sunraj Diamond Exports Ltd.', 'Djs Stock & Shares Ltd', 'DEE KARTAVYA FINANCE LTD.', 'Delton Cables Limited', 'D-LINK (INDIA) LTD', 'DLF4.BO', 'DMC EDUCATION LTD', 'Donear Industries Limited', 'Dolphin Medical Services Ltd.', 'SUPER DOMESTIC MACHINES LTD.', 'Dolat Investments Limited', 'DOLPHIN HOTELS LTD.', 'HINDUSTAN DORR-OLIVER LTD.', 'Dollex Industries Ltd.', 'DOT COM GLOBAL LTD.', 'DPL', 'DQ Entertainment (International) Limited', 'LA TIM Metal & Industries Ltd.', 'PAN DRUGS LTD.', 'DREDGING CORPORATION OF INDIA', 'Parenteral Drugs (India) Limited', 'KILITCH DRUGS (INDIA) LTD.', 'LIFELINE DRUGS & PHARMA LTD.', 'NAGARJUNA DRUGS LTD.', 'DRAVYA INDUSTRIAL CHEMICALS LT', 'MOON DRUGS LTD.', 'United Drilling Tools Ltd', 'Combat Drugs Limited', 'D.R.INDUSTRIES LTD.', 'DR.DATSONS LABS LIMITED', 'Narmada Macplast Drip Irrigation Systems Limited', 'HI-TECH DRUGS LTD.', 'Dr. Lal Pathlabs Limited', 'RATNA DRUGS LTD.', 'Kabra Drugs Limited', 'Godavari Drugs Ltd.', 'Concord Drugs Limited', 'PARABOLIC DRUGS LTD', "Dr. Reddy's Laboratories Ltd.", 'KOPRAN DRUGS', 'DR. SABHARWALS MFG. LABS. LTD', 'Jindal Drilling & Industries Limited', 'DYNACONS SYSTEMS & SOLUTIONS L', 'DSKULKARNI6.BO', 'DSQ SOFTWARE LTD.', 'D.S.KULKARNI DEVELOPERS LTD.', 'Duro Pack Limited', 'Duke Offshore Ltd', 'Dujodwala Paper Chemicals Ltd.', 'Dutron Polymers Limited', 'DUNLOP India Ltd.', 'DUPONT SPORTSWEAR LTD.', 'DUCK TARPAULINS LTD.', 'DUGAR HOUSING DEVELOPMENTS LTD', 'DUNCANS INDUSTRIES LTD.', 'Schrader Duncan Limited', 'DUJOHN LABORATORIES LTD.', 'Dune Mercantile Ltd.', 'DWITIYA TRADING LTD', 'Dwarikesh Sugar Industries Limited', 'Dynemic Products Limited', 'DYNAVOX INDUSTRIES LTD.', 'SHREEJI DYE-CHEM LTD.', 'DUCON INFRATECHNOLOGIES LTD', 'Dynavision Ltd.', 'DYNA LAMPS & GLASS WORKS LTD.', 'MAFATLAL DYES & CHEMICALS LTD.', 'OMNI DYE-CHEM EXPORTS LTD.', 'Dynamic Portfolio Management & Services Ltd.', 'Vidhi Dyestuffs Manufacturing Ltd.', 'Dynamic Industries Ltd.', 'DYNAMIC MICROSTEPPERS LTD.', 'SM DYECHEM LTD.', 'SPAN DYESTUFF INDUSTRIES LTD.', 'DYNAMATIC TECHNOLOGIES LTD.', 'Eastern Treads Ltd.', 'Eastcoast Steel Limited', 'WEIZMANN FINCORP LTD.', 'The Great Eastern Shipping Company Limited', 'EASUN REYROLLE LTD.', 'SHARMA EAST INDIA HOSPITALS &', 'EASTERN SUGAR & INDUSTRIES LTD', 'NORTH EASTERN CARRYING CORPORA', 'Mathew Easow Research Securities Ltd.', 'SECURE EARTH TECHNOLIGIES LTD.', 'Eastern Gases Limited', 'EBERS PHARMACEUTICALS LTD.', 'eClerx Services Limited', 'Ecoboard Industries, Ltd.', 'Vikas EcoTech Limited', 'ECO RECYCLING LTD.', 'GANESHA ECOSPHERE LTD.', 'Ecoplast Limited', 'Natco Economicals Limited', 'ECO FRIENDLY FOOD PROCESSING P', 'ELECTRIC CONTROL GEAR (INDIA)', 'ECLERX*', 'ECLERX6.BO', 'Econo Trade (India) Limited', 'Info Edge (India) Limited', 'IEC Education Ltd', 'Greycells Education Ltd', 'CORE EDUCATION & TECHNOLOGIES', 'Edelweiss ETF- Nifty 50', 'EDYNAMICS SOLUTIONS LTD.', 'USHA MARTIN EDUCATION & SOLUTI', 'Remi Edelstahl Tubulars Ltd', 'Edelweiss Financial Services L', 'Edelweiss Financial Services Limited', 'Everonn Education Limited', 'Emergent Global Edu and Services Limited', 'NAVNEET EDUCATION LIMITED', 'EDUEXEL INFOTAINMENT LIMITED', 'VJTF EDUSERVICES LTD.', 'MT EDUCARE LTD.', 'Educomp Solutions Limited', 'NAUKRI6.BO', 'VIRTUAL GLOBAL EDUCATION LTD.', 'Sylph Education Solutions Limi', 'EDSERV SOFTSYSTEMS LTD.', 'JOINTECA EDUCATION SOLUTIONS L', 'COREEDUTEC6.BO', 'EFFINGO TEXTILE & TRADING LIMI', 'SKM EGG PRODUCTS EXPORT (INDIA', 'Eicher Motors Ltd.', 'EIDPARRY6.BO', 'EIH LTD.', 'EIDER TELECOM LTD.', 'EIMCO ELECON (INDIA) LTD.', 'EIDER ELECTRONICS INDUSTRIES L', 'EICHERMOT6.BO', 'Ekam Leasing & Finance Company Ltd', 'Salzer Electronics Limited', 'Rexnord Electronics and Controls Limited', 'Precision Electronics Ltd.', 'MINTAGE ELECTRO EQUIPMENTS LTD', 'MIC Electronics Limited', 'Envair Electrodyne Ltd.', 'Elegant Marbles & Grani Industries Ltd.', 'Elder Pharmaceuticals Limited', 'ELBEE SERVICES LTD.', 'Trend Electronics Ltd', 'PG ELECTROPLAST LTD.', 'LEEL ELECTRICALS LIMITED', 'ELECTCAST6.BO', 'KUSAM ELECTRICAL INDUSTRIES LT', 'SCHNEIDER ELECTRIC INFRASTRUCT', 'KRISONS ELECTRONIC SYSTEMS LTD', 'MONICA ELECTRONICS LTD.', 'SEPSL.BO', 'RECLTD4.BO', 'ELCID INVESTMENTS LTD.', 'Magna Electro Castings Ltd.', 'Elecon Engineering Company Limited', 'SATKAR ELECTRONICS LTD.', 'Gujarat Poly Avx Electronics Ltd.', 'REMI ELEKTROTECHNIK LIMITED', 'EON ELECTRIC LTD.', 'Elango Industries Ltd.', 'Ellenbarrie Industrial Gases Ltd.', 'STARVOX.BO', 'LLOYDELENG6.BO', 'TVS ELECTRONICS LTD.', 'KHAITAN ELECTRICALS LTD.', 'Lakshmi Electrical Control Systems Ltd', 'KIRLOSKAR ELECTRIC COMPANY LTD', 'GUJARAT PERSTORP ELECTRONICS L', 'ELQUE POLYESTERS LTD.', 'ELCONFN.BO', 'ELECTROSTEEL CASTINGS LTD.', 'MYSTIC ELECTRONICS LIMITED', 'KHANDELWAL HERMANN ELECTRONICS', 'SHREE GANESH ELASTOPLAST LTD.', 'ELEGANT PHARMACEUTICALS LTD.', 'TOYAMA ELECTRIC LTD.', 'Elnet Technologies Ltd.', 'ELECTROTHERM (INDIA) LTD.', 'Rasi Electrodes Ltd.', 'ELECTREX (INDIA) LTD.', 'BAJAJ ELECTRICALS LTD.', 'ELLORA PAPER MILLS LTD.', 'Elixir Capital Limited', 'ELTROL LTD.', 'TUMUS ELECTRIC CORPORATION LTD', 'ELECTROSTEEL STEELS LTD.', 'Elder Health Care Limited', 'El Forge Ltd.', 'Procal Electronics India Ltd', 'Trishakti Electronics & Industries Ltd.', 'Rural Electrification Corporation Limited', 'BARODA ELECTRIC METERS LTD.', 'Tata Elxsi Limited', 'NAMTECH ELECTRONIC DEVICES LTD', 'Pan Electronics India Ltd.', 'Elder Projects Ltd.', 'ELPRO INTERNATIONAL LTD.', 'SHAW WALLACE ELECTRONICS LTD.', 'MAESTROS ELECTRONICS & TELECOM', 'INDIA NIPPON ELECTRICALS LTD.', 'JCT ELECTRONICS LTD.', 'ELDERPHARM6.BO', 'STAR PRECISION ELECTRONICS (IN', 'ELGI Equipments Limited', 'ELANTAS Beck India Limited', 'SM Energy Teknik & Electronics Ltd.', 'Positive Electronics Limited', 'MIRC ELECTRONICS LTD.', 'LALIT POLYMERS & ELECTRONICS L', 'REIL ELECTRICALS INDIA LTD.', 'Thana Electric Supply Company Ltd.', 'Empire Industries Limited', 'Emmsons International Limited', 'EMCO Limited', 'Emami Paper Mills Ltd.', 'PIONEER EMBROIDERIES LTD.', 'EMAMI LTD.', 'EMA India Ltd.', 'EMMBI INDUSTRIES LTD', 'Emerald Leasing Finance & Inve', 'EMPORIS PROJECTS LIMITED', 'NUMECH EMBALLAGE LTD.', 'EMKAY GLOBAL FINANCIAL SERVICE', 'EMPHOTR.BO', 'EMERGY PHAARMA LTD.', 'EMAMI INFRASTRUCTURE LTD.', 'EMED.COM TECHNOLOGIES LTD', 'E-METALS INDIA LTD.', 'EMPOWER INDIA LTD.', 'EMTEX INDUSTRIES (I) LTD.', 'Technofab Engineering Limited', 'SWELECT ENERGY SYSTEMS LIMITED', 'Swaraj Engines Ltd.', 'Sir Shadi Lal Enterprises Limited', 'Shaily Engineering Plastics Limited', 'Sarda Energy & Minerals Limited', 'Sadbhav Engineering, Ltd.', 'PTL Enterprises Limited', 'Fact Enterprise Ltd', 'Ensa Steel Industries Ltd.', 'Entertainment Network (India) Ltd.', 'Encore Software Ltd.', 'Encash Entertainment Limited', 'MONNET ISPAT & ENERGY LTD.', 'Lakshmi Energy and Foods Ltd.', 'GTV Engineering Limited', 'TALBROS ENGINEERING LIMITED', 'SWOJAS ENERGY FOODS LTD.', 'MALVICA ENGINEERING LTD.', 'GALLOPS ENTERPRISE LTD.', 'FILTRON ENGINEERS LTD.', 'Enterprise International Limited', 'TOP MEDIA ENTERTAINMENT LTD.', 'Jyotirgamya Enterprises Limite', 'TEXMACO RAIL & ENGINEERING LTD', 'Satellite Engineering Ltd.', 'Suzlon Energy Limited', 'KESAR ENTERPRISES LTD.', 'Meenakshi Enterprises Ltd.', 'VASCON ENGINEERS LTD', 'Sita Enterprises Limited', 'KILBURN ENG*', 'EONOUR TECHNOLOGIES LTD.', 'EONELEC*', 'EPC Industrie Ltd.', 'Epsom Properties Ltd', 'Raunaq EPC International Limit', 'Epic Energy Ltd', 'EPIC ENZYMES PHARMACEUTICALS', 'RAUNAQINTL.BO', 'Shriram EPC Limited', 'IDFC MUTUAL FUND - IDFC EQUITY', 'REVATHI EQUIPMENT LTD.', 'Swiss Glasscoat Equipments Limited', 'IDFC EQUITY OPPORTUNITY- SERIE', 'IDFC MUTUAL FUND- IDFC EQUITY', 'IDFC MUTUAL FUND - IDFC EQUITY', 'Loyal Equipments Limited', 'IDFC EQUITY OPPORTUNITY- SERIE', 'OTOKLIN PLANTS & EQUIPMENTS LT', 'IDFC MUTUAL FUND- IDFC EQUITY', 'Era Infra Engineering Limited', 'ERAINFRA6.BO', 'HANIL ERA TEXTILES LTD.', 'EROS INTERNATIONAL MEDIA LTD.', 'ERP Soft Systems Ltd', 'Popular Estate Management Ltd.', 'Essel Propack Limited', 'Escorts Limited', 'ESCORTS6.BO', 'UNIQUE ESTATES DEVELOPMENTS CO', 'PRESTIGE ESTATES PROJECTS LTD.', 'ESQUIRE MONEY GUARANTEES LTD.', 'HB Estate Developers Ltd.', 'ESTER INDUSTRIES LTD.', 'ESCORTS FINANCE LTD.', 'ESSAR INVESTMENTS LTD.', 'E.STAR INFOTECH LTD.', 'ESSAR SHIPPING LTD.', 'COCHIN MALABAR ESTATES & INDUS', 'LAN ESEDA INDUSTRIES LTD.', 'PREM KUTIR ESTATES & PROPERTIE', 'ESTAR INFOPP', 'ESSEM CATALYST LTD.', 'ESSAROIL4.BO', 'Essar Oil Ltd.', 'Esaar India Ltd', 'ESSKAY TELECOM LTD.', 'NITESH ESTATES LTD', 'ESSJAY SYNTHETICS LTD.', 'ESAB India Limited', 'ESHA MEDIA RESEARCH LIMITED', 'ESSAR SECURITIES LTD', 'ETT LTD', 'SBI MUTUAL FUND - SBI ETF SENS', 'ETP CORPORATION LTD.', 'EURO MULTIVISION LTD.', 'Euro Leder Fashion Ltd.', 'EUPHARMA LABORATORIES LTD.', 'Eureka Industries Ltd.', 'INDO EURO INDCHEM LTD.', 'EUROTEX INDUSTRIES & EXPORTS L', 'Everlon Synthetics Ltd', 'EVEREST INDUSTRIES LTD.', 'Hindustan Everest Tools Limited', 'Everest Organics Limited', 'EVEREADY INDUSTRIES INDIA LTD.', 'EVERGREEN TEXTILES LIMITED', 'Tulsi Extrusions Limited', 'Reliance Mutual Fund - R* Shares Gold ETF', 'Mishka Exim Limited', 'Magna Industries And Exports Ltd.', 'Indian Extractions Ltd', 'Extol Commercial Ltd', 'Exide Industries Limited', 'Innovation Software Exports Ltd.', 'KABRA EXTRUSIONTECHNIK LTD.', 'SOFTRAK TECHNOLOGY EXPORTS LTD', 'SHRI RAJIVLOCHAN OIL EXTRACTIO', 'NATURAL STONE EXPORTS LTD.', 'Gamma Infoway Exalt Ltd.', 'SAKUMA EXPORTS LTD.', 'EXIDE INDUSTRIES LTD', 'Steel Exchange India Ltd.', 'SUBHLAXMI EXPORTS LTD.', 'BARODA EXTRUSION LTD.', 'SELAN EXPLO*', 'Orbit Exports Ltd.', 'KEMROCK6.BO', 'Polyspin Exports Ltd.', 'ROXY EXPORTS LIMITED', 'NEPTUNE EXPORTS LTD.', 'GOLDMAN SACHS LIQUID EXCHANGE', 'Expo Gas Containers Ltd.', 'Progressive Extractions & Exports Limited', 'KEMROCK INDUSTRIES & EXPORTS L', 'RT Exports Ltd.', 'GOLDMAN SACHS GOLD EXCHANGE TR', 'INTEGRATED RUBIAN EXPORTS LTD.', 'Hindustan Oil Exploration Company Limited', 'Goldman Sachs Mutual Fund - Goldman Sachs Nifty Junior Exchange Traded Scheme', 'Exelon Infrastructure Ltd', 'PRAKASH SOLVENT EXTRACTIONS LT', 'EXCEL INDUSTRIES LTD.', 'RAJESH EXPORTS LTD.', 'NAMASTE EXPORTS LTD.', 'ORISSA EXTRUSIONS LTD.', 'JJ Exporters Ltd.', 'MACRO (INTERNATIONAL) EXPORTS', 'CHOKHANI GLOBAL EXPRESS LTD.', 'NUCLEUS SOFTWARE EXPORTS LTD.', 'Premier Explosives Limited', 'EXOTIC COAL LTD.', 'CHARMINAR GRANITES EXPORTS LTD', 'GOKALDAS EXPORTS LTD.', 'MAHARASHTRA EXPLOSIVES LTD.', 'ORIND EXPORTS LTD.', 'MULTI COMMODITY EXCHANGE OF IN', 'ION EXCHANGE (INDIA) LTD.', 'Explicit Finance Limited', 'SG GLOBAL EXPORTS LTD.', 'SUN GRANITE EXPORT LIMITED', 'HARIA EXPORTS LTD.', 'UTI Mutual Fund - UTI-Gold Exchange Traded Fund', 'Reliance Mutual Fund - Reliance Banking Fund', 'NORBEN TEA & EXPORTS LTD.', 'THAPAR EXPORTS LTD.', 'SBI Mutual Fund - SBI-ETF Gold', 'Sunday Exports Ltd', 'Devhari Exports (India) Limite', 'KOLUTHARA EXPORTS LTD.', 'VISHAL EXPORTS OVERSEAS LTD.', 'Uniroyal Marine Exports Ltd.', 'Goldman Sachs Mutual Fund - Goldman Sachs Nifty Exchange Traded Scheme', 'RAJESHEXPO4.BO', 'EXCEL REALTY N INFRA LTD.', 'SANTOGEN EXPORTS LTD.', 'PRIME SOLVENT EXTRACTIONS LTD.', 'Noble Explochem Ltd.', 'Worldwide Leather Exports Limited', 'TOWELS INDIA EXPORTS LTD.', 'Selan Exploration Technology Limited', 'INTERLINK EXPORTS LTD.', 'TROMBO EXTRACTIONS LTD', 'Goldman Sachs Mutual Fund - Goldman Sachs PSU Bank Exchange Traded Scheme', 'NAGREEKA EXPORTS LTD.', 'HINDOILEXP6.BO', 'Simran Farms Ltd', 'Faze Three Ltd.', 'Fairdeal Filaments Ltd', 'Facor Steels Ltd.', 'SOLAR FARMACHEM LTD.', 'Farmax India Limited', 'Falcon Tyres Ltd.', 'PRIYADARSHINI FABS LTD.', 'Santosh Fine Fab Ltd', 'Farry Industries Limited', 'INDIAN TERRAIN FASHIONS LTD.', 'Khator Fibre & Fabrics Limited', 'VISHAL FABRICS LTD', 'JAYBHARAT FABRICS MILLS LTD.', 'FUTURE LIFESTYLE FASHIONS LTD', 'Filatex Fashions Limited', 'SUNDRMFAST6.BO', 'Monte Carlo Fashions Limited', 'PDS MULTINATIONAL FASHIONS LIM', 'FABWRTH IND', 'Fast Track Entertainment Ltd.', 'KAMADGIRI FASHION LTD.', 'KRISHANA FABRICS LIMITED', 'RAVALGAON SUGAR FARM LTD.', 'KAVITA FABRICS LTD.', 'Samtex Fashions Ltd.', 'FERTILIZERS & CHEMICALS TRAVAN', 'DEV FASTENERS LTD.', 'FCS Software Solutions Limited', 'FINEOTEX CHEMICAL LTD.', 'FDC LIMITED*', 'FDC Limited', 'FDC6.BO', 'FEDERAL-MOGUL GOETZE (INDIA) L', 'Fenoplast Ltd.', 'FE (INDIA) LTD', 'Krishna Ferro Products Limited', 'Cosmo Ferrites Limited', 'FERVENT SYNERGIES LTD.', 'FEDDERS ELECTRIC AND ENG LTD', 'IMPEX FERRO TECH LTD.', 'VEGEPRO FOODS & FEEDS LTD.', 'Madras Fertilizer Limited', 'GSFC6.BO', 'Gujarat State Fertilizers & Chemicals Ltd.', 'FERRO CONCRETE CO.(INDIA) LTD.', 'Shree Pushkar Chemicals & Fert', 'Rohit Ferro-Tech Limited', 'FEDERAL BANK LTD.', 'Khaitan Chemicals & Fertilizers Ltd.', 'USHAIRN.BO', 'CHAMBAL FERTILISERS & CHEMICAL', 'DEEPAKFERT6.BO', 'Gujarat Narmada Valley Fertilizers & Chemicals Limited', 'RAASHI FERTILIZERS LTD.', 'Kirloskar Ferrous Industries Limited', 'ADARSH CHEMICALS & FERTILIZERS', 'FGP Ltd.', 'Sumedha Fiscal Services Limited', 'SREI Infrastructure Finance Limited', 'Siel Financial Services Ltd.', 'RR Financial Consultants Limited', 'RAUNAQ FINANCE LTD.', 'NCC Finance Limited', 'Nalin Lease Finance Ltd.', 'Max Financial Services Limited', 'LIC Housing Finance Ltd.', 'Ladderup Finance Limited', 'Inter Globe Finance Ltd.', 'HB Leasing & Finance Co. Ltd.', 'GV Films Limited', 'Golechha Global Finance Ltd.', 'Fusion Fittings (I) Limited', 'Firstsource Solutions Limited', 'Filatex India Ltd.', 'Munoth Financial Services Limited', 'INCAP FINANCIAL SERVICES LTD.', 'S R G SECURITIES FINANCE LTD', 'SPS FINQUEST LTD', 'Minda Finance Limited', 'LLOYDS FINANCE LTD.', 'GLOBAL INFRATECH & FINANCE LIM', 'Richfield Financial Services L', 'TCI FINANCE LTD.', 'Savani Financials Ltd.', 'MAFATLAL LUBRICANTS LTD.', 'Real Touch Finance Limited', 'FINCABLES6.BO', 'Fiberweb (India) Ltd.', 'KUBER AUTO GENERAL FINANCE & L', 'Karnavati Finance Limited', 'GDL Leasing & Finance Ltd', 'Fiem Industries Ltd.', 'Sarvottam Finvest Limited', 'INDIABULLS HOUSING FINANCE LTD', 'SURYAKRIPA FINANCE LTD.', 'RAMCHANDRA LEASING & FINANCE L', 'Tokyo Finance Ltd.', 'First Financial Services Limited', 'Kumbhat Financial Services Ltd.', 'MAFATLAL FINANCE CO.LTD.', 'KONGARAR INTEGRATED FIBRES LTD', 'GENERIC ENGINEERING CONSTR&PROJ', 'FINPIPE6.BO', 'ORACLE FINANCIAL SERVICES SOFT', 'LIBERAL FINLEASE LTD.', 'Raj Irrigation Pipes & Fittings Ltd.', 'GINNI FILAMENTS LTD.', 'TRC Financial Services Ltd.', 'Glance Finance Ltd.', 'Upsurge Investment and Finance Limited', 'KIEV FINANCE LTD.', 'Lead Financial Services Ltd.', 'GRUH FINANCE LTD.', 'Tirupati Fin-Lease Ltd.', 'TRIA FINE-CHEM LTD.', 'Rishab Financial Services Ltd', 'STERLING HOLIDAY FINANCIAL SER', 'SRG HOUSING FINANCE LTD.', 'MUTHOOT FINANCE LTD.', 'PUNJAB FIBRES LTD.', 'V. B. Desai Financial Services Limited', 'SBI HOME FINANCE LTD.', 'SSPN Finance Limited', 'Shivansh Finserv Limited', 'FINKURVE FINANCIAL SERVICES LT', 'Indus Fila Limited', 'GUJARAT FISCON LTD.', 'Shalibhadra Finance Limited', 'GIC HOUSING FINANCE LTD.', 'Cosmo Films Limited', 'GANDHINAGAR LEASING & FINANCE', 'LIBORD FINANCE LTD', 'NAGARJUNA FINANCE LTD.', 'SAKTHI FINANCE LTD.', 'NIYOGIN FINTECH LIMITED', 'SANCHAY FINVEST LTD.', 'Golden Legand Leasing and Finance Limited', 'PTC INDIA FINANCIAL SERVICES L', 'Srestha Finvest Limited', 'P. B. Films Limited', 'RAHIL INVESTMENT & FINANCE LTD', 'RAJATH FINANCE LIMITED', 'MONEY MASTERS LEASING & FINANC', 'FINANTECH6.BO', 'PMC FINCORP LIMITED', 'Mudit Finlease Ltd.', 'Gujarat Lease Financing Limited', 'TCFC Finance Ltd.', 'NATIONAL FITTINGS LIMITED', 'BAJRANG FINANCE LTD.', 'GANON TRADING FINANCE CO.LTD.', 'PROLINE SOFTWARE & FINANCE LTD', 'INTERACTIVE FINANCIAL SERVICES', 'PUSHPANJALI FLORICULTURE LTD.', 'Purity Flex Pack Ltd', 'GUJFLUORO6.BO', 'Gujarat Fluorochemicals Limited', 'NATIONAL FLASK INDUSTRIES LTD.', 'FLEXITUFF INTERNATIONAL LTD.', 'Fluidomat Ltd.', 'MAYUR FLOORINGS LTD.', 'PL FINANCE & INVESTMENT LTD.', 'FLORENCE INVESTECH LIMITED', 'NAVIN FLUORINE INTERNATIONAL L', 'Flex Foods Ltd.', 'KUBER FLORITECH LTD.', 'Hindustan Fluorocarbons Ltd.', 'PREMIER VINYL FLOORING LTD.', 'Flora Textiles Ltd', 'ENJAYES NATURAL FLAVOURS LTD.', 'HRB FLORICULTURE LTD.', 'Gujarat Narmada Flyash Company Limited', 'FLEETWELD (INDIA) LTD.', 'F MEC INTERNATIONAL FINANCIAL', 'FUTURE MARKET NETWORKS LTD.', 'SYNCOM FORMULATIONS (INDIA) LT', 'Syncom Formulations India Ltd', 'Spectrum Foods Ltd.', 'Sita Shree Food Products Ltd.', 'Rajkumar Forge Ltd.', 'Rainbow Foundations Limited', 'P G Foils Limited', 'NB Footwear Limited', 'Hinduja Foundries Limited', 'Fortis Healthcare Limited', 'HIMGIRI FOODS LTD.', 'S.S. Forgings & Engineering Limited', 'FORTUNE INTERNATIONAL LTD.', 'LGB FORGE LTD.', 'LANYARD FOODS LTD.', 'Kore Foods Limited', 'Shah Foods Limited', 'Ador Fontech Ltd.', 'NHC FOODS LTD.', 'SOURCE NATURAL FOODS & HERBAL', 'Gujarat Foils Ltd.', 'TRANSGLOBE FOODS LTD.', 'SMITHS & FOUNDERS (INDIA) LIMI', 'GOLD COIN HEALTH FOODS LTD', 'Suryo Foods & Industries Ltd', 'KMG MILK FOOD LTD.', 'Mishtann Foods Limited', 'MICRO FORGE (INDIA) LTD.', 'Mahaan Foods Limited', 'SUPER FORGINGS & STEELS LTD.', 'RCL FOODS LIMITED', 'FOCUS INDUSTRIAL RESOURCES LTD', 'Unjha Formulations Limited', 'KALYANI FORGE LTD.', 'RIVERDALE FOODS LTD.', 'SQUARE FOUR PROJECTS INDIA LIM', 'SHREE GANESH FORGINGS LTD.', 'GRAND FOUNDRY LTD.', 'Himalchuli Food Products Limited', 'METALYST FORGINGS LIMITED', 'FORTIS MALAR HOSPITALS LIMITED', 'TRANS TECHNO FOODS LTD.', 'MUNIS FORGE LTD.', 'Kore Foods Limited', 'Forbes & Company Limited', 'Tarai Foods Ltd', 'IGC Foils Limited', 'FOSECO INDIA LTD.', 'Prime Focus Limited', 'Fomento Resorts & Hotels Limited', 'VINTAGE FOODS & INDUSTRIES LTD', 'RMI FOODS LTD.', 'Ramkrishna Forgings Limited', 'Synthiko Foils Ltd.', 'PRESTIGE FOODS LTD.', 'TEMPTATION FOODS LTD.', 'Kohinoor Foods Ltd.', 'SPARKLE FOODS LTD.', 'Heritage Foods Limited', 'GANESH FOUNDRY & CASTINGS LTD.', 'FORTUNE FOODS LTD.', 'Techno Forge Limited', 'Nimbus Foods Industries Ltd', 'GOA FRUIT SPECIALITIES LTD.', 'Fredun Pharmaceuticals Limited', 'FUTURE ENTERPRISES LTD', 'FRONTIER CAPITAL LIMITED', 'TRICOM FRUIT PRODUCTS LIMITED', 'Frontier Springs Ltd.', 'Sang Froid Labs (India) Limite', 'Frontline Securities Ltd.', 'FRONTLINE FINANCIAL SERVICES L', 'Frontier Informatics Limited', 'FRL4.BO', 'ICICI Prudential Mutual Fund', 'Futuristic Securities Limited', 'HDFC Mutual Fund', 'Kotak Mahindra Mutual Fund - Kotak Sensex ETF', 'SBI Mutual Fund', 'SBI Mutual Fund', 'RELIANCE MUTUAL FUND - RELIANC', 'Reliance Mutual Fund', 'HDFC Mutual Fund', 'HDFC MUTUAL FUND - HDFC RAJIV', 'SBI Mutual Fund', 'Himachal Futuristic Communications Ltd.', 'Reliance Mutual Fund', 'Reliance Mutual Fund', 'SOUTHERN FUEL LTD.', 'RELIANCE MUTUAL FUND - RELIANC', 'ICICI Prudential Mutual Fund', 'ICICI Prudential Mutual Fund', 'UTI Mutual Fund', 'ICICI Prudential Mutual Fund', 'RELIANCE MUTUAL FUND- RELIANCE', 'ICICI Prudential Mutual Fund', 'Kotak Mahindra Mutual Fund', 'ICICI PRUDENTIAL VALUE FUND SE', 'LIC MF RGESS FUND SR- 2 REG PL', 'ICICI PRUDENTIAL MUTUAL FUND -', 'Reliance Mutual Fund', 'IPRU2366.BO', 'HDFC Mutual Fund', 'SBI Mutual Fund', 'ICICI PRUDENTIAL MUTUAL FUND -', 'SBI Mutual Fund', 'ICICI Prudential Mutual Fund', 'Kotak Mahindra Mutual Fund - Kotak Nifty ETF', 'IPRU2586.BO', 'LIC MF RGESS FUND SR-3-DRT PL', 'ICICI Prudential Mutual Fund', 'LIC MF RGESS FUND SR-2 DRT PL', 'SBI Mutual Fund', 'ICICI Prudential Mutual Fund', 'ICICI Prudential Mutual Fund', 'ICICI Prudential Mutual Fund', 'ICICI Prudential Mutual Fund', 'IPRU8566.BO', 'ICICI Prudential Mutual Fund', 'ICICI Prudential Mutual Fund', 'HDFC Mutual Fund', 'Reliance Mutual Fund', 'GOLDMAN SACHS MUTUAL FUND', 'HDFC MUTUAL FUND - HDFC GOLD E', 'ICICI Prudential Mutual Fund', 'RELIANCE MUTUAL FUND - RELIANC', 'ICICI Prudential Mutual Fund', 'Kotak Mahindra Mutual Fund - Kotak PSU Bank ETF', 'RELIANCE MUTUAL FUND - RELIANC', 'ICICI Prudential Mutual Fund', 'Kotak Mahindra Mutual Fund', 'MOTILAL OSWAL MUTUAL FUND', 'HDFC MUTUAL FUND - HDFC RAJIV', 'ICICI Prudential Mutual Fund', 'Reliance Mutual Fund', 'Reliance Mutual Fund', 'IDBI MUTUAL FUND - IDBI GOLD E', 'RELIANCE MUTUAL FUND- RELIANCE', 'ICICI Prudential Mutual Fund', 'HDFC Mutual Fund', 'Reliance Mutual Fund', 'FUNWORLD & TOURISM DEVELOPMENT', 'Reliance Mutual Fund', 'ICICI Prudential Mutual Fund', 'RELIANCE MUTUAL FUND- RELIANCE', 'ICICI PRUDENTIAL VALUE FUND SE', 'Reliance Mutual Fund', 'RELIANCE MUTUAL FUND- RELIANCE', 'ICICI Prudential Mutual Fund', 'ICICI Prudential Mutual Fund', 'ICICI PRUDENTIAL MUTUAL FUND -', 'HDFC Mutual Fund', 'Reliance Mutual Fund', 'ICICI Prudential Mutual Fund', 'LIC MF RGESS FUND SR-3 DRT PL-', 'ICICI Prudential Mutual Fund', 'ICICI PRUDENTIAL GROWTH FUND S', 'ICICI Prudential Mutual Fund', 'UTI Mutual Fund', 'KOTAKNIFTY2.BO', 'RELIANCE MUTUAL FUND- RELIANCE', 'Kotak Mahindra Mutual Fund - Kotak Gold ETF', 'Reliance Mutual Fund', 'FUTURA POLYESTERS LTD.', 'Reliance Mutual Fund', 'ICICI PRUDENTIAL GROWTH FUND S', 'Reliance Mutual Fund', 'HDFC Mutual Fund', 'HDFC Mutual Fund', 'RELIANCE MUTUAL FUND- RELIANCE', 'ICICI Prudential Mutual Fund', 'Ucal Fuel Systems Ltd.', 'Funny Software Limited', 'Reliance Mutual Fund', 'ICICI Prudential Mutual Fund', 'LIC MF EXCHNG TRADED FUND-SENS', 'Kotak Mahindra Mutual Fund', 'ICICI Prudential Mutual Fund', 'Reliance Mutual Fund', 'RELIANCE MUTUAL FUND- RELIANCE', 'Reliance Mutual Fund', 'LIC MF EXHGE TRADED FUND-NIFTY', 'RELIANCE MUTUAL FUND- RELIANCE', 'RELIANCE MUTUAL FUND - R SHARE', 'SBI Mutual Fund', 'Kotak Mahindra Mutual Fund', 'Reliance Mutual Fund', 'SURYA FUN CITY LTD.', 'RELIANCE MUTUAL FUND- RELIANCE', 'ICICI Prudential Mutual Fund', 'RELIANCE MUTUAL FUND- RELIANCE', 'ICICI Prudential Mutual Fund', 'Garg Furnace Ltd', 'MOTILAL OSWAL MUTUAL FUND - MO', 'RELIANCE MUTUAL FUND- RELIANCE', 'ICICI Prudential Mutual Fund', 'ICICI PRUDENTIAL GROWTH FUND S', 'Reliance Mutual Fund', 'ICICI PRUDENTIAL MUTUAL FUND -', 'LIC MF RGESS FUND SR-3-REG PL', 'HDFC Mutual Fund', 'ICICI Prudential Mutual Fund', 'LIC MF RGESS FUND SR-2 DRT PLN', 'ICICI Prudential Mutual Fund', 'Seasons Furnishings Ltd', 'ICICI Prudential Mutual Fund', 'HDFC MUTUAL FUND - HDFC RAJIV', 'ICICI Prudential Mutual Fund', 'ICICI PRUDENTIAL VALUE FUND SE', 'RELIANCE MUTUAL FUND- RELIANCE', 'LIC MF RGESS FUND SR-2 REG PL', 'FRL6.BO', 'HDFC MUTUAL FUND - HDFC RAJIV', 'ICICI Prudential Mutual Fund', 'IPRU2626.BO', 'RELIANCE MUTUAL FUND - R SHARE', 'HDFC Mutual Fund', 'ICICI Prudential Mutual Fund', 'FUTURISTIC SOLUTIONS LTD.', 'SBI Mutual Fund', 'ICICI PRUDENTIAL VALUE FUND SE', 'ICICI PRUDENTIAL GROWTH FUND S', 'Reliance Mutual Fund', 'Reliance Mutual Fund', 'ICICI PRUDENTIAL MUTUAL FUND -', 'ICICI Prudential Mutual Fund', 'ICICI Prudential Mutual Fund', 'LIC MF RGESS SR-3 RG PLN-DVD P', 'Gayatri Sugars Ltd.', 'Garware Marine Industries Ltd.', 'Garnet International Limited', 'Garnet Construction Ltd.', 'Gangotri Iron & Steel Co., Ltd.', 'Gabriel India Limited', 'Gaurav Mercantile Limited', 'GAJANAN SECURITIES SERVICES LT', 'Gujarat Gas Company Limited', 'Ganga Pharmaceuticals Limited', 'GAMMON INFRASTRUCTURE PROJECTS', 'GANESH HOUSING CORPORATION LTD', 'Gammon India Limited', 'GANDHIDHAM SPINNING & MANUFACT', 'GAIL (India) Limited', 'KITEX GARMENTS LTD.', 'Rajasthan Gases Limited', 'GANGOTRI IRON & STEEL COMPANY', 'Garware-Wall Ropes Ltd.', 'Galada Power And Telecommunication Limited', 'UTTAM GALVA STEELS LTD.', 'Gujarat Gas Limited', 'Garware Polyester Limited', 'Gagan Gases Limited', 'GAIL4.BO', 'PGHH6.BO', 'GAGAN POLYCOT INDIA LTD.', 'Galaxy Entertainment Corporation Limited', 'GARLON POLYFAB INDUSTRIES LTD.', 'Gallantt Metal Ltd.', 'GANESH HOLDINGS LTD.', 'GAMMONIND6.BO', 'GAYATRI TISSUE & PAPERS LTD.', 'GANDHI SPECIAL TUBES LTD.', 'GAZI FINANCIAL SERVICES & INVE', 'SIDDHESWARI GARMENTS LTD.', 'Galaxy Consolidated Finance Limited', 'Garware Synthetics Limited', 'UPPER GANGES SUGAR & INDUSTRIE', 'SRI GANAPATHY MILLS CO.LTD.', 'GARWAREWAL*', 'GALAXY BEARINGS LTD.', 'Garden Silks Mills Ltd.', 'Galada Finance Limited', 'GALLANTT ISPAT LTD.', 'SHREE GANESH KNIT (INDIA) LTD.', 'Gandhinagar Enterprise Limited', 'GALORE PRINTS INDUSTRIES LTD.', 'GANGA PAPERS INDIA LTD.', 'PROCTER & GAMBLE HYGIENE & HEA', 'Indraprastha Gas Limited', 'GAIL*', 'Gati Ltd', 'GCV SERVICES LIMITED', 'GCM COMMODITY & DERIVATIVES LT', 'GCCL INFRASTRUCTURE & PROJECTS', 'GCCL CONSTRUCTION & REALITIES', 'GCM SECURITIES LTD', 'GDR MEDIA LTD.', 'Geometric Limited', 'RACL Geartech Limited', 'The Hi-Tech Gears Ltd', 'Gemstone Investments Limited', 'GEODESIC6.BO', 'GEOMETRIC6.BO', 'Swarnsarita Gems Limited', 'GEE Limited', 'GEMMIA OILTECH (INDIA) LTD.', 'National General Industries Limited', 'GENELEC LTD.', 'GEI Industrial Systems Ltd.', 'GITANJALI GE', 'GEMINI COM*', 'SHANTHI GEARS LTD.', 'GEM CABLES & CONDUCTORS LTD.', 'Gujarat Automotive Gears Ltd.', 'G.G.AUTOMOTIVE GEARS LTD.', 'GEECEEVEN*', 'Gem Spinners India Ltd.', 'Gitanjali Gems Ltd.', 'GEMINI COMMUNICATION LTD.', 'Genus Commu Trade Ltd', 'GREATEAST*', 'Nitta Gelatin India Limited', 'Genesys International Corporation Limited', 'Gee Gee Granites Ltd.', 'Gennex Laboratories Limited', 'Scanpoint Geomatics Ltd', 'MOTOR & GENERAL FINANCE LTD.', 'GEODESIC LTD.', 'GENUS POWER INFRASTRUCTURES LT', 'GEOLOGGING INDUSTRIES LTD.', 'Genus Prime Infra Limited', 'India Gelatine & Chemicals Ltd.', 'GEOD LTD*', 'NARMADA GELATINES LTD.', 'RACL Geartech Limited', 'GFL FINANCIALS INDIA LIMITED', 'GHANSHYAM STEEL WORKS LTD.', 'GHCL Limited', 'Gini Silk Mills Limited', 'Gillette India Limited', 'GIRNAR FIBRES LTD.', 'GI ENGINEERING SOLUTIONS LTD.', 'GITA RENEWABLE ENERGY LIMITED', 'GILT PACK LTD.', 'GIRIRAJ PRINT PLAST LTD.', 'Gujarat Industries Power Co. Ltd.', 'PNB Gilts Ltd.', 'Gilada Finance & Investments L', 'Meyer Apparel Limited', 'GLORY POLYFILMS LTD.', 'Triveni Glass', 'Shree Global Tradefin Limited', 'Premco Global Ltd.', 'Haldyn Glass Ltd', 'Glodyne Technoserve Limited', 'Glittek Granites Ltd.', 'Globus Spirits Ltd.', 'OnMobile Global Limited', 'SANCIA GLOBAL INFRAPROJECTS LI', 'POWERSOFT GLOBAL SOLUTIONS LTD', 'Sphere Global Services Ltd', 'Milestone Global Ltd', 'GLOBAL LAND MASTERS CORPORATIO', 'HINDUJA GLOBAL SOLUTIONS LTD.', 'GLOBAL VECTRA HELICORP LTD.', 'HINDUSTHAN NATIONAL GLASS & IN', 'GLOBAL KNITFAB LTD.', 'GLEITLAGER (INDIA) LTD.', 'GSKCONS6.BO', 'MANNA GLASS-TECH INDUSTRIES LT', 'BAJAJ GLOBAL LTD.', 'KARUTURI GLOBAL LTD.', 'Mediaone Global Entertainment Ltd.', 'PEARL GLOBAL INDUSTRIES LIMITE', 'GLAXOSMITHKLINE CONSUMER HEALT', 'TeleCanor Global Ltd', 'SEZAL GLASS LIMITED', 'GLOBUS CORPORATION LTD.', 'RATAN GLITTER INDUSTRIES LTD.', 'Sarthak Global Ltd.', 'KOTHSOY.BO', 'KHEMSONS GLOBAL LTD.', 'Global Securities Ltd', 'Glenmark Pharmaceuticals Ltd.', 'GLOSTER LTD', 'MASCON GLOBAL LTD.', 'Oscar Global Ltd.', 'Rajratan Global Wire Limited', 'STL GLOBAL LTD.', 'IFM Impex Global Limited', 'Virgo Global Limited', 'T & I Global Limited', 'GLOBAL INDUSTRIES LTD.', 'S V GLOBAL MILL LTD.', 'Vibrant Global Capital Limited', 'PENTAGON GLOBAL SOLUTIONS LTD.', 'Nouveau Global Ventures Ltd.', 'GLODYNE6.BO', 'GLAXOSMITHKLINE PHARMACEUTICAL', 'CANA GLASS LTD.', 'GLOBAL SYNTEX (BHILWARA) LTD.', 'GLOBAL OFFSHORE SERVICES LTD.', 'SVP GLOBAL VENTURES LTD.', 'Hit Kit Global Solutions Ltd.', 'HARYANA SHEET GLASS LTD.', 'HOTLINE GLASS LTD.', 'GLOBAL INFRASTRUCTURE & TECHNO', 'INDIA GLYCOLS LTD.', 'RADFORD GLOBAL LIMITED', 'Urja Global Ltd', 'Global Capital Market & Infrastructures Ltd', 'Nutech Global Ltd.', 'GMR Infrastructure Limited', 'GMM Pfaudler Ltd.', 'GMRINFRA4.BO', 'GUJARAT MINERAL DEVELOPMENT CO', 'GMDCLTD6.BO', 'GUJARAT METALLIC COAL & COKE L', 'GUJARAT NATURAL RESOURCES LIMI', 'Gothi Plascon (India) Limited', 'Godfrey Phillips India Limited', 'Goldstone Infratech Ltd.', 'GOA CARBON LTD.', 'Gopal Iron & Steels Company Gujarat Ltd', 'Godrej Industries Ltd.', 'Godrej Consumer Products Limited', 'SHIRPUR GOLD REFINERY LTD.', 'MOTILAL OSWAL MOST SHARES GOLD', 'GOLDWON TEXTILES LTD.', 'Gokul Refoils And Solvent Limited', 'i-NAV RELIANCE GOLD', 'Gontermann-Peipers (India) Limited', 'GOLDEN TOBACCO LTD.', 'GOLDIAM INTERNATIONAL LTD.', 'Govind Rubber Ltd.', 'GOLD LINE INTERNATIONAL FINVES', 'GOLD MULTIFAB LTD.', 'GOOD VALUE MARKETING CO.LTD.', 'GOL OFFSHORE LTD.', 'GOODRICKE GROUP LTD.', 'GODREJ PROPERTIES LTD', 'Gopala Polyplast Ltd.', 'GOODYEAR INDIA LTD.', 'Sea Gold Infrastructure Limited', 'GOLDENPROP.BO', 'Saint-Gobain Sekurit India Limited', 'VAISHNAVI GOLD LIMITED', 'GOLDEN GOENKA FINCORP LIMITED', 'GOLDCREST CORPORATION LIMITED', 'GODFRYPHLP6.BO', 'Goplee Infotech Ltd.', 'Goodluck India Limited', 'GOLDIAM INT*', 'Goldstone Technologies Ltd.', 'Gorani Industries Ltd', 'Golden Carpets Ltd', 'Gokak Textiles Ltd.', 'HARI GOVIND INTERNATIONAL LTD.', 'GOCL Corporation Limited', 'GODREJIND4.BO', 'GOM INDUSTRIES LTD.', 'Godawari Power & Ispat Ltd.', 'MIDWEST GOLD LTD.', 'GOOD VALUE IRRIGATION LTD.', 'GPT INFRAPROJECTS LTD.', 'Grandeur Products Limited', 'GUJARAT PIPAVAV PORT LTD.', 'GP PETROLEUMS LTD', 'Timex Group India Limited', 'Rathi Graphic Technologies Ltd.', 'Pentamedia Graphics Ltd.', 'Grasim Industries Limited', 'Gsb Finance Ltd', 'GSPL4.BO', 'GSS INFOTECH LTD.', 'GSL (INDIA) LTD.', 'Gujarat State Petronet Limited', 'GSL Nova Petrochemicals Limited', 'Gsl Securities Ltd', 'GTN Textiles Ltd.', 'GTN Industries Limited', 'GTL Infrastructure Ltd.', 'GTL Ltd.', 'G-Tech Info-Training Ltd.', 'GTCL MOBILE-COM TECHNOLOGY LTD', 'Gujarat Cotex Ltd.', 'Gujarat Toolroom Limited', 'Gujarat Intrux Limited', 'GUJARAT CONTAINERS LTD.', 'GUJARAT REFRACTORIES LTD.', 'VENTURA GUARANTY LTD.', 'Steelco Gujarat Ltd.', 'GUJARAT NRE COKE LTD', 'GUJARAT WEDGE WIRE SCREENS LTD', 'Gujarat Petrosynthese Ltd.', 'Gulshan Polyols Limited', 'GUJRATGAS6.BO', 'Gujarat Terce Laboratories Ltd.', 'STERLING GUARANTY & FINANCE LT', 'Gupta Synthetics Ltd.', 'GUJARAT STATE FINANCIAL CORPOR', 'GUJARAT NRE COKE LTD.', 'GUJARAT TEXSPIN LTD.', 'GUJARAT MEDITECH LTD.', 'TIMES GUARANTY LTD.', 'GUJARAT FILAMENTS LTD.', 'Gujarat Investa Ltd.', 'Switching Technologies Gunther Ltd.', 'Gujarat Raffia Industries Ltd.', 'GUJARAT INJECT (KERALA) LTD.', 'INDO GULF INDUSTRIES LTD.', 'GUJNRECOKE6.BO', 'GVK Power & Infrastructure Limited', 'GVKPIL6.BO', 'GWALIOR SUGAR CO.LTD.', 'GWALIOR POLYPIPES LTD.', 'Hazoor Multi Projects Ltd', 'HARSH POLYMERS (INDIA) LTD.', 'Hindustan Hardy Spicer Ltd.', 'HARVIC MANAGEMENT SERVICES (IN', 'HARTNCO.BO', 'HARRISONS MALAYALAM LTD.', 'HARBOR NETWORK SYSTEMS LTD.', 'HARITA SEATING SYSTEMS LTD.', 'HARYANA TEXPRINTS (OVERSEAS) L', 'Haryana Capfin Limited', 'HARYANA FINANCIAL CORPORATION', 'HAWKINS COOKERS LTD.', 'Hawa Engineers ltd.', 'SHREE HANUMAN SUGAR & INDUSTRI', 'Srinivasa Hatcheries Limited', 'Hanung Toys and Textiles Limited', 'ROCK HARD PETROCHEMICAL INDUST', 'HANUMAN TEA CO.LTD.', 'Hardcastle & Waud Manufacturing Company Ltd', 'Havells India Ltd.', 'Harmony Capital Services Limited', 'CHISEL & HAMMER (MOBEL) LIMITE', 'HARI.BO', 'HARIYANA METALS LTD.', 'HANJER FIBRES LTD.', 'Hasti Finance Ltd.', 'Hariyana Ship Breakers Ltd.', 'HANSAFLON PLASTO CHEM LTD.', 'HB Stockholdings Limited', 'HB Portfolio Limited', 'HBL POWER SYSTEMS LTD.', 'HCL Technologies Ltd.', 'HIND COMMERCE LIMITED', 'HealthCare Global Enterprises', 'HCL INFOSYSTEMS LTD.', 'HDFCBANK6.BO', 'i-NAV HDFC NIFTY', 'HDIL4.BO', 'HDFC Bank Limited', 'i-NAV HDFC SENSEX', 'HDIL6.BO', 'Heera Ispat Ltd', 'HEALTHY INVESTMENTS LTD.', 'CADILAHC6.BO', 'HEMANG RESOURCES LIMITED', 'LOOKS HEALTH SERVICES LIMITED', 'HERUK AGRO FOODS LTD.', 'Tejnaksh Healthcare Limited', 'TTK HEALTHCARE LTD.', 'HERO MOTOCORP LTD.', 'HEALTHFORE TECHNOLOGIES LTD.', 'HELIOS & MATHESON INFORMATION', 'HEMAKUTA INDUSTRIAL INVESTMENT', 'ISGEC HEAVY ENGINEERING LTD.', 'Hercules Hoists Limited', 'Hexaware Technologies Limited', 'Secunderabad Healthcare Ltd.', 'CORE HEALTHCARE LTD.', 'HEG Limited', 'GRAN HEAL PHARMA LTD.', 'Cadila Healthcare Limited', 'MOHATTA & HECKEL LTD.', 'HEIDELBERGCEMENT INDIA LTD.', 'Helpage Finlease Ltd.', 'ORIENTAL REMEDIES & HERBALS LT', 'HEG6.BO', 'HEGLTD*', 'HEXA TRADEX LTD.', 'SUNIL HEALTHCARE LTD', 'SAFAL HERBS LIMITED', 'TTK HEALTH*', 'HEMO ORGANIC LIMITED', 'Integrated Hitech Ltd.', 'Hittco Tools Limited', 'Hisar Metal Industries Ltd.', 'Hind Industries Ltd', 'Hindalco Industries Ltd.', 'Himalya International Ltd.', 'Himatsingka Seide Ltd.', 'Hikal Limited', 'SEVEN HILL INDUSTRIES LIMITED', 'HILTON RUBBERS LTD.', 'HNDTRAN.BO', 'HINDUST COM*', 'HINDALCO6.BO', 'SREE RAYALASEEMA HI-STRENGTH H', 'HIL LTD.', 'HINDOOSTAN MILLS LTD.', 'HINDUSTAN MOTORS LTD.', 'HIMATSINGKA AUTO ENTERPRISES L', 'HINDUJA VENTURES LTD.', 'High Energy Batteries (India) Ltd.', 'HITECHI JEWELLERY INDUSTRIES L', 'HIMGIRI FINCAP LTD.', 'HIGH STREET FILATEX LTD.', 'HINDUSTAN COMPOSITES LTD.', 'Himalaya Granites Ltd.', 'Bajaj Hindusthan Sugar Limited', 'HINDUSTAN UNILEVER LTD.', 'HINDUSTAN PHOTO FILMS MFG.CO.L', 'HIND RECTIFIERS LTD.', 'HIND SYNTEX LTD.', 'HINDUSTAN COPPER LTD.', 'HITESH TEXTILE MILLS LTD.', 'Hisar Spinning Mills Ltd.', 'HINAFIL INDIA LTD.', 'Himachal Fibres Ltd.', 'HINDUSTAN ORGANIC CHEMICALS LT', 'Hindustan Media Ventures Limited', 'HIGH GROUND ENTERPRISE LTD', 'Hiran Orgochem Ltd', 'HITECH CORPORATION LTD', 'Hipolin Limited', 'HIGHLAND INDUSTRIES LTD.', 'HITKARI INDUSTRIES LTD.', 'Iykot Hitech Toolroom Limited', 'HINDUSTAN DEVELOPMENT CORPORAT', 'HITKARI CHINA LTD.', 'HIND UNI LT*', 'HINDUSTAN PETROLEUM CORPORATIO', 'H.K.Trade International Limite', 'HMT Ltd.', 'Mahindra Holidays and Resorts India Ltd.', 'India Home Loan Limited', 'HOV Services Limited', 'HOTLINE TELETUBE & COMPONENTS', 'SUPREME HOLDINGS & HOSPITALITY', 'HS India Limited', 'INTERNATIONAL HOMETEX LTD.', 'STERLING (GUJARAT) HOSPITALS L', 'Sahara Housingfina Corporation Limited', 'Regency Hospital Limited', 'Polo Hotels Ltd.', 'HP Cotton Textile Mills Ltd.', 'Narayana Hrudayalaya Limited', 'HSIL Limited', 'HT Media Limited', 'HTMEDIA*', 'HTMEDIA6.BO', 'CORAL HUB LIMITED', 'Shreejal Info Hubs Ltd', 'HUBTOWN LTD.', 'INDIAN HUME PIPE CO.LTD.', 'Natura Hue Chem Ltd.', 'HYTONE TEXSTYLES LTD.', 'HYPERSOFT TECHNOLOGIES LIMITED', 'HYDRO S&S*', 'Indsil Hydro Power and Manganese Ltd.', 'TECIL CHEMICALS & HYDRO POWER', 'IAG COMPANY LTD.', 'IB Infotech Enterprises Limited', 'SORIL HOLDINGS AND VENTURES LIM', 'INDIABULLS VENTURES LTD.', 'ICRA Limited', 'HOV SERV ICES*', 'ICSA (INDIA) LTD.', 'SUPREMEX SHINE STEELS LTD', 'ICI INDIA', 'INDO COUNT INDUSTRIES LTD.', 'ICICI Bank Ltd.', 'ICRA6.BO', 'Indo Cotspin Limited', 'ICSIL*', 'ICCON OIL & SPECIALITIES LTD.', 'ICDS LTD.', 'ICICIBANK6.BO', 'Integrated Capital Services Lt', 'IDFC Limited', 'IDream Film Infrastructure Company Ltd', 'IDI LTD.', 'IDFC6.BO', 'IDEAL TEXBUILD LIMITED', 'IDEAL CARPETS LTD.', 'IDEAL HOTELS & INDUSTRIES LTD.', 'IFGL REFRACTORIES LTD.', 'INDIA FINSEC LTD.', 'IFCI Limited', 'IFL Promoters Limited', 'IFSL LTD.', 'IFB Industries Ltd.', 'I G PETROCHEMICALS LTD.', 'IGARASHI MOTORS INDIA LTD.', 'Industrial Investment Trust Limited', 'IIFL HOLDINGS LIMITED', 'IIFL*', 'IITL PROJECTS LIMITED', 'IIFL6.BO', 'IKF Technologies Ltd.', 'Ikab Securities & Investment Limited', 'IL&FS TRANSPORTATION NETWORKS', 'IL&FS INVESTMENT MANAGERS LTD.', 'IMP POWERS LTD.', 'Shivagrico Implements Ltd.', 'SANYO IMPEX LTD.', 'RAVRAJ IMPEX LTD.', 'Mahavir Impex Ltd.', 'IM+ CAPITALS LIMITED', 'Choksi Imaging Ltd.', 'IMC FINANCE LTD.', 'Shivkamal Impex Limited', 'SCANDENT IMAGING LIMITED', 'IO System Limited', 'IOLN6.BO', 'IOL NETCOM LTD.', 'IOB4.BO', 'Ipca Laboratories Limited', 'IP RINGS LTD.', 'IPCA LAB*', 'I Power Solutions India Ltd', 'IQ INFOTECH LTD.', 'Tata Sponge Iron Limited', 'SUNFLAG IRON & STEEL CO.LTD.', 'Orissa Sponge Iron And Steel Limited', 'IRIS MEDIAWORKS LTD.', 'USHA IRON &F', 'PITTSBURGH IRON & STEELS LTD.', 'JAIN IRRIGATION SYSTEMS LTD.', 'IRB4.BO', 'KUSUM IRON & STEEL LTD.', 'Rungta Irrigation Limited', 'MOVILEX IRRIGATION LTD.', 'IST Limited', 'SML ISUZU LIMITED', 'ISTREET NETWORK LIMITED', 'ISHWAR MEDICAL SERVICES LTD.', 'ISHWARSHAKTI HOLDINGS & TRADER', 'ISPAT PROFILES INDIA LTD.', 'ISPL INDUSTRIES LTD.', 'ISL CONSULTING LTD.', 'ISGECBBPH', 'SINGHAL SWAROOP ISPAT LTD.', 'THAPAR ISPAT', 'MONNETISPA6.BO', 'THAPAR ISP-B', 'RATHI ISPAT LTD.', 'SATHAVAHANA ISPAT LTD.', 'Sharda Ispat Limited', 'Aditya Ispat Ltd.', 'ISF LIMITED', 'Intrasoft Technologies Ltd.', 'ISMT LTD.', 'LORDS ISHWAR HOTELS LIMITED', 'THAPAR IS-BP', 'USHAISPAT.BO', 'THAPAR ISPAT LTD.', 'ITI Limited', 'ITC Limited', 'ITC4.BO', 'INFORMATION TECHNOLOGIES (INDI', 'ITL Industries Limited', 'PS IT INFRASTRUCTURE & SERVICE', 'Pil Italica Lifestyle Limited', 'INDIA TOURISM DEVELOPMENT CORP', 'IVP Ltd.', 'Vivanza Biosciences Limited', 'IVRCL Limited', 'IZMO Limited', 'Jain Marmo Industries Ltd.', 'JAIN STUDIOS LTD.', 'Jainco Projects (India) Limited', 'JAGATJIT INDUSTRIES LTD.', 'JAYASWAL NECO INDUSTRIES LTD.', 'Sree Jayalakshmi Autospin Ltd', 'Jay Shree Tea & Industries Ltd.', 'JAIDKA INDUSTRIES LTD.', 'MAA JAGDAMBE TRADELINKS LIMITE', 'JAI CORP LTD.', 'Jagan Lamps Ltd.', 'Jagran Prakashan Ltd', 'Jayavant Products Limited', 'JAIHIND PROJECTS LTD.', 'Jasch Industries Ltd.', 'JAMNA AUTO INDUSTRIES LTD.', 'Jaipan Industries Ltd', 'Shri Jagdamba Polymers Ltd.', 'JPPOWER6.BO', 'Jagjanani Textiles Ltd.', 'SRI JAYALAKSHMI SPINNING MILLS', 'Jauss Polymers Limited', 'JACKSON INVESTMENTS LTD', 'JAMMU & KASHMIR BANK LTD.', 'The Jamshri Ranjitsinghji Spinning and Weaving Mills Company Limited', 'JALPAC INDIA LTD.', 'Jayshree Chemicals Ltd.', 'JAY MAHESH INFRAVENTURES LTD.', 'J.B.CHEMICALS & PHARMACEUTICAL', 'JBFIND6.BO', 'JBFIND*', 'JBM Auto Limited', 'JCL LTD.', 'JD ORGOCHEM LTD.', 'Patdiam Jewellery Limited', 'Jeypore Sugar Company Ltd.', 'THANGAMAYIL JEWELLERY LTD', 'Renaissance Jewellery Ltd.', 'JEM INDUSTRIES LTD.', 'Uday Jewellery Industries Limi', 'ENCHANTE JEWELLERY LTD.', 'Shukra Jewellery Limited', 'TARA JEWELS LTD.', 'JFLABS.BO', 'JHAGADIA COPPER LTD.', 'JHS Svendgaard Laboratories Ltd.', 'JINDAL COTEX LTD.', 'Jindal Stainless (Hisar) Limit', 'Jindal Capital Ltd.', 'JINDALSTEL4.BO', 'JINDAL POLY*', 'JJ Finance Corporation Ltd', 'J.K.PHARMACHEM LTD.', 'J.K.CEMENT LTD.', 'JLA Infraville Shoppers Limite', 'JM FINANCIAL LTD.', 'JMFINANCIL6.BO', 'JMT AUTO LTD.', 'JMG Corporation Limited', 'Joindre Capital Services Ltd.', 'Jolly Plastic Industries Ltd.', 'JOLLY MERCHANDISE LTD.', 'Joonktollee Tea & Industries Limited', 'JOG ENGINEERING LTD.', 'JUPITER INDUSTRIES & LEASING L', 'JR Foods Ltd.', 'JRI INDUSTRIES & INFRASTRUCTUR', 'JSW Holdings Limited', 'JSWENERGY6.BO', 'JSWSTEEL6.BO', 'JSL INDUSTRIES LTD.', 'JSPL*', 'JUBILANT INDUSTRIES LTD.', 'Ludlow Jute & Specialities Ltd.', 'JUBILANT LIFE SCIENCES LIMITED', 'Justride Enterprises Limited', 'JYOTHI INFRAVENTURES LTD.', 'Jyothy Laboratories Limited', 'Jyoti Overseas Ltd', 'JYOTI STRUCTURES LTD.', 'KALINDEE6.BO', 'Kanchi Karpooram Ltd.', 'KAMAT HOTELS (INDIA) LTD.', 'KARTIK INVESTMENTS TRUST LTD.', 'Kabra Commercial Limited', 'KARAN FINANCE LTD.', 'KARNIMATA COLD STORAGE LTD', 'KAVIT INDUSTRIES LIMITED', 'KAMAL OVERSEAS LTD.', 'KAMA HOLDINGS LIMITED', 'KARUR K.C.P.PACKKAGINGS LTD.', 'Kakatiya Textiles Ltd.', 'Kaushalya Infrastructure Development Corporation Limited', 'Kamron Laboratories Ltd.', 'KALECONSUL*', 'KALPATARU POWER TRANSMISSION L', 'KANCHAN INTERNATIONAL LTD.', 'STERLING KALKSAND BRICKS LTD.', 'Kalptaru Papers Ltd', 'Kaya Limited', 'Kalpa Commercial Limited', 'KALYANI INVESTMENT COMPANY LTD', 'KANSAL FIBRES LTD.', 'KAPRINAS PHARMACEUTICALS & CHE', 'SHRI KALYAN HOLDINGS LTD.', 'KTKBANK6.BO', 'Manor Estates and Industries Limited', 'KAJAL SYNTHETICS & SILK MILLS', 'Kanpur Plastipack Ltd', 'Kanishk Steel Industries Ltd.', 'Kabsons Industries Limited', 'KALPAVRIKSHA INDUSTRIES LTD.', 'KANORIA*', 'KARMA ENERGY LTD.', 'KALINDEE RAIL NIRMAN (ENGINEER', 'MATRA KAUSHAL ENTERPRISE LIMIT', 'Kamanwala Housing Construction Limited.', 'Kachchh Minerals Ltd.', 'KARUR VYSYA BANK LTD.', 'Kay Power And Paper Limited', 'Kanco Enterprises Ltd.', 'KAASHYAP TECHNOLOGIES LTD.', 'Kanika Infrastructure & Power Ltd.', 'KAISER CORPORATION LIMITED', 'Kamdhenu Limited', 'MEUSE KARA & SUNGRACE MAFATLAL', 'KANORIA CHEMICALS & INDUSTRIES', 'KANORIA PLASCHEM LTD.', 'KAVVERI TELECOM PRODUCTS LTD.', 'Kallam Spinning Mills Ltd.', 'KANCO TEA & INDUSTRIES LTD.', 'Kanani Industries Ltd', 'Kamdhenu Limited', 'KALYANI STEELS LTD.', 'Kayel Securities Ltd.', 'KARMA INDUSTRIES LTD.', 'Kappac Pharma Ltd.', 'KAMAR CHEMICALS & INDUSTRIES L', 'KAPASHI COMMERCIALS LTD.', 'Kapil Raj Finance Ltd.', 'KANSAI NEROLAC PAINTS LTD.', 'KANDHARI RUBBERS LTD.', 'SAATAL KATTHA & CHEMICALS LTD.', 'KAMALA TEA CO.LTD.', 'KARTAVYA.BO', 'KAREEMS SPUN SILK LTD.', 'Kapil Cotex Ltd.', 'KAUSAMBI VANIJYA LTD', 'KBS INDIA LIMITED', 'KCL Infra Projects Limited', 'KCCL PLASTIC LTD.', 'K.C.TEXTILES LTD.', 'KCP Sugar & Industries Corp Ltd.', 'Khemani Distributors & Marketi', 'KEC INTERNATIONAL LTD.', 'Kew Industries Ltd.', 'KESORAMIND6.BO', 'Kesar Petroproducts Limited', 'KESAR TERMINALS & INFRASTRUCTU', 'KEMISTAR CORPORATION LIMITED', 'Keerthi Industries Limited', 'Ken Financial Services Ltd', 'KESWANI SYNTHETICS INDUSTRIES', 'KELVIN FINCAP LTD', 'KEDIA INFOTECH LTD.', 'Kedia Construction Co., Ltd.', 'KEYNOTE CORPORATE SERVICES LTD', 'Kernex Microsystems India Ltd', 'Kesoram Industries Ltd.', 'KEY CORP LTD.', 'KELLTON TECH SOLUTIONS LTD.', 'KEI INDUSTRIES LTD.', 'KEDIA VANASPATI LTD.', 'KGN ENTERPRISES LTD.', 'KGNIND6.BO', 'KGN Industries Ltd.', 'KG Denim Ltd.', 'K G Petrochem Ltd', 'KHODIYAR INDUSTRIES LTD.', 'Khyati Multimedia Entertainment Ltd.', 'RADICO6.BO', 'Radico Khaitan Ltd.', 'KHOOBSURAT LTD', 'COX & KINGS LIMITED', 'KIRI INDUSTRIES LTD.', 'KIRAN VYAPAR LTD', 'KILLICK NIXON LTD.', 'Kisan Mouldings Limited', 'KINETIC TRUST LTD.', 'KINGS INFRA VENTURES LIMITED', 'KIRLOSKAR*', 'KIFS FINANCIAL SERVICES LTD.', 'Kingfa Science & Technology (I', 'KIRLOSKAR MULTIMEDIA LTD.', 'KINETIC ENGINEERING LTD.', 'KIRLOSKAR INDUSTRIES LTD', 'KIRLOSKAR OIL ENGINES LTD.', 'Kiran Print Pack Ltd', 'Kilburn Engineering Limited', 'Kiduja India Ltd', 'KJMC Financial Services Ltd.', 'K.J.INTERNATIONAL LTD.', 'KMF LTD.', 'K K Fincorp Limited', 'KKALPANA INDUSTRIES (INDIA) LT', 'Kkalpana Plastick Limited', 'KLRF LTD.', 'KLG SYSTEL LTD.', 'Klg Capital Services Ltd', 'K-LIFESTYLE & INDUSTRIES LIMIT', 'KMC Speciality Hospitals (India) Ltd.', 'NACHMO KNITEX LTD.', 'KND ENGINEERING TECHNOLOGIES L', 'VANDANA KNITWEAR LTD.', 'INTEGRAL KNIT CO.LTD.', 'LWS KNITWEAR LTD.', 'KOTHARI INDUSTRIAL CORPORATION', 'KONKAN TYRES LTD.', 'KOPRAN6.BO', 'Kohinoor Techno Engineers Limited', 'KOLTE-PATIL DEVELOPERS LTD.', 'KOTAKBANK6.BO', 'KOUTONS RETAIL INDIA LTD.', 'KOTHARI WORLD FINANCE LTD.', 'K.P. Energy Limited', 'SRI KPR INDUSTRIES LTD.', 'KPIT TECHNOLOGIES LIMITED', 'K.P.R. Mill Limited', 'Kreon Finnancial Services Ltd', 'Shri Krishna Devcon Limited', 'Krypton Industries Ltd.', 'KRIPTOL INDUSTRIES LTD.', 'KRM INTERNATIONAL LTD.', 'KRISHNA SYNTHETICS LTD.', 'SHRI KRISHNA PRASADAM LTD', 'KRIDHAN INFRA LIMITED', 'Kriti Nutrients Ltd', 'K.S.OILS LTD.', 'KSHITIZ INVESTMENT LTD.', 'KSS LIMITED', 'KSE LTD.', 'KSK6.BO', 'KSB Pumps Limited', 'KSOILS6.BO', 'KSERASERA6.BO', 'S KUM SYN', 'S KUMARSYNFB', 'Kulkarni Power Tools Ltd.', 'S KUMAR SNFB', 'KUMARS COTEX LTD.', 'KUMAKA INDUSTIES LTD.', 'KUANTUM PAPERS LTD.', 'S KUMARSNFAB', 'KUNAL OVERSEAS LTD.', 'S. Kumars Nationwide Ltd.', 'Kuber Udyog Limited', 'S KUMAR SNFB', 'S. Kumars Online Ltd.', 'KYRA LANDSCAPES LIMITED', 'Sri Lakshmi Saraswathi Textiles (Arni) Limited', 'Shri Lakshmi Cotsyn Limited', 'Rishi Laser Ltd', 'Raymed Labs Ltd.', 'Morepen Laboratories Ltd.', 'Lawreshwar Polymers Ltd.', 'LAKSHMI PRECISION SCREWS LTD.', 'Laffans Petrochemicals Limited', 'LARSEN & TOUBRO LTD.', 'LAKSHMI MILLS COMPANY LTD.', 'Landmarc Leisure Corporation Limited', 'PITTI LAMINATIONS LTD.', 'LAKHOTIA POLYESTERS (INDIA) LT', 'Ortin Laboratories Ltd.', 'BROOKS LABORATORIES LTD.', 'ORTIN LABORATORIES LTD', 'La Opala RG Limited', 'LAUREL ORGANICS LTD.', 'PARNAX LAB LTD.', 'LANDMARK PROPERTY DEVELOPMENT', 'Unichem Laboratories Limited', 'UNICHEM LABORATORIES LTD', 'LYKA LABS LTD.', 'PHOENIX LAMPS LIMITED', 'SOUTHERN LATEX LTD.', 'DENIS CHEM LAB LTD', 'NEULAND LABORATORIES LTD.', 'La Tim Metal & Industries Limi', 'Auro Laboratories Ltd.', 'BALMER LAWRIE FREIGHT CONTAINE', 'VIVIMED LABS LTD.', 'Mercury Laboratories Limited', 'LAKSHMI MACHINE WORKS LTD.', 'Colinz Laboratories Ltd.', 'SHILPAX LABORATORIES LTD.', 'SARVODAYA LABS LTD.', 'SANDUR LAMINATES LTD.', 'Veejay Lakshmi Engineering Works Limited', 'IND-SWIFT LABORATORIES LTD.', 'LAKHANI INDIA LTD.', 'Lancor Holdings Ltd.', 'RUPAL LAMINATES LTD.', 'Makers Laboratories Limited', 'LITL6.BO', 'Ranbaxy Laboratories Ltd.', 'LABH CONSTRUCTION LTD.', 'Coral Laboratories Limited', 'LAXMIMACH6.BO', 'TEEM LABORATORIES LTD.', 'PENINSULA LAND LTD.', 'PENINLAND6.BO', 'Lanco Infratech Limited', 'OMEGALAB.BO', 'Rekvina Laboratories Limited', 'BALMER LAWRIE & CO.LTD.', 'Lambodhara Textiles Ltd', 'Lactose (India) Ltd.', 'LCC INFOTECH LTD.', 'L.D.TEXTILE INDUSTRIES LTD.', 'Inox Leisure Limited', 'SEAGULL LEAFIN LTD.', 'OSWAL LEASING LTD.', 'Lee & Nee Softwares (Exports) Ltd.', 'First Leasing Company of India Ltd.', 'Bervin Investment & Leasing Ltd.', 'SAM LEASECO LTD.', 'United Leasing & Industries Ltd', 'RAMCO SUPER LEATHERS LTD.', 'SOMPLAST LEATHER INDUSTRIES LT', 'Mayur Leather Products Ltd.', 'Voltaire Leasing & Finance Ltd.', 'UNIROLL LEATHER INDIA LTD.', 'Ledo Tea Company Ltd.', 'M.C.C.INVESTMENT & LEASING CO.', 'LEAFIN INDIA LTD.', 'PRETTO LEATHER INDUSTRIES LTD.', 'UCIL LEASING LTD.', 'LESHA INDUSTRIES LTD.', 'LE WATERINA RESORTS & HOTELS L', 'Swadeshi Industries & Leasing Ltd.', 'Brijlaxmi Leasing & Finance Ltd.', 'PRAKASH LEASING LTD.', 'SHREEVATSAA FINANCE & LEASING', 'SHIKHAR LEASING & TRADING LTD.', 'MAA LEAFIN & CAPITAL LTD.', 'DELTA LEASING & FINANCE LTD.', 'TRINITY LEAGUE INDIA LTD.', 'L.G.BALAKRISHNAN & BROS.LTD.', 'Lincoln Pharmaceuticals Ltd.', 'Linaks Microelectronics Ltd.', 'Manaksia Steels Limited', 'Capfin India Limited', 'SUPER TANNERY LIMITED', 'SAB INDUSTRIES LIMITED', 'SAUMYA CAPITAL LIMITED', 'SKIL Infrastructure Limited', 'SVP HOUSING LTD', 'RICHIRICH INVENTURES LIMITED', 'LIC MF EXHNGE TRADED FUND NIFT', 'SMS TECHSOFT (INDIA) LIMITED', 'NAKODA LIMITED', 'Strides Shasun Limited', 'Captain Pipes Limited', 'Spaceage Products Limited', 'LOVABLE LINGERIE LTD.', 'SPML INFRA LIMITED', 'Mahaveer Infoway Limited', 'NOESIS INDUSTRIES LIMITED', 'Oyeeee Media Limited', 'LIBORD SECURITIES LTD.', 'NOBLE POLYMERS LIMITED', 'METROGLOBAL LIMITED', 'RAJESWARI INFRASTRUCTURE LIMIT', 'PARAB INFRA LIMITED', 'LKPFINANCE*', 'LKP Finance Limited', 'PUNJLLOYD4.BO', 'LLOYD ROCKFIBRES LTD.', 'Stewarts & Lloyds Of India Ltd.', 'Punj Lloyd Ltd.', 'LML Ltd.', 'Petronet LNG Ltd.', 'LN INDUSTRIES INDIA LTD.', 'Patel Integrated Logistics Limited', 'Longview Tea Company Ltd.', 'Lohia Securities Ltd.', 'LOHIA POLYESTER LTD.', 'TIGER LOGISTICS (INDIA) LTD', 'Sical Logistics Ltd.', 'LOGIXMICRO6.BO', 'LOKESH MACHINES LTD.', 'SHREYAS SHIPPING & LOGISTICS L', 'SNOWMAN LOGISTICS LTD', 'WOMENS NEXT LOUNGERIES LTD', 'Loyal Textile Mills Limited', 'Lok Housing & Constructions Ltd.', 'LORDS CHEMICALS LTD.', 'Shahi Shipping Limited', 'SHRI SHAKTI LPG LTD.', 'LS INDUSTRIES LTD.', 'Shetron Ltd.', 'Shervani Industrial Syndicate Ltd', 'Senbo Industries Limited', 'Priyadarsini Limited', 'Praj Industries Ltd.', 'Photoquip India Ltd.', 'Persistent Systems Limited', 'Parsharti Investment Ltd', 'Invicta Meditek Limited', 'Infomedia Press Limited', 'Industrial & Prudential Investment Company Ltd.', "Country Condo'S Limited", 'Tyroon Tea Co. Ltd.', 'Tyche Industries Ltd', 'TVS Motor Company Limited', 'Tutis Technologies Ltd', 'TSL Industries Limited', 'Triton Corp Limited', 'TRF Limited', 'Trans Freight Containers Limited', 'TPL Plastech Limited', 'Tamilnadu Telecommunications Limited', 'Thomas Cook (India) Limited', 'Thermax Ltd.', 'Sterling Powergensys Limited', 'Techtran Polylenses Ltd.', 'Tata Consultancy Services Limited', 'TCM Limited', 'The Tata Power Company Limited', 'Tata Metaliks Limited', 'Tashi India Limited', 'TANTIA CONSTRUCTIONS LTD.', 'Tanla Solutions Limited', 'Syschem India Ltd.', 'Symphony Limited', 'SUYOG TELEMATICS LTD', 'The Supreme Industries Limited', 'SUPER SALES INDIA LTD.', 'LUSTRE TILES LTD.', 'Luminaire Technologies Ltd.', 'Lupin Limited', 'LUPIN LTD', 'LUMAX AUTOMOTIVE SYSTEMS LTD.', 'Luharuka Media & Infra Limited', 'LUX Industries Limited', 'Lumax Industries Limited', 'LYONS CORPORATE MARKET LTD.', 'Lycos Internet Limited', 'LYKIS LIMITED', 'Solitaire Machine Tools Limited', 'Shree Manufacturing Company Limited', 'SEL Manufacturing Company Limited', 'Mahanagar Telephone Nigam Limited', 'Mahalaxmi Rubtech Ltd', 'Mazda Ltd', 'Mawana Sugars Limited', 'Matra Realty Ltd', 'Maruti Suzuki India Limited', 'Marico Limited', 'Manjeera Constructions Ltd.', 'Man Infraconstruction Limited', 'Mandhana Industries Limited', 'Manaksia Limited', 'Maharashtra Seamless Limited', 'Mahamaya Steel Industries Ltd.', 'Mahalaxmi Seamless Ltd.', 'Machino Plastics Limited', 'Inani Marbles & Industries Limited', 'Malabar Trading Company Ltd.', 'Madhusudan Securities Ltd.', 'Bank of Maharashtra', 'MANAV PHARMA LTD.', 'MANALI PETROCHEMICAL LTD.', 'MAHSEAM*', 'MANIYAR PLAST LTD.', 'MADHAV MARBLES & GRANITES LTD.', 'MAYA SPINNERS LTD.', 'MARVEL INDUSTRIES LTD.', 'MAN INDUSTRIES (INDIA) LTD.', 'MODERN MALLEABLES LTD.', 'Maximaa Systems Limited', 'PRIME CAPITAL MARKET LTD.', 'MANSAROVARPA', 'Mardia Samyoung Capillary Tubes Company Ltd.', 'MADHUCON PROJECTS LTD.', 'Mastek Limited', 'Manipal Finance Corp Ltd.', 'Integra Capital Management Ltd.', 'Tech Mahindra Limited', 'Manvijay Development Company L', 'SRI MALINI SPINNING MILLS LTD.', 'NEERAJ PAPER MARKETING LIMITED', 'MAYA RASAYAN LTD.', 'MAHENDRA PETROCHEMICALS LTD.', 'Maris Spinners Ltd.', 'STANROSE MAFATLAL INVESTMENTS', 'MARUTI TELSTAR INDUSTRIES LTD.', 'MAHARASHTRA CORPORATION LTD.', 'MASTEKLTD*', 'Mefcom Capital Markets Limited', 'Marg Projects And Infrastructure Ltd.', 'Rajasthan Tube Manufacturing Company Ltd', 'MAHASHREE TRADING LTD.', 'MARAL OVERSEAS LTD.', 'MAYUR UNIQUOTERS LTD.', 'MAHINDRA LIFESPACE DEVELOPERS', 'Manaksia Coated Metals & Indus', 'MANUGRAPH INDIA LTD.', 'ABANS ENTERPRISES LIMITED', 'SUPREME TEX MART LTD.', 'Premium Capital Market & Investment Ltd.', 'MANGALAM TIMBER PRODUCTS LTD.', 'MARG LTD.', 'Marksans Pharma Ltd.', 'MAHINDRA & MAHINDRA LTD.', 'MAHAGANESH TEXPRO LTD.', 'Manaksia Industries Limited', 'RGF Capital Markets Limited', 'Mangalya Soft-Tech Ltd.', 'Standard Capital Markets Limited', 'UMA MAHESWARI MILLS LTD.', 'MARGO FINANCE LIMITED', 'Marathon Nextgen Realty Ltd', 'TELEDATA MARINE SOLUTIONS LTD.', 'MANGALAM INDUSTRIAL FINANCE LT', 'MBL Infrastructures Limited', 'M.B. Parikh Finstocks Limited', 'Mac Charles (India) Ltd.', 'MCS Limited', 'MCDOWELL HOLDINGS LTD.', 'MODERN TERRY TOWELS LTD.', 'MODERN THREADS (INDIA) LTD.', 'Modern Steels Ltd.', 'MADRAS PETRO-CHEM LTD.', 'MODERN SYNTEX (INDIA) LTD.', 'M.D. Inducto Cast Limited', 'Sanguine Media Ltd.', 'MESCO PHARMACEUTICALS LTD.', 'Megasoft Ltd.', 'Mega Corporation Ltd.', 'PICTUREHOUSE MEDIA LTD.', 'INDBANK MERCHANT BANKING SERVI', 'Modison Metals Ltd.', 'Mercantile Ventures Limited', 'Mewar Polytex Limited', 'Medi-Caps Limited', 'MEENAKSHI STEEL INDUSTRIES LTD', 'OM METALS INFRAPROJECTS LTD.', 'MEP Infrastructure Developers', 'UNIVERSAL MEDIA NETWORK LTD.', 'SANRAA MEDIA LTD.', 'MEHTA SULFITES (INDIA) LTD.', 'SILCAL METALLURGICAL LTD.', 'MERCATOR6.BO', 'Palco Metals Limited', 'Megri Soft Limited', 'Trans Medicare Limited', 'Shiva Medicare Limited', 'SOBHAGYA MERCHANTILE LTD.', 'STANDARD MEDICAL & PHARMACEUTI', 'B.A.G.FILMS & MEDIA LTD.', 'NORRIS MEDICINES LTD.', 'Menon Pistons Ltd.', 'MEGLON INFRA-REAL (INDIA) LTD.', 'LINTAS MERCANTILE LTD.', 'PRESHA METALLURGICAL LTD.', 'VARUN MERCANTILE LTD.', 'UNISON METALS LTD', 'Vishvas Projects Limited', 'Mercury Metals Limited', 'MEHTA SECURITIES LTD.', 'SHELL MERCANTILE CORP.LTD.', 'Splendid Metal Products Limite', 'PERFECT-OCTAVE MEDIA PROJECTS', 'METALMAN INDUSTRIES LTD.', 'Power Mech Projects Limited', 'Paul Merchants Ltd.', 'METROPOLI OVERSEAS LTD.', 'Soni Medicare Limited', 'MFS INTERCORP LTD.', 'MFL INDIA LTD.', 'MH MILLS & INDUSTRIES LTD.', 'Mahasagar Travels Ltd.', 'Subhash Silk Mills Limited', 'Skyline Millars Ltd.', 'Rama Paper Mills Ltd.', 'Pranavaditya Spinning Mills Limited', 'NAHAR SPINNING MILLS LTD.', 'MindTree Limited', '8K MILES SOFTWARE SERVICES LTD', 'RADHIKA SPINNING MILLS LTD.', 'Shree Rajeshwaranand Paper Mills Ltd.', 'Mirch Technologies Ltd.', 'SAJJAN TEXTILES MILLS LTD.', 'RESURGERE MINES & MINERALS IND', 'MICRO TECHNOLOGIES (INDIA) LTD', '20 MICRONS LTD.', 'NIWAS SPINNING MILLS LTD.', 'MIDEAST (INDIA) LTD.', 'Cochin Minerals & Rutile Ltd.', 'RUBY MILLS LTD.', 'MIRZA INTERNATIONAL LTD.', 'MINAL INDUSTRIES LIMITED', 'MILK PARTNERS INDIA LIMITED', 'Minda Corporation Limited', 'MIDAS INFRA TRADE LIMITED', 'SATYA MINERS & TRANSPORTERS LT', 'MINI SOFT LTD.', 'Mihika Industries Ltd.', 'MICROSE INDIA LTD.', 'MIDFIELD INDUSTRIES LTD.', 'Milkfood Ltd.', 'UTTAM SUGAR MILLS LTD.', 'Mohit Paper Mills Limited', 'THE PHOENIX MILLS LTD', 'VIJAYKUMAR MILLS LTD.', 'MID INDIA INDUSTRIES LTD.', 'Suryalata Spinning Mills Limited', 'The Mysore Paper Mills Limited', 'MIKADO TEXTILE INDUSTRIES LTD.', 'SIRPUR PAPER MILLS LTD.', 'Mindteck (India) Limited', 'MINDTREE LTD', 'Suryaamba Spinning Mills Ltd', 'West Coast Paper Mills Limited', 'MAJESCO LIMITED', 'MMTC4.BO', 'MEDIA MATRIX WORLDWIDE LTD.', 'M.M.FORGINGS LTD.', 'MMTC Ltd.', 'MM Rubber Co. Ltd.', 'MMS INFRASTRUCTURE LTD', 'Mega Nirman & Industries Limit', 'MANAKSIA LT*', 'Moving Picture Co. (India) Ltd.', 'Mount Shivalik Industries Ltd', 'Motherson Sumi Systems Ltd.', 'MODEX INTERNATIONAL SECURITIES', 'Moser-Baer India Ltd.', 'MONALISA INFOTECH LTD.', 'SPICEMOBI6.BO', 'MONNET PROJECT DEVELOPERS LTD.', 'Mobile Telecommunications Ltd.', 'Monsanto India Limited', 'MODERN INSULATORS LTD.', 'MODEL FINANCIAL CORPORATION LT', 'Monnet Industries Ltd', 'Monotype India Ltd.', 'SANGHVI MOVERS LTD.', 'MODISTO.BO', 'Modipon Ltd.', 'MOTOROL SPECIALITY OILS LTD.', 'MODI HOOVER INTERNATIONAL LTD.', 'MONOZYME INDIA LTD.', 'MOD.WOOL(CIS', 'MOTILAL OSWAL FINANCIAL SERVIC', 'MORINDA OVERSEAS INDUSTRIES LT', 'MONTARI INDUSTRIES LTD.', 'MODI NATURALS LIMITED', 'PINCON LIFESTYLE LTD', 'Modern Shares & Stockbrokers Ltd', 'RAI SAHEB REKHCHAND MOHOTA SPG', 'MOHITE INDUSTRIES LIMITED', 'MORARJEE TEXTILES LTD.', 'MOH LTD.', 'MODI TELE FIBRES LTD.', 'SUMAN MOTELS LTD.', 'MONEYCF.BO', 'RANA MOHENDRA PAPERS LTD.', 'Thambbi Modern Spinning Mills Ltd', 'MOTILAL OSWAL MOST SHARES NASD', 'MOTILALOFS*', 'TATAMOTORS6.BO', 'MOTHER MIRA INDUSTRIES LTD.', 'My Money Securities Ltd.', 'Mohit Industries Limited', 'SPICE MOBILITY LIMITED', 'Morarka Finance Limited', 'MODI RUBBER LTD.', 'Modern India Ltd', 'MOONGIPA CAPITAL FINANCE LTD.', 'MORGAN INDUSTRIES LTD.', 'MOONBEAM INDUSTRIES LTD.', 'MOLD-TEK PACKAGING LIMITED', 'Mold Tek Technologies Ltd', 'SHARDA MOTOR INDUSTRIES LTD', 'NEELKANTH MOTELS & HOTELS LTD.', 'MONNETISP*', 'Monarch Networth Capital Limit', 'Moongipa Securities Ltd.', 'UFO Moviez India Limited', 'MORYO INDUSTRIES LTD.', 'MOIL LTD.', 'MONSANTO6.BO', 'MPS Limited', 'M.P.TELELINKS LTD.', 'MPF Systems Limited', 'MIPCO SEAMLESS RINGS (GUJARAT)', 'MphasiS Limited', 'MPL PLASTICS LTD.', 'MRO-TEK Realty Limited', 'MRPL6.BO', 'MARINE CARGO COMPANY LTD.', 'MRUGESH TRADING LTD.', 'MARMAGOA STEELS LTD.', 'MRF Ltd.', 'MRO-TEK Realty Limited', 'MSP STEEL & POWER LTD.', 'MSL INDUSTRIES LTD.', 'Mangalam Seeds Limited', 'MS SECURITIES LTD.', 'MSR INDIA LTD.', 'MTZ POLYFILMS LTD.', 'MTZ INDUSTRIES LTD.', 'Munoth Communication Ltd', 'Multibase India Ltd', 'Mukesh Strips Ltd', 'Mukesh Steels Ltd', 'Mukand Limited', 'Munoth Capital Market Limited', 'Multiplus Holdings Ltd.', 'Sundaram Multi Pap Ltd.', 'MUNAK CHEMICALS LTD.', 'MUKERIAN PAPERS LTD.', 'SHAMKEN MULTIFAB LTD.', 'MUNJAL SHOWA LTD.', 'MUKAND ENGINEERS LTD.', 'MULTI-ARC INDIA LTD.', 'MURABLACK INDIA LTD.', 'MUKUND SYNTEX LTD.', 'MURLI INDUSTRIES LTD.', 'MAURIA UDYOG LIMITED', 'SRIVEN MULTI-TECH LTD.', 'MUKUNDA INDUSTRIAL FINANCE LTD', 'Muller & Phipps (India) Limited', 'Munjal Auto Industries Limited', 'MULTICOLOUR OFFSET LTD.', 'Mukat Pipes Ltd', 'Mukesh Babu Financial Services Limited', 'Shree Rama Multi-Tech Ltd.', 'MVL Limited', 'MV COTSPIN LTD.', 'MW UNITEXX LTD.', 'MYM TECHNOLOGIES LTD.', 'STATE BANK OF MYSORE', 'MYSORE PETRO CHEMICALS LTD.', 'NATIONAL PLYWOOD INDUSTRIES LT', 'National Plastic Technologies Ltd', 'NAM SECURITIES LTD', 'NARANG INDUSTRIES LTD.', 'SRI NANDAA SPINNERS LTD.', 'NATIONAL OXYGEN LTD.', 'NATCO PHARMA LTD.', 'PNC6.BO', 'Narendra Properties Ltd.', 'NAGREEKA CAPITAL & INFRASTRUCT', 'NAVCOM INDUSTRIES LTD.', 'NAKSHATRA INFRASTRUCTURE LTD.', 'RELIANCE NATURAL RESOURCES LTD', 'Proaim Enterprises Limited', 'NAHAR INDUSTRIAL ENTERPRISES L', 'NAINA SEMICONDUCTOR LTD.', 'National Plastic Industries Ltd.', 'NAVAL TECHNOPLAST INDUSTRIES L', 'Nardhana Infrastructure Limited', 'Natural Capsules Ltd.', 'NAHAR POLYFILMS LTD.', 'Natraj Proteins Ltd.', 'NATIONAL SWITCHGEARS LTD.', 'NUWAY ORGANIC NATURALS INDIA L', 'SCINDIA STEAM NAVIGATION CO.LT', 'NAGARJUNA OIL REFINERY LTD.', 'Navkar Corporation Limited', 'NANDAN DENIM LIMITED', 'Navketan Merchants Limited', 'Punjab National Bank', 'NAYAGARA PAPER PRODUCTS (INDIA', 'Nagpur Power & Industries Ltd.', 'NARAINGARH SUGAR MILLS LTD.', 'SKUMARN6.BO', 'NALWA SONS INVESTMENTS LTD.', 'Naysaa Securities Limited', 'NATIONAL STANDARD (INDIA) LTD.', 'Tamil Nadu Newsprint and Papers Limited', 'NATH PULP & PAPER MILLS LTD.', 'NAGARJUNA GRANITES LTD.', 'NCL Industries Limited', 'NCJ INTER PP', 'NISSAN COPPER LTD.', 'NCL Research and Financial Services Limited', 'NCC LIMITED', 'NDA Securities Ltd.', 'NEPC TEXTILES LTD.', 'Netlink Solutions India Ltd', 'Network Limited', 'Nelco Limited', 'DEN6.BO', 'NEXCEN SOFTECH LTD.', 'NEHA INTERNATIONAL LTD.', 'NETVISION WEB TECHNOLOGIES LTD', 'CORAL NEWSPRINTS LTD.', 'RICH UNIVERSE NETWORK LTD.', 'Supreme Telecom & Network India Limited', 'SHREE RAMA NEWSPRINT LTD.', 'SMARTLINK6.BO', 'Tulsyan NEC Ltd.', 'NEO INFRACON LTD.', 'NEXT MEDIAWORKS LTD.', 'INDUS NETWORKS LTD.', 'Nexxoft Infotel Ltd', 'Neil Industries Ltd.', 'NEPC INDIA LTD.', 'TV TODAY NETWORK LTD.', 'NEYCER INDIA LTD.', 'Neelkanth Technologies Ltd.', 'NETVISTA INFORMATION TECHNOLOG', 'NESTLEIND6.BO', 'Nectar Lifesciences Limited', 'Neo Corp International Ltd', 'NESTLE INDIA LTD.', 'Neogem India Ltd.', 'NET4.BO', 'SEA TV NETWORK LTD.', 'Network18 Media & Investments Limited', 'NEXUS SOFTWARE LTD.', 'NESCO LTD.', 'SITI CABLE NETWORK LTD.', 'NETWORK186.BO', 'DEN Networks Limited', 'SUNTV6.BO', 'NEWTIME INFRASTRUCTURE LIMITED', 'Nexus Commodities & Technologi', 'NGL Fine-Chem Ltd.', 'NHPC Ltd.', 'Nirav Commercials Limited', 'NILACHAL REFRACTORIES LTD.', 'NIMBUS INDUSTRIES LTD.', 'Deepak Nitrite Ltd.', 'Sadhana Nitro Chem Ltd.', 'NITINFIRE6.BO', 'NIIT LTD.', 'Nilkamal Limited', 'NICCO CORPORATION LTD.', 'INDU NISSAN OXO-CHEMICAL INDUS', 'Nicco Parks & Resorts Limited', 'NITIN INDUSTRIES LTD.', 'Nitin Fire Protection Industries Limited', 'NITINFIRE*', 'INDO-NATIONAL LTD.', 'i-NAV RELIANCE NIFTY', 'NIVYAH INFRASTRUCTURE & TELECO', 'NIMBUS PROJECTS LTD.', 'CHANNEL NINE ENTERTAINMENT LTD', 'NK Industries Ltd.', 'NMDC LTD.', 'FOURTH GENERATION INFORMATION', 'GRINDWELL NORTON LTD.', 'NORTHERN PROJECTS LTD.', 'NOVA PUBLICATIONS INDIA LTD', 'NOVARTIS INDIA LTD.', 'NovaGold Petro Resources Ltd', 'NOVARTIND6.BO', 'NOCIL Limited', 'WELLNESS NONI LTD.', 'NOIDA TOLL BRIDGE COMPANY LTD.', 'NRC Ltd.', 'NR International Ltd.', 'NTC INDUSTRIES LTD.', 'NUTRAPLUS INDIA LTD', 'Nu Tek India Ltd', 'NUCHEM LTD.', 'Sampre Nutritions Ltd.', 'Nutricircle Limited', 'NUMERO UNO PROJECTS LTD.', 'Nu Tech Corporate Services Ltd', 'NUBAL (INDIA) LTD.', 'NYSSA CORPORATION LIMITED', 'NYLOFIL.BO', 'Silver Oak India Ltd.', 'OASIS MEDIA MATRIX LTD.', 'OASIS TRADELINK LTD', 'OASIS TEXTILES LTD.', 'SILVER OAK COMMERCIAL LTD.', 'Oasis Securities Ltd.', 'OBEROI REALTY LTD.', 'Overseas Synthetics Ltd.', 'OBJECTONE INFORMATION SYSTEMS', 'OCEAN INFRASTRUCTURE LTD.', 'Odyssey Technologies Limited', 'ODYSSEY VIDEO COMMUNICATIONS L', 'Odyssey Corporation Ltd', 'ORIENTAL BANK OF COMMERCE', 'Container Corporation of India Ltd.', 'Tube Investments of India Limited', 'ORIENTBANK6.BO', 'STATE TRADING CORPORATION OF I', 'AUTOMOBILE PRODUCTS OF INDIA L', 'STCINDIA6.BO', 'OFSS6.BO', 'OFS Technologies Limited', 'SCI4.BO', 'United Bank of India', 'Universal Office Automation Ltd.', 'Union Bank of India', 'TOURISM FINANCE CORPORATION OF', 'STATE BANK OF INDIA', 'Power Grid Corporation of India Limited', 'POWERGRID4.BO', 'SCI6.BO', 'STEEL TUBES OF INDIA LTD.', 'OIL COUNTRY TUBULAR LTD.', 'Savita Oil Technologies Limited', 'TIDE WATER OIL (INDIA) LTD.', 'OIL6.BO', 'Inter State Oil Carrier Ltd.', 'Olympia Industries Ltd.', 'OLYMPIC MANAGEMENT & FINANCIAL', 'OLYMPIC CARDS LTD.', 'OLYMPIA CAPITALS LTD.', 'OMANSH ENTERPRISES LTD', 'OMKAR PHARMACHEM LTD.', 'OMMETALS6.BO', 'OMAX AUTOS LTD.', 'Omnitex Industries (India) Limited', 'Omega Interactive Technologies Limited', 'SHREE TULSI ONLINE.COM LTD.', 'Ontrack Systems Limited', 'ONIDA SAKA LTD.', 'ONMOBGLO', 'ONESOURCE TECHMEDIA LTD.', 'ONIDA.BO', 'ONWARD TECHNOLOGIES LTD.', 'O. P. Chains Limited', 'Optimus Finance Limited', 'ORIQUAL.BO', 'Oriental Veneer Products Ltd.', 'Oricon Enterprises Limited', 'Smruthi Organics Limited', 'ORISSA MINERALS DEVELOPMENT CO', 'ORIENT TRADELINK LTD.', 'SCAN ORGANICS LTD.', 'ORIENTAL TRIMEX LTD.', 'Ortel Communications Limited', 'VINATI ORGANICS LTD.', 'PANCHSHEEL ORGANICS LTD.', 'ORIENT REFRACTORIES LTD.', 'Orchid Pharma Limited', 'ORIENT GREEN POWER COMPANY LTD', 'VIBROS ORGANICS LTD.', 'UNICORN.BO', 'Pentokey Organy (India) Limited', 'MANGALAM ORGANICS LIMITED', 'S.S. Organics Limited', 'ORIENTAL INDUSTRIAL INVESTMENT', 'ORBIT POLYESTER LTD.', 'Orient Beverages Ltd.', 'ORG INFORMATICS LTD.', 'Meghmani Organics Limited', 'REVATI ORGANICS LTD.', 'ORBIT CORPORATION LTD.', 'OROSIL SMITHS INDIA LTD.', 'Oriental Hotels Limited', 'Oswal Spinning and Weaving Mills Limited', 'Oswal Overseas Limited', 'OSIAN INDUSTRIES LTD.', 'OSEASPRE CONSULTANTS LTD.', 'OTCO International Ltd.', 'OUDH SUGAR MILLS LTD.', 'Unimode Overseas Limited', 'TRIPEXO.BO', 'SUN TECHNO OVERSEAS LTD.', 'GRM Overseas Ltd.', 'Pradip Overseas Limited', 'PONDY OXIDES & CHEMICALS LTD.', 'Sarda Papers Limited', 'Sanjivani Paranteral Ltd.', 'Ruchira Papers Ltd.', 'PARAS SYN LT', 'Pratik Panels Ltd.', 'Pankaj Polymers Ltd', 'Palsoft Infosystems Ltd.', 'PADMINI TECHNOLOGIES LTD.', 'Pacific Industries Limited', 'Page Industries Limited', 'PANAMA PETROCHEM LTD.', 'Simplex Papers Ltd.', 'Sibar Auto Parts Ltd', 'Indo Pacific Projects Limited', 'PANORAMIC UNIVERSAL LTD.', 'Pankaj Piyush Trade & Inv. Ltd', 'SARIKA PAINTS LTD.', 'PAN India Corporation Ltd.', 'PARAMOUNT PRINTPACKAGING LTD.', 'Parle Software Limited', 'PITAMBAR COATED PAPERS LTD.', 'PASCHIM PETROCHEM LTD.', 'Pariksha Fin-Invest-Lease Limi', 'PANASONIC CARBON INDIA CO.LTD.', 'PATSPIN INDIA LTD.', 'Panchmahal Steels, Ltd.', 'PARAMOUNT COMMUNICATIONS LTD.', 'RAINBOW PAPERS LTD.', 'PASHUPATI SEOHUNG LTD.', 'PARRYS SUGAR INDUSTRIES LTD.', 'PARASRAMPURIA SYNTHETICS LTD.', 'PAREKH PLATINUM LTD.', 'Speciality Papers Ltd.', 'Panther Industrial Products Ltd', 'Padmanabh Industries Ltd', 'STAR PAPER MILLS LTD.', 'PADMALAYA TELEFILMS LTD.', 'Pasupati Spinning & Weaving Mills Limited', 'PARAS SYN PP', 'AUTO PAL IND', 'MANSAROVER PAPER & INDUSTRIES', 'Parsvnath Developers Limited', 'SHALIMAR PAINTS LTD.', 'PANAFIC INDUSTRIALS LTD', 'PANKAJ POLYPACK LTD.', 'CHADHA PAPERS LTD.', 'PAN AUTO LTD.', 'Innovative Tech Pack Ltd.', 'Pagaria Energy Limited', 'Panasonic Energy India Company Limited', 'PANAMA*', 'PUDUMJEE PULP & PAPER MILLS LT', 'SUPERB PAPERS LTD.', 'PAINTEX CHEMICALS (BOMBAY) LTD', 'PASHUPATI CABLES LTD.', 'Paramount Cosmetics (India) Limited', 'Sree Sakthi Paper Mills Limited', 'Soma Papers and Industries Limited', 'SHIVA PAPER MILLS LTD.', 'PAWANSUT HOLDINGS LTD.', 'TCPL Packaging Limited', 'Pba Infrastructure Ltd.', 'PBM Polytex Limited', 'PCS Technology Limited', 'PC Products India Limited', 'Pudumjee Paper Products Limite', 'PUDUMJEE INDUSTRIES LTD.', 'SUPREME PETROCHEM LTD.', 'PERSIAN CARPET & TEXTILES LTD.', 'Continental Petroleums Ltd.', 'Interlink Petroleum Ltd.', 'PETRON ENGINEERING CONSTRUCTIO', 'Linc Pen & Plastics Limited', 'RAMA PETROCHEMICALS LTD.', 'PENTAF PR-FC', 'Permanent Magnets Limited', 'PEARL ENGINEERING POLYMERS LTD', 'PIRAMAL ENTERPRISES LTD.', 'PENTAFOUR PRODUCTS LTD.', 'PNTSF6.BO', 'PENTA PHARMADYES LTD.', 'Tamilnadu Petroproducts Ltd.', 'Pervasive Commodities Limited', 'Rajasthan Petro Synthetics Limited', 'PEARL POLYMERS LTD.', 'PARAS PETROFILS LTD.', 'SARLA PERFORMANCE FIBERS LTD.', 'PEOPLES INVESTMENTS LTD.', 'PET PLASTICS LTD.', 'PENNAR IND*', 'SOUTHERN PETROCHEMICALS LTD.', 'PENTAFOUR SOLEC TECHNOLOGY LTD', 'SUPREME PET*', 'Peeti Securities Ltd', 'Chennai Petroleum Corporation Ltd', 'Confidence Petroleum India Ltd.', 'PENNARIND*', 'PRIME PETRO PRODUCTS LTD.', 'SHAYONA PETROCHEM LTD.', 'Perfectpac Ltd.', 'PENNAR INDUSTRIES LTD.', 'PENTAMEDIA GRAPHICS LTD', 'Power Finance Corporation Limited', 'PFL Infotech Ltd', 'Pfizer Limited', 'PFIZER6.BO', 'PG INDUSTRY LTD.', 'SMS Pharmaceuticals Limited', 'Relish Pharmaceuticals Limited', 'Plethico Pharmaceuticals Limited', 'Pharmaids Pharmaceuticals Ltd.', 'Sun Pharmaceutical Industries Limited', 'SURYA PHARMACEUTICAL LTD.', 'PH Capital Ltd.', 'PH TRADING LTD.', 'Bacil Pharma Ltd', 'SHASUNPHAR.BO', 'SUPRIYA PHARMACEUTICALS LTD.', 'SWORD & SHIELD PHARMA LTD.', 'SHREEJI PHOSPHATE LTD.', 'RICHLINE PHARMA LTD.', 'Pneumatic Holdings Limited', 'TORNTPHARM6.BO', 'TORRENT PHARMACEUTICALS LTD.', 'Vista Pharmaceuticals Limited', 'Twilight Litaka Pharma Limited', 'Sandu Pharmaceuticals Limited', 'Rama Phosphates Limited', 'PHOENIX INTERNATIONAL LTD.', 'Samrat Pharmachem Limited', 'BAFNA PHARMACEUTICALS LTD.', 'PHOENIX-E-W', 'TOHEAL PHARMACHEM LTD.', 'PHOENIX TOWNSHIP LTD', 'POLAR PHARMA INDIA LTD.', 'Phaarmasia Limited', 'BAL PHARMA LTD.', 'Photon Capital Advisors Ltd.', 'VYSALI PHARMACEUTICALS LTD.', 'Phyto Chem (India) Limited', 'PIRAMAL PHYTOCARE LIMITED', 'SUNPHARMA4.BO', 'AUROBINDO PHARMA LTD.', 'Pix Transmissions Ltd.', 'Pioneer Investcorp Limited', 'Pidilite Industries Limited', 'Poddar Pigments Limited', 'AUTO PINS (INDIA) LTD.', 'PINKY CHEMICALS LTD.', 'PODDAR PIG*', 'Texmo Pipes and Products Limited', 'Srikalahasthi Pipes Limited', 'PREMIER PIPES LTD.', 'P.I.INDUSTRIES LTD.', 'Ultramarine & Pigments Ltd.', 'PIYUSH STEELS LTD.', 'Pithampur Poly Products Ltd', 'Pincon Spirit Limited', 'SKIP PLASTICS LTD.', 'Sand Plast India Ltd', 'Promact Plastics Limited', 'Prima Plastics Ltd.', 'TAINWALA CHEMICALS & PLASTICS', 'PM Telelinnks Ltd', 'PNC Infratech Limited', 'Polyplex Corporation Limited', 'Polycon International Ltd.', 'Polaris Consulting & Services Limited', 'Swadeshi Polytex Ltd.', 'TIJARIA POLYPIPES LTD.', 'ADANIPOWER6.BO', 'RTS Power Corporation Ltd.', 'Starlit Power Systems Limited', 'STERLING POWERGENSYS LTD', 'DELTA POLYSTERS LTD.', 'Polson Ltd.', 'POLY MEDICURE LTD.', 'Brilliant Portfolios Ltd.', 'RAMGOPAL POLYTEX LTD.', 'TORNTPOWER6.BO', 'POLYTEX INDIA LTD.', 'SOUTH POLE SECURITIES LTD.', 'POLYMAC THERMOFORMERS LTD', 'Pochiraju Industries Ltd.', 'PONNI SUGARS (ERODE) LTD.', 'Polymechplast Machines, Ltd.', 'Pokarna Ltd.', 'VIRGO POLYMERS (INDIA) LTD.', 'Maharashtra Polybutenes Ltd.', 'VENUS POWER VENTURES (INDIA) L', 'VALLABH POLY-PLAST INTERNATION', 'Suryachakra Power Corporation Limited', 'RATTANINDIA POWER LTD.', 'S&S POWER SWITCHGEAR LTD.', 'S.E. POWER LTD.', 'PREMIER POLYFILM LTD.', 'TORRENT POWER LTD.', 'POLAR INDUSTRIES LTD.', 'RAJASTHAN POLYESTERS LTD.', 'POCL ENTERPRISES LTD', 'VIKASH METAL & POWER LTD.', 'MIDLAND POLYMERS LTD.', 'INDIA POLYSPIN LTD.', 'Mideast Portfolio Management Limited', 'SHEKHAWATI POLY-YARN LTD.', 'T D POWER SYSTEMS LTD.', 'VARDHAMAN WIRES & POLYMERS LTD', 'IND RENEWABLE ENERGY LTD', 'SANGHI POLYESTERS LTD.', 'CAREER POINT LTD.', 'RPOWER4.BO', 'HONDA SIEL POWER PRODUCTS LTD.', 'VARDHMAN POLYTEX LTD.', 'VENTRON POLYMERS LTD.', 'USHMA POLYMERS LTD.', 'ADVANCE POWERINFRA TECH LIMITE', 'Polychem Ltd.', 'Computer Point Ltd.', 'VINAYAK POLYCON INTERNATIONAL', 'Rathi Steel and Power Ltd', 'Polylink Polymers ( India ) Limited', 'BEST STEEL LOGISTICS LTD', 'INDPLYF.BO', 'TOP CASSE PP', 'SREI PP2.5PD', 'SOFT TECH PP', 'V K SOFT PP', 'SEQ SOFT PP', 'Shalimar Productions Limited', 'Prism Informatics Ltd.', 'Pricol Ltd.', 'Premier Ltd.', 'Control Print Ltd', 'STI PRODUCTS INDIA LTD.', 'Sadbhav Infrastructure Project', 'Integrated Proteins Ltd.', 'PRAJIND6.BO', 'PRESISH.BO', 'PRIME URBAN DEVELOPMENT INDIA', 'Chandra Prabhu International Ltd.', 'PRASHANT INDIA LTD.', 'Precision Containeurs Limited', 'SAGAR PRODUCTIONS LIMITED', 'PURVA6.BO', 'Puravankara Projects Limited', 'PRIMA INDUSTRIES LTD.', 'In House Productions Limited', 'RPP INFRA PROJECTS LTD.', 'INLAND PRINTERS LTD.', 'Prime Industries Ltd.', 'Pressure Sensitive Systems (India) Ltd.', 'Priya Ltd.', 'Precision Wires India Ltd.', 'ROCKLINE PROJECT LTD.', 'Satra Properties India Ltd', 'ENERGY PRODUCTS (INDIA) LTD.', 'Tentiwala Metal Products Limit', 'INGERMS.BO', 'Premier Synthetics Ltd.', 'PREMIND.BO', 'PREMIER PROTEINS LTD.', 'SHRI SAINATH PROTEINS LTD.', 'Investment & Precision Castings Ltd', 'PRISMER.BO', 'U.P.MINERAL PRODUCTS LTD.', 'PREMIER SYNT', 'Sarda Proteins Ltd.', 'TRANSOCEANIC PROPERTIES LTD.', 'Shakti Press Limited', 'PREM SOMANI FINANCIAL SERVICES', 'PRAVEEN PROPERTIES LTD.', 'PROZONINTU', 'SAGAR SOYA PRODUCTS LTD.', 'Precision Camshafts Limited', 'PREMIUM INTERNATIONAL FINANCE', 'PSL LTD.', 'PYRAMID SAIMIRA THEATRE LTD.', 'PUNJAB & SIND BANK', 'PTC Industries Ltd.', 'PTC India Limited', 'PTC INDIA LTD', 'PURSHOTTAM INVESTOFIN LTD', 'Punit Commercials Ltd.', 'Rishiroop Limited', 'PUSHPSONS INDUSTRIES LTD.', 'PULSAR INTERNATIONAL LTD.', 'PUNCTUAL TRADING LTD.', 'Punjab Woolcombers Limited', 'Punjab Communications Ltd.', 'Rama Pulp and Papers Limited', 'SHAKTI PUMPS (INDIA) LTD.', 'Roto Pumps Limited', 'PUNSUMI INDIA LTD.', 'Purohit Construction Limited', 'PVV Infra Limited', 'PVR Limited', 'PVR LTD*', 'Prakash Woollen & Synthetic Mi', 'Pyxis Finvest Limited', 'Rasoi Ltd.', 'Rammaica (India) Ltd.', 'Ramco Systems Limited', 'Ramco Industries Limited', 'Rajvir Industries Ltd', 'RANSI SOFTWARE (INDIA) LTD.', 'INDIA RADIATORS LTD.', 'Rander Corporation Ltd.', 'INDO RAMA SYNTHETICS (INDIA) L', 'Rainbow Denim Ltd.', 'RADIX INDUSTRIES (INDIA) LIMIT', 'RANE (MADRAS) LTD.', 'Raasi Refractories Ltd.', 'R T C L Limited', 'Rap Media Ltd.', 'RAMA VISION LTD.', 'RAPID INVESTMENTS LTD.', 'Radhagobind Commercial Limited', 'RAYMOND6.BO', 'RANE ENGINE VALVE LTD.', 'Rajkamal Synthetics Ltd.', 'RAIN', 'Raminfo Limited', 'RATNAMANI METALS & TUBES LTD.', 'RAJAPALAYAM MILLS LTD.', 'BARODA RAYON CORPORATION LTD.', 'RANE HOLDINGS LTD.', 'RAMS TRANSFORMERS LTD.', 'Rasandik Engineering Industries India Ltd.', 'Anjani Foods Limited', 'Shree Rang Mark Travels Limited', 'Raymond Limited', 'RATTANINDIA INFRASTRUCTURE LTD', 'RAJESH MALLEABLES LTD.', 'RAJ RAYON INDUSTRIES LIMITED', 'RANE COMPUTERS CONSULTANCY LTD', 'Royale Manor Hotels & Industries Ltd.', 'Raghuvir Synthetics Ltd.', 'Ravileela Granites Ltd.', 'RAVI SPINNING LTD.', 'Shivalik Rasayan Ltd.', 'RANE BRAKE LINING LTD.', 'RAGHAV INDUSTRIES LTD.', 'RAJLAXMI INDUSTRIES LTD.', 'RADIANT ROTOGRAVURE LTD.', 'Rana Sugars Ltd.', 'SHREE RAM 19', 'RAJSHREE SUGARS & CHEMICALS LT', 'RAIN6.BO', 'Ranklin Solutions Ltd.', 'Rallis India Limited', 'RAINBRE.BO', 'RANJIT SECURITIES LTD.', 'RAJENDRA MINING SPARES CO.LTD.', 'RAJESH SOLVEX LTD.', 'RAMKY INFRASTRUCTURE LTD.', 'Rama Steel Tubes Limited', 'Rajkot Investment Trust Limite', 'RAJSANKET REALTY LIMITED', 'VASUNDHARA RASAYANS LTD', 'Ramsarup Industries Ltd.', 'RAJA BAHADUR INTERNATIONAL LTD', 'Sri Ramakrishna Mills (Coimbatore) Limited', 'Ramsons Projects Limited', 'RATTAN VANASPATI LTD.', 'Shree Ram Urban Infrastructure, Ltd.', 'Rajoo Engineers Ltd.', 'Desh Rakshak Aushdhalaya Limited', 'RDB RASAYANS LTD.', 'RAAJ MEDISAFE INDIA LTD.', 'Raghunath International Ltd.', 'Rasoya Proteins Limited', 'Rahul Merchandising Limited', 'Raj Packaging Industries Ltd.', 'PARTAP RAJASTHAN SPECIAL STEEL', 'RADAAN MEDIAWORKS (I) LTD.', 'R.B.GUPTA FINANCIALS LTD.', 'RCL RETAIL LTD.', 'RCI INDUSTRIES & TECHNOLOGIES', 'Reliance Communications Ltd.', 'RDB REALTY & INFRASTRUCTURE LT', 'Reliance Defence and Engineeri', 'Rishabhdev Technocable Limited', 'Resonance Specialties Limited', 'Reliance Infrastructure Ltd', 'Relic Technologies Ltd.', 'Regaliaa Realty Ltd.', 'Refex Industries Limited', 'Indoco Remedies Limited', 'Real Growth Commercial Enterpr', 'ROHINI STRIPS LTD.', 'RHUTU UDYOG (INDIA) LTD.', 'Ritesh International Ltd.', 'Riba Textiles Limited', 'RISA INTERNATIONAL LTD.', 'Ruttonsha International Rectifier Ltd.', 'Ricoh India Limited', 'Rico Auto Industries Limited', 'Rishiroop Rubber (International) Ltd.', 'Rishiroop Limited', 'Richa Industries Ltd', 'RIDHI SYNTHETICS LTD.', 'RISHI TECHTEX LTD.', 'Reliance Industrial Infrastructure Limited', 'Riga Sugar Co. Ltd.', 'R.J.SHAH & CO.LTD.', 'RLF Ltd.', 'ROSELABS LTD.', 'RMI STEELS LTD.', 'R&B DENIMS LTD', 'RNB INDUSTRIES LTD.', 'Rockon Enterprises Limited', 'Surya Roshni Limited', 'ROSSELL INDIA LTD.', 'ROOFIT INDUSTRIES LTD.', 'ROPLAS (INDIA) LTD.', 'Rolta India Limited', 'ROSEKAMAL TEXTILES LTD.', 'ROCKONFIN.BO', 'Roopa Industries Ltd.', 'Roselabs Finance Limited', 'SHAKTI RODS & WIRES LTD.', 'RODIUM REALTY LIMITED', 'ROSE MERC.LTD.', 'Rollatainers Limited', 'ROSE INVESTMENTS LTD.', 'TAYO ROLLS LTD.', 'ROCKLAND THERMIONICS LTD.', 'ROYAL INDIA CORPORATION LIMITE', 'Rolcon Engineering Company Limited', 'RPG LIFE SCIENCES LTD.', 'REAL NEWS & VIEWS LTD', 'R. R. Securities Ltd', 'SAAG RR INFRA LTD.', 'RSC International Ltd', 'R.S.SOFTWARE INDIA LTD.', 'RSWM LTD.', 'R SYSTEMS INTERNATIONAL LTD.', 'RSL TEXTILES (INDIA) LTD.', 'R.S.PETROCHEMICALS LTD.', 'R Systems International Limite', 'R.S CORPORATION LTD.', 'Rubfila International Limited', 'RUSHIL DECOR LTD.', 'RUTRON INTERNATIONAL LTD.', 'RUSODAY.BO', 'SHREE RUBBER INDUSTRIES LTD.', 'RUCHI INFRASTRUCTURE LTD.', 'MAGNUS RUBBER INDUSTRIES LTD.', 'Indag Rubber Limited', 'RUNEECHA TEXTILES LTD.', 'Ruchi Soya Industries Limited', 'DEWAN RUBBER INDUSTRIES LTD.', 'INDRUBR.BO', 'RUDRAKSH CAP-TECH LTD.', 'RUBRA MEDICAMENTS LTD.', 'RUPA & COMPANY LTD.', 'The Rubber Products Limited', 'MEHTA RUBBER CHEMICALS LTD.', 'HOTEL RUGBY LTD.', 'Savant Infocomm Ltd.', 'SAVERA INDUSTRIES LTD.', 'Sat Industries Limited', 'Sasken Communication Technologies Limited', 'Saregama India Ltd', 'Samtel Color Ltd.', 'Saksoft Limited', 'Saven Technologies Limited', 'The Sandesh Limited', 'SANOFI INDIA LTD', 'SAI CAPITAL LTD.', 'SALEM TEXTILES LTD.', 'REMI SALES & ENGINEERING LTD.', 'SASKEN COM*', 'SAKTHISUGAR', 'Tirupati Sarjan Limited', 'SANTOWIN CORPORATION LTD.', 'SANBLUE CORPORATION LTD.', 'SARAF SONS (TRADERS) LTD.', 'SARUP INDUSTRIES LTD.', 'Samtel India Limited', 'SAGAR TOURIST RESORTS LTD.', 'SALORA INTERNATIONAL LTD.', 'SBEC Sugar Limited', 'SB & T INTERNATIONAL LTD.', 'SB&TINTL6.BO', 'SBEC SYSTEMS (INDIA) LTD.', 'Scooters India Ltd.', 'Schablona India Ltd', 'SCOPE INDUSTRIES (INDIA) LIMIT', 'SCINTILLA SOFTWARE TECHNOLOGY', 'Suven Life Sciences Limited', 'SEQUENT SCIENTIFIC LTD.', 'CAMLIN FINE SCIENCES LTD.', 'Suncare Traders Limited', 'Scan Steels Limited', 'Maharashtra Scooters Ltd.', 'THOMAS SCOTT (INDIA) LIMITED', 'SCAN PROJECTS LTD.', 'Sunshine Capital Ltd.', 'Skypak Service Specialists Ltd.', 'SELLWIN TRADERS LIMITED', 'Ser Industries Ltd', 'PRIME SECURITIES LTD.', 'Vintage Securities Ltd.', 'SENTHIL INFOTEK LTD', 'SERENE INDUSTRIES LTD.', 'PROVESTMENT SERVICES LTD.', 'SFL INDUSTRIES LTD.', 'SFL International Limited', 'SFL International Limited', 'SGN Telecoms Ltd.', 'Shrenuj & Company Limited', 'Shoppers Stop Limited', 'Sharp India Ltd.', 'SHONKH TECHNOLOGIES INTERNATIO', 'VARUN SHIPNG', 'Shree Precoated Steels Limited', 'SHIVA TEXYARN LTD.', 'SHYAMA INFOSYS LTD.', 'SHAAN INTERWELL (INDIA) LTD.', 'SHYAMKAMAL INVESTMENTS LTD.', 'Sharp Industries Ltd.', 'SHILPI CABLE TECHNOLOGIES LTD.', 'Shreyas Intermediates Limited', 'LIBERTY SHOES LTD.', 'SHARAT INDUSTRIES LTD.', 'SHRUTI SYNTHETIC LTD.', 'SHAMKEN COTSYN LTD.', 'SHREE INDUSTRIES LTD.', 'SHEENA.BO', 'Shardul Securities Ltd.', 'Shailja Commercial Trade Frenz', 'SHARP INVESTMENTS LTD', 'SHAMKEN SPINNERS LTD.', 'Western India Shipyard Limited', 'SHREEJI INDUSTRIES LTD.', 'SHENTR CHEMI', 'SHESHADRI INDUSTRIES LIMITED', 'Shricon Industries Ltd.', 'Shristi Infrastructure Development Corporation Ltd.', 'SHREYANS INDUSTRIES LTD.', 'RENUKA6.BO', 'SHIKHAR CONSULTANTS LTD.', 'SHREENATH INVESTMENTS CO.LTD.', 'SHREE METALLOYS LTD.', 'SHIVA SUITINGS LTD.', 'SHYAMAL HOLDINGS & TRADING LTD', 'Shilp Gravures Limited', 'SHEMAROO ENTERTAINMENT LIMITED', 'SHABA CHEMICALS LTD.', 'SHIVAM AUTOTECH LTD.', 'SHYAM TELECOM LTD.', 'Varun Shipping Co. Ltd.', 'Sharp Scan & Prints Limited', 'SIDDHI VINAYAK SHIPPING CORPOR', 'SHENTRACON CHEMICALS LTD.', 'SHREE SURGOVIND TRADELINK LTD.', 'SHAMROCK INDUSTRIAL CO.LTD.', 'SHAH CONSTRUCTION CO.LTD.', 'SHREE SHALEEN TEXTILES LIMITED', 'SHILPA MEDICARE LTD.', 'SHELTER INFRA PROJECTS LTD.', 'SHALIBHADRA INFOSEC LTD.', 'SHRIRAM TRANSPORT FINANCE CO.L', 'Shreenath Industrial Investmen', 'Shree Pacetronix Ltd', 'SHELL INFOTECH LTD.', 'Shilchar Technologies Limited', 'Shree Securities Ltd.', 'SHRIDIN*', 'SHIVGARH RESORTS LTD.', 'SIP Industries Ltd.', 'Sintex Industries Limited', 'SIMPLEX INFRASTRUCTURES LTD.', 'SILVERLINE TECHNOLOGIES LTD.', 'Sika Interplant Systems Ltd.', 'Siemens Limited', 'Simmonds-Marshall Ltd', 'Sinclairs Hotels Limited', 'SILKTEX LTD.', 'SIRIS LTD.', 'South India Projects Ltd.', 'SILSPL', 'SIL INVESTMENTS LTD.', 'SIBAR SOFTWARE SERVICES (INDIA', 'SUPERIOR INDUSTRIAL ENTERPRISE', 'SAGAR SILK INDUSTRIES LTD.', 'STANDARD INDUSTRIES LTD.', 'SIRHIND STEEL LTD.', 'SILVERPOINT INFRATECH LTD', 'Sirohia & Sons Limited', 'Simbhaoli Sugars Limited', 'Sicagen India Limited', 'SINNER ENERGY INDIA LIMITED', 'REI Six Ten Retail Limited', 'SIMPLEX CASTINGS LTD.', 'SIDDHI VINAYAK METAL COMPANY L', 'Simplex Mills Company Limited', 'SIMCO INDUSTRIES LTD.', 'Singer India Ltd.', 'SIYARAM SILK MILLS LTD.', 'SIDDHARTHA TUBES LTD.', 'SINDU VALLEY TECHNOLOGIES LTD.', 'SIGNET INDUSTRIES LIMITED', 'SUVIDHA INFRAESTATE CORPORATIO', 'SINDHU TRADE LINKS LIMITED', 'Simplex Realty Limited', 'SI CAPITAL & FINANCIAL SERVICE', 'SIGRUN HOLDINGS LIMITED', 'SIBAR MEDIA & ENTERTAINMENT LT', 'SJ Corporation Ltd.', 'SJVN Limited', 'SKP Securities Limited', 'SKIPPER LTD', 'SKSMICRO6.BO', 'SATKAR FINLEASE LTD', 'SRI SKANDAN INDUSTRIES LTD.', 'Sri Krishna Constructions (Ind', 'SKF INDIA LTD.', 'SKYLID TELECOMMUNICATION LTD.', 'SKUMAR SYNFA', 'SKUMARSYNFAB', 'SKS MICROFINANCE LTD.', 'SKUMAR SYNFA', 'SMILAX INDUSTRIES LIMITED', 'SMSPHARMA*', 'Smart Finsec Limited', 'SNOWCEM INDIA LTD.', 'SNS Textiles Ltd.', 'Sun Source (india) Ltd', 'Soma Textiles & Industries Limited', 'Solid Stone Company Limited', 'Softech Infinium Solutions Limited', 'INFO-DRIVE SOFTWARE LTD.', 'TAKSHEEL SOLUTIONS LTD.', 'TOWA SOKKI LTD.', 'COMPUCOM SOFTWARE LTD.', 'TELESYS SOFTWARE LTD.', 'TELEDATA TECHNOLOGY SOLUTIONS', 'CALIFORNIA SOFTWARE CO.LTD.', 'B2B Software Technologies Ltd.', 'WEP SOLUTIONS LTD.', 'SOFCOM SYSTEMS LIMITED', 'INTEGRA TELECOMMUNICATION & SO', 'SOLID CONTAINERS LTD.', 'Indian Infotech & Software Ltd.', 'SURANA SOLAR LTD.', 'CAUVERY SOFTWARE ENGINEERING S', 'aurionPro Solutions Limited', 'SOFTSOL IND*', 'Sobha Limited', 'MAARS SOFTWARE INTERNATIONAL L', 'Unisys Softwares & Holdings Industries Limited', 'Sonal Mercantile Limited', 'SUPERIOR SOX LTD.', 'AURUM SOFT SYSTEMS LIMITED', 'Prithvi Information Solutions Limited', 'WASHINGTON SOFTWARES LTD.', 'VALUEMART RETAIL SOLUTIONS LTD', 'SOUNDCRAFT.BO', 'PRITHVI EXCHANGE(INDIA) LTD', 'SOFTWARE TECHNOLOGY GROUP INTE', 'Spanco Ltd', 'Take Solutions Ltd.', 'USG TECH SOLUTIONS LTD.', 'Tera Software Ltd.', 'SOURCE INDUSTRIES (INDIA) LTD.', 'The South India Paper Mills Limited', 'SPS International Ltd.', 'Spl Industries Ltd', 'MILK SPECIALITIES LTD.', 'SPL TECHNOCHEM LTD.', 'United Spirits Limited', 'SPICEMBBPH', 'SPARC SYSTEMS LTD.', 'Spentex Industries Limited', 'SAMRAT SPINNERS LTD.', 'Vertex Spinning Limited', 'Spenta International Limited', 'SPECULAR MARKETING & FINANCING', 'SQL STAR INTERNATIONAL LTD.', 'SQLST6.BO', 'SQSBFSI', 'SREECHEM RESINS LTD.', 'SRS REAL INFRASTRUCTURE LTD.', 'S R K INDUSTRIES LTD.', 'SRI MALINI S', 'SRI VASAVI INDUSTRIES LTD.', 'SREEL2.BO', 'SAMRUDDHI REALTY LTD.', 'SRF LTD.', 'SRS LTD.', 'SRF LIMITED*', 'SREINFRA6.BO', 'Sri Vajra Granites Limited', 'S R Industries Limited', 'SRS FINANCE LTD', 'SREELEATHERS LTD.', 'SRM Energy Ltd', 'SRIYANSH STEEL LTD.', 'TVS Srichakra', 'SREI INTERNA', 'SUNSTAR REALTY DEVELOPMENT LTD', 'SRH SYNTHETICS LTD.', 'SSK Lifestyles Limited', 'SSPDL Ltd', 'S&S INDUSTRIES & ENTERPRISES L', 'Stovec Industries, Ltd.', 'Starlog Enterprises Limited', 'SWEATAMBER STEEL LTD.', 'STERLING TOOLS LTD.', 'Sterlite Technologies Limited', 'TATA STEEL LTD.', 'S & T Corporation Limited', 'STEEL STRIPS LTD.', 'STELLAR CAPITAL SERVICES LTD', 'STANDARD BATTERIES LTD.', 'STI INDIA LTD.', 'STERLING SPINNERS LTD.', 'VISA Steel Ltd.', 'Steelcast Ltd', 'STELCO STRIPS LTD.', 'STOCKNET INTERNATIONAL LTD.', 'VISHWAS STEELS LTD.', 'Starlite Components Ltd.', 'Tirupati Starch & Chemicals Ltd.', 'S.T. SERVICES LIMITED', 'INERTIA STEEL LTD.', 'STERLING WEBNET LTD.', 'MALHOTRA STEEL INDUSTRIES LTD.', 'STANDARD CHARTERED PLC', 'STI GRANITE INDIA LTD.', 'STEL HOLDINGS LIMITED', 'STOTZ-BLACKSMITHS LTD.', 'STAR DELTA TRANSFORMERS LIMITE', 'Step Two Corporation Limited', 'STAMPEDE CAPITAL LIMITED', 'STANDARD SURFACTANTS LTD.', 'Sterling Green Woods Limited', 'STARCOM INFORMATION TECHNOLOGY', 'SUNCITY INDUSTRIES LTD.', 'Suditi Industries Ltd.', 'Sudal Industries Limited', 'SUMEET INDUSTRIES LTD.', 'Sumeru Industries Ltd.', 'SURAJ HOLDINGS LTD.', 'Suchitra Finance & Trading Com', 'SURYODAYA PLASTICS LTD.', 'Sujala Trading & Holding Ltd.', 'SUMMIT SECURITIES LTD.', 'SURBHI INDUSTRIES LTD.', 'SUBEX LTD.', 'Sujana Towers Limited', 'SUNKU.BO', 'Indian Sucrose Ltd.', 'Surya India Limited', 'SUNLAKE RESORTS & HOTELS LTD.', 'SURYA INDUSTRIAL CORPORATION L', 'SURAJ LTD.', 'SULABH ENGINEERS & SERVICES LT', 'SURAJ INDUSTRIES LTD.', 'SUCHAK TRADING LTD.', 'SURANA INDUSTRIES LTD.', 'SUNFLEX FINANCE & INVESTMENTS', 'SUPRAJIT ENGINEERING LTD.', 'SUJANATWR6.BO', 'INDIA SUGARS & REFINERIES LTD.', 'SURYAJYOTI SPINNING MILLS LTD.', 'SUNRISE INDUSTRIAL TRADERS LTD', 'SUN INFOWAYS LTD.', 'Suraj Products Ltd.', 'Subros', 'Supertex Industries Ltd.', 'Super Bakers (India) Ltd.', 'SUDARSHAN CHEMICAL INDUSTRIES', 'SWASTIK SURFACTANTS LTD.', 'UGAR SUGAR WORKS LTD.', 'SUJANA UNIVERSAL INDUSTRIES LT', 'SURANA CORPORATION LTD.', 'SURYALAKSHMI COTTON MILLS LTD.', 'MANGALWEDHA SUN-SOYA LTD.', 'Sundaram Brake Linings Ltd.', 'PRUDENTIAL SUGAR CORPORATION L', 'SUPER SPINNING MILLS LTD.', 'Suncity Synthetics Ltd.', 'SURYA MARKETING LTD', 'SUDAR INDUSTRIES LTD.', 'Sunshield Chemicals Ltd.', 'SW SURFACTNT', 'SUBH TEX (INDIA) LTD', 'Sungold Capital Ltd.', 'Surabhi Chemicals and Investments Ltd.', 'VENUS SUGAR LTD.', 'Surat Textile Mills Limited', 'SUNDARAM-CLAYTON LTD.', 'SAKTHI SUGARS LTD.', 'SUPERHOUSE LTD.', 'SUPER SYNCOTEX (INDIA) LTD.', 'Sunil Industries Limited', 'SVC Superchem Limited', 'Supreme Infrastructure India Ltd', 'SUPRA TRENDS LIMITED', 'Suryavanshi Spinning Mills Limited', 'Svam Software Ltd.', 'SVA INDIA LTD.', 'INTEGRA SWITCHGEAR LTD.', 'Swastika Investmart Limited', 'Swagatam Trading & Services Li', 'Swarna Securities Limited', 'SW INVESTMENTS LTD', 'SWORD-EDGE COMMERCIALS LIMITED', 'SWAGRUHA INFRASTRUCTURE LTD.', 'SWAN ENERGY LTD.', 'Symbiox Investment & Trading C', 'SAGAR SYSTECH LTD.', 'INFRONICS SYSTEMS LTD', 'TECPRO SYSTEMS LTD.', 'SONU SYNTHETICS LTD.', 'Systematix Corporate Services Limited', 'SYSTEMATIX SECURITIES LTD.', 'Syndicate Bank', 'Syngene International Limited', 'Maestros Mediline Systems Ltd', 'SYSTEL INFOTECH LTD.', 'VEDAVAAG SYSTEMS LTD.', 'Sybly Industries Ltd.', 'Sparc Systems Ltd.', 'Lippi Systems Ltd.', 'Prakash Woollen & Synthetic Mills Limited', 'DESIGN AUTO SYSTEMS LTD.', 'ADHUNIK SYNTHETICS LTD.', 'SYNERGY COSMETICS (EXIM) LTD.', 'WEBSOL ENERGY SYSTEM LTD.', 'Sylph Technologies Ltd.', 'SYNTHETICS & CHEMICALS LTD.', 'ENVIRO-CLEAN SYSTEMS LTD.', 'PRAJAY ENGINEERS SYNDICATE LTD', 'TAMARAI MILLS LTD.', 'TARAPUR TRANSFORMERS LTD', 'Taaza International Ltd', 'TAVERNIER RESOURCES LIMI', 'Tata Teleservices (Maharashtra) Limited', 'TALBROS AUTOMOTIVE COMPONENTS', 'Tata Motors Limited', 'Tamboli Capital Limited', 'TCS6.BO', 'Tai Industries Limited', 'Tata Coffee Ltd.', 'TARINI INTERNATIONAL LTD', 'Tata Investment Corporation Ltd.', 'TANFAC INDUSTRIES LTD.', 'Tata Communications Limited', 'TAPARIA TOOLS LTD.', 'Tamilnadu Steel Tubes Ltd.', 'TARMAT LTD.', 'TARANG PROJECTS & CONSULTANT L', 'TCI DEVELOPERS LTD.', 'TCI Industries Ltd.', 'Indo Tech Transformers Limited', 'ENKAY TEXFOODS INDUSTRIES LTD.', 'TEA TIME LTD.', 'Terai Tea Company Limited', 'SPANC TELESY', 'Balaji Telefilms Ltd.', 'Bala Techno Industries Limited .', 'Texplast Industries Ltd.', 'TERRYFAB (INDIA) LTD.', 'TECHIN', 'INDOVATION TECHNOLOGIES LTD.', 'Intense Technologies Ltd.', 'SANRHEA TECHNICAL TEXTILES LTD', 'TERRUZZI', 'Ventura Textiles Ltd.', 'TIME TECHNOPLAST LTD.', 'VEENA TEXTILES LTD.', 'TECHNOJET CONSULTANTS LTD.', 'Typhoon Financial Services Lim', 'Transwarranty Finance Limited', 'THOMASCOOK6.BO', 'THAPAR CONCAST LTD.', 'TILAKNAGAR INDUSTRIES LTD.', 'TIPS INDUSTRIES LTD.', 'Tirupati Industries (India) Limited', 'TIVOLI CONSTRUCTION LTD.', 'TIRTH PLASTIC LTD.', 'TIMBOR HOME LTD.', 'Tirupati Fincorp Limited', 'TILAKFIN.BO', 'Tirupati Tyres Ltd.', 'TIRUPATI INKS LTD.', 'TIRUPATI FIBRES & INDUSTRIES L', 'TIL Limited', 'TITAN6.BO', 'Timken India Limited', 'Titan Company Limited', 'Titan Securities Limited', 'TIMETECHNO6.BO', 'TIPS INDUST', 'TIMEX NCRPS', 'TINNA FINEX LTD.', 'Technocraft Industries (India) Ltd.', 'TMT (INDIA) LTD.', 'Miven Machine Tools Ltd', 'TOP TELEMEDIA LTD.', 'Total Hospitality Limited', 'TORRCABS.BO', 'TOKYO PLAST INTERNATIONAL LTD.', 'TRIDENT TOOLS LTD.', 'THIRANI PROJECTS LTD', 'TPI INDIA LTD.', 'TRANSCHEM LTD.', 'TRIVENI ENTERPRISES LTD', 'BRINDABAN HOLDINGS & TRADING L', 'TRIUMPH INTERNATIONAL FINANCE', 'TRIGYN TECHNOLOGIES LTD.', 'TRILLENIUM TECHNOLOGIES LTD.', 'Transpek Industry Limited', 'ENBEE TRADE & FINANCE LTD.', 'Trade Wings Limited', 'TRINITY TRADELINK LIMITED', 'TRANSTREAM INDIA.COM LTD.', 'DEVINSU TRADING LTD.', 'Sanco Trans Ltd.', 'TRUPTI TWISTERS LTD.', 'PRECIOUS TRADING & INVESTMENTS', 'Trans Financial Resources Limited', 'MERCURY TRADE LINKS LTD.', 'Gromo Trade & Consultancy Ltd.', 'TRIVENI ENGINEERING & INDUSTRI', 'Regency Trust Ltd.', 'VISHVJYOTI TRADING LTD.', 'MACK TRADING CO.LTD.', 'Trinethra Infra Ventures Ltd.', 'TRIVENI TURBINE LTD.', 'Master Trust Limited', 'Transformers & Rectifiers (India) Limited', 'TTI ENTERPRISE LTD', 'TTK PRESTIGE LTD.', 'TT Limited', 'TURBOTECH ENGINEERING LTD.', 'Tulip Star Hotels Ltd', 'Tuni Textile Mills Ltd.', 'Tulip Telecom Limited', 'TYPHOON HOLDINGS LTD.', 'UBE INDUSTRIES LTD.', 'UNITED BREWERIES LTD.', 'UB ENGINEERING LTD.', 'UBHOLDINGS6.BO', 'UCOBANK4.BO', 'UCO BANK', 'PRIYANKA UDYOG LTD.', 'BAGALKOT UDYOG LTD.', 'Uflex Limited', 'UFM INDUSTRIES LTD.', 'UFLEX6.BO', 'U G Hotels & Resorts Ltd.', 'UJAAS ENERGY LIMITED', 'Ultracab (India) Limited', 'Umiya Tubes Limited', 'UNNO INDUSTRIES LTD.', 'Unitech International Ltd', 'UNITED INTERACTIVE LTD.', 'UNIJOLLY INVESTMENTS CO.LTD.', 'Uniroyal Industries Limited', 'UNIVERSAL CABLES LTD.', 'Unity Infraprojects Limited', 'UNIVCABLES6.BO', 'Uniphos Enterprises Ltd.', 'Uniply Industries Ltd.', 'Venus Universal Ltd', 'Unimers India Ltd.', 'UNIPORT COMPUTERS LTD.', 'UNITED VAN DER HORST LTD.', 'Unimin India Limited', 'CARBORUNIV6.BO', 'Unitech Ltd.', 'UNIWORTH TEXTILES LTD.', 'UNIWORTH SECURITIES LTD.', 'UNISHIRE URBAN INFRA LTD', 'UNIWORTH INTERNATIONAL LTD.', 'Uniworth Ltd.', 'Universal Autofoundry Limited', 'UPL LIMITED', 'UP Hotels Ltd.', 'U.P.LIME-CHEM LTD.', 'USHA MARTIN LTD.', 'UTL INDUSTRIES LIMITED', 'VARDHMAN TEXTILES LTD.', 'VARDHMAN CONCRETE LIMITED', 'VANASTHALI TEXTILE INDUSTRIES', 'Vaksons Automobiles Limited', 'Vapi Enterprise Limited', 'Valiant Communications Limited', 'Vas Infrastructure Limited', 'Varun Industries Limited', 'VA TECH WABAG LTD.', 'VALUE INDUSTRIES LTD.', 'VANTECH INDUSTRY LTD.', 'VALIANTCOM*', 'VASWANI INDUSTRIES LTD.', 'VATSA CORPORATIONS LTD.', 'VADILAL INDUSTRIES LTD.', 'Valson Industries Ltd.', 'Vadilal Enterprises Ltd', 'VALECHA ENGINEERING LTD.', 'VAJRA BEARINGS LTD.', 'Vani Commercials Limited', 'VAARAD VENTURES LTD', 'VAKRANGEE LIMITED', 'Valley Magnesite Company Limit', 'MIHIJAM VANASPATI LTD.', 'VARDHMAN HOLDINGS LTD.', 'Vallabh Steels Limited', 'V B INDUSTRIES LIMITED', 'VCK Capital Market Services Limited', 'Vertex Securities Limited', 'VEERHEALTH CARE LIMITED', 'INNOVENTIVE VENTURE LTD.', 'Velan Hotels Ltd', 'Spectacle Ventures Limited', 'Indiaco Ventures Ltd', 'VERTICAL INDUSTRIES LTD', 'Vegetable Products Limited.', "Venky's (India) Limited", 'Intellivate Capital Ventures Ltd', 'VEDANTA LIMITED', 'Reliable Ventures India Ltd.', 'FRUITION VENTURE LTD', 'Veritas (India) Ltd.', 'VENUS REMEDIES LTD.', 'KRISHNA VENTURES LIMITED', 'Veljan Denison Limited', 'VIJI FINANCE LTD', 'Vintron Informatics Ltd', 'VIP Industries Limited', 'VICTORIA ENTERPRISES LTD.', 'VISHVA VISHAL ENGINEERING LTD.', 'VICEROY HOTELS LTD.', 'Virinchi Limited', 'VISHAL CHAIRS LTD.', 'Vikalp Securities Limited', 'Ed & Tech international Limited', 'VIJAYABANK4.BO', 'Vijay Textiles Ltd.', 'MARVEL VINYLS LTD.', 'VITAL COMMUNICATIONS LTD.', 'Vishnu Chemicals Limited', 'VIRTUAL INDUSTRIES LTD.', 'Vision Corporation Ltd.', 'Virinchi Limited', 'Vipul Ltd', 'VIJAYABANK6.BO', 'VISAKA INDUSTRIES LTD.', 'INDAGE VINTNERS LTD.', 'VIKSIT ENGINEERING LTD.', 'VITARA CHEMICALS LTD.', 'Virat Industries Ltd', 'VISHWAMITRA FINANCIAL SERVICES', 'VIDEOCON INDUSTRIES LTD.', 'Vijaya Bank Ltd.', 'VISHAL PAPERTECH (INDIA) LTD.', 'Vishal Bearings Limited', 'VINSARI FRUITECH LTD.', 'VISAGAR FINANCIAL SERVICES LTD', 'Vidli Restaurants Limited', 'VKS PROJECTS LTD.', 'Vantage Knowledge Academy Limi', 'VLS FINANCE LTD.', 'VMV Holidays Limited', 'V-MART RETAIL LTD.', 'Voltamp Transformers Limited', 'VOLPLAST LTD.', 'Volant Textile Mills Limited', 'VR Woodart Ltd.', 'V.S.T.TILLERS TRACTORS LTD.', 'VSD CONFIN LTD.', 'VTX INDUSTRIES LIMITED', 'VTM LTD.', 'WALCHANDNAGAR INDUSTRIES LTD.', 'WATSON SOFTWARE LTD.', 'WARREN TEA LTD.', 'Grauer & Weil (India) Ltd.', 'WESTLIFE DEVELOPMENT LTD.', 'WELSPUN CORP LIMITED', 'WELLESLEY CORPORATION LTD.', 'WEBEL COMMUNICATION INDUSTRIES', 'WEBEL SEN CAPACITORS LTD.', 'WELLWIN INDUSTRY LTD.', 'WELL PACK PAPERS & CONTAINERS', 'Wendt (India) Limited', 'WESTERN MINISTIL LTD.', 'WESTERN INDUSTRIES LTD.', 'GREAT WESTERN INDUSTRIES LTD.', 'INDORE WIRE CO.LTD.', 'WILLARD INDIA LTD.', 'Williamson Financial Services Limited', 'COMPUDYNE WINFOSYSTEMS LTD.', 'WINDSOR MACHINES LTD.', 'WILWAYFORT INDIA LTD.', 'WIPRO6.BO', 'WOODSVILLA LTD.', 'WOCKHARDT LTD.', 'WORTH INVESTMENT & TRADING CO', 'WS Industries (India)', 'Adcon Capital Services Limited', 'ADC INDIA COMMUNICATIONS LIMIT', 'ADVANI HOTELS & RESORTS (INDIA', 'AUNDE INDIA LIMITED', 'Auroma Coke Ltd.', 'Ausom Enterprise Ltd', 'AUSTIN ENGG*', 'Greenearth Resources and Projects Ltd', 'Austin Engineering Company Limited', 'Autoline Industries Limited', 'Competent Automobiles Company Limited', 'Majestic Auto Ltd.', 'Autopal Industries Limited', 'Sar Auto Products Limited', 'BAJAJ AUTO LTD.', 'AUTORIDERS FINANCE LTD.', 'HONEYWELL AUTOMATION INDIA LTD', 'Setco Automotive Limited', 'BAFFIN ENGINEERING PROJECTS LT', 'BAJAJ HOLDINGS & INVESTMENT LT', 'BAJAJ FINANCE LIMITED', 'BAJAJ FINSERV LTD.', 'Bajaj Steel Industries Ltd.', 'BALAJI HOTELS & ENTERPRISES LT', 'BALJ HOT ENT', 'BALLARPUR6.BO', 'BALLARPUR INDUSTRIES LTD.', 'IndusInd Bank Limited', 'BANAS FINANCE LTD.', 'CANARA BANK', 'INDUSINDBK6.BO', 'BANCO PRODUCTS (INDIA) LTD.', 'B&A PACKAGING INDIA LIMITED', 'Baron Infotech Limited', 'Basil Infrastructure Projects Ltd.', 'BATAINDIA4.BO', 'BATA INDIA LTD.', 'BATHINA TECHNOLOGIES (INDIA) L', 'BEARDSELL LIMITED', 'Beryl Securities Ltd', 'BETA CORPORATION LTD.', 'Brand Realty Services Ltd.', 'BRANDHOUSE RETAILS LTD.', 'BRAHMAPUTRA INFRASTRUCTURE LTD', 'BRANDHOUSE6.BO', 'BRIGHT BRO*', 'Britannia Industries Limited', 'Bright Brothers Limited', 'Saboo Brothers Limited', 'Brushman (India) Limited', 'Finolex Cables Ltd.', 'CORDS CABLE INDUSTRIES LTD.', 'GR Cables Ltd.', 'TELEPHONE CABLES LTD.', 'CAIRN4.BO', 'CAIRN*', 'Cals Refineries Limited', 'Camex Ltd.', 'C & C Constructions Limited', 'CANTABIL RETAIL INDIA LTD.', 'Can Fin Homes Ltd.', 'CANVAY CHEMICALS LTD.', 'INDITRADE CAPITAL LIMITED', 'CAPRIHANS INDIA LTD.', 'Chartered Capital and Investment Limited', 'Premier Capital Services Limited', 'Capman Financials Ltd.', 'Madhur Capital & Finance Limited', 'Intec Capital Ltd.', 'Finaventure Capital Limited', 'Pro Fin Capital Services Ltd.', 'PRAMAN CAPITAL MARKET SERVICES', 'MINDVISION CAPITAL LTD', 'CARONA LTD.', 'CAREWELL.BO', 'CASTROL INDIA LTD.', 'CASTRON TECHNOLOGIES LTD.', 'CASTEX TECHNOLOGIES LIMITED', 'CATVISION LIMITED', 'CHAMPION FINSEC LTD.', 'CHAMAK HOLDINGS LIMITED', 'Charms Industries Ltd', 'RENCAL CHEMICALS (INDIA) LTD.', 'Continental Chemicals Limited', 'Sapan Chemicals Ltd.', 'MASTER CHEMICALS LTD.', 'Reliance Chemotex Industries Limited', 'CHIPLUN FINE CHEMICALS LTD.', 'Chhattisgarh Industries Limited', 'CHL Ltd.', 'Saboo Sodium Chloro Ltd.', 'COASTAL CORPORATION LTD.', 'Metal Coatings (india) Ltd', 'COAL INDIA LTD.', 'Coventry Coil-o-Matic Haryana Limited', 'Ennore Coke Limited', 'MAGNA COLORS LTD.', 'COLGATE-PALMOLIVE (INDIA) LTD', 'COLGATE-PALMOLIVE (INDIA) LTD.', 'Compuage Infocom Ltd.', 'Comfort Intech Ltd', 'COMPUTERSKILL LTD.', 'COMPUTECH INTERNATIONAL LTD.', 'International Combustion (India) Ltd.', 'COMFORT COMMOTRADE LTD.', 'COMMEX TECHNOLOGY LIMITED', 'SAWACA COMMUNICATION LTD.', 'Fintech Communication Limited', 'COROMANDEL ENGINEERING COMPANY', 'COMFORT FINCAP LTD.', 'Ind Agiv Commerce Ltd', 'CONTINENTAL CONSTRUCTION LTD.', 'International Conveyors Ltd', 'CONCURRENT (INDIA) INFRASTRUCT', 'Regal Entertainment & Consultants Ltd.', 'Continental Controls Ltd.', 'Contil India Ltd', 'Conart Engineers Limited', 'Saumya Consultants Ltd.', 'CONDEQUIP ENGINEERS (INDIA) LT', 'PRAKASH CONSTROWELL LTD.', 'Cosco (India) Limited', 'Cosboard Industries Ltd.', 'MALWA COTTON SPINNING MILLS LT', 'GREAVES COTTON LTD.', 'SALONA COTSPIN LTD.', 'GREAVESCOT6.BO', 'COVIDH', 'COVENTRY SPRING & ENGINEERING', 'Mayukh Dealtrade Limited', 'Deco-Mica Limited', 'Deep Industries Ltd', 'DELTA MAGNETS LTD.', 'Delta Corp Limited', 'Delta Industrial Resources Lim', 'Dena Bank Ltd.', 'DETROIT INDUSTRIES LTD.', 'Prime Property Development Corporation Ltd.', 'ENERGY DEVELOPMENT COMPANY LTD', 'ENGINERSIN6.BO', 'Incon Engineers Ltd', 'ENGINEERS INDIA LTD.', 'INTEGRA ENGINEERING INDIA LTD.', 'Servotech Engineering Industries Ltd.', 'SADBHAV6.BO', 'TRANSPOWER ENGINEERING LTD.', 'A2ZMES6.BO', 'INCEN.BO', 'A2Z INFRA ENGINEERING LIMITED', 'PATEL ENGINEERING LTD.', 'ENSO SECUTRACK LTD.', 'Religare Enterprises Limited', 'Entegra Ltd', 'Regent Enterprises Limited', 'Proaim Enterprises Limited', 'SANATHNAGAR ENTERPRISES LIMITE', 'Indo-Global Enterprises Limite', 'MIDVALLEY ENTERTAINMENT LTD.', 'FILAMENTS INDIA LTD.', 'Max Financial Services Limited', 'MAHINDRA & MAHINDRA FINANCIAL', 'Interface Financial Services Limited', 'Manraj Housing Finance Limited', 'REALTIME FINLEASE LTD.', 'PRAMADA FINVEST LTD.', 'Thirdwave Financial Intermediaries Limited', 'L&T FINANCE HOLDINGS LTD.', 'MEGA FIN (INDIA) LTD.', 'MAGMA FINCORP LTD.', 'INTEGRATED FINANCE COMPANY LTD', 'MINOLTA FINANCE LTD.', 'Mehta Housing Finance Ltd.', 'Indergiri Finance Ltd.', 'Sainik Finance & Industries Ltd.', 'REPCO HOME FINANCE LTD.', 'GREENCREST FINANCIAL SERVICES', 'Mansi Finance (Chennai) Ltd.', 'MAGMA6.BO', 'Ushakiran Finance Limited', 'MAGNANIMOUS TRADE & FINANCE LT', 'Pasupati Fincap Ltd.', 'CORAL INDIA FINANCE & HOUSING', 'Paragon Finance Ltd.', '63 MOONS TECHNOLOGIES LTD', 'International Housing Finance Corporation Limited', 'MANAPPURAM FINANCE LTD.', 'LIVERPOOL FINANCE LTD.', 'Mehta Integrated Finance Limited', 'GRAHAM FIRTH STEEL PRODUCTS LT', 'Firstobject Technologies Ltd', 'Freshtrop Fruits Limited', 'Frontline Corporation Limited', 'Gratex Industries Limited', 'Graphite India Ltd.', 'GRAVITA INDIA LTD.', 'Gravity (India) Limited', 'GRADIENTE INFOTAINMENT LTD.', 'INLAC GRANSTON LTD.', 'GRADIENTE', 'Granules India Limited', 'Greenply Industries Limited', 'GREENFIELD CORP.LTD.', 'Greenlam Industries Ltd', 'Grovy India Limited', 'GRP LTD.', 'INDHOTEL6.BO', 'SAYAJI HOTELS LTD.', 'INDIAN HOTELS CO.LTD.', 'Howard Hotels Limited', 'MAYHO.BO', 'Tribhuvan Housing Limited', 'Inani Securities Ltd.', 'Indokem Limited', '3M INDIA LTD.', 'Parth Industries Limited', 'PACKTECH INDUSTRIES LTD.', 'TECHTREK INDIA LTD.', 'Pact Industries Ltd.', 'Indowind Energy Limited', 'SANGHI INDUSTRIES LTD.', 'RELIANCE4.BO', 'Indo-City Infotech Limited', 'SEQUELSOFT INDIA LTD.', 'IND-SWIFT LTD.', 'INDOSOLAR LTD.', 'IndiaNivesh Ltd.', 'REMSONS INDUSTRIES LTD.', 'Twinstar Industries Ltd.', 'Safari Industries India Ltd.', 'Informed Technologies India Ltd', '3MINDIA6.BO', 'INDITALIA REFCON LTD.', 'VIP CLOTHING LTD', 'Salguti Industries Limited', 'Indra Industries Ltd.', 'INDIA INFRASPACE LTD.', 'Prabhav Industries Ltd.', 'INDIA E-COMMERCE LTD.', 'SARTHAK INDUSTRIES LTD.', 'INNOVENTIVE INDUSTRIES LTD.', 'SAMBANDAM SPINNING MILLS LTD.', 'MINDA INDUSTRIES LTD.', 'Sahyadri Industries Ltd', 'MAGNUM LTD.', 'Steel Strips Infrastructures Limited', 'Infinite Computer Solutions (India) Ltd.', 'Innocorp Ltd', 'SATELLITE INFOCONCEPTS LTD', 'i-NAV RELIANCE BANK', 'TELEDATA INFORMATICS LTD.', 'TRANSCON RESEARCH & INFOTECH L', 'Infra Industries Ltd.', 'INFY4.BO', 'INFRAQUEST', 'i-NAV RELIANCE SENSEX', 'MAPLLE INFRAPROJECTS LTD.', 'Sankhya Infotech Ltd.', 'INFY6.BO', 'RESPONSE INFORMATICS LTD', 'SARDA INFORMATION TECHNOLOGY L', 'Prerna Infrabuild Limited', 'TEXMACO INFRASTRUCTURE & HOLDI', 'INFRAQUEST INTERNATIONAL LTD.', 'SANMIT INFRA LIMITED', 'Maruti Infrastructure Limited', 'KRATOS ENERGY & INFRASTRUCTURE', 'MAXHEIGHTS INFRASTRUCTURE LTD.', 'INFINITE*', 'TEJ INFOWAYS LIMITED', 'Melstar Information Technologies Ltd.', '3I INFOTECH LTD.', 'INGERRAND6.BO', 'INGERSOLL-RAND (INDIA) LTD.', 'INNOVASSYNTH INVESTMENTS LTD.', 'INNOVISION E-COMMERCE LTD.', 'Insilco Ltd.', 'INSTA FINANCE LIMITED', 'INSECTICIDES (INDIA) LTD.', 'INTERCRAFT LTD.', 'Samyak International Limited', 'Millennium Online Solutions (India) Limited', 'INVENTURE GROWTH & SECURITIES', 'SOLITAIRE INVESTMENTS CO.LTD.', 'KRBL*', 'KRBL Limited', 'Linkson International Limited', 'LINDE INDIA LIMITED', 'LINKHOUSE INDUSTRIES LTD.', 'Linear Industries Limited', 'LINDEINDIA6.BO', 'MAARSOFTW6.BO', 'MACKINNON MACKENZIE & CO.LTD.', 'REMI PROCESS PLANT & MACHINERY', 'Madhusudan Industries Ltd.', 'Madhur Industries Ltd', 'Maestros Medi*', 'MAGAN INDUSTRIES LTD.', 'Magnum Limited', 'TERRAFORM MAGNUM LTD.', 'MAHAVIR INDUSTRIES LIMITED', 'Mahan Industries Ltd.', 'Mahanivesh (India) Limited', 'MAHADUSHI INTERNATIONAL TRADE', 'MAJESTIC INDUSTRIES LTD.', 'MALLCOM (INDIA) LTD.', 'Malu Paper Mills Ltd.', 'MALVIKA STEEL LTD.', 'Mapro Industries Ltd.', 'Maruti Securities Ltd', 'Marathwada Refractories Ltd.', 'MASTEK6.BO', 'Mavi Industries Ltd', 'MAZDA PROPERTIES LTD.', 'THEMIS MEDICARE LTD.', 'Sowbhagya Media Limited', 'SAMBHAAV MEDIA LTD.', 'Merck Ltd.', 'TRIO MERCANTILE & TRADING LTD.', 'MERCATOR LTD.', 'MERCKLTD*', 'TWPL.BO', 'Sacheta Metals Limited', 'Pradeep Metals Limited', 'MICROENERGY (INDIA) LTD.', 'MICRO PLANTAE LTD.', 'MIDLAND PLASTICS LTD.', 'Pasari Spinning Mills Ltd', 'Minaxi Textiles Ltd.', 'Mitshi India Limited', 'INDO PACIFIC PROJECTS LIMITED', 'PAE Ltd.', 'PALRED TECHNOLOGIES LIMITED', 'PANJON LTD.', 'Sangal Papers Ltd', 'SERVALAKSHMI PAPER LTD.', 'PARSHWANATH CORPORATION LTD.', 'PARASRAMPURIA INDUSTRIES LTD.', 'PARSOLI CORPORATION LTD.', 'Paushak Limited', 'PLATINUM CORPORATION LTD.', 'PLASTIBLENDS INDIA LTD.', 'PLUS FINANCE LTD.', 'Sarda Plywood Industries', 'PRAKASH STEELAGE LTD.', 'PRAKASH INDUSTRIES LTD.', 'PRAJIND', 'PREMIER INDUSTRIES (INDIA) LTD', 'PRISM FINANCE LTD.', 'PROTCHEM INDUSTRIES (INDIA) LT', 'PROVOGUEIND*', 'Redex Protech Ltd.', 'PROGRESSIVE STEELS (INDIA) LTD', 'PROVOGUE (INDIA) LTD.', 'Triochem Products Limited', 'TERRAFORM REALSTATE LIMITED', 'Real Strips Limited', 'Redington (India) Ltd.', 'RELSON INDIA LTD.', 'RELIANCE INDUSTRIES LTD.', 'RELINFBBPH*', 'RELIANCIND*', 'Relicab Cable Manufacturing Li', 'REMI SECURITIES LTD.', 'Repro India Limited', 'SACHS INDIA LTD.', 'SAFFRON INDUSTRIES LIMITED', 'SAFAL SECURITIES LTD', 'SAIANAND COMMERCIAL LIMITED', 'SAI INDUSTRIES LTD.', 'SAM INDUSTRIES LTD.', 'SANGAM (INDIA) LTD.', 'Santaram Spinners Ltd.', 'SANDESH LTD*', 'Sanghi Corporate Services Limited', 'SANVAN SOFTWARE LTD.', 'SARITA SOFTWARE & INDUSTRIES L', 'SASHWAT TECHNOCRATS LIMITED', 'SATIA INDUSTRIES LIMITED', 'Seamec Limited', 'Seasons Textiles Limited', 'SECALS LTD.', 'S.E.INVESTMENTS LTD.', 'SPEL Semiconductor Limited', 'TeamLease Services Limited', 'Thakral Services India Ltd.', 'Seshachal Technologies Ltd', 'SEYA INDUSTRIES LTD.', 'SOFTTECHGR6.BO', 'SONATA SOFTWARE LTD.', 'SOLAR INDUSTRIES INDIA LTD.', 'SOUTH INDIAN BANK LTD.', 'SPECIALITY RESTAURANTS LTD.', 'Spectra Industries Ltd.', 'Spisys Limited', 'Sportking India Ltd.', 'STELLANT SECURITIES (INDIA) LT', 'Inducto Steels Limited', 'STILES INDIA LTD.', 'Stone India Ltd.', 'STYLAM INDUSTRIES LIMITED', '7SEAS TECHNOLOGIES LTD', 'Integrated Technologies Ltd', 'TERRYGOLD (INDIA) LTD.', 'TEXEL INDUSTRIES LTD.', 'THACKER & CO.LTD.', 'INDO THAI SECURITIES LTD.', 'THERMAX6.BO', 'INTEGRATED THERMOPLASTICS LTD.', 'Transcorp International Limited', 'Trent Ltd.', 'Trijal Industries Limited', 'TRIDENT LTD.', 'USHA (INDIA) LTD.', 'INDIANB6.BO', 'BANKA (INDIA) LTD.', 'COROMANDEL INTERNATIONAL LTD.', 'Finolex Industries Limited', 'Incap Ltd.', 'INTERCORP INDUSTRIES LTD.', 'INDBULL*', 'INDOBCL*', 'INDSOYA LTD.', 'Responsive Industries Limited']
            completer = QCompleter(names)
            completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            self.searchbox.setCompleter(completer)
            vbox.addWidget(self.searchbox)
        else:
            vbox = QVBoxLayout()
            names = ['Bharti Airtel Limited', 'Ashok Leyland Limited', 'Aurobindo Pharma Limited', 'Sanwaria Agro Oils Limited', 'Almondz Global Securities Limited', 'State Bank of India', 'Bharat Petroleum Corporation Limited', 'McNally Bharat Engineering Company Limited', 'Bank of Maharashtra', 'Bosch Limited', 'IDBI Bank Limited', 'Dabur India Limited', 'TCI Developers Limited', "Dr. Reddy's Laboratories Limited", 'India Power Corporation Limited', 'Prabhat Dairy Limited', 'Mahindra Lifespace Developers Limited', 'Landmark Property Development Company Limited', 'Kaushalya Infrastructure Development Corporation Limited', 'IRB Infrastructure Developers Limited', 'Housing Development and Infrastructure Limited', 'Housing Development Finance Corporation Limited', 'Goenka Diamond and Jewels Limited', 'Energy Development Company Limited', 'Schneider Electric Infrastructure Limited', 'Tata Elxsi Limited', 'Swaraj Engines Limited', 'Rural Electrification Corporation Limited', 'Piramal Enterprises Limited', 'Everonn Education Limited', 'Essel Propack Limited', 'Entegra Limited', 'Adani Ports and Special Economic Zone Limited', 'Oracle Financial Services Software Limited', 'LIC Housing Finance Limited', 'Sita Shree Food Products Limited', 'PTC India Financial Services Limited', 'Power Finance Corporation Limited', 'Muthoot Finance Limited', 'Max Financial Services Limited', 'Magma Fincorp Limited', 'The Fertilisers And Chemicals Travancore Limited', 'Weizmann Forex Limited', 'Gujarat State Petronet Limited', 'GAIL (India) Limited', 'Power Grid Corporation of India Limited', 'Vardhman Holdings Limited', 'Hindustan Unilever Limited', 'Hindustan Petroleum Corporation Limited', 'Hindustan Construction Company Limited', 'Hind Rectifiers Limited', 'Syncom Healthcare Limited', 'Royal Orchid Hotels Limited', 'Jubilant Industries Limited', 'Jain Irrigation Systems Limited', 'Zodiac-JRD-MKJ Limited', 'State Bank of Bikaner & Jaipur', 'PC JEWELLER LIMITE INR10', 'Jyothy Laboratories Limited', 'Jubilant FoodWorks Limited', 'Jubilant Life Sciences Limited', 'JSW Steel Limited', 'Jaiprakash Power Ventures Limited', 'Jindal Poly Investment and Finance Company Limited', 'JK Tyre & Industries Limited', 'JK Paper Limited', 'Jain Irrigation Systems Limited', 'Jindal Cotex Limited', 'Jindal Saw Limited', 'JBF Industries Limited', 'Jaihind Projects Limited', 'Jagran Prakashan Limited', 'JM FINANCIAL INR1', 'JAGSONPAL PHARMACE INR5', 'Jamna Auto Industries Limited', 'Jai Corp Limited', 'Jullundur Motor Agency (Delhi) Limited', 'JYOTI STRUCTURES INR2', 'Just Dial Limited', 'J. Kumar Infraprojects Limited', 'The Jammu and Kashmir Bank Limited', 'JUST DIAL LTD INR10', 'THE JAMMU & KASHMIR BANK LIMITE', 'JAMNA AUTO INDUSTRIES LIMITED', 'JSW STEEL LTD 0.01% PRF 15/03/1', 'JCT ELECTRONICS INR1.00', 'PC Jeweller Limited', 'JSW HOLDINGS LIMIT INR10', 'Tara Jewels Limited', 'JSW Energy Limited', 'JAYASWAL NECO IND INR10', 'J.K. Cement Limited', 'JUMBO-BZ.NS', 'JK PAPER LIMITED', 'Goldman Sachs Junior BeES ETF', 'JINDAL COTEX LIMITED', 'Jindal Photo Limited', 'JAI BALAJI INDUSTRIES LIMITED', 'Jayant Agro-Organics Limited', 'Jai Balaji Industries Limited', 'Jindal Worldwide Limited', 'JIK INDUSTRIES INR10', 'JMT AUTO LIMITED', 'JSW Holdings Limited', 'JAIHIND PROJECTS LIMITED', 'K.P.R. Mill Limited', 'KPIT Technologies Limited', 'Kotak Mahindra Bank Limited', 'Kesar Terminals & Infrastructure Limited', 'KSK Energy Ventures Limited', 'KSS Limited', 'Kaveri Seed Company Limited', 'Kothari Products Limited', 'Kothari Sugars and Chemicals Limited', 'Kopran Limited', 'KNR Constructions Limited', 'Kitex Garments Limited', 'Kirloskar Oil Engines Limited', 'Kirloskar Brothers Investments Ltd.', 'Karuturi Global Limited', 'Kesar Enterprises Limited', 'KEC International Limited', 'K.C.P. Sugar and Industries Corporation Limited', 'Everest Kanto Cylinder Limited', 'Kalyani Steels Limited', 'Kansai Nerolac Paints Limited', 'S. Kumars Nationwide Ltd.', 'KALYANI INVESTMENT COMPANY LIMI', 'MRF Limited', 'Tata Steel Limited', 'Reliance Industries Limited', 'NOCIL Limited', 'Indo Count Industries Limited', 'Tata Consultancy Services Limited', 'Surana Industries Limited', 'Sasken Technologies Limited', 'Reliance Infrastructure Limited', 'Praj Industries Limited', 'Nicco Corporation Limited', 'Maruti Suzuki India Limited', 'Lupin Limited', 'Cairn India Limited', 'Zenith Birla (India) Limited', 'Yes Bank Limited', 'Xpro India Limited', 'Voltas Limited', 'Visaka Industries Limited', 'Usher Agro Limited', 'UFO Moviez India Limited', 'Uflex Limited', 'TV18 Broadcast Limited', 'Trigyn Technologies Limited', 'Trent Limited', 'Tide Water Oil Co. (India), Ltd.', 'Tech Mahindra Limited', 'Tata Motors Limited', 'Tata Chemicals Limited', 'Sun Pharmaceutical Industries Limited', 'Sujana Universal Industries Limited', 'Subros', 'The South Indian Bank Limited', 'SKF India Limited', 'Siemens Limited', 'Murli Industries Ltd.', 'Mindtree Limited', 'Minda Industries Limited', 'Megasoft Limited', 'UNITED SPIRITS INR10', 'Magnum Ventures Limited', 'Sri Adhikari Brothers Television Network Limited', 'Pritish Nandy Communications Ltd', 'NTPC Limited', 'NCL Industries Limited', 'NBCC (India) Limited', 'The United Nilgiri Tea Estates Company Limited', 'Shree Rama Newsprint Limited', 'NMDC Limited', 'NIIT Limited', 'NHPC Limited', 'Nelco Limited', 'Nelcast Limited', 'North Eastern Carrying Corporation Limited', 'Container Corporation of India Limited', 'Union Bank of India', 'SORIL Infra Resources Limited', 'The Oudh Sugar Mills Limited', 'Orbit Corporation Limited', 'Omaxe Limited', 'Omax Autos Limited', 'Oil India Limited', 'Oberoi Realty Limited', 'Multi Commodity Exchange of India Limited', 'Motilal Oswal MOSt Shares Midcap 100 ETF', 'La Opala RG Limited', 'Birla Cable Limited', 'Bank of India Limited', 'Bang Overseas Limited', 'Aban Offshore Limited', 'Onward Technologies Limited', 'SHIV-VANI-EQ.NS', 'SABERO ORGANICS GUJRAT', 'Transport Corporation of India Limited', 'Orient Bell Limited', 'Ortin Laboratories Ltd', 'ORBIT EXPORTS LTD INR10', 'SVOGL Oil Gas and Energy Limited', 'Quintegra Solutions Limited', 'Quick Heal Technologies Limited', 'Quantum Gold ETF', 'QUINTEGRA SOLUTIONS LTD.', 'Quantum Index ETF', 'Ruchi Soya Industries Limited', 'Indoco Remedies Limited', 'GOKUL REFOILS & SO INR2', 'Texmaco Rail & Engineering Limited', 'Uttam Value Steels Limited', 'Uttam Galva Steels Limited', 'Usha Martin Limited', 'Unitech Limited', 'Uniply Industries Limited', 'Uniphos Enterprises Ltd.', 'Usha Martin Education & Solutions Limited', 'The Ugar Sugar Works Limited', 'City Union Bank Limited', 'Barak Valley Cements Limited', 'V.S.T. Tillers Tractors Limited', 'VST Industries Limited', 'Voltamp Transformers Limited', 'Ed & Tech international Limited', 'VIP Industries Limited', 'Vimta Labs Limited', 'Videocon Industries Limited', 'Spectacle Ventures Limited', 'Hotel Leelaventure Limited', 'Hindustan Media Ventures Limited', 'VLS Finance Limited', 'VISU INTERNATIONAL INR10', 'VALECHA ENGINEERIN INR10', 'Vidhi Specialty Food Ingredients Limited', 'VARDHMAN POLYTEX INR10', 'GEECEE VENTURES LIMITED', 'Valecha Engineering Limited', 'Hinduja Ventures Limited', 'VARDHMAN SPECIAL STEELS LIMITED', 'VIKAS ECOTECH LIMI INR1', 'SPEC VENTURES LTD INR1', 'SUNDARAM ASSET MAN MICRO CAP VI', 'VTXIND-BE.NS', 'V-Mart Retail Limited', 'GeeCee Ventures Limited', 'Vinyl Chemicals India Ltd.', 'Gujarat Narmada Valley Fertilizers & Chemicals Limited', 'VTXIND.NS', 'Vesuvius India Limited', 'Vaibhav Global Limited', 'VALUE INDUSTRIES LIMITED', 'Vadilal Industries Limited', 'UTTAM VALUE STEELS INR1', 'VIDEOCON INDUSTRIES LIMITED', 'Vaswani Industries Limited', 'GLOBAL VECTRA HELI INR10', 'Wipro Limited', 'Wanbury Limited', 'Todays Writing Instruments Limited', 'SORIL Holdings and Ventures Limited', 'First Winner Industries Limited', 'WINDSOR MACHINES INR2', 'Welspun India Limited', 'Websol Energy System Limited', 'WELSPUN SYNTEX', 'Wabco India Limited', 'WEST COAST PAPER M INR2.00', 'The Rai Saheb Rekhchand Mohota Spinning & Weaving Mills Ltd.', 'WILLIAMSON MAGOR & COMPANY LIMI', 'WELSPUN SYNTEX', 'LAKSHMI MACHINE WORKS LIMITED', 'Wockhardt Limited', 'WOCKHARDT INR5', 'INDIABULLS WHOLESALE SERVICES L', 'WEIZMANN INR10', 'Whirlpool of India Limited', 'Williamson Magor & Co. Limited', 'Wendt (India) Limited', 'Zydus Wellness Limited', 'West Coast Paper Mills Limited', 'TODAYS WRITING INS INR10', 'Welspun Enterprises Limited', 'Steel Strips Wheels Limited', 'Wonderla Holidays Limited', 'RELIANCE CAPITAL A FHF XXI SER', 'XCHANGING SOLUTIONS LIMITED', 'Xchanging Solutions Limited', 'UTI MUTUAL FUND FTI XII-X 1096D', 'XL Energy Limited', 'YES BANK LIMITED', 'WINSOME YARNS LTD INR10', 'Winsome Yarns Limited', 'Zylog Systems Limited', 'Zensar Technologies Limited', 'Hindustan Zinc Limited', 'Zandu Realty Limited', 'Zenith Exports Limited', 'ZENITH EXPORTS LTD INR10', 'ZEE LEARN LIMITED', 'ZEE ENTERTAIN ENT 6% CUM RED NO', 'Tribhovandas Bhimji Zaveri Limited', 'Zee Entertainment Enterprises Limited', 'Zuari Global Limited', 'ZICOM ELECTRONIC SECURITY SYSTE', 'Zenith Computers Limited', 'Zee Media Corporation Limited', 'ZANDU REALTY LIMITED', 'Zuari Agro Chemicals Limited', 'Zee Learn Limited', 'Zen Technologies Limited', 'Zen Technologies Limited', 'ZEN TECHNOLOGIES INR1', 'ZENITH BIRLA(INDIA INR10', 'ZODIAC CLOTHING COMPANY LIMITED', 'Zensar Technologies Limited', 'HINDUSTAN ZINC LIMITED', 'Zodiac Clothing Company Limited', 'ZYDUS WELLNESS LIMITED', 'Zicom Electronic Security Systems Limited', 'Aarvee Denims and Exports Limited', 'AARTI DRUGS LTD INR10', 'AARTI INDUSTRIES LIMITED', 'Aarti Industries Limited', 'Aarti Drugs Limited', 'ABB India Limited', 'Aditya Birla Chemicals (India) Limited', 'INEOS STYROLUTION INR10', 'Aditya Birla Fashion and Retail Limited', 'ABG Shipyard Limited', 'Abhishek Corporation Ltd', 'ADITYA BIRLA NUVO LIMITED', 'Orient Abrasives Limited', 'ORIENT ABRASIVES INR1 (POST SUB', 'Aditya Birla Nuvo Limited', 'Abbott India Limited', 'ADITYA BIRLA CHEMICALS (INDIA)', 'India Motor Parts and Accessories Limited', 'ACROPETAL TECHNOLO INR10', 'Accelya Kale Solutions Limited', 'ACCEL FRONTLINE LIMITED', 'Accel Frontline Limited', 'Action Construction Equipment Limited', 'ACCELYA KALE SOLUT INR10', 'Acropetal Technologies Limited', 'Tree House Education & Accessories Limited', 'ACC Limited', 'ACROPETAL TECHNOLOGIES LIMITED', 'VARDHMAN ACRYLICS INR10', 'Vardhman Acrylics Limited', 'Advance Metering Technology Limited', 'Advanta Limited', 'Allied Digital Services Ltd', 'Adhunik Metaliks Limited', 'Adani Transmissions Limited', 'Adani Enterprises Limited', 'Advani Hotels & Resorts (India) Limited', 'Adani Transmission Ltd', 'Onelife Capital Advisors Limited', 'ADF FOODS LIMITED', 'ALLIED DIGITAL SER INR5', 'ADHUNIK METALIKS LIMITED', 'Pressman Advertising Limited', 'ADVANI HOTELS & RE INR2.00', 'ADLABS ENTERTAINME INR10', 'Aditya Birla Fashion and Retail Limited', 'ADI FINECHEM LTD INR10', 'Ador Welding Limited', 'PRESSMAN ADVERTISI INR2', 'Aditya Birla Money Limited', 'Adani Power Limited', 'Sun Pharma Advanced Research Company Limited', 'SBI MUTUAL FUND SBI DUAL ADVANT', 'Adlabs Entertainment Limited', 'SRI ADHIKARI BROTHERS TELEVISIO', 'Aegis Logistics Limited', 'Aftek Limited', 'AFTEK LIMITED', 'AFTEK-BE.NS', 'Aries Agro Limited', 'REI AGRO LTD INR1', 'IFB Agro Industries Limited', 'Proseed India Limited', 'Agro Tech Foods Limited', 'Agro Dutch Industries Limited', 'AGC Networks Limited', 'NATIONAL STEEL & A INR10', 'Agri-Tech (India) Ltd', 'ARIES AGRO LIMITED', 'NATIONAL STEEL & AGRO IND', 'GREEN FIRE AGRI CO INR1', 'AGARWAL INDUSTRIAL INR10', 'AGRO TECH FOODS LIMITED', 'JULLUNDUR MOTOR AG INR10', 'JAYANT AGRO ORGANICS LIMITED', 'HATSUN AGRO PRODUC INR1', 'Agri-Tech (India) Limited', 'Agarwal Industrial Corporation Ltd.', 'REI AGRO LTD INR1', 'AGRI-TECH (INDIA) INR10', 'Gokul Agro Resources Limited', 'Hatsun Agro Product Limited', 'Dhanuka Agritech Limited', 'JVL Agro Industries Limited', 'AGRO DUTCH INDUSTRIES LTD', 'REI Agro Limited', 'National Steel and Agro Industries Limited', 'Asian Hotels (West) Limited', 'Metalyst Forgings Limited', 'AHIMSA INDUSTRIES INR10', 'AHIMSA INDUSTRIES INR10', 'AHIMSA INDUSTRIES INR10', 'AHIMSA INDUSTRIES INR10', 'AHIMSA INDUSTRIES INR10', 'Ahluwalia Contracts (India) Limited', 'Asian Hotels (East) Limited', 'AHIMSA INDUSTRIES INR10', 'AHIMSA INDUSTRIES INR10', 'AI Champdany Industries Limited', 'AIA Engineering Limited', 'AI CHAMPDANY INDUS INR5', 'Jet Airways (India) Limited', 'Ashapura Intimates Fashion Limited', 'KINGFISHER AIRLINES LTD', 'ASHAPURA INTIMATES INR10', 'GE Power India Limited', 'Ajmera Realty & Infra India Limited', 'Ajanta Pharma Limited', 'Akzo Nobel India Limited', 'AKZO NOBEL INDIA LIMITED', 'Aksh Optifibre Limited', 'Allsec Technologies Limited', 'Alok Industries Limited', 'Alkem Laboratories Limited', 'Metkore Alloys & Industries Limited', 'Gujarat Alkalies and Chemicals Limited', 'MANAKSIA ALUMINIUM INR1', 'Manak Aluminium Co. Ltd.', 'SHAH ALLOYS INR10', 'Indian Metals and Ferro Alloys Limited', 'S.A.L. Steel Limited', 'Alicon Castalloy Limited', 'ALPA LABORATORIES INR10', 'ALLSEC TECHNOLOGIE INR10', 'INDIAN METALS & FERRO ALLOYS LI', 'Allahabad Bank', 'Alembic Pharmaceuticals Limited', 'ALOK INDUSTRIES LIMITED', 'Shah Alloys Limited', 'CHEMFAB ALKALIS LIMITED', 'GYSCOAL ALLOYS LIMITED', 'Alkali Metals Limited', 'Alankit Limited', 'Chemfab Alkalis Limited', 'Alembic Limited', 'National Aluminium Company Limited', 'Allcargo Logistics Limited', 'Maithan Alloys Limited', 'Gyscoal Alloys Limited', 'ALMONDZ GLOBAL SEC INR6', 'Alpa Laboratories Limited', 'ALKEM LAB LTD INR2', 'Ess Dee Aluminium Limited', 'MANAKSIA ALUMINIUM INR1', 'ALPHAGEO (INDIA) LIMITED', 'ALPS INDUSTRIES LIMITED', 'Maan Aluminium Limited', 'Alchemist Limited', 'PAREKH ALUM. LTD', 'ALKALI METALS LIMITED', 'ALPA LABORATORIES INR10', 'SHAH ALLOYS INR10', 'Alps Industries Limited', 'ALANKIT LIMITED INR1', 'ALPINEHOU-BE.NS', 'Alkyl Amines Chemicals Limited', 'METKORE ALLOYS & INDUSTRIES LIM', 'Alphageo (India) Limited', 'GE T&D India Limited', 'Gujarat Ambuja Exports Limited', 'Bannari Amman Sugars Limited', 'Amtek Auto Limited', 'Ambika Cotton Mills Limited', 'AMIT SPINNING IND INR5.00', 'ASIL-BE.NS', 'BANNARI AMMAN SPIN INR10', 'AMRUTANJAN HEALTH CARE LIMITED', 'AMTEK INDIA LIMITED', 'Bannari Amman Spinning Mills Limited', 'Amit Spinning Industries Limited', 'Ambuja Cements Limited', 'Castex Technologies Limited', 'AMD Industries Limited', 'AMARA RAJA BATTERI INR1', 'Amrutanjan Health Care Limited', 'GUJARAT AMBUJA EXPORTS LIMITED', 'Balaji Amines Limited', 'Amara Raja Batteries Limited', 'ADVANCE METERING T INR5', 'AMRUTANJAN HEALTH INR2', 'AMLSTEEL-BE.NS', 'Mangalore Refinery and Petrochemicals Limited', 'Lotus Eye Hospital and Institute Limited', 'IOL Chemicals and Pharmaceuticals Limited', 'Ansal Properties & Infrastructure Limited', 'Anik Industries Limited', 'Anant Raj Limited', 'The Anandam Rubber Company Limited', 'DALMIA BHARAT SUGAR AND INDUSTR', 'CYBERTECH SYSTEMS AND SOFTWARE', 'LAKSHMI ENERGY & F INR2', 'EUROTEX INDUSTRIES INR10', 'Dalmia Bharat Sugar and Industries Limited', 'GOKUL REFOILS AND SOLVENT LIMIT', 'Andhra Bank', 'HELIOS AND MATHESON INFORMATION', 'Andhra Cements Limited', 'HIMADRI CHEMICALS AND INDUSTRIE', 'Seshasayee Paper and Boards Limited', 'ANSAL PROPERTIES & INFRASTRUCTU', 'Rashtriya Chemicals And Fertilizers Limited', 'Tainwala Chemicals and Plastics (India) Limited', 'Eurotex Industries and Exports Limited', 'THE ANANDAM RUBBER INR10', 'S H KELKAR AND COM INR10', 'Madhav Marbles and Granites Limited', 'Antarctica Limited', 'Sutlej Textiles and Industries Limited', 'helios and matheson information technology limited', 'AUTOMOTIVE STAMPINGS AND ASSEMB', 'IOL CHEMICALS AND PHARMACEUTICA', 'HOUSING DEVELOPMENT AND INFRAST', 'HITACHI HOME AND LIFE SOLUTIONS', 'THE ANDHRA SUGARS LIMITED', 'Ankit Metal & Power Limited', 'DEEPAK FERTILIZERS AND PETROCHE', 'Balmer Lawrie & Co. Limited', 'CHOLAMANDALAM INVESTMENT AND FI', 'ANIK INDUSTRIES INR10', 'MANGALAM DRUGS & O INR10', 'Cholamandalam Investment and Finance Company Limited', 'Veto Switchgears and Cables Limited', 'Procter & Gamble Hygiene and Health Care Limited', 'ANTARCTICA LIMITED', 'TGB BANQUETS AND H INR10(DEMAT)', 'STAR FERRO AND CEM INR1', 'KEMROCK INDUSTRIES INR10', 'Som Distilleries & Breweries Limited', 'ANDHRA CEMENTS INR10', 'OCL Iron & Steel Limited', 'Deepak Fertilisers And Petrochemicals Corporation Limited', 'Ansal Housing & Construction Limited', 'MANGALORE REFINERY AND PETROCHE', 'Monnet Ispat and Energy Limited', 'SUTLEJ TEXTILES AND INDUSTRIES', 'OCL IRON AND STEEL LIMITED', 'ANTARCTICA LIMITED INR1', 'FERTILIZERS AND CHEMICALS TRAVA', 'Surana Telecom and Power Limited', 'RELIANCE DEFENCE AND ENGINEERIN', 'The Andhra Sugars Limited', 'EMKAY TAPS AND CUT INR10', 'GODAWARI POWER AND ISPAT LIMITE', 'CARE Ratings Limited', 'Star Ferro and Cement Limited', 'ANG Industries Limited', 'Sanghvi Forging & Engineering Limited', 'B.L. Kashyap and Sons Limited', 'Cox & Kings Limited', 'ANG INDUSTRIES LTD INR10', 'TGB Banquets And Hotels Limited', 'JINDAL POLY INV & INR10', 'TEXMO PIPES & PROD INR10', 'CREDIT ANALYSIS AND RESEARCH LI', 'Welspun Investments and Commercials Limited', 'Aptech Limited', 'Apollo Sindoori Hotels Limited', 'APL Apollo Tubes Limited', 'Apar Industries Limited', 'E-Land Apparel Limited', 'MOMAI APPARELS LTD INR10', 'APCOTEX INDUSTRIES LIMITED', 'APOLLO HOSPITALS INR5', 'Apollo Tyres Limited', 'Apcotex Industries Limited', 'Apollo Hospitals Enterprise Limited', 'Butterfly Gandhimathi Appliances Limited', 'APOLLO TYRES INR1.00', 'Apollo Sindoori Hotels Li', 'Gujarat Apollo Industries Limited', 'APOLLO SINDOORI HO INR10', 'INTERNATIONAL PAPE INR10', 'E-LAND APPAREL LTD INR10', 'Panasonic Appliances India Company Limited', 'APLAB-BE.NS', 'Arshiya Limited', 'ARSS Infrastructure Projects Limited', 'Arihant Foundations & Housing Limited', 'Archies Limited', 'Archidply Industries Limited', 'Thiru Arooran Sugars Limited', 'ARIHANT FOUNDATION INR10(DEMAT)', 'ARVIND REMEDIES LIMITED', 'INTELLECT DESIGN A INR5', 'MUKTA ARTS LIMITED', 'GILLANDERS ARBUTHN INR10', 'ARVIND INFRASTRUCT INR10', 'ARVIND REMEDIES LIMITED', 'ARVIND INFRASTRUCT INR10', 'Aro Granite Industries Limited', 'ARROW GREENTECH LI INR10', 'Arvind Remedies Limited', 'Intellect Design Arena Limited', 'Arcotech Limited', 'Arvind Limited', 'ARCHIES LIMITED', 'Mukta Arts Limited', 'ARROW GREENTECH LI INR10', 'Arvind SmartSpaces Limited', 'ARO GRANITE INDUS INR10', 'ARROW TEXTILES LTD INR10', 'Arrow Textiles Limited', 'Gillanders Arbuthnot and Company Limited', 'ARCOTECH LTD INR10', 'Asian Paints Limited', 'Astec LifeSciences Limited', 'Assam Company India Limited', 'Automotive Stampings and Assemblies Limited', 'EIH Associated Hotels Limited', 'BIRLA SUN LIFE ASS NIFTY GROWTH', 'Asian Hotels (North) Limited', 'DEUTSCHE ASSET MGM DWS HYBRID F', 'Ashapura Minechem Limited', 'Astra Microwave Products Limited', 'DEUTSCHE ASSET MGM DWS FMP SR 6', 'ASIAN ELECTRONIC LTD', 'HDFC ASSET MANAGEM FMP 371D JUN', 'UTI ASSET MANAGEME FOCUS EQTY I', 'BIRLA SUN LIFE ASS CAPITAL PRT', 'SUNDARAM ASSET MAN MICRO CAP V', 'BIRLA SUN LIFE ASS SERIES 1-REG', 'ASHAPURA MINE CHEM INR2', 'HDFC ASSET MANAGEM SR 1-FEB 201', 'AstraZeneca Pharma India Limited', 'HDFC ASSET MANAGEM FMP 370D AUG', 'Astral Poly Technik Limited', 'Jaiprakash Associates Limited', 'ASAHI INDIA GLASS INR1', 'HDFC ASSET MANAGEM SR 1-FEB 201', 'IDBI ASSET MGMT SR I PLAN A-GRO', 'RELIANCE NIPPON LI RELIANCE ETF', 'SUNDARAM ASSET MAN SELECT MICRO', 'KOTAK MAHINDRA ASS KOTAK NIFTY', 'Asahi Songwon Colors Limited', 'Ashiana Housing Limited', 'SUNDARAM ASSET MAN MICRO CAP V', 'SUNDARAM ASSET MAN MICRO CAP VI', 'SHRI ASTER SILICAT INR10', 'SUNDARAM ASSET MAN SELECT SMALL', 'ASIAN HOTELS(NORTH INR10', 'Ashima Limited', 'ASHIMA INR10', 'IDBI ASSET MGMT SR I PLAN A-DIV', 'Asian Granito India Limited', 'ASTEC LIFESCIENCES LIMITED', 'BIRLA SUN LIFE ASS FIXED TERM P', 'Shri Aster Silicates Limited', 'ASAHI SONGWON COLO INR10', 'SUNDARAM ASSET MAN TOP 100 III(', 'Asahi India Glass Limited', 'BIRLA SUN LIFE ASS SERIES 1-REG', 'Ashoka Buildcon Limited', 'Atul Ltd', 'ATUL AUTO LTD INR5', 'ATN INTERNATIONAL INR4.00', 'Atlas Cycles (Haryana) Limited', 'ATN International Ltd.', 'Atul Auto Limited', 'Atlanta Limited', 'ATNINTER-BE.NS', 'Bajaj Auto Limited', 'Munjal Auto Industries Limited', 'Autolite (India) Limited', 'CLUTCH AUTO INR10', 'AUSOM ENTERPRISE INR10', 'PPAP Automotive Limited', 'Lumax Auto Technologies Limited', 'AURIONPRO SOLUTIONS LIMITED', 'InterGlobe Aviation Limited', 'AVT Natural Products Limited', 'AVANTI FEEDS INR2', 'AVANTI FEEDS INR2', 'AVT NATURAL PRODUCTS LIMITED', 'INTERGLOBE AVIATIO INR10', 'Axis Bank Limited', 'AXIS BANK INR2', 'AXISCADES Engineering Technologies Limited', 'AXISCADES ENGINEER INR10', 'Axis Gold ETF', 'Automotive Axles Limited', 'AYM Syntex Limited', 'ICICI Bank Limited', 'Canara Bank', 'Ballarpur Industries Limited', 'Indian Bank', 'IDFC Bank Limited', 'HDFC Bank Limited', 'INDUSIND BANK INR10', 'BASF India Limited', 'Bajaj Corp Limited', 'B.A.G. Films and Media Limited', 'Bafna Pharmaceuticals Limited', 'BAJAJ FINSERV LIMITED', 'Goldman Sachs Bank BeES ETF', 'PUNJAB & SIND BANK', 'BAJAJ AUTO LTD INR10', 'Goldman Sachs PSU Bank BeES ETF', 'Oriental Bank of Commerce', 'Bajaj Finance Limited', 'BARAK VALLEY CEMEN INR10', 'Bharat Bijlee Limited', 'BOMBAY BURMAH TRADING CORPORATI', 'BHARAT BIJLEE LIMITED', 'The Bombay Burmah Trading Corporation, Limited', 'BDR Buildcon Limited', 'BDR Buildcon Limited', 'BDR BUILDCON LTD INR10', 'BEML Limited', 'Manpasand Beverages Limited', 'GOLDMAN SACHS PS PSU BANK BENCH', 'Schaeffler India Limited', 'BEDMUTHA INDUSTRIES LIMITED', 'BEML LIMITED', 'BHANSALI ENGINEERING POLYMERS L', 'BENCHMARK MUTUAL SHARIAH BENCHM', 'Talwalkars Better Value Fitness Limited', 'RELIANCE NIPPON LI RELIANCE ETF', 'Tata Global Beverages Limited', 'Bedmutha Industries Limited', 'FAG BEARINGS INDIA LIMITED', 'Berger Paints India Limited', 'BEARDSELL LTD INR2', 'NRB INDUSTRIAL BEA INR2', 'MANPASAND BEVERAGE INR10', 'BEARDSELL LTD INR10', 'BERGER PAINTS (I) LIMITED', 'NRB Bearings Limited', 'NIFTY JR BENCHMARK ETF', 'ORIENT BELL LIMITED', 'NRB Industrial Bearings Limited', 'BEARDSELL LTD INR10', 'NRB INDUSTRIAL BEA INR2', 'BEARDSELL LTD INR10', 'Menon Bearings Limited', 'BENCHMARK BANKBEES', 'Bharat Electronics Limited', 'Goldman Sachs Nifty BeES ETF', 'Goldman Sachs Liquid BeES ETF', 'Goldman Sachs Shariah BeES ETF', 'Goldman Sachs Gold BeES ETF', 'Banaras Beads Limited', 'BEARDSELL LTD INR10', 'Goldman Sachs Hang Seng BeES ETF', 'BF Utilities Limited', 'BF Investment Limited', 'SQS INDIA BFSI LTD INR10', 'SQS India BFSI Limited', 'BGR Energy Systems Limited', 'BHARATIYA GLOBAL INFOMEDIA LIMI', 'BGR ENERGY SYSTEMS LIMITED', 'BHARATIYA GLOBAL I INR10', 'Bharatiya Global Infomedia Limited', 'Bharti Infratel Limited', 'Bharat Heavy Electricals Limited', 'BHARTI INFRATEL LIMITED', 'BHAGYANAGAR INDIA INR2', 'BHARATI SHIPYARD LTD.', 'Bharat Forge Limited', 'BHARTIYA INTERNATIONAL LIMITED', 'Dalmia Bharat Limited', 'BHARATI SHIPYARD LTD.', 'Bharat Gears Limited', 'Jay Bharat Maruti Limited', 'BHAGERIA INDUSTRIE INR5', 'Bharati Defence And Infrastructure Limited', 'Bharat Rasayan Limited', 'Bhansali Engineering Polymers Limited', 'Bharat Wire Ropes Limited', 'Bhartiya International Limited', 'Nava Bharat Ventures Limited', 'Bhagyanagar India Limited', 'BHUSHAN STEEL LIMITED', 'Bhushan Steel Limited', 'Biocon Limited', 'Celestial Biolabs Limited', 'BIL ENERGY SYSTEMS INR1', 'BIRLA COTSYN (INDI INR1', 'NATH BIO-GENES (IN INR10', 'OSWAL GREENTECH LI INR10', 'Birla Sun Life Nifty ETF', 'Sterling Biotech Limited', 'Nath Bio-Genes (India) Limited', 'BIRLA POWER SOL. LTD', 'Oswal Greentech Limited', 'Bil Energy Systems Limited', 'OSWAL CHEM & FERT-DEP SET', 'BIOCON LIMITED', 'Birla Cotsyn (India) Limited', 'Birla Sun Life Gold ETF', 'BIRLA SUN LIFE MUT EMERGING LEA', 'KDL BIOTECH LIMITED', 'BIRLA SUN LIFE MUT CAPITAL PR O', 'CELESTIAL BIOLABS LIMITED', 'BIRLA SUN LIFE MUT FTP LV 1099D', 'BILPOWER LTD INR10(DEMAT)', 'BILPOWER LIMITED', 'Panacea Biotec Limited', 'BIRLA SUN LIFE MUT FOCUSED EQ 2', 'Nath Bio-Genes (I) Ltd', 'Sharon Bio-Medicine Ltd.', 'ADITYA BIRLA MONEY INR1', 'HESTER BIOSCIENCES INR10', 'Bilpower Limited', 'BIRLA ERICSON LTD.', 'STERLING BIOTECH INR1', 'Edayar Zinc Limited', 'Gufic Biosciences Limited', 'Birla Corporation Limited', 'Hester Biosciences Limited', 'BK OF BARODA INR2', 'Pennar Eng Bldg Sys Ltd', 'BLB INR1', 'BLB Limited', 'Phillips Carbon Black Limited', 'Blue Dart Express Limited', 'Blue Coast Hotels Limited', 'BLUE BLENDS (INDIA INR10', 'Bliss Gvs Pharma Limited', 'BLUE STAR INFOTECH LIMITED', 'Blue Chip India Limited', 'BLUE CHIP INDIA LTD.', 'BLUE COAST HOTELS INR10', 'PHILLIPS CARBON BLACK LIMITED', 'BLUE BLENDS (INDIA INR10', 'BLUE BLENDS (I) LTD', 'Blue Star Limited', 'Blue Star Infotech Ltd.', 'BLUE COAST HOTELS INR10', 'NIFTY BMARK EXCH. TRD FND', 'Geojit Financial Services Limited', 'GEOJIT BNP PARIBAS INR1', 'BNP PARIBAS MF CAPITAL PRT ORIE', 'Bodal Chemicals Limited', 'BODAL CHEMICALS INR2.00', 'BOSCH LIMITED', 'GENUS PAPER AND BO INR10', 'The Bombay Dyeing and Manufacturing Company Limited', 'BOMBAY DYEING & MFG COMPANY LIM', 'Genus Paper & Boards Limited', 'Commercial Engineers & Body Builders Co Limited', 'BODHTREE-BE.NS', 'Bombay Rayon Fashions Limited', 'COMMERCIAL ENGINEERS & BODY BUI', 'BPL Limited', 'BPL LIMITED', 'DB (International) Stock Brokers Ltd', 'United Breweries Limited', 'Sundaram Brake Linings Limited', 'Broadcast Initiatives Limited', 'Kirloskar Brothers Limited', 'NOIDA TOLL BRIDGE COMPANY LIMIT', 'Brooks Laboratories Limited', 'Rane Brake Lining Limited', 'SUNDARAM BRAKE LININGS LIMITED', 'Noida Toll Bridge Company Limited', 'SOM DISTIL & BREW INR10', 'KIRLOSKAR BROTHERS INR2', 'BSEL Infrastructure Realty Limited', 'BSL LIMITED', 'BS Limited', 'BSL Limited', 'Burnpur Cement Limited', 'Pennar Engineered Building Systems Limited', 'BURNPUR CEMENT LTD INR10', 'Vijay Shanthi Builders Limited', 'PENNAR ENGINEERED INR10', 'THE BYKE HOSPITALI INR10', 'The Byke Hospitality Limited', 'THE BYKE HOSPITALI INR10', 'Goa Carbon Limited', 'Electrosteel Castings Limited', 'Castrol India Limited', 'C & C Constructions Limited', 'Cadila Healthcare Limited', 'SATIN CREDIT CARE INR10', 'CAPLIN POINT LABOR INR2', 'CANFIN HOMES INR10', 'ICICI PRUDENTIAL A CAP PRO ORIE', 'Consolidated Construction Consortium Limited', 'Country Club Hospitality & Holidays Limited', 'COUNTRY CLUB HOSPI INR2', 'CCL Products (India) Limited', 'Idea Cellular Limited', 'Prism Cement Limited', 'ITD Cementation India Limited', 'Euro Ceramics Limited', 'CESC Limited', 'Cera Sanitaryware Limited', 'CEAT Limited', 'CENTURY EXTRUSIONS LIMITED', 'The Ramco Cements Limited', 'CENTUM ELECTRONICS INR10', 'SAGAR CEMENTS LIMITED', 'Century Extrusions Limited', 'ORIENT CEMENT LTD INR1', 'IDEA CELLULAR LIMITED', 'UltraTech Cement Limited', 'EUROCERA-BE.NS', 'Kovai Medical Center & Hospital Ltd.', 'CEREBRA INTEGRATED INR10', 'Mangalam Cement Limited', 'Sagar Cements Limited', 'Cerebra Integrated Technologies Limited', 'Somany Ceramics Limited', 'Shyam Century Ferrous Ltd', 'REGENCY CERAMICS INR10', 'Shree Cement Limited', 'Kakatiya Cement Sugar and Industries Limited', 'CELEBRITY FASHIONS INR10', 'Gujarat Sidhee Cement Limited', 'Century Plyboards (India) Limited', 'Orient Cement Limited', 'RAMCO CEMENTS(THE) INR1', 'Decolight Ceramics Ltd.', 'CERA SANITARYWARE LIMITED', 'Murudeshwar Ceramics Limited', 'CENTRAL BANK OF INDIA', 'JK CEMENT LIMITED', 'Central Bank of India', 'Regency Ceramics Limited', 'SHYAM CENTURY FERR INR1', 'Century Textiles and Industries Limited', 'DECOLIGHT CERAMICS INR10', 'GUJARAT SIDHEE CEM INR10 (NEW)', 'SHYAM CENTURY FERR INR1', 'JK Lakshmi Cement Limited', 'Celebrity Fashions Limited', 'Deccan Cements Limited', 'Centum Electronics Limited', 'Century Enka Limited', 'SOMANY CERAMICS LD INR2', 'The India Cements Limited', 'Kajaria Ceramics Limited', 'CAPRI GLOBAL CAPIT INR2', 'Capri Global Capital Limited', 'Sudarshan Chemical Industries Limited', 'Clariant Chemicals (India) Limited', 'Chromatic India Limited', 'Rajshree Sugars and Chemicals Limited', 'GUJARAT STATE FER INR2(POST SUB', 'BALRAMPUR CHINI MI INR1', 'FINEOTEX CHEMICAL INR2', 'Thirumalai Chemicals Limited', 'OMKAR SPECIALITY CHEMICALS LIMI', 'MANGALORE CHEMICALS & FERTILIZE', 'Chamundeswari Sug Ltd', 'ORCHID CHEMICALS & PHARMACEUTIC', 'DHARANI SUGARS & CHEMICALS LIMI', 'Himadri Speciality Chemical Limited', 'Cipla Limited', 'CIGNITI TECHNOLOGI INR10', 'CIL NOVA PETROCHEM INR10', 'Cinevista Limited', 'Mahindra CIE Automotive Limited', 'CIPLA LIMITED', 'Opto Circuits (India) Ltd', 'MAHINDRA CIE AUTO INR10', 'Cineline India Limited', 'Shriram City Union Finance Limited', 'OPTO CIRCUITS (INDIA) LIMITED', 'CIL Nova Petrochemicals Limited', 'CIGNITI TECHNOLOGI INR10', 'SHRIRAM CITY UNION FINANCE LIMI', 'Cimmco Limited', 'CIL NOVA PETROCHEM INR10', 'Classic Diamonds (India)', 'The Indian Card Clothing Company Limited', 'CLUTCH AUTO LTD', 'Kewal Kiran Clothing Limited', 'CLASSIC DIAMONDS (I) LTD', 'Clutch Auto Ltd.', 'CLASSIC DIAMONDS (I) LTD', 'CLUTCH AUTO LTD', 'CLASSIC DIAMONDS (INDIA) LIMITE', 'C. Mahendra Exports Limited', 'C.MAHENDRA EXPORTS LTD', 'CMC Limited', 'Goldman Sachs CPSE ETF', 'RELIANCE NIPPON LI CPSE ETF*', 'Ganesh Housing Corporation Limited', 'CANARA ROBECO MF GOLD ETF', 'SHARDA CROPCHEM INR10', 'CREATIVE EYE LTD INR10', 'Satin Credit Net Ltd', 'CREST COMM NPP251099DEPO', 'CG Power and Industrial Solutions Limited', 'SATIN CREDIT CARE INR10', 'Excel Crop Care Limited', 'Creative Eye Limited', 'SATIN CREDIT CARE INR10', 'CRISIL Limited', 'SATIN CREDIT CARE INR10', 'SATIN CREDIT CARE NETWORK LTD S', 'Sharda Cropchem Limited', 'CREST VENTURES INR10', 'SATIN CREDIT CARE INR10', 'Satin Creditcare Network Limited', 'Punjab Chemicals and Crop Protection Limited', 'SATIN CREDIT CARE INR10', 'Crest Ventures Limited', 'Bayer CropScience Limited', 'Canara Robeco Gold ETF', 'CAMBRIDGE TECH ENT INR10', 'CAMBRIDGE TECHNOLOGY ENTERPRISE', 'Cambridge Technology Enterprises Limited', 'JSW STEEL LTD INR10 10% CUM RED', 'CUMMINS INDIA INR2', 'CURA Technologies Limited', 'Cubex Tubings Limited', 'CUBEXTUBINGS-ROLLSETT', 'CUBEX TUBINGS INR10', 'CURA TECHNOLOGIES INR10', 'Cummins India Limited', 'CyberTech Systems and Software Limited', 'Cyber Media (India) Limited', 'CYIENT LIMITED INR5', 'EVEREST KANTO CYLINDER LIMITED', 'CYBER MEDIA (INDIA INR10', 'Cyient Limited', 'Coffee Day Enterprises Limited', 'COFFEE DAY ENTERPR INR10', 'Hathway Cable & Datacom Limited', 'HATHWAY CABLE & DA INR2', 'DATAMATICS GLOBAL INR5', 'UMANG DAIRIES INR5', 'UMANG DAIRIES INR5', 'LT Foods Limited', 'PRABHAT DAIRY LTD INR10', 'RELIANCE CAPITAL A RELIANCE DA', 'Datamatics Global Services Limited', 'DB Realty Ltd', 'D B CORP LTD INR10', 'D. B. Corp Limited', 'DCW Limited', 'DCB BANK LIMITED INR10', 'DCM Limited', 'DCB Bank Limited', 'DCM Shriram Limited', 'DCM SHRIRARM LTD INR2', 'Dewan Housing Finance Corporation Limited', 'Delta Corp Limited', 'Deep Industries Limited', 'HIL Limited', 'Nandan Denim Limited', 'Dhunseri Investments Limited', 'DHUNSERI TEA & IND INR10', 'Dharani Sugars and Chemicals Limited', 'DHUNSERI TEA & IND INR10', 'DHUNSERI PETROCHEM INR10(DEMAT', 'Dhunseri Tea & Ind. Ltd.', 'Dhampur Sugar Mills Limited', 'Dhunseri Petrochem Limited', 'Dhanlaxmi Bank Limited', 'Dish TV India Limited', 'Diamond Power Infrastructure Limited', 'GOENKA DIAMOND&JEWELS LTD', 'Digjam Limited', 'UTI MUTUAL FUND RGSS DIRECT DIV', 'Gateway Distriparks Limited', 'RAVI KUMAR DISTILLERIES LIMITED', 'DIC INDIA LIMITED', 'Ravi Kumar Distilleries Limited', 'PIONEER DISTILLERI INR10', 'Dishman Pharmaceuticals and Chemicals Limited', 'FOURTH DIMENSION S INR10', 'R*Shares Dividend Opportunities ETF', 'DIC India Limited', 'Pioneer Distilleries Limited', 'Empee Distilleries Limited', "Divi's Laboratories Limited", 'DLF Limited', 'D-Link (India) Limited', 'Donear Industries Limited', 'Dolphin Offshore Enterprises (India) Limited', 'Hindustan Dorr-Oliver Limited', 'DOLPHIN OFFSHORE ENTERPRISES (I', 'DONEAR INDUSTRIES INR2', 'DPSC LIMITED', 'DQ Entertainment (International) Limited', 'DQ ENTERTAINMENT (INTERNATIONAL', "DR. REDDY'S LABORATORIES LIMITE", 'Parenteral Drugs (India) Limited', 'Dr.Datsons Labs Limited', 'DR LAL PATHLABS LT INR10', 'DR.DATSONS LABS LT INR10', 'Kilitch Drugs (India) Limited', 'DREDGING CORPORATION OF INDIA L', 'Parabolic Drugs Limited', 'Dr. Lal PathLabs Limited', 'Mangalam Drugs & Organics Limited', 'PARABOLIC DRUGS INR10(DEMAT)', 'Dredging Corporation of India Limited', 'KILITCH DRUGS (INDIA) LIMITED', 'Jindal Drilling & Industries Limited', 'D.S. KULKARNI DEVE INR10', 'D.S. Kulkarni Developers Limited', 'DYNACONS SYS SOLUT INR10', 'Dynacons Systems & Solutions Limited', 'DUNCANS INDUSTRIES INR10', 'RELIANCE MUTUAL FD DUAL ADVANTA', 'Duncans Industries Limited', 'DUNCANS INDUSTRIES INR10', 'DEUTSCHE MUTUAL FU MID CAP 1 RE', 'Dwarikesh Sugar Industries Limited', 'DWARIKESH SUGAR INDUSTRIES LIMI', 'DWARIKESH SUGAR IN INR10', 'DYNACONS TECHNOLOG INR1', 'DUCON INFRATECHNOL INR1', 'Dynamatic Technologies Limited', 'Ducon Infratechnolgies Limited', 'DYNAMATIC TECHNOLO INR10', 'The Great Eastern Shipping Company Limited', 'EASTERN SILK IND INR2', 'EASUN REYROLLE LTD INR2', 'Easun Reyrolle Limited', 'Eastern Silk Industries Limited', 'Edelweiss ETF - Nifty Bank', 'eClerx Services Limited', 'GANESHA ECOSPHERE INR10', 'Vikas EcoTech Limited', 'Vikas EcoTech Limited', 'ECE INDUSTRIES LIMITED', 'ECLERX SERVICES LIMITED', 'ECE Industries Limited', 'Ganesha Ecosphere Limited', 'Educomp Solutions Limited', 'Edelweiss Financial Services Limited', 'EDELWEISS FINANCIAL SERVICES LI', 'USHA MARTIN EDU INR1', 'MT Educare Limited', 'Info Edge (India) Limited', 'Edelweiss ETF - Nifty 50', 'Navneet Education Limited', 'NAVNEET EDUCATION INR2', 'EVERONN EDUCATION LIMITED', 'CORE EDUCATION & TECH LTD', 'INFO EDGE INR10', 'CORE Education and Technologies Limited', 'CORE EDUCATION & TECHNOLOGIES L', 'EDELWEISS MUTUAL F EDELWEISS ET', 'MT EDUCARE LIMITED', 'SKM EGG PRODUCTS INR10', 'SKM Egg Products Export (India) Limited', 'Eicher Motors Limited', 'EIH Limited', 'Eimco Elecon (India) Limited', 'EIMCO ELECON(I)LTD', 'E.I.D.-Parry (India) Limited', 'EIMCO ELECON INDIA INR10 (100%', 'EID PARRY INDIA LIMITED', 'Techno Electric & Engineering Company Limited', 'ELGI Equipments Limited', 'ELECTROTHERM (INDI INR10', 'TVS Electronics Limited', 'Khaitan Electricals Limited', 'Elite Conductors Limited', 'TVS ELECTRONICS LIMITED', 'KIRLOSKAR ELECTRIC COMPANY LIMI', 'LEEL Electricals Limited', 'ELECTROSTEEL STEELS LIMITED', 'TECHNO ELECTRIC & ENGINEERING C', 'SCHNEIDER ELECTRIC INFRASTRUCTU', 'ELGI RUBBER COMPANY LIMITED', 'KHAITAN ELECTRICAL INR10', 'MIRC Electronics Limited', 'Eon Electric Limited', 'Elder Pharmaceuticals Limited', 'MIC Electronics Limited', 'Bajaj Electricals Limited', 'JCT Electronics Limited', 'India Nippon Electricals Limited', 'ELECON ENGINEERING INR2 (POST S', 'EON ELECTRIC LTD INR5', 'ELFORGE-BE.NS', 'Electrotherm (India) Limited', 'ELDER PHARM INR10(DEMAT)', 'SALZER ELECTRONICS INR10', 'Elgi Rubber Company Limited', 'PG ELECTROPLAST LIMITED', 'ELDER PHARMA LTD.', 'Kirloskar Electric Company Limited', 'PG Electroplast Limited', 'MIRC ELECTRONICS INR1', 'Elecon Engineering Company Limited', 'ELDER PHARM INR10(DEMAT)', 'Electrosteel Steels Limited', 'SALZER ELECTRONICS INR10', 'EMCO Limited', 'EMCO LIMITED', 'Pioneer Embroideries Limited', 'Emami Limited', 'Emmbi Industries Limited', 'Emami Infrastructure Limited', 'Emkay Global Financial Services Limited', 'EMAMI INFRASTRUCTU INR2', 'PIONEER EMBROID LT INR10', 'EMKAY GLOBAL FIN INR10', 'Shemaroo Entertainment Limited', 'Sadbhav Engineering Limited', 'Religare Enterprises Limited', 'Patel Engineering Limited', 'Era Infra Engineering Limited', 'Entertainment Network (India) Limited', 'Future Consumer Limited', 'PENNAR ENGINEERED INR10', 'Karma Energy Limited', 'PENNAR ENGINEERED INR10', 'A2Z Infra Engineering Limited', 'Shriram EPC Limited', 'SHRIRAM EPC LIMITED', 'Revathi Equipment Limited', 'REVATHI EQUIPMENT INR10', 'ICICI PRUDENTIAL A EQUITY SAVIN', 'ERAINFRA-BE.NS', 'ERA INFRA ENGINEER INR2(DEMAT)', 'Eros International Media Limited', 'Essar Shipping Limited', 'Escorts Limited', 'ESAB India Limited', 'UNITED NILGIRI TEA INR10', 'NITESH ESTATES LIMITED', 'Ester Industries Limited', 'Indiabulls Real Estate Limited', 'Essar Oil Ltd.', 'Nitesh Estates Limited', 'ESSAR SHIPPING POR INR10', 'Prestige Estates Projects Limited', 'ESTER INDUSTRIES LIMITED', 'PRESTIGE ESTATES PROJECTS LIMIT', 'ESSAR PORTS LIMITED', 'R* Shares Gold ETF', 'ICICI Prudential Nifty ETF', 'Invesco India Nifty ETF', 'Motilal Oswal MOSt Shares M50 ETF', 'Kotak Nifty ETF', 'Kotak Gold ETF', 'UTI Sensex ETF', 'R*Shares NV20 ETF', 'Motilal Oswal MOSt Shares NASDAQ 100 ETF', 'UTI Gold ETF', 'LIC MF ETF Nifty 50', 'Kotak Banking ETF', 'IDBI Gold ETF', 'Invesco India Gold ETF', 'IDBI MUTUAL FUND IDBI GOLD ETF', 'HDFC Gold ETF', 'R* Shares CNX 100 ETF', 'ICICI Prudential GOLD ETF', 'R*Shares Consumption ETF', 'HDFC Nifty ETF', 'HDFC Sensex ETF', 'ICICI Prudential Nifty100 ETF', 'ICICI Prudential GOLD ETF', 'R* Shares Banking ETF', 'MOST SHARES M100 ETF', 'UTI Nifty ETF', 'R* Shares Nifty ETF', 'Kotak PSU Bank ETF', 'Kotak NV 20 ETF', 'RELIGARE MUTUAL FD NIFFTY ETF', 'Euro Multivision Limited', 'EURO MULTIVISION L INR10', 'EURO MULTIVISION L INR10', 'Eveready Industries India Limited', 'Everest Industries Limited', 'Tulsi Extrusions Limited', 'Exide Industries Limited', 'GOLDMAN SACHS GOLD GOLD EXCH TR', 'Excel Realty N Infra Limited', 'Hindustan Oil Exploration Company Limited', 'RAJESH EXPORTS INR1', 'Excel Industries Limited', 'Norben Tea & Exports Ltd', 'Nagreeka Exports Limited', 'EXCEL REALTY N INF INR10', 'NAGREEKA EXPORTS INR5', 'MULTI COMMODITY EX INR10', 'Nucleus Software Exports Limited', 'Orbit Exports Limited', 'Selan Exploration Technology Limited', 'KABRA EXTRUSIONTEC INR5.00', 'ICICI PRUDENTIAL A GOLD EXCHANG', 'Kemrock Industries and Exports Limited', 'Rajesh Exports Limited', 'EXIDE INDUSTRIES LIMITED', 'Excel Realty N Infra Limited', 'Kabra Extrusiontechnik Limited', 'Sakuma Exports Limited', 'Gokaldas Exports Limited', 'LOTUS EYE CARE HOSPITAL LIMITED', 'PDS Multinational Fashions Limited', 'Farmax India Limited', 'INDIAN TERRAIN FAS INR2', 'Monte Carlo Fashions Limited', 'ADITYA BIRLA FASH INR10', 'FARMAX INDIA LTD INR1', 'PDS MULTINATIONAL INR10', 'Sundram Fasteners Limited', 'Indian Terrain Fashions Limited', 'MONTE CARLO FASHIO INR10', 'Future Lifestyle Fashions Limited', 'FUTURE LIFESTYLE F INR2', 'FCS SOFTWARE SOLUT INR1', 'FCS Software Solutions Limited', 'FUTURE CONSUMER EN INR6', 'Fineotex Chemical Limited', 'FDC Limited', 'RELIANCE MUTUAL FD RELIANCE ETF', 'FDC LIMITED', 'Federal-Mogul Goetze (India) Limited', 'UTI MUTUAL FUND FEF-S-I-1100D R', 'The Federal Bank Limited', 'Gujarat State Fertilizers & Chemicals Limited', 'Shree Pushkar Chemicals & Fertilisers Limited', 'THE FEDERAL BANK LIMITED', 'Rohit Ferro-Tech Limited', 'MADRAS FERTILIZERS INR10(DEMAT)', 'Fedders Electric and Engineering Limited', 'Impex Ferro Tech Limited', 'Shre Push Chem & Fert Ltd', 'SHREE PUSHKAR CHEM INR10', 'Chambal Fertilisers and Chemicals Limited', 'National Fertilizers Limited', 'ROHIT FERRO-TECH INR10', 'Madras Fertilizers Limited', 'Shriram Transport Finance Co. Ltd.', 'Shriram Transport Finance Company Limited', 'Sarla Performance Fibers Limited', 'NAHAR POLY FILMS LIMITED', 'Indus Fila Limited', 'Indiabulls Housing Finance Limited', 'Firstsource Solutions Limited', '63 Moons Technologies Limited', 'INDUS FILA LIMITED', 'FINOLEX CABLES LIMITED', 'Lakshmi Fin Ind Corp Ltd', 'CONSOLIDATED FINVE INR10', 'GIC Housing Finance Limited', 'CAMLIN FINE SCIENC INR1', 'Consolidated Finvest & Holdings Limited', 'JM Financial Limited', 'Sundaram Finance Limited', 'LAKSHMIFIN-BE.NS', 'Nahar Capital and Financial Services Limited', 'ORACLE FINANCIAL SERVICES SOFTW', 'FIEM INDUSTRIES LIMITED', 'L&T FINANCE HOLDINGS LIMITED', 'Gujarat Lease Financing Limited', 'GINNI FILAMENTS LIMITED', 'GUJARAT STATE FINANCIAL CORPORA', 'Filatex India Limited', 'TCI Finance Limited', 'Nahar Poly Films Limited', 'FINANCIAL TECHNOLOGIES (INDIA)', 'Nitin Fire Protection Industries Limited', 'POWER FINANCE CORPORATION LIMIT', 'GIC HOUSING FINANCE LIMITED', 'Motilal Oswal Financial Services Limited', 'NAVIN FLUORINE INT INR2', 'Gujarat Fluorochemicals Limited', 'Navin Fluorine International Limited', 'Flexituff International Limited', 'L&T MUTUAL FUND FMP GRWT OPT 03', 'Future Market Networks Limited', 'FUTURE MKT NETWORK INR10', 'Shree Ganesh Forgings Limited', 'MM Forgings Limited', 'Foseco India Limited', 'Fortis Healthcare Limited', 'FORTIS HEALTHCARE LIMITED', 'Hinduja Foundries Limited', 'ADF Foods Limited', 'Ramkrishna Forgings Limited', 'METALYST FORGINGS INR10', 'LGB FORGE LIMITED', 'Heritage Foods Limited', 'KALYANI FORGE INR10', 'Metalyst Forgings Limited', 'KALYANI FORGE INR10', 'PRIME FOCUS LIMITED', 'Prime Focus Limited', 'RELAXO FOOTWEARS LIMITED', 'Relaxo Footwears Limited', 'SITA SHREE FOOD PRODUCTS LIMITE', 'KOHINOOR FOODS LIMITED', 'HERITAGE FOODS LTD INR10', 'Hilton Metal Forging Limited', 'Kohinoor Foods Limited', 'VIMAL OIL & FOOD INR10', 'MM FORGINGS LIMITED', 'LGB Forge Limited', 'SITA SHREE FOOD PR INR10', 'Vimal Oil & Foods Limited', 'SHREE GANESH FORG INR10', 'SHREE GANESH FORG INR10', 'Kalyani Forge Limited', 'Future Enterprises Limited', 'FUTURE ENTERPRISES INR2', 'Himachal Futuristic Communications Limited', 'SUNDARAM MUTUAL FU SEL SMALL CA', 'Ucal Fuel Systems Limited', 'UTI MUTUAL FUND RGSS RET GROWTH', "FUTURE ENTERPRISES INR2 'B' (BO", 'HDFC MUTUAL FUND HDFC-RAJ GANDH', 'RELIANCE MUTUAL FD R NIFTY DIVI', 'UTI MUTUAL FUND CAP PRO OR IV-I', 'SBI MUTUAL FUND DEBT 366D 38 RE', 'HDFC MUTUAL FUND CAP PRO 36M RE', 'SUNDARAM MUTUAL FU MICROCAP III', 'HDFC MUTUAL FUND SR I-36M OCT 2', "FUTURE ENTERPRISES INR2 'B' (BO", 'ICICI PRUDENTIAL A ICICI PRUDEN', 'Indraprastha Gas Limited', 'Gabriel India Limited', 'Gallantt Ispat Limited', 'Gati Limited', 'GUJARAT GAS LIMITE INR10 NEW', 'GUJARAT GAS LIMITE INR10 NEW', 'Garden Silks Mills Ltd.', 'GAIL (INDIA) LIMITED', 'GAMMON INFRASTRUCT INR2', 'Gujarat Gas Limited', 'KITEX GARMENTS LIMITED', 'Gammon Infrastructure Projects Limited', 'Gandhi Special Tubes Limited', 'SVOGL OIL GAS AND INR10', 'GALLANTT METAL LIMITED', 'OIL & NATURAL GAS CORPORATION L', 'Gammon India Limited', 'Oil and Natural Gas Corporation Limited', 'Garden Silk Mills Limited', 'Shree Ganesh Jewellery House (I) Limited', 'GANGOTRI TEXTILE INR5(POST SUBD', 'Integra Garments and Textiles Limited', 'GANESH HOUSING CP INR10(DEMAT)', 'SVOGL Oil Gas and Energy Limited', 'INTEGRA GARMENTS A INR3', 'Gangotri Textiles Limited', 'Gayatri Projects Limited', 'GARWARE WALL ROPES INR10', 'Garware-Wall Ropes Limited', 'Upper Ganges Sugar & Industries Limited', 'GALLANTT ISPAT LIMITED', 'INTEGRA GARMENTS A INR3', 'Gallantt Metal Limited', 'GANGOTRI TEXTILE INR5(POST SUBD', 'Genus Power Infrastructures Limited', 'Gemini Communication Limited', 'Lypsa Gems & Jewellery Limited', 'GEI Industrial Systems Limited', 'GENUS POWER INFRA INR1', 'Genesys International Corporation Limited', 'Geometric Limited', 'Genus P&B Limited', 'Shanthi Gears Limited', 'The Motor & General Finance Limited', 'MOTOR & GENERAL FINANCE L', 'MOTOR & GEN FINANC INR10', 'LYPSA GEMS & JEWEL INR10', 'The Hi-Tech Gears Limited', 'GEMINI COMM LTD INR1', 'GEOMETRIC LIMITED', 'SHANTHI GEARS INR1', 'Gitanjali Gems Limited', 'GITANJALI GEMS LIMITED', 'GHCL Limited', 'GHCL LIMITED', 'PNB Gilts Ltd.', 'Gujarat Industries Power Company Limited', 'GIR Natureview Resort Ltd', 'GI ENGINEERING SOL INR10', 'GI ENGINEERING SOLUTIONS LTD IN', 'GIR NATUREVIEW RES INR10', 'GILLETTE INDIA LIMITED', 'GIR Natureview Resorts Limited', 'Ginni Filaments Limited', 'GI Engineering Solutions Limited', 'Gillette India Limited', 'GKW LIMITED INR10', 'GKW Limited', 'Globus Spirits Limited', 'Glenmark Pharmaceuticals Limited', 'GlaxoSmithkline Pharmaceuticals Limited', 'STL GLOBAL LTD INR10', 'India Glycols Limited', 'GLENMARK PHARMACEUTICALS LIMITE', 'SEZAL GLASS INR10', 'VAIBHAV GLOBAL LTD INR10', 'Sejal Glass Limited', 'ONMOBILE GLOBAL LIMITED', 'Sphere Global Services Limited', 'Global Offshore Services Limited', 'STL Global Limited', 'OnMobile Global Limited', 'GLOBAL VECTRA HELI INR10', 'STL GLOBAL LTD INR10', 'Hindusthan National Glass & Industries Limited', 'GLODYNE-BE.NS', 'Global Vectra Helicorp Limited', 'GUJARAT LEASE INR10', 'GLODYNE TECHNOSERVE LTD.', 'GlaxoSmithKline Consumer Healthcare Limited', 'SPHERE GLOBAL SERV INR10', 'Hinduja Global Solutions Limited', 'SEZAL GLASS INR10', 'Glodyne Technoserve Limited', 'Pearl Global Industries Limited', 'HINDUJA GLOBAL SOLUTIONS LIMITE', 'G.M.Breweries Limited', 'Gujarat Mineral Development Corporation Limited', 'GMR INFRASTRUCTURE LIMITED', 'GMR Infrastructure Limited', 'Godrej Industries Limited', 'Godawari Power & Ispat Limited', 'Godrej Consumer Products Limited', 'Gokul Refoils & Solvent Ltd', 'GOL Offshore Limited', 'Golden Tobacco Limited', 'GOLDSTONE INFRATECH LIMITED', 'INVESCO MUTUAL FUND', 'GOA CARBON LIMITED', 'GOLDSTONE TECHNOLOGIES LT', 'GOCL CORPORATION L INR2', 'GOLDEN TOBACCO LTD INR10 (DEMAT', 'SHIRPUR GOLD REFINERY LIMITED', 'Shirpur Gold Refinery Limited', 'SBI MUTUAL FUND SBI-ETF GOLD', 'Goldstone Infratech Limited', 'Goldstone Technologies Limited', 'Goldiam International Limited', 'SBI MUTUAL FUND SBI-ETF GOLD', 'GOCL CORPORATION L INR2', 'GODREJ CONSUMER PRODUCTS LIMITE', 'Godrej Properties Limited', 'GOLDIAM INTERNATIONAL LIMITED', 'Goodluck India Limited', 'RELIANCE CAPITAL A R SHARES GOL', 'Godfrey Phillips India Limited', 'GOODLUCK INDIA LTD INR2', 'GULFCORP-EQ.NS', 'Gujarat Pipavav Port Limited', 'GP PETROLEUMS LTD INR5', 'GP Petroleums Limited', 'GP Petroleums Limited', 'Greaves Cotton Limited', 'Granules India Limited', 'STG Lifecare Limited', 'INVENTURE GROWTH & SECURITIES L', 'GSS INFOTECH LTD INR10', 'GSS Infotech Limited', 'GTL Infrastructure Limited', 'GTL Limited', 'GTN Industries Limited', 'GTL LIMITED', 'GTN Textiles Limited', 'GTN TEXTILES INR10', 'GUJARAT NRE COKE LIMITED', 'GULF OIL LUBRICANT INR2', 'Gulf Oil Lubricants India Limited', 'Gujarat NRE Coke Ltd.', 'Gulshan Polyols Limited', 'Times Guaranty Ltd.', 'Gujarat NRE Coke Ltd.', 'TIMES GUARANTY LIMITED', 'GVK Power & Infrastructure Limited', 'GVK POWER & INFRASTRUCTURE LIMI', 'TAJGVK Hotels & Resorts Limited', 'Hanung Toys and Textiles Limited', 'HAVELLS INDIA LIMITED', 'Harrisons Malayalam Limited', 'Harita Seating Systems Limited', 'HARITA SEATING SYSTEMS LIMITED', 'Havells India Limited', 'HBL Power Systems Limited', 'HB Stockholdings Limited', 'HB STOCKHOLDINGS INR10', 'HCL Technologies Limited', 'HCL INFOSYSTEMS INR2', 'HealthCare Global Enterprises Limited', 'HCL Infosystems Limited', 'HOUSING DEVELOPMENT FINANCE COR', 'HDFC MUTUAL FUND SENSEX ETF', 'HDFC MUTUAL FUND NIFTY ETF', 'HDFC BANK INR2', 'HeidelbergCement India Limited', 'TTK HEALTHCARE INR10', 'HELIOS & MATHINFTECH LTD.', 'HEC INFRA PROJECTS INR10', 'HELIOS & MATHINFTECH LTD.', 'HEG Limited', 'SYNCOM HEALTHCARE LIMITED', 'Hexa Tradex Limited', 'HERCULES HOISTS LIMITED', 'HEIDELBERGCEMENT INDIA LIMITED', 'Hercules Hoists Limited', 'TTK HEALTHCARE INR10', 'Hero MotoCorp Limited', 'HEXAWARE TECHNOLOGIES LIMITED', 'Hexaware Technologies Limited', 'HEXA TRADEX LTD INR2', 'HEC Infra Projects Ltd', 'Hindustan Motors Limited', 'HINDUSTAN PETROLEUM CORPORATION', 'Hindustan Composites Limited', 'HINDUSTAN MEDIA VENTURES LIMITE', 'Hitech Corporation Limited', 'HINDUSTAN MOTORS INR5', 'Hindustan Copper Limited', 'Hikal Limited', 'HINDUSTAN COPPER LIMITED', 'HI TECH PIPES LTD INR10', 'Bajaj Hindusthan Sugar Limited', 'Johnson Controls - Hitachi Air Conditioning India Limited', 'SREE RAYALASEEMA H INR10', 'HINDUSTAN ORGANIC CHEMICALS LIM', 'Hindalco Industries Limited', 'Hind Syntex Limited', 'Sunil Hitech Engineers Limited', 'HIKAL LIMITED', 'SUNIL HITECH ENGIN INR1', 'Himatsingka Seide Limited', 'HINDUSTAN UNILEVER INR1', 'HIND SYNTEX INR10', 'Hindustan Organic Chemicals Limited', 'Bajaj Holdings & Investment Limited', 'United Breweries (Holdings) Limited', 'HMT Limited', 'Pneumatic Holdings Ltd', 'NARAYANA HRUDAYALA INR10', 'Narayana Hrudayalaya Limited', 'HSIL Limited', 'HSIL LIMITED', 'HT Media Limited', 'The Indian Hume Pipe Company Limited', 'Huhtamaki PPL Limited', 'Husys Consulting Limited', 'Hubtown Limited', 'INDIABULLS HOUSING INR2', 'INDIABULLS VENTURE INR2', 'Indiabulls Ventures Limited', 'ICICI BANK LIMITED', 'ICICI PRUDENTIAL A ICICI PRUDEN', 'ICICI PRUDENTIAL A NIFTY', 'ICSA (INDIA) LIMITED', 'ICICI PRUDENTIAL A 73 830D J RE', 'ICRA Limited', 'ICICI PRUDENTIAL A ICICI PRUDEN', 'ICICIPRAMC - IPRU-8484', 'ICSA (India) Limited', 'IDFC Limited', 'IDBI BANK LIMITED', 'IDFC LIMITED INR10', 'IDFC BANK LTD INR10', 'IDFC Bank Limited', 'IFCI Limited', 'IFB Industries Limited', 'IFGL Refractories Limited', 'IFCI LIMITED', 'Igarashi Motors India Limited', 'IG PETROCHEMICALS LIMITED', 'I G Petrochemicals Limited', 'Industrial Investment Trust Limited', 'IIFL HOLDINGS LTD INR2', 'IIFL Holdings Limited', 'INDUSTRIAL INVESTMENT TRUST LIM', 'IL&FS INVESTMENT MANAGERS LIMIT', 'IL&FS Engineering and Construction Company Limited', 'IL&FS Transportation Networks Limited', 'IL&FS Investment Managers Limited', 'IL&FS Transportation Networks Limited', 'SUPREME (INDIA) IM INR10', 'IMP Powers Limited', 'Indian Overseas Bank', 'Indian Oil Corporation Limited', 'IPCA LABORATORIES INR2', 'IPCA LABORATORIES LIMITED', 'Ipca Laboratories Limited', 'International Paper APPM Limited', 'TATA SPONGE IRON INR10', 'Tata Sponge Iron Limited', 'JAIN IRRIGATION INR2', 'Sunflag Iron And Steel Company Limited', 'ISFT-BE.NS', 'ISMT Limited', 'IntraSoft Technologies Limited', 'SATHAVAHANA ISPAT LIMITED', 'SML Isuzu Limited', 'Sathavahana Ispat Limited', 'ISMT LTD INR5', 'SOUTHERN ISPAT & ENGY LTD INR10', 'ITC Limited', 'PILIND-EQ.NS', 'PIL ITALICA LIFEST INR1', 'PIL Italica Lifestyle Limited', 'ITI Limited', 'PIL ITALICA LIFESTYLE LIMITED', 'ITC LIMITED', 'IVRCL Limited', 'IVRCL LIMITED', 'IVP Limited', 'IZMO LIMITED INR10', 'IZMO Limited', 'Jagsonpal Pharmaceuticals Limited', 'JAIN STUDIOS LTD', 'Jain Studios Limited', 'Jayaswal Neco Industries Limited', 'JAYSHREE TEA INR5', 'JAI CORP LIMITED', 'JAIN STUDIOS INR10', 'JAYSHREE TEA INR5', 'Jaypee Infratech Limited', 'JBM AUTO LTD INR5', 'J. B. Chemicals & Pharmaceuticals Limited', 'JB CHEMICALS & PHARMACEUTICALS', 'JBM Auto Limited', 'Renaissance Jewellery Limited', 'THANGAMAYIL JEWELL INR10', 'Jenson & Nicholson (India) Limited', 'JENSON & NICHOLSON INR2', 'Thangamayil Jewellery Limited', 'Jeypore Sugar Company Ltd.', 'JHS Svendgaard Laboratories Limited', 'JHS SVEND. LAB. LTD', 'JHS SVEND. LAB. LTD', 'Jindal Stainless (Hisar) Limited', 'JINDAL STEEL & PWR INR1.00', 'JIK Industries Limited', 'Jindal Steel & Power Limited', 'Jindal Poly Films Limited', 'JINDAL SAW LTD INR2(DEMAT)', 'JINDAL POLY FILMS LIMITED', 'Jindal Stainless Limited', 'JINDAL STAINLESS INR2', 'JMT Auto Limited', 'JMC Projects (India) Limited', 'Jocil Limited', 'Jyoti Structures Limited', 'Kamdhenu Limited', 'Kalpataru Power Transmission Limited', 'KAVERI SEED COMPAN INR2', 'Kanani Industries Limited', 'KANSAI NEROLAC PAINTS LIMITED', 'KAVVERI TELECOM PR INR10', 'Kamdhenu Limited', 'PERIATEA-BE.NS', 'KAYA LIMITED INR10', 'KALYANI STEELS LIMITED', 'Peria Karamalai Tea & Produce Co. Ltd.', 'Kaya Limited', 'KAVERI SEED COMPANY LIMITED', 'Kamat Hotels (India) Limited', 'KANANI INDUSTRIES LIMITED', 'KALINDEE RAIL NIRMAN (ENGINEERS', 'KAMAT HOTELS (I) LIMITED', 'The Karur Vysya Bank Limited', 'Kaya Limited', 'PERIA KARAMALAI TE INR10', 'Kalindee Rail Nirman (Engineers) Limited', 'The Karnataka Bank Limited', 'The Peria Karamalai Tea and Produce Company Limited', 'KAUSHALYA INFRASTRUCTURE DEVELO', 'Kanoria Chemicals & Industries Limited', 'Kalyani Investment Company Limited', 'Kavveri Telecom Products Limited', 'The KCP Limited', 'KDDL Limited', 'KEYNOTE CORPORATE SERVICES LIMI', 'KEYNOTECORPORATE', 'KESORAM INDUSTRIES LTD', 'KEC INTERNATIONAL INR2', 'KEI Industries Limited', 'KESAR ENTERPRISES LIMITED', 'Kernex Microsystems (India) Limited', 'Keynote Corporate Services Limited', 'KESAR TERMINALS & INFRASTRUCTUR', 'Kellton Tech Solutions Limited', 'Kesoram Industries Limited', 'S H Kelkar and Company Limited', 'KERNEX MICROSYSTEM INR10', 'KESORAM INDUSTRIES LIMITED', 'KESORAM INDUSTRIES INR10', 'KHANDWALA SEC LTD INR10', 'Radico Khaitan Limited', 'RADICO KHAITAN LIMITED', 'Khandwala Securities Limited', 'KHAITAN (INDIA) LTD. INR10', 'Khaitan (India) Limited', 'KHAITAN (INDIA)LTD INR10', 'Kiri Industries Limited', 'KITPLY INDUSTRIES LTD', 'KIRLOSKAR INDUSTRIES LIMITED', 'KIRLOSKAR OIL ENGINES LIMITED', 'Kirloskar Industries Limited', 'KM SUGAR MILLS LTD INR2', 'KM SUGAR MILLS LTD INR2', 'K M Sugar Mills Limited', 'KOTHARI PETROCHEM INR10', 'KOTAK MAHINDRA MF BANKING DIV P', 'KOLTE - PATIL DEVELOPERS LIMITE', 'Kothari Petrochemicals Limited', 'KOTAK MAHINDRA ASS KOTAK NV 20', 'Kokuyo Camlin Limited', 'KOTAK MAHINDRA BAN INR5', 'KOTAKMAMC - KTKNV20ETF', 'Kolte-Patil Developers Limited', 'Sona Koyo Steering Systems Limited', 'K.P.R. MILL LIMITED', 'KRISHNA ENGINEERING WORKS LTD.', 'KRISHNAENGGWORKS', 'KRISHNAENGGWORKS', 'KRIDHAN INFRA LIMI INR2', 'KRBL Limited', 'KRIDHAN INFRA LIMI INR2', 'KSE-BE.NS', 'KSK ENERGY VENTURES LIMITED', 'KSS LTD INR1', 'KS Oils Ltd.', 'KSB Pumps Limited', 'S KUMARS NATIONWIDE LTD', 'KWALITY LIMITED', 'Kwality Limited', 'Larsen & Toubro Limited', 'Morepen Laboratories Limited', 'Lyka Labs Limited', 'Unichem Laboratories Limited', 'Shri Lakshmi Cotsyn Limited', 'Pitti Laminations Limited', 'PENINSULA LAND LIMITED', 'SHRI LAKSHMI COTSYN LTD', 'LAMBODHARA TEXTILE INR5', 'LANDMARK PROP DEV INR1', 'Lakshmi Precision Screws Limited', 'NEULAND LABORATORIES LIMITED', 'Lambodhara Textiles Limited', 'Vivimed Labs Limited', 'Ind-Swift Laboratories Limited', 'PHOENIX LAMPS LTD INR10(DEMAT)', 'SHRI LAKSHMI COTSYN LTD.', 'Neuland Laboratories Limited', 'VIMTA LABS LIMITED', 'Ranbaxy Laboratories Ltd.', 'LARSEN & TOUBRO LIMITED', 'Lakshmi Machine Works Limited', 'Phoenix Lamps Limited', 'LAKSHMI FINANCE & INR10', 'IND-SWIFT LABORATORIES LIMITED', 'SHRI LAKSHMI COTSYN LTD', 'Peninsula Land Limited', 'CAPLIN POINT LABOR INR2', 'Lanco Infratech Limited', 'VIVIMED LABS LIMITED', 'MOREPEN LABORATORI INR2', 'LAKSHMI ENERGY & F INR2', 'ORTIN LABORATORIES INR10', 'LYKA LABS LIMITED', 'ORTIN LABORATORIES INR10', 'Lakshmi Finance & Industrial Corporation Limited', 'The Lakshmi Vilas Bank Limited', 'LCC INFOTECH INR2', 'LCC Infotech Limited', 'LCC INFOTECH INR2', 'INOX LEISURE LIMITED', 'Inox Leisure Limited', 'FIRST LEASING CO OF INDIA', 'L.G. Balakrishnan & Bros Limited', 'Suven Life Sciences Limited', 'Sonata Software Limited', 'SNOWMAN LOGISTICS INR10', 'RPG Life Sciences Limited', 'PREMIER POLYFILM L INR5', 'Nissan Copper Limited', 'PARAMOUNT COMMUNIC INR2', 'Motherson Sumi Systems Limited', 'McLeod Russel India Limited', "Country Condo'S Limited", 'Coromandel International Limited', 'ORCHID PHARMA LTD INR10', 'Resurgere Mines & Minerals India Limited', 'RESURGERE MINES & MINERALS LIMI', 'PRAKASH CONSTROWEL INR1', 'REFEX INDUSTRIES L INR10', 'SAM Industries Limited', 'PRAKASH INDUSTRIES LIMITED', 'MOIL Limited', 'NILA INFRASTRUCTUR INR1', 'Symphony Limited', 'MINDA INDUSTRIES LIMITED', 'CAIRN INDIA LIMITED', 'Nectar Lifesciences Limited', 'ORIENT PRESS LTD INR10', 'LYCOS INTERNET LTD INR2', 'MCLEOD RUSSEL INDIA LIMITED', 'ENGINEERS INDIA LIMITED', 'ORIENT REFRACTORIES LIMITED', 'PONNI SUGARS ERODE INR10.00', 'TIMBOR HOME LIMITED', 'THERMAX LIMITED', 'The Phoenix Mills Limited', 'GRP LTD INR10 (DEMAT)', 'INSECTICIDES (INDIA) LIMITED', 'NESTLE INDIA LIMITED', 'TORRENT PHARMACEUTICALS LIMITED', 'MAJESCO LIMITED INR5', 'SKF INDIA LIMITED', 'POLYPLEX CORPORATION LIMITED', 'Mangalam Timber Products Limited', 'TATA METALIKS LIMITED', 'TI Financial Holdings Limited', 'SPLENDID METAL PRO INR10', 'Banco Products (India) Limited', 'UPL Limited', 'Salora International Limited', 'VRL LOGISTICS LTD INR10', 'STEL HOLDINGS LIMITED', 'IndusInd Bank Limited', 'SIGNET INDUSTRIES INR1', 'MOLD-TEK PACKAGING INR5', 'MCDOWELL HOLDINGS LIMITED', 'GREAVES COTTON LIMITED', 'TAMILNADU TELECOMM INR10', 'UNIVERSAL CABLES INR10', 'Gravita India Limited', 'TECHINDIA NIRMAN LIMITED', 'SHARDA MOTOR INDUS INR10', 'NITCO LIMITED', 'UNITY INFRAPROJECTS LIMITED', 'PNEUMATIC HOLDINGS INR10', 'GRASIM INDUSTRIES INR2', 'PROZONE INTU PROPE INR2', 'TATA STEEL LIMITED', 'PAN INDIA CORP INR10', 'INDO TECH TRANSFORMERS LIMITED', 'Castex Technologies Limited', 'SUPREME INDUSTRIES INR2', 'SHREYAS-BE.NS', 'MBL INFRASTRUCTURES LIMITED', 'GRAVITA INDIA LIMITED', 'DELTA MAGNETS LTD INR10', 'Punj Lloyd Limited', 'LLOYDS FINANCE INR10', 'LML Limited', 'PETRONET LNG LIMITED', 'PETRONET LNG INR10', 'Petronet LNG Limited', 'Sical Logistics Limited', 'Patel Integrated Logistics Limited', 'Shreyas Shipping and Logistics Limited', 'Lovable Lingerie Limited', 'Lokesh Machines Limited', 'Snowman Logistics Limited', 'LOVABLE LINGERIE LIMITED', 'VRL Logistics Limited', 'Sakthi Sugars Limited', 'Prime Securities Limited', 'Infomedia Press Limited', 'TVS Motor Company Limited', 'Tata Teleservices (Maharashtra) Limited', 'TRF Limited', 'Titan Company Limited', 'Tijaria Polypipes Limited', 'Tilaknagar Industries Ltd.', 'Thermax Limited', 'Tecpro Systems Limited', 'Tata Motors Limited', 'Tata Communications Limited', 'TAKE Solutions Limited', 'Surana Solar Limited', 'Lumax Automotive Systems Limited', 'Lux Industries Limited', 'LUMAX INDUSTRIES LIMITED', 'LUMAX AUTO TECHNOLOGIES LIMITED', 'OPAL LUXURY TIME P INR10', 'LUX INDUSTRIES LTD INR2', 'Lumax Industries Limited', 'LUPIN LTD INR2', 'Lycos Internet Limited', 'Mahanagar Telephone Nigam Limited', 'Mastek Limited', 'Marksans Pharma Limited', 'Malwa Cotton Spinning Mills Limited', 'Malu Paper Mills Limited', 'MAHINDRA HOLIDAYS & RESORTS IND', 'MARUTI SUZUKI IND INR5', 'MALWA COTTON SPG. MILLS L', 'Manaksia Industries Ltd', 'MANAKSIA INDUSTRIE INR1', 'Man Industries (India) Limited', 'Marico Limited', 'RADHA MADHAV CORP INR10', 'Mahindra & Mahindra Financial Services Limited', 'MANAKSIA STEELS LT INR1', 'MARAL OVERSEAS LIMITED', 'SUPREME TEX MART INR5', 'Man Infraconstruction Limited', 'MBL Infrastructures Limited', 'UNITED SPIRITS INR10', 'McDowell Holdings Limited', 'Sambhaav Media Limited', 'Radaan Mediaworks India Limited', 'Precot Meridian Limited', 'Mig Media Neurons Limited', 'Splendid Metal Products Limited', 'MIG MEDIA NEURONS INR10', 'Poly Medicure Limited', 'SAMBHAAV-BE.NS', 'MIG Media Neurons Limited', 'OM METALS INFRAPROJECTS LIMITED', 'MEGASOFT LIMITED', 'MEP Infrastructure Developers Limited', 'Shilpa Medicare Limited', 'MEP INFRASTRUCTURE INR10', 'Melstar Information Technologies Limited', 'MERCK LIMITED', 'MEGHMANI ORGANICS LIMITED', 'Ratnamani Metals & Tubes Limited', 'INDRAPRASTHA MEDICAL CORPORATIO', 'Indraprastha Medical Corporation Limited', 'Man Coat Metal & Ind Ltd', 'INDBANK MERCHANT BANKING SERVIC', 'THEMIS MEDICARE LT INR10', 'MELSTAR INFORMATION TECH', 'POWER MECH PROJECT INR10', 'MANAKSIA COATED ME INR1', 'Max Financial Services Limited', 'Mahindra Holidays & Resorts India Limited', 'Mirza International Limited', '20 Microns Limited', 'Minda Corporation Limited', 'NIRVIKARA PAPER MI INR10', 'Pudumjee Pulp & Paper Mills Limited', 'SIRPUR PAPER MILLS LTD', 'Sirpur Paper Mills Ltd.', 'RAJ OIL MILLS LTD INR10', 'MIRZA INTERNATIONAL LIMITED', 'Sarda Energy & Minerals Limited', 'PHOENIX MILLS INR2', 'Suryajyoti Spinning Mills Limited', '8K MILES SOFTWARE INR5 (DEMAT)', 'PUDUMJEE PULP & PA INR2.00', 'Rajapalayam Mills Ltd.', 'MMTC Limited', 'Spice Mobility Limited', 'Morarjee Textiles Limited', 'Mohit Industries Limited', 'MOTHERSON SUMI SYS INR1', 'MOHIT INDUSTRIES INR10', 'MORARJEE TEXTILES INR7', 'MOSER-BAER (I) LIMITED', 'MOTILAL OSWAL FINA GROWTH UNITS', 'Mold-Tek Packaging Limited', 'Monsanto India Limited', 'SHARDA MOTOR INDUS INR10', 'Sanghvi Movers Limited', 'SPICE MOBILITY LTD INR3', 'RAI SAHEB REKHCHAN INR10', 'MOTILAL OSWAL FINA INR1', 'Moser Baer India Limited', 'SANGHVI MOVERS INR2.00', 'UFO MOVIEZ INDIA INR10', 'MONSANTO INDIA LIMITED', 'MphasiS Limited', 'MPS Limited', 'MPS LTD INR10', 'MRF LIMITED', 'MRO-TEK Realty Limited', 'MRO-TEK REALTY LTD INR5', 'MSP Steel & Power Limited', 'Shree Rama Multi-Tech Limited', 'Sundaram Multi Pap Limited', 'MUKAND 0.01 % CUM RED PRF INR10', '3rd Rock Multimedia Ltd', '3rd Rock Multimedia Limited', 'Mukand Limited', 'Munjal Showa Limited', '3RD ROCK MULTIMEDI INR10', 'MUKAND LIMITED', 'MUTHOOT CAPITAL SE INR10', 'SHREE RAMA MULTI INR5', 'MUTHOOT CAPITAL SE INR10', 'MURLI INDUSTRIES INR2', 'Mukand Engineers Limited', 'MVL Limited', 'MVL LTD INR1', 'Navkar Corporation Limited', 'Natco Pharma Limited', 'Nakoda Limited', 'NAKODA LTD INR5', 'Nalwa Sons Investments Limited', 'PRITISH NANDY COMM INR10', 'TAMIL NADU NEWSPRINT & PAPERS L', 'Nahar Spinning Mills Ltd', 'NAGREEKA CAPITAL & INR5', 'NANDAN DENIM LTD INR10', 'NATCO PHARMA LTD INR2', 'NAGARJUNA OIL REFI INR1', 'PUNJAB NATL BANK INR2', 'NAVKAR CORPORATION INR10', 'Punjab National Bank', 'NAHAR IND ENTERPRI INR10', 'PUNJAB NATL BANK INR2', 'NAGREEKA CAPITAL & INR5', 'Nagarjuna Oil Refinery Limited', 'Nahar Industrial Enterprises Limited', 'Tamil Nadu Newsprint and Papers Limited', 'NISSAN COPPER LTD INR10', 'NCC Limited', 'NISSAN COPPER LIMITED', 'NCL INDUSTRIES LIMITED', 'New Delhi Television Limited', 'NECTAR LIFESCIENCES LIMITED', 'Sun TV Network Limited', 'Neyveli Lignite Corporation Limited', 'NEOCORP-BE.NS', 'Nesco Limited', 'Net 4 India Limited', 'Raj Television Network Limited', 'Network18 Media & Investments Limited', 'Nestlé India Limited', 'Next Mediaworks Limited', 'NELCAST LIMITED', 'T.V. Today Network Limited', 'NESCO LIMITED', 'DEN Networks Limited', 'TV TODAY NETWORK LIMITED', 'NEPC India Limited', 'Smartlink Network Systems Limited', 'SBI MUTUAL FUND SBI-ETF NIFTY N', 'NEXT MEDIAWORKS LT INR10', 'NEPC INDIA LTD', 'RAJ TEL NETWORK INR5', 'NELCO LIMITED', 'SBI MUTUAL FUND SBI-ETF NIFTY N', 'SITI Networks Limited', 'NORTHGATE COM TECH INR10', 'Spacenet Enterprises India Limited', 'NORTHGATE COM TECH INR10', 'NICCO CORPN INR2', 'SBI MUTUAL FUND SBI-ETF NIFTY 5', 'NILKAMAL LIMITED', 'NIIT LIMITED', 'Nitin Spinners Ltd.', 'NICCO CORPN INR2', 'NIIT Technologies Limited', 'DEEPAK NITRITE INR2', 'TECHINDIA NIRMAN L INR10', 'NITIN SPINNERS LIMITED', 'Balkrishna Paper Mills Limited', 'Indo National Limited', 'NILA INFRASTRUCTUR INR1', 'NITIN FIRE PROTECTION INDUSTRIE', 'Nilkamal Limited', 'Nirvikara Paper Mills Ltd', 'SBI MUTUAL FUND SBI-ETF NIFTY B', 'SBI MUTUAL FUND SBI-ETF NIFTY B', 'SBI MUTUAL FUND SBI-ETF NIFTY 5', 'Nitco Limited', 'Techindia Nirman Limited', 'N.K Industries Limited', 'NOCIL LIMITED', 'DE NORA INDIA INR10', 'Grindwell Norton Limited', 'De Nora India Limited', 'Noesis Industries Limited', 'NORBEN TEA &EXPORTS LTD', 'NOESIS INDUSTRIES INR10', 'UNIVCABLES NPP130599 DEPO', 'VISESH INFO NPP231299 DEP', 'NRB BEARING LIMITED', 'NRC LIMITED', 'Nu Tek India Limited', 'OCL India Limited', 'ORIENTAL CARB & CH INR10', 'The Shipping Corporation of India Limited', 'The Tinplate Company Of India Limited', 'POWER GRID CORPORATION OF INDIA', 'The State Trading Corporation of India Limited', 'State Bank of Travancore', 'ORIENTAL BK OF COM INR10', 'Steel Authority of India Limited', 'THE TINPLATE COMPANY OF INDIA L', 'United Bank of India', 'Bank of Baroda', 'State Bank of Mysore', 'Tourism Finance Corporation of India Limited', 'WHIRLPOOL OF INDIA LIMITED', 'Oil Country Tubular Limited', 'Raj Oil Mills Limited', 'Savita Oil Technologies Limited', 'SAVITA OIL TECHNOLOGIES LIMITED', 'Omkar Speciality Chemicals Limited', 'Omnitech Infosolutions Ltd', 'Om Metals Infraprojects Limited', 'OMAXE LIMITED', 'STORE ONE RETAIL INR10', 'ONELIFE CAPITAL ADVISORS LIMITE', 'Oriental Trimex Limited', 'Orient Press Limited', 'VINATI ORGANICS INR2', 'ORICON ENTERPRISES INR2', 'ORIENT PAPER & INDUSTRIES LIMIT', 'Orient Paper & Industries Limited', 'Orient Refractories Limited', 'Ortel Communications Limited', 'ORTEL COMMUNICATIO INR10', 'ORIENTAL TRIMEX LTD INR10', 'ORIENTAL TRIMEX INR10', 'Panchsheel Organics Ltd', 'Meghmani Organics Limited', 'ORICON ENTERPRISES INR2', 'The Orissa Minerals Development Company Limited', 'Orient Green Power Company Limited', 'ORIENT GREEN POWER INR10', 'ORIENTAL HOTELS LIMITED', 'Vinati Organics Limited', 'Orchid Pharma Limited', 'Oriental Hotels Limited', 'Signet Industries Limited', 'PRADIP OVERSEAS LT INR10', 'Maral Overseas Limited', 'Pradip Overseas Limited', 'BANG OVERSEAS LTD INR10', 'Page Industries Limited', 'Rainbow Papers Limited', 'PATSPIN INDIA INR10', 'PALRED TECHNOLOGIE INR10', 'Parsvnath Developers Limited', 'PARAS PETROFILS LTD.', 'Palred Technologies Limited', 'Servalakshmi Paper Limited', 'PANAMA PETROCHEM LIMITED', 'PALRED TECHNOLOGIE INR10', 'SHALIMAR PAINTS LIMITED', 'Patspin India Limited', 'Paramount Printpackaging Limited', 'Shalimar Paints Limited', 'Palred Technologies Ltd', 'PARAS PETROFILS LT INR1', 'Paramount Communications Limited', 'MALU PAPER MILLS LIMITED', 'PARAMOUNT PRINTPACK LTD', 'PANCHSHEE.NS', 'RAINBOW PAPERS LIMITED', 'PANORAMIC UNIVERSL INR5', 'Panama Petrochem Limited', 'SERVALAKSHMI PAPER INR10', 'Panoramic Universal Limited', 'PREMIER AUTO ELECT INR10', 'Star Paper Mills Limited', 'PBA Infrastructure Limited', 'PUDUMJEE INDUSTRIE INR2', 'Pudumjee Paper Products Limited', 'Pudumjee Industries Limited', 'Southern Petrochemical Industries Corporation Limited', 'LINC PEN & PLASTIC INR10', 'Petron Engineering Construction Limited', 'PEARL POLYMERS LIMITED', 'PEARL ENG POL INR10(POST RECON)', 'PERFECT INFRAENGIN INR10', 'Pearl Polymers Limited', 'Pennar Industries Limited', 'LINC PEN & PLASTIC INR10', 'Paras Petrofils Ltd', 'Supreme Petrochem Limited', 'Chennai Petroleum Corporation Limited', 'PENNAR ENGINEERED INR10', 'Persistent Systems Limited', 'PENNAR ENGINEERED INR10', 'Tamilnadu Petroproducts Limited', 'PENNAR ENGINEERED INR10', 'SOUTHERN PETROCHEMICALS INDUSTR', 'MANALI PETROCHEMS INR5', 'Manali Petrochemicals Limited', 'Pfizer Limited', 'SMS Pharmaceuticals Limited', 'LINCOLN PHARMA LTD INR10', 'SUN PHARMACEUTICALS INDUSTRIES', 'Torrent Pharmaceuticals Limited', 'PLETHICO PHARMACE LIMITED', 'PIRAMAL PHYTOCARE INR10', 'Plethico Pharmaceuticals Limited', 'PLETHICO PHARMA INR10', 'SHASUN PHARMACEUTICALS LIMITED', 'Piramal Phytocare Limited', 'SMS PHARMACEUTICALS LIMITED', 'SURYA PHARMACEUTICAL LTD.', 'Bal Pharma Limited', 'LINCOLN PHARMA LTD INR10', 'PI Industries Limited', 'Pilani Investment and Industries Corporation Limited', 'PILANI INVESTMENT INR10.00', 'PIDILITE INDUSTRIE INR1(POST SU', 'Srikalahasthi Pipes Limited', 'Pidilite Industries Limited', 'Texmo Pipes and Products Limited', 'SRIKALAHASTHI PIPE INR10', 'The P K Tea Prod Co Ltd', 'Plastiblends India Ltd.', 'PNC Infratech Limited', 'Pneumatic Holdings Limited', 'PNC INFRATECH LTD INR2', 'Polaris Consulting & Services Limited', 'Ponni Sugars (Erode) Limited', 'TIJARIA POLYPIPES LTD INR10', 'Premier Polyfilm Ltd.', 'S.E. POWER LIMITED', 'Pochiraju Industries Limited', 'RATTANINDIA POWER INR10', 'PREMIER POLYFILM L INR5', 'Polyplex Corporation Limited', 'Honda Siel Power Products Limited', 'Reliance Power Limited', 'Vardhman Polytex Limited', 'Torrent Power Limited', 'RattanIndia Power Limited', 'S. E. Power Limited', 'VISAGAR POLYTEX INR1', 'Power Mech Projects Limited', 'VIKASHMET.NS', 'SHEKHAWATI POLY INR1', 'Visagar Polytex Limited', 'Shekhawati Poly-Yarn Limited', 'POLY MEDICURE LIMITED', 'Career Point Limited', 'The Tata Power Company Limited', 'POWER GRID CORP INR10', 'TD Power Systems Limited', 'Pricol Limited prior to merger with Pricol Pune Limited', 'Premier Limited', 'Puravankara Limited', 'Simplex Projects Limited', 'VKS Projects Limited', 'TTK Prestige Limited', 'Prakash Steelage Limited', 'Pratibha Industries Limited', 'Rasoya Proteins Limited', 'Provogue (India) Limited', 'Prakash Constrowell Limited', 'PRITHVI SOFTECH LTD INR10', 'PSL Limited', 'PSL LIMITED', 'PSL LIMITED', 'Punjab & Sind Bank', 'PTC India Limited', 'PTL Enterprises Limited', 'PURAVANKARA PROJECTS LIMITED', 'Shakti Pumps (India) Limited', 'PVR Limited', 'PVP Ventures Limited', 'Rana Sugars Limited', 'Ramky Infrastructure Limited', 'Rajvir Industries Limited', 'Ingersoll-Rand (India) Limited', 'Rama Steel Tubes Limited', 'Raj Rayon Industries Limited', 'Raymond Limited', 'Ramsarup Industries Limited', 'Indo Rama Synthetics (India) Limited', 'RAMKY INFRASTRUCTURE LIMITED', 'RAIN INDUSTRIES LT INR2', 'RAMSARUP INDUSTRIE INR10', 'Rallis India Limited', 'RADAAN MEDIAWORKS (I) LTD', 'Ramco Industries Limited', 'INDO RAMA SYNTHETICS (INDIA) LI', 'Rane Engine Valve Limited', 'RAJSHREE SUG &CHEM INR10', 'RAMA STEEL TUBES INR5', 'Sree Rayalaseema Hi-Strength Hypo Limited', 'RATTANINDIA INFRAS INR2', 'RASOYA PROTEINS LI INR1', 'Rama Steel Tubes Limited', 'Ranklin Solutions Ltd.', 'RattanIndia Infrastructure Limited', 'RANE BRAKE LINING LIMITED', 'Rane Holdings Limited', 'Rane (Madras) Limited', 'Rain Industries Limited', 'Ramco Systems Limited', 'Radha Madhav Corporation Limited', 'Reliance Communications Limited', 'Reliance Defence and Engineering Limited', 'Reliance Industrial Infrastructure Limited', 'Redington (India) Limited', 'RELIANCE INDUSTRIAL INFRASTRUCT', 'Rico Auto Industries Limited', 'Rolta India Limited', 'SANGHIINDUS ROLL SETT', 'Surya Roshni Limited', 'Rossell India Limited', 'RPP Infra Projects Limited', 'RPG LIFE SCIENCES LIMITED', 'R Systems International Limited', 'R. S. Software (India) Limited', 'RSWM Limited', 'SBIAMC - RSDFSA27GR', 'Ruchira Papers Limited', 'Rushil Décor Limited', 'Rupa & Company Limited', 'HOTEL RUGBY LTD INR10', 'RUPA & COMPANY LIMITED', 'RUCHI INFRASTRUCTURE LTD', 'The Ruby Mills Limited', 'Ruchi Infrastructure Limited', 'Hotel Rugby Limited', 'Sanghi Industries Limited', 'SAMTEL COLOR LTD', 'Saksoft Limited', 'Saregama India Limited', 'SAYAJIHOT.NS', 'Super Sales India Ltd.', 'Sarthak Industries Ltd', 'SAKSOFT LIMITED', 'Savera Industries Limited', 'The Sandesh Limited', 'Sangam (India) Limited', 'SALORA INTL INR10', 'SAYAJIHOTL-BE.NS', 'SBIAMC - SETFBANK', 'SBIAMC - SETFNIFJR', 'SBIAMC - SETFNIFTY', 'SB & T INTL LTD INR10', 'Thomas Scott (India) Limited', 'THOMAS SCOTT (INDI INR10', 'Maharashtra Scooters Limited', 'THOMAS SCOTT (INDI INR10', 'Sequent Scientific Limited', 'CAMLIN FINE SCIENC INR1', 'Maharashtra Seamless Limited', 'Inventure Growth & Securities Limited', 'SEL MANUFACTURING COMPANY LIMIT', 'SFCL-BE.NS', 'Shyam Telecom Limited', 'Shiva Texyarn Limited', 'Shoppers Stop Limited', 'SHEMAROO ENTERTAIN INR10', 'Shivam Autotech Limited', 'SHAIVAL REALITY LT INR10', 'Liberty Shoes Limited', 'SHOPPERS STOP INR5', 'Shree Renuka Sugars Limited', 'VARUN SHIPPING INR10', 'SHREYANS INDUSTRIES LIMITED', 'Shilpi Cable Technologies Limited', 'SHREE RENUKA SUGARS LIMITED', 'Varun Shipping Co. Ltd.', 'STRIDES SHASUN LTD INR10', 'Strides Shasun Limited', 'SHRIRAM TRANSPORT INR10', 'Shreyans Industries Limited', 'Shrenuj & Company Limited', 'Simbhaoli Sugars Limited', 'SIMPLEX INFRASTRUC INR2', 'Siyaram Silk Mills Limited', 'SIGNET INDUSTRIES INR1', 'SIYARAM SILK MILLS LIMITED', 'Sicagen India Limited', 'SIMPLEX CASTINGS LTD.', 'SIMBHAOLI SUGARS LIMITED', 'SIL Investments Ltd.', 'STANDARD INDS INR5', 'Sintex Industries Limited', 'REI Six Ten Retail Limited', 'Standard Industries Limited', 'Simplex Infrastructures Limited', 'SJVN Limited', 'Skipper Limited', 'SKIL INFRASTRUCTUR INR10', 'Bharat Financial Inclusion Limited', 'SKIL Infrastructure Limited', 'SKIPPER LTD INR1', 'SKIL INFRASTRUCTURE LTD.', 'SMSANCO.NS', 'SMMOMAI.NS', 'SMOPAL.NS', 'SMSIIL.NS', 'SMMITCON.NS', 'SMTHEJO.NS', 'SMVETO.NS', 'Solar Industries India Limited', 'Infinite Computer Solutions (India) Limited', 'CALIFORNIA SOFTWARE CO LT', 'TANLA SOLUTIONS LIMITED', 'SOFTTECHGRNPP070100', 'SOFTWARE TECH GP INR10', 'Compucom Software Limited', 'SOMA TEXTILE INUSTRIES LT', 'SOMA TEXTILE & IND INR10', 'TELEDATAI.NS', 'SURANA SOLAR LTD INR5', 'COMPUCOM SOFTWARE LIMITED', 'PRITHVI INFO. SOLN. LTD.', 'California Software Company Limited', 'Sobha Limited', 'aurionPro Solutions Limited', 'Prithvi Softech Limited', '8K Miles Software Services Limited', 'SOBHA LIMITED', 'SONATA SOFTWARE INR1', 'Soma Textiles & Industries Limited', 'SURYAJYOTI SPG MIL INR10', 'SPML Infra Limited', 'Spentex Industries Limited', 'Speciality Restaurants Limited', 'SPL Industries Limited', 'Vardhman Special Steels Limited', 'SRF Limited', 'SRICHAMUN.NS', 'Sreeleathers Limited', 'PAN INDIA CORP INR10', 'SREI Infrastructure Finance Limited', 'SREELEATHERS LTD INR10', 'TVS Srichakra', 'SRGINFOTECH (INDIA) LTD.', 'SRS Limited', 'Vedanta Limited', 'SSLT-EQ.NS', 'Sterlite Technologies Limited', 'STI INDIA LTD', 'STI India Limited', 'STANDARD CHART PLC IDR EACH REP', 'STI INDIA INR10', 'VISA Steel Limited', 'Sterling Tools Limited', 'STEL HOLDINGS LTD INR10', 'STERLITE TECHNOLOGIES LIMITED', 'PRAKASH STEELAGE LIMITED', 'STERLING TOOLS LIMITED', 'STEL Holdings Limited', 'Supreme Infrastructure India Limited', 'Suzlon Energy Limited', 'Sunteck Realty Limited', 'Sumeet Industries Limited.', 'Sundaram-Clayton Limited', 'SUPRAJIT ENGINEERING LIMITED', 'Suprajit Engineering Limited', 'SUNDARAM-BE.NS', 'Superhouse Limited', 'Summit Securities Limited', 'Mawana Sugars Limited', 'Sudar Industries Limited', 'The Supreme Industries Limited', 'SUPERHOUSE LTD INR10', 'Super Spinning Mills Limited', 'Suryalakshmi Cotton Mills Limited', 'SUDAR INDUSTRIES L INR10', 'SURANA INDUSTRIES INR10', 'Uttam Sugar Mills Limited', 'Supreme Tex Mart Limited', 'Neueon Towers Limited', 'UTTAM SUGAR MILLS INR10', 'SUPER SPINNING INR1', 'UGAR SUGAR WORKS INR1', 'SUNDARAM FINANCE LIMITED', 'SUNDARMAMC - WB3RG', 'SUPREME TEX MART INR5', 'Surana Corporation Limited', 'NEUEON TOWERS LTD', 'SAKTHI SUGARS LIMITED', 'PARRYS SUGAR INDUS INR10', 'Parrys Sugar Industries Limited', 'Subex Limited', 'SUBEX LIMITED', 'SUMEET INDUSTRIES INR10', 'Swan Energy Limited', 'VETO SWITCHGEARS A INR10', 'Swelect Energy Systems Limited', 'SYNGENE INTERNATIO INR10', 'TECPRO SYSTEMS LTD INR10', 'Syngene International Limited', 'TECPRO SYSTEMS LIMITED', 'Banswara Syntex Limited', 'SYNDICATE BANK', 'TECPRO SYSTEMS LTD', 'Prajay Engineers Syndicate Limited', 'Syndicate Bank', 'SYMPHONY LIMITED', 'WEBSOL ENERGY SYST INR10', 'Talbros Automotive Components Limited', 'Tata Metaliks Limited', 'Tarmat Limited', 'TANTIA CONSTRUCTIONS LIMITED', 'TALBROS AUTO INR10', 'Tamilnadu Telecommunications Limited', 'TATA TELESERVICES (MAHARASHTRA)', 'Tata Investment Corporation Limited', 'Tantia Constructions Limited', 'Tantia Constructions Limited', 'Tata Coffee Limited', 'TATA INVESTMENT CORPORATION LIM', 'Tanla Solutions Limited', 'Tarapur Transformers Limited', 'TCP Limited', 'TCPLTD-BE.NS', 'TCI FINANCE LTD INR10', 'TCI DEVELOPERS LTD INR10', 'TeamLease Services Limited', 'CASTEX TECHNOLOGIE INR2', 'Technocraft Industries (India) Limited', 'VARDHMAN TEXTILES LIMITED', 'Transwarranty Finance Limited', 'TRANSWARRANTY FINA INR10', 'THOMAS COOK (INDIA) LIMITED', 'Indo Thai Securities Limited', 'Time Technoplast Limited', 'TIL Limited', 'TIL LIMITED', 'Timken India Limited', 'TECHNOCRAFT INDUSTRIES (INDIA)', 'Tips Industries Limited', 'Timbor Home Limited', 'MANGALAM TIMBER INR10', 'TIMBOR HOME LTD INR10', 'TIMKEN INDIA LIMITED', 'TIPS INDUSTRIES LIMITED', 'Titagarh Wagons Limited', 'TITAN COMPANY LIMITED', 'VST TILLERS TRACT INR10', "TODAY'S WRITING PRODUCTS", 'TOKYO PLAST INTL INR10', 'Tokyo Plast International Limited', 'TPL PLASTECH LTD. INR10', 'TPL PLASTECH LTD. INR10', 'Tricom India Limited', 'Transformers & Rectifiers (India) Limited', 'Triveni Engineering & Industries Limited', 'TRICOM INDIA LTD INR2', 'TRIGYN TECHNOLOGIE INR10', 'TT LTD INR10', 'T.T. Limited', 'TULIP TELECOM LIMITED', 'Triveni Turbine Limited', 'UB ENGINEERING LTD', 'UNITED BREWERIES (HOLDINGS) LIM', 'UCO Bank', 'UFLEX LIMITED', 'UJAAS ENERGY LTD INR1', 'Ujaas Energy Ltd.', 'CARBORUNDUM UNIVERSAL LIMITED', 'Unity Infraprojects Limited', 'UNIPLY INDUSTRIES INR10', 'Carborundum Universal Limited', 'Universal Cables Limited', 'Mayur Uniquoters Limited', 'UNITECH LIMITED', 'UPL LIMITED INR2', 'UTI ASSET MANAGEME FTI XIX X 10', 'UTI MUTUAL FUND UTI NIFTY ETF', 'UTI MUTUAL FUND UTI- SENSEX ETF', 'Vardhman Textiles Limited', 'VAKRANGEE LTD INR1', 'VASCON ENGINEERS LIMITED', 'Vakrangee Limited', 'VASWANI INDUSTRIES LTD INR10', 'VARUN INDUS. LTD.', 'VA Tech Wabag Limited', 'Value Industries Limited', 'Venus Remedies Limited', 'SPEC VENTURES LTD INR1', "Venky's (India) Limited", 'VEDANTA LIMITED INR1', 'VENUS REMEDIES LIMITED', 'Vedanta Limited', 'MAGNUM VENTURES LT INR10', 'V-Guard Industries Limited', 'MPS Infotecnics Limited', 'VISHNU CHEMICALS L INR10', 'Vipul Limited', 'VISESH INFOTECNICS INR1', 'Vindhya Telelinks Limited', 'VINDHYA TELELINKS LIMITED', 'VINYL CHEMICALS(IN INR1', 'Viceroy Hotels Limited', 'VIJAYA BANK INR10', 'Vishnu Chemicals Limited', 'VIPUL LTD INR1', 'Vijaya Bank', 'VISU INTERNATIONAL INR10', 'VKS PROJECTS LTD INR1', 'VLS FIN LTD INDIA INR10', 'V-MART RETAIL LIMITED', 'V-MART RETAIL LTD INR10', 'VOLTAMP TRANSFORMERS LIMITED', 'VTM Limted', 'WABCO INDIA LIMITED', 'WALCHANDNAGAR INDUSTRIES LIMITE', 'WANBURY LTD INR10', 'Walchandnagar Industries Limited', 'WELSPUN ENTERPRISE INR10', 'Welspun Corp Limited', 'WEALTH FIRST PORTF INR10', 'Weizmann Limited', 'WELSPUN ENTERPRISE INR10', 'Wheels India Limited', 'INOX INDIA LIMITED INR10', 'Precision Wires India Ltd.', 'Inox Wind Limited', 'Windsor Machines Limited', 'KRISHNA ENGINEERING WORKS LTD.', 'WONDERLA HOLIDAYS INR10', 'WS Industries (India)', 'ADANI TRANSMISS.IN INR1', 'ADI FINECHEM LTD INR10', 'Greenearth Resources & Projects Limited', 'Ausom Enterprise Limited', 'Autoline Industries Limited', 'Honeywell Automation India Limited', 'AUTOLITE (INDIA) LIMITED', 'Bajaj Finserv Limited', 'Balaji Telefilms Limited', 'BALKRISHNA INDUSTRIES LIMITED', 'Balrampur Chini Mills Limited', 'BALKRISHNA INDUSTRIES LTD', 'Balkrishna Industries Limited', 'Corporation Bank', 'Indbank Merchant Banking Services Limited', 'INDUSIND BANK INR10', 'Bartronics India Limited', 'BARTRONICS INDIA L INR10', 'Bata India Limited', 'BEARDSELL LTD INR10', 'Beardsell Limited', 'BANARAS BEADS LTD INR10', 'MENON BEARINGS LTD INR1', 'BRANDHOUSE RETAILS LTD', 'BRANDHOUSE RETAILS INR10', 'BRANDHOUSE RETAILS INR10', 'Brigade Enterprises Limited', 'Britannia Industries Limited', 'BROADCAST INITIATI INR10', 'CORDS CABLE INDUST INR10', 'Finolex Cables Limited', 'Cords Cable Industries Limited', 'Precision Camshafts Limited', 'Cantabil Retail India Limited', 'CANTABIL RETAIL INDIA LIMITED', 'Can Fin Homes Limited', 'C & C CONSTRUCTIONS LIMITED', 'Capital First Limited', 'Reliance Capital Limited', 'CASTEX TECHNOLOGIES LTD.', 'CASTROL INDIA INR5', 'Mangalore Chemicals & Fertilizers Limited', 'CHROMATIC INDIA LIMITED', 'Coal India Limited', 'MANAKSIA COATED ME INR1', 'Samtel Color Limited', 'SAMTEL COLOUR INR10', 'Colgate-Palmolive (India) Limited', 'MITCON CONSU & ENG INR10', 'Thomas Cook (India) Limited', 'Cosmo Films Limited', 'Salona Cotspin Limited', 'SALONA COTSPIN INR10', 'Delta Magnets Limited', 'DELTA CORP LIMITED', 'Dena Bank', 'DENA BANK', 'MASTEK - DEPO SETT', 'ENERGY DEV CO LTD INR10(DEMAT)', 'MAHINDRA LIFESPACE DEVELOPERS L', 'Indowind Energy Limited', 'INDOWIND ENERGY INR10', 'Engineers India Limited', 'Technofab Engineering Limited', 'TECHNOFAB ENGINEERING LIMITED', 'A2Z INFRA ENGINEER INR10', 'THEJO ENGINEERING INR10', 'ENTEGRA INFRASTRUC INR10', 'ENTEGRA INFRASTRUC INR10', 'Fiem Industries Limited', 'INDUS FILA LIMITED', 'Finolex Industries Limited', 'MAGMA FINCORP LIMITED', 'Sastasundar Ventures Limited', 'L&T Finance Holdings Limited', 'REPCO HOME FINANCE INR10', 'GRUH Finance Limited', 'Repco Home Finance Limited', 'MANAPPURAM FINANCE LIMITED', 'MICROSEC FINANCIAL SERVICES LIM', 'Manappuram Finance Limited', 'LIC HOUSING FINANCE LIMITED', 'GRASIM INDUSTRIES LIMITED', 'Grasim Industries Limited', 'Graphite India Limited', 'GREENLAM INDUSTRIE INR5', 'Greenlam Industries Ltd.', 'Greenply Industries Limited', 'GREENLAM INDUSTRIE INR5', 'GRP Limited', 'The Indian Hotels Company Limited', 'HOV Services Limited', 'INNOVENTIVE IND LTD', 'Innoventive Industries Limited', 'Remsons Industries Limited', '3M India Limited', 'Insecticides (India) Limited', 'Linde India Limited', 'Sam Industries Ltd', 'REPRO INDIA LIMITED', 'Responsive Industries Limited', 'Indosolar Limited', 'IND SWIFT LTD INR2', 'Infosys Limited', 'MERCATOR LIMITED', 'PRECOT MERIDIAN LIMITED', 'REGENCYCERAMICS-LTD', 'V2 Retail Limited', '3I INFOTECH LTD INR10', 'LIC MUTUAL FUND ETF- NIFTY 50-', '3I INFOTECH LTD.', 'RELIANCE MUTUAL FD RELIANCE ETF', 'InfoBeans Tech Ltd', 'Sadbhav Infrastructure Project Limited', 'LICNAMC - LICNFENGP', 'RELIANCE MUTUAL FD RELIANCE ETF', 'Texmaco Infrastructure & Holdings Limited', 'MELSTAR INFORMATIO INR10', 'RELIANCE NIPPON LI RELIANCE ETF', 'LIC MUTUAL FUND G-SEC LONG TERM', 'LICNAMC - LICNMFET', 'SADBHAV INFRA PROJ INR10', '3i Infotech Limited', 'INFOMEDIA PRESS LI INR10', 'LIC MUTUAL FUND G-SEC LONG TERM', 'V2 RETAIL LTD INR10', 'Sanofi India Limited', 'SANCO IND LIMITED INR10', 'THEMIS MEDICARE LT INR10', 'Trident Limited', 'MANAKSIA INDUSTRIE INR1', 'PALRED-EQ.NS', 'Mercator Limited', 'Insecticides (India) Limited', 'COROMANDEL INTERNATIONAL LIMITE', 'S.E. Investments Limited', 'LINDE INDIA LTD INR10', 'Madhucon Projects Limited', 'Mahindra & Mahindra Limited', 'Majesco Limited', 'MAJESCO LIMITED INR5', 'Manaksia Limited', 'MAN INDUSTRIES (INDIA) LIMITED', 'SEL Manufacturing Company Limited', 'Mandhana Industries Limited', 'MANAKSIA STEELS LT INR1', 'Manugraph India Limited', 'Manaksia Steels Ltd', 'MAXWELL INDUSTRIES INR2', 'VIP Clothing Limited', 'SAMBHAAV MEDIA LTD INR1', 'Themis Medicare Limited', 'Merck Limited', 'Sambandam Spinning Mills Ltd.', 'MINDA CORP LTD INR2', 'PAE Limited', 'PRATIBHA INDUSTRIES LIMITED', 'Prakash Industries Limited', 'PRICOL LIMITED', 'Prozone Intu Properties Limited', 'REDINGTON (INDIA) LIMITED', 'Refex Industries Limited', 'Remsons Industries Limited', 'Repro India Limited', 'SANGAM (INDIA) LIMITED', 'SEAMEC LIMITED', 'Seamec Limited', 'SPL INDUSTRIES LTD INR10', 'THE STATE TRADING CORPORATION O', 'Indo Tech Transformers Limited', 'INDO THAI SECURITIES LIMITED', 'IND-SWIFT LIMITED', 'Ind-Swift Limited']
            completer = QCompleter(names)
            completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            self.searchbox.setCompleter(completer)
            vbox.addWidget(self.searchbox)

    def searchee(self):
        sharename = self.searchbox.text()
        try:
            if self.radioButton.isChecked():
                cp.cursor.execute("Select ticker from bse where name ='"+sharename+"'")
            else:
                cp.cursor.execute("Select ticker from nse where name ='"+sharename+"'")
            result = cp.cursor.fetchone()
            mp.sharenamemp.setText(result[0])
            msft = yf.Ticker(result[0])
            unam = ug.username_ug.text()
            mp.stock_name.setText(sharename)
            mp.username_ug.setText(unam)
            sql = """INSERT INTO search_hist (tickname, username) Values(%s,%s)"""
            val = (sharename,unam)
            cp.cursor.execute(sql,val)
            cp.connection.commit()
            mp.show()
            ug.close()
            global started
            started = True
            t10 = threading.Thread(target= mp.seninmp, args=())
            t10.start()
            t20 = threading.Thread(target=mp.niftyinmp, args= ())
            t20.start()
            self.searchbox.setText("")

        except:
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("ERROR!! No such share name found")
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_()
        
        hist = msft.history(period="1d")
        df = pd.DataFrame(hist)
        v = str(df.values.tolist())
        ab = v[2:-2]
        abc = list(ab.split(","))
        mp.open_price.setText(str(abc[0]))
        mp.high_price.setText(str(abc[1]))
        mp.low_price.setText(str(abc[2]))
        mp.close_price.setText(str(abc[3]))
        mp.volume.setText(str(abc[4]))
        mp.dividends.setText(str(abc[5]))
        mp.stocksplits.setText(str(abc[6]))

    def sen(self):
        
        while started:
         
            page ='https://finance.yahoo.com/quote/%5Ebsesn/'
            HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                    'Accept-Language': 'en-US, en;q=0.5'})
            webpage = requests.get(page, headers=HEADERS)
            soup = BeautifulSoup(webpage.content, "lxml")
            try:
                sensex = soup.find("fin-streamer", attrs={'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).string.strip()

            except:
                sensex= ""
                print("err")
            if len(sensex)==0:
                ug.serverdown.setStyleSheet("background-color: rgb(255, 255, 255);border:1px ridge;")
                ug.serverdown.setText("We are facing a temporary issue!! We will be right back..\n Sorry for the inconvinience caused")
            else:
                ug.serverdown.setStyleSheet("")
                ug.serverdown.setText("")
                ug.sensexlabel_test.setText(sensex)

            
            if started == False:
                    print("thread1 end")
                    break   

    def nifty(self):
        
        while started: 
                      
                page ='https://finance.yahoo.com/quote/%5ENSEI/'
                HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                        'Accept-Language': 'en-US, en;q=0.5'})
                webpage = requests.get(page, headers=HEADERS)
                soup = BeautifulSoup(webpage.content, "lxml")
                try:
                    nifty = soup.find("fin-streamer", attrs={'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).string.strip()
                except:
                    nifty = ""
                    print("err")
                if len(nifty)==0:
                    ug.serverdown.setStyleSheet("background-color: rgb(255, 255, 255);border:1px ridge;")
                    ug.serverdown.setText("We are facing a temporary issue!! We will be right back..\n Sorry for the inconvinience caused")
                else:
                    ug.serverdown.setStyleSheet("")
                    ug.serverdown.setText("")
                    ug.niftylabel_test.setText(nifty)

                if started == False:
                    print("thread2 end")
                    break

    def sensex_ch_rs(self):
        while started:
                    
                page ='https://finance.yahoo.com/quote/%5EBSESN?p=^BSESN&.tsrc=fin-srch'
                # Headers for request
                HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                        'Accept-Language': 'en-US, en;q=0.5'})
                webpage = requests.get(page, headers=HEADERS)
                soup = BeautifulSoup(webpage.content, "lxml")
                try:
                    sensex_ch_rs_var_nv = soup.find("fin-streamer", attrs={'class':'Fw(500) Pstart(8px) Fz(24px)'}).string.strip()
                except:
                    print("err")
                
                if sensex_ch_rs_var_nv.find(",")==-1:
                    sensex_ch_rs_var_nv_flo = float(sensex_ch_rs_var_nv)
                else:
                    r = sensex_ch_rs_var_nv.find(",")
                    sensex_ch_rs_var_nv_flo = float(sensex_ch_rs_var_nv[0:r]+sensex_ch_rs_var_nv[r+1:])     
            
                if sensex_ch_rs_var_nv_flo < 0:
                    ug.sensex_ch_per_lab_test.setStyleSheet("color: rgb(255, 0, 0);background-color: rgb(255, 255, 255);border:1px ridge ;")
                    ug.serverdown.setStyleSheet("")
                    ug.serverdown.setText("")
                    ug.sensex_ch_per_lab_test.setText(sensex_ch_rs_var_nv)
                else:
                    ug.sensex_ch_per_lab_test.setStyleSheet("color: rgb(0, 255, 0);background-color: rgb(255, 255, 255);border:1px ridge ;")
                    ug.serverdown.setStyleSheet("")
                    ug.serverdown.setText("")
                    ug.sensex_ch_per_lab_test.setText(sensex_ch_rs_var_nv)
                
                if started == False:
                    print("thread3 end")
                    break

    def nifty_ch_rs(self):
        while started:
                     
                page ='https://finance.yahoo.com/quote/%5ENSEI?p=^NSEI&.tsrc=fin-srch'
                # Headers for request
                HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                        'Accept-Language': 'en-US, en;q=0.5'})
                webpage = requests.get(page, headers=HEADERS)
                soup = BeautifulSoup(webpage.content, "lxml")
                try:
                    nifty_ch_rs_var_nv = soup.find("fin-streamer", attrs={'class':'Fw(500) Pstart(8px) Fz(24px)'}).string.strip()
                except:
                    nifty_ch_rs_var_nv = ""
                    print("err")

                if nifty_ch_rs_var_nv.find(",")==-1:
                    nifty_ch_rs_var_nvv = float(nifty_ch_rs_var_nv)
                else:
                    r = nifty_ch_rs_var_nv.find(",")
                    nifty_ch_rs_var_nvv = float(nifty_ch_rs_var_nv[0:r]+nifty_ch_rs_var_nv[r+1:])

                if len(nifty_ch_rs_var_nv)==0:
                    ug.serverdown.setStyleSheet("background-color: rgb(255, 255, 255);border:1px ridge;")
                    ug.serverdown.setText("We are facing a temporary issue!! We will be right back..\n Sorry for the inconvinience caused")
                elif nifty_ch_rs_var_nvv < 0:
                        ug.nifty_ch_per_lab_test.setStyleSheet("color: rgb(255, 0, 0);background-color: rgb(255, 255, 255);border:1px ridge ;")
                        ug.serverdown.setStyleSheet("")
                        ug.serverdown.setText("")
                        ug.nifty_ch_per_lab_test.setText(nifty_ch_rs_var_nv)
                else:
                    ug.nifty_ch_per_lab_test.setStyleSheet("color: rgb(0, 255, 0);background-color: rgb(255, 255, 255);border:1px ridge ;")
                    ug.serverdown.setStyleSheet("")
                    ug.serverdown.setText("")
                    ug.nifty_ch_per_lab_test.setText(nifty_ch_rs_var_nv)
                if started == False:
                    print("thread4 end")
                    break

    def timeeee(self):
        while started:
                       
                page ='https://finance.yahoo.com/quote/%5EBSESN?p=^BSESN&.tsrc=fin-srch'
                HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                        'Accept-Language': 'en-US, en;q=0.5'})
                webpage = requests.get(page, headers=HEADERS)
                soup = BeautifulSoup(webpage.content, "lxml")
                try:
                    timee = soup.find("div", attrs={'id':'quote-market-notice'}).string.strip()
                except:
                    timee = ""
                    print("err")
                if len(timee)==0:
                    ug.serverdown.setStyleSheet("background-color: rgb(255, 255, 255);border:1px ridge;")
                    ug.serverdown.setText("We are facing a temporary issue!! We will be right back..\n Sorry for the inconvinience caused")
                else:
                    ug.serverdown.setStyleSheet("")
                    ug.serverdown.setText("")
                    ug.sensex_ch_per_lab_test_2.setText(timee)
                    
                
                if started == False:
                    print("thread5 end")
                    break

    def timeeeenif(self):
            while started:
                     
                page ='https://finance.yahoo.com/quote/%5ENSEI?p=^NSEI&.tsrc=fin-srch'
                HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                        'Accept-Language': 'en-US, en;q=0.5'})
                webpage = requests.get(page, headers=HEADERS)
                soup = BeautifulSoup(webpage.content, "lxml")
                try:
                    timeen = soup.find("div", attrs={'id':'quote-market-notice'}).string.strip()
                except:
                    timeen = ""
                    print("err")
                if len(timeen)==0:
                    ug.serverdown.setStyleSheet("background-color: rgb(255, 255, 255);border:1px ridge;")
                    ug.serverdown.setText("We are facing a temporary issue!! We will be right back..\n Sorry for the inconvinience caused")
                else:
                    ug.serverdown.setStyleSheet("")
                    ug.serverdown.setText("")
                    ug.nifty_ch_per_lab_test_2.setText(timeen)

                if started == False:
                    print("thread6 end")
                    break    
                         
    def sensex_ch_per(self):
        while started:
                    
            page ='https://finance.yahoo.com/quote/%5EBSESN?p=^BSESN&.tsrc=fin-srch'
            HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                        'Accept-Language': 'en-US, en;q=0.5'})
            webpage = requests.get(page, headers=HEADERS)
            soup = BeautifulSoup(webpage.content, "lxml")
            try:
                sensex_ch_per_var_nv = soup.find_all("fin-streamer", attrs={'class':'Fw(500) Pstart(8px) Fz(24px)'})
            except:
                sensex_ch_per_var_nv = ""
                print("err")
            
            if sensex_ch_per_var_nv[0].text.find(",")==-1:
                    sensex_ch_per_var_nvvvv = float(sensex_ch_per_var_nv[0].text)
            else:
                r = sensex_ch_per_var_nv[0].text.find(",")
                sensex_ch_per_var_nvvvv = float(sensex_ch_per_var_nv[0].text[0:r]+sensex_ch_per_var_nv[0].text[r+1:])

            if len(sensex_ch_per_var_nv[0])==0:
                    ug.serverdown.setStyleSheet("background-color: rgb(255, 255, 255);border:1px ridge;")
                    ug.serverdown.setText("We are facing a temporary issue!! We will be right back..\n Sorry for the inconvinience caused")
            elif sensex_ch_per_var_nvvvv < 0:
                ug.sensex_ch_per_lab_test_3.setStyleSheet("color: rgb(255, 0, 0);background-color: rgb(255, 255, 255);border:1px ridge ;")
                ug.serverdown.setStyleSheet("")
                ug.serverdown.setText("")
                ug.sensex_ch_per_lab_test_3.setText(sensex_ch_per_var_nv[1].text)
            else:
                ug.sensex_ch_per_lab_test_3.setStyleSheet("color: rgb(0, 255, 0);background-color: rgb(255, 255, 255);border:1px ridge ;")
                ug.serverdown.setStyleSheet("")
                ug.serverdown.setText("")
                ug.sensex_ch_per_lab_test_3.setText(sensex_ch_per_var_nv[1].text)
            if started == False:
                    print("thread7 end")
                    break

    def nifty_ch_per(self):
        while started:
                    
                page ='https://finance.yahoo.com/quote/%5ENSEI?p=^NSEI&.tsrc=fin-srch'
                # Headers for request
                HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                        'Accept-Language': 'en-US, en;q=0.5'})
                webpage = requests.get(page, headers=HEADERS)
                soup = BeautifulSoup(webpage.content, "lxml")
                try:
                    nifty_ch_per_var_nv = soup.find_all("fin-streamer", attrs={'class':'Fw(500) Pstart(8px) Fz(24px)'})
                except:
                    print("err")
                    nifty_ch_per_var_nv = ""
                
                if nifty_ch_per_var_nv[0].text.find(",")==-1:
                    nifty_ch_per_var_nvv =  float(nifty_ch_per_var_nv[0].text)
                else:
                    r = nifty_ch_per_var_nv[0].text.find(",")
                    nifty_ch_per_var_nvv = float(nifty_ch_per_var_nv[0].text[0:r]+nifty_ch_per_var_nv[0].text[r+1:])

                if len(nifty_ch_per_var_nv[0])==0:
                    ug.serverdown.setStyleSheet("background-color: rgb(255, 255, 255);border:1px ridge;")
                    ug.serverdown.setText("We are facing a temporary issue!! We will be right back..\n Sorry for the inconvinience caused")
                elif nifty_ch_per_var_nvv < 0:
                        ug.nifty_ch_per_lab_test_3.setStyleSheet("color: rgb(255, 0, 0);background-color: rgb(255, 255, 255);border:1px ridge ;")
                        ug.serverdown.setStyleSheet("")
                        ug.serverdown.setText("")
                        ug.nifty_ch_per_lab_test_3.setText(nifty_ch_per_var_nv[1].text)
                else:
                    ug.nifty_ch_per_lab_test_3.setStyleSheet("color: rgb(0, 255, 0);background-color: rgb(255, 255, 255);border:1px ridge ;")
                    ug.serverdown.setStyleSheet("")
                    ug.serverdown.setText("")
                    ug.nifty_ch_per_lab_test_3.setText(nifty_ch_per_var_nv[1].text)

                if started == False:
                    print("thread8 end")
                    break    

class Favourite(QDialog):
    
    def __init__(self):
        super(Favourite,self).__init__()
        loadUi("Favourite.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.dash.clicked.connect(self.dashh)
        self.supp.clicked.connect(self.suppo)
        self.hist.clicked.connect(self.histoo)
        self.port.clicked.connect(self.portf)
        self.sett.clicked.connect(self.prosett)
        self.predict.clicked.connect(self.predicts)
        self.remove.clicked.connect(self.rem)
    
    def predicts(self):
        unam = f.username_ug.text()
        pre = int(f.pre_sr.text())
        sto = f.tableWidget.item(pre-1,0).text()
        sql = "Select ticker from wishlist where username='"+unam+"'and stockname = '"+sto+"'"
        cp.cursor.execute(sql)
        res = cp.cursor.fetchone()
        try:
            mp.sharenamemp.setText(res[0])
            msft = yf.Ticker(res[0])
            unam = ug.username_ug.text()
            mp.stock_name.setText(sto)
            mp.username_ug.setText(unam)
            sql = """INSERT INTO search_hist (tickname, username) Values(%s,%s)"""
            val = (sto,unam)
            cp.cursor.execute(sql,val)
            cp.connection.commit()
            f.pre_sr.setText("")
            mp.show()
            f.close()
            global started
            started = True
            t10 = threading.Thread(target= mp.seninmp, args=())
            t10.start()
            t20 = threading.Thread(target=mp.niftyinmp, args= ())
            t20.start()
        except:
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("ERROR!! No such share name found")
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_()
        hist = msft.history(period="1d")
        df = pd.DataFrame(hist)
        v = str(df.values.tolist())
        ab = v[2:-2]
        abc = list(ab.split(","))
        mp.open_price.setText(str(abc[0]))
        mp.high_price.setText(str(abc[1]))
        mp.low_price.setText(str(abc[2]))
        mp.close_price.setText(str(abc[3]))
        mp.volume.setText(str(abc[4]))
        mp.dividends.setText(str(abc[5]))
        mp.stocksplits.setText(str(abc[6]))

    def rem(self):
        unam = f.username_ug.text()
        re = int(f.rem_sr.text())
        sto = f.tableWidget.itemAt(re,0).text()
        sql = "delete from wishlist where username = '"+unam+"'and stockname = '"+sto+"'"
        cp.cursor.execute(sql)
        cp.connection.commit()
        err = QMessageBox()
        err.setIcon(QMessageBox.Information)
        err.setText("Removed from wishlist Successfully!!")
        err.setWindowTitle("Success")
        err.setStandardButtons(QMessageBox.Ok)
        retval = err.exec_()
        f.rem_sr.setText("")
        cp.cursor.execute("Select stockname from wishlist where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        f.tableWidget.setColumnCount(1)
        f.tableWidget.setHorizontalHeaderLabels([""])
        f.tableWidget.setColumnWidth(0,1011)
        f.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            f.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        
    def closeEvent(self, event):
            event.accept()
            global started
            started = False

    def dashh(self):
        unam = self.username_ug.text()
        ug.username_ug.setText(unam)
        ug.show()
        f.close()
        global started
        started = True
        t1 = threading.Thread(target= ug.sen, args=())
        t1.start()
        t2 = threading.Thread(target=ug.nifty, args= ())
        t2.start()
        t3 = threading.Thread(target=ug.sensex_ch_rs, args=())
        t3.start()
        t4 = threading.Thread(target=ug.nifty_ch_rs,args=())
        t4.start()
        t5 = threading.Thread(target=ug.timeeee,args=())
        t5.start()
        t6 = threading.Thread(target=ug.timeeeenif,args=())
        t6.start()
        t7 = threading.Thread(target=ug.sensex_ch_per,args=())
        t7.start()
        t8 = threading.Thread(target=ug.nifty_ch_per,args=())
        t8.start()
   
    def suppo(self):
        unam = self.username_ug.text()
        sup.username_ug.setText(unam)
        sup.show()
        f.close()
        global started
        started = False
        global intche
        intche = False 

    def histoo(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select tickname from search_hist where username='"+unam+"'")
        res = cp.cursor.fetchall()
        his.tableWidget.setColumnCount(1)
        his.tableWidget.setHorizontalHeaderLabels([""])
        his.tableWidget.setColumnWidth(0,1011)
        his.tableWidget.setRowCount(len(res))
        i = 0 
        for row in res:
            his.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        his.username_ug.setText(unam)
        his.show()
        f.close()
        global started
        started = False

    def portf(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select stockname from portfolio where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        por.tableWidget.setColumnCount(1)
        por.tableWidget.setHorizontalHeaderLabels([""])
        por.tableWidget.setColumnWidth(0,1011)
        por.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            por.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        por.username_ug.setText(unam)
        por.show()
        f.close()
        global started
        started = False

    def prosett(self):
        unam = self.username_ug.text()
        ug.username_ug.setText(unam)
        se.show()
        f.close()
        global started
        started = False

class History(QDialog):
    
    def __init__(self):
        super(History,self).__init__()
        loadUi("History.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.fav.clicked.connect(self.favo)
        self.dash.clicked.connect(self.dashh)
        self.supp.clicked.connect(self.suppo)
        self.port.clicked.connect(self.portf)
        self.sett.clicked.connect(self.prosett)
        self.clr_hist.clicked.connect(self.clr)

    def closeEvent(self, event):
            event.accept()
            global started
            started = False

    def dashh(self):
        unam = self.username_ug.text()
        ug.username_ug.setText(unam)
        ug.show()
        his.close()
        global started
        started = True
        t1 = threading.Thread(target= ug.sen, args=())
        t1.start()
        t2 = threading.Thread(target=ug.nifty, args= ())
        t2.start()
        t3 = threading.Thread(target=ug.sensex_ch_rs, args=())
        t3.start()
        t4 = threading.Thread(target=ug.nifty_ch_rs,args=())
        t4.start()
        t5 = threading.Thread(target=ug.timeeee,args=())
        t5.start()
        t6 = threading.Thread(target=ug.timeeeenif,args=())
        t6.start()
        t7 = threading.Thread(target=ug.sensex_ch_per,args=())
        t7.start()
        t8 = threading.Thread(target=ug.nifty_ch_per,args=())
        t8.start()
   
    def suppo(self):
        unam = self.username_ug.text()
        sup.username_ug.setText(unam)
        sup.show()
        his.close()
        global started
        started = False
        global intche
        intche = False 

    def favo(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select stockname from wishlist where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        f.tableWidget.setColumnCount(1)
        f.tableWidget.setHorizontalHeaderLabels([""])
        f.tableWidget.setColumnWidth(0,1011)
        f.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            f.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        f.username_ug.setText(unam)
        f.show()
        his.close()
        global started
        started = False

    def portf(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select stockname from portfolio where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        por.tableWidget.setColumnCount(1)
        por.tableWidget.setHorizontalHeaderLabels([""])
        por.tableWidget.setColumnWidth(0,1011)
        por.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            por.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        por.username_ug.setText(unam)
        por.show()
        his.close()
        global started
        started = False

    def prosett(self):
        unam = self.username_ug.text()
        se.username_ug.setText(unam)
        se.show()
        his.close()
        global started
        started = False

    def clr(self):
        unam = self.username_ug.text()
        cp.cursor.execute("delete from search_hist where username ='"+unam+"'")
        cp.connection.commit()
        cp.cursor.execute("Select tickname from search_hist where username='"+unam+"'")
        res = cp.cursor.fetchall()
        his.tableWidget.setColumnCount(1)
        his.tableWidget.setHorizontalHeaderLabels([""])
        his.tableWidget.setColumnWidth(0,1011)
        his.tableWidget.setRowCount(len(res))
        i = 0 
        for row in res:
            his.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1

class Profileset(QDialog):
    
    def __init__(self):
        super(Profileset,self).__init__()
        loadUi("Settings.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.fav.clicked.connect(self.favo)
        self.dash.clicked.connect(self.dashh)
        self.supp.clicked.connect(self.suppo)
        self.hist.clicked.connect(self.histoo)
        self.port.clicked.connect(self.portf)
        self.mypro.clicked.connect(self.myp)
        self.deleteaccount.clicked.connect(self.delt)

    def closeEvent(self, event):
            event.accept()
            global started
            started = False

    def histoo(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select tickname from search_hist where username='"+unam+"'")
        res = cp.cursor.fetchall()
        his.tableWidget.setColumnCount(1)
        his.tableWidget.setHorizontalHeaderLabels([""])
        his.tableWidget.setColumnWidth(0,1011)
        his.tableWidget.setRowCount(len(res))
        i = 0 
        for row in res:
            his.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        his.username_ug.setText(unam)
        his.show()
        se.close()
        global started
        started = False

    def dashh(self):
        unam = self.username_ug.text()
        ug.username_ug.setText(unam)
        ug.show()
        se.close()
        global started
        started = True
        t1 = threading.Thread(target= ug.sen, args=())
        t1.start()
        t2 = threading.Thread(target=ug.nifty, args= ())
        t2.start()
        t3 = threading.Thread(target=ug.sensex_ch_rs, args=())
        t3.start()
        t4 = threading.Thread(target=ug.nifty_ch_rs,args=())
        t4.start()
        t5 = threading.Thread(target=ug.timeeee,args=())
        t5.start()
        t6 = threading.Thread(target=ug.timeeeenif,args=())
        t6.start()
        t7 = threading.Thread(target=ug.sensex_ch_per,args=())
        t7.start()
        t8 = threading.Thread(target=ug.nifty_ch_per,args=())
        t8.start()
   
    def suppo(self):
        unam = self.username_ug.text()
        sup.username_ug.setText(unam)
        sup.show()
        se.close()
        global started
        started = False
        global intche
        intche = False 

    def portf(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select stockname from portfolio where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        por.tableWidget.setColumnCount(1)
        por.tableWidget.setHorizontalHeaderLabels([""])
        por.tableWidget.setColumnWidth(0,1011)
        por.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            por.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        por.username_ug.setText(unam)
        por.show()
        his.close()
        global started
        started = False
    
    def favo(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select stockname from wishlist where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        f.tableWidget.setColumnCount(1)
        f.tableWidget.setHorizontalHeaderLabels([""])
        f.tableWidget.setColumnWidth(0,1011)
        f.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            f.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        f.username_ug.setText(unam)
        f.show()
        se.close()
        global started
        started = False

    def myp(self):
        unam = self.username_ug.text()
        m.username_ug.setText(unam)
        sql = "Select * from profile where username = '"+unam+"'"
        cp.cursor.execute(sql)
        res = cp.cursor.fetchall()
        m.name_lb.setText(res[0][0])
        m.mobile_lb.setText(res[0][1])
        m.email_lb.setText(res[0][2])
        m.dob_lb.setText(res[0][5])
        m.gender_lb.setText(res[0][6])
        m.show()
    
    def delt(self):
        unam = self.username_ug.text()
        err = QMessageBox()
        err.setIcon(QMessageBox.Information)
        err.setText("Do you really want to delete all your data ?")
        err.setWindowTitle("")
        err.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = err.exec_()

        if QMessageBox.Yes:

            sql = "delete from profile where username = '"+unam+"'"
            sql_1 = "delete from portfolio where username = '"+unam+"'"
            sql_2 = "delete from search_hist where username = '"+unam+"'"
            sql_3 = "delete from wishlist where username = '"+unam+"'"

            cp.cursor.execute(sql)
            cp.cursor.execute(sql_1)
            cp.cursor.execute(sql_2)
            cp.cursor.execute(sql_3)
            cp.connection.commit()

            
            err = QMessageBox()
            err.setIcon(QMessageBox.Information)
            err.setText("Account successfully Deleted")
            err.setWindowTitle("Success")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_()

            login.show()
            global started 
            started = False
            login.un.setText("")
            login.pa.setText("")
            se.close()
             
class mypr(QDialog):

    def __init__(self):
        super(mypr,self).__init__()
        loadUi("mypro.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.back_mypr.clicked.connect(self.back)

    def back(self):
        unam = self.username_ug.text()
        se.username_ug.setText(unam)
        se.show()
        m.close()

class Support(QDialog):
    
    def __init__(self):
        super(Support,self).__init__()
        loadUi("Support.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.fav.clicked.connect(self.favo)
        self.dash.clicked.connect(self.dashh)
        self.hist.clicked.connect(self.histoo)
        self.port.clicked.connect(self.portf)
        self.sett.clicked.connect(self.prosett)
        self.send.clicked.connect(self.sendee)

    def closeEvent(self, event):
            event.accept()
            global started
            started = False
            global intche
            intche = False 

    def dashh(self):
        unam = self.username_ug.text()
        ug.username_ug.setText(unam)
        ug.show()
        sup.close()
        global started
        started = True
        t1 = threading.Thread(target= ug.sen, args=())
        t1.start()
        t2 = threading.Thread(target=ug.nifty, args= ())
        t2.start()
        t3 = threading.Thread(target=ug.sensex_ch_rs, args=())
        t3.start()
        t4 = threading.Thread(target=ug.nifty_ch_rs,args=())
        t4.start()
        t5 = threading.Thread(target=ug.timeeee,args=())
        t5.start()
        t6 = threading.Thread(target=ug.timeeeenif,args=())
        t6.start()
        t7 = threading.Thread(target=ug.sensex_ch_per,args=())
        t7.start()
        t8 = threading.Thread(target=ug.nifty_ch_per,args=())
        t8.start()

    def histoo(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select tickname from search_hist where username='"+unam+"'")
        res = cp.cursor.fetchall()
        his.tableWidget.setColumnCount(1)
        his.tableWidget.setHorizontalHeaderLabels([""])
        his.tableWidget.setColumnWidth(0,1011)
        his.tableWidget.setRowCount(len(res))
        i = 0 
        for row in res:
            his.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        his.username_ug.setText(unam)
        his.show()
        sup.close()
        global started
        started = False

    def favo(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select stockname from wishlist where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        f.tableWidget.setColumnCount(1)
        f.tableWidget.setHorizontalHeaderLabels([""])
        f.tableWidget.setColumnWidth(0,1011)
        f.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            f.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        f.username_ug.setText(unam)
        f.show()
        sup.close()
        global started
        started = False
    
    def portf(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select stockname from portfolio where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        por.tableWidget.setColumnCount(1)
        por.tableWidget.setHorizontalHeaderLabels([""])
        por.tableWidget.setColumnWidth(0,1011)
        por.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            por.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        por.username_ug.setText(unam)
        por.show()
        sup.close()
        global started
        started = False

    def prosett(self):
        unam = self.username_ug.text()
        se.username_ug.setText(unam)
        se.show()
        sup.close()
        global started
        started = False

    def sendee(self):
        
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("amjh32255@gmail.com","klwmihjqxbmiiqja")

        nameee = self.name.text()
        emailee = self.email.text()
        mess = self.message.text()
        
        text = nameee +"\n"+ emailee +"\n"+ mess 
        
        SUBJECT = "CUSTOMER SUPPORT"
        TEXT = text
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        try:
            server.sendmail("amjh32255@gmail.com","amjh32255@gmail.com",message)
            print("success")
            self.cont.setText("YOUR COMPLAINT SENT SUCCESSFUL")

        except smtplib.SMTPRecipientsRefused:
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("ERROR!! Invalid Email Address...")
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_() 
        finally:
            server.quit()
            self.name.setText("")
            self.email.setText("")
            self.message.setText("")

class Portfolio(QDialog):
        
    def __init__(self):
        super(Portfolio,self).__init__()
        loadUi("Portfol.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.fav.clicked .connect(self.favo)
        self.dash.clicked.connect(self.dashh)
        self.hist.clicked.connect(self.histoo)
        self.supp.clicked.connect(self.suppo)
        self.sett.clicked.connect(self.prosett)
        self.predict.clicked.connect(self.predicts)
        self.remove.clicked.connect(self.rem)

    def closeEvent(self, event):
            event.accept()
            global started
            started = False
            global intche
            intche = False 

    def dashh(self):
        unam = self.username_ug.text()
        ug.username_ug.setText(unam)
        ug.show()
        por.close()
        global started
        started = True
        t1 = threading.Thread(target= ug.sen, args=())
        t1.start()
        t2 = threading.Thread(target=ug.nifty, args= ())
        t2.start()
        t3 = threading.Thread(target=ug.sensex_ch_rs, args=())
        t3.start()
        t4 = threading.Thread(target=ug.nifty_ch_rs,args=())
        t4.start()
        t5 = threading.Thread(target=ug.timeeee,args=())
        t5.start()
        t6 = threading.Thread(target=ug.timeeeenif,args=())
        t6.start()
        t7 = threading.Thread(target=ug.sensex_ch_per,args=())
        t7.start()
        t8 = threading.Thread(target=ug.nifty_ch_per,args=())
        t8.start()

    def histoo(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select tickname from search_hist where username='"+unam+"'")
        res = cp.cursor.fetchall()
        his.tableWidget.setColumnCount(1)
        his.tableWidget.setHorizontalHeaderLabels([""])
        his.tableWidget.setColumnWidth(0,1011)
        his.tableWidget.setRowCount(len(res))
        i = 0 
        for row in res:
            his.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        his.username_ug.setText(unam)
        his.show()
        por.close()
        global started
        started = False

    def favo(self):
        unam = self.username_ug.text()
        cp.cursor.execute("Select stockname from wishlist where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        f.tableWidget.setColumnCount(1)
        f.tableWidget.setHorizontalHeaderLabels([""])
        f.tableWidget.setColumnWidth(0,1011)
        f.tableWidget.setRowCount(len(resa))
        i = 0 
        for row in resa:
            f.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1
        f.username_ug.setText(unam)
        f.show()
        por.close()
        global started
        started = False

    def prosett(self):
        unam = self.username_ug.text()
        se.username_ug.setText(unam)
        se.show()
        por.close()
        global started
        started = False

    def suppo(self):
        unam = self.username_ug.text()
        sup.username_ug.setText(unam)
        sup.show()
        por.close()
        global started
        started = False

    def predicts(self):
        unam = self.username_ug.text()
        pre = int(por.pre_sr.text())
        sto = por.tableWidget.itemAt(pre,0).text()
        sql = "Select ticker from portfolio where username='"+unam+"'and stockname = '"+sto+"'"
        cp.cursor.execute(sql)
        res = cp.cursor.fetchone()
        try:
            mp.sharenamemp.setText(res[0])
            msft = yf.Ticker(res[0])
            unam = por.username_ug.text()
            mp.stock_name.setText(sto)
            mp.username_ug.setText(unam)
            sql = """INSERT INTO search_hist (tickname, username) Values(%s,%s)"""
            val = (sto,unam)
            cp.cursor.execute(sql,val)
            cp.connection.commit()
            por.pre_sr.setText("")
            mp.show()
            por.close()
            global started
            started = True
            t10 = threading.Thread(target= mp.seninmp, args=())
            t10.start()
            t20 = threading.Thread(target=mp.niftyinmp, args= ())
            t20.start()
        except:
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("ERROR!! No such share name found")
            err.setWindowTitle("Warning")
            err.setStandardButtons(QMessageBox.Ok)
            retval = err.exec_()
        hist = msft.history(period="1d")
        df = pd.DataFrame(hist)
        v = str(df.values.tolist())
        ab = v[2:-2]
        abc = list(ab.split(","))
        mp.open_price.setText(str(abc[0]))
        mp.high_price.setText(str(abc[1]))
        mp.low_price.setText(str(abc[2]))
        mp.close_price.setText(str(abc[3]))
        mp.volume.setText(str(abc[4]))
        mp.dividends.setText(str(abc[5]))
        mp.stocksplits.setText(str(abc[6]))

    def rem(self):
        unam = self.username_ug.text()
        re = int(por.rem_sr.text())
        sto = por.tableWidget.itemAt(re,0).text()
        sql = "delete from portfolio where username = '"+unam+"'and stockname = '"+sto+"'"
        cp.cursor.execute(sql)
        cp.connection.commit()
        err = QMessageBox()
        err.setIcon(QMessageBox.Information)
        err.setText("Removed from portfolio Successfully!!")
        err.setWindowTitle("Success")
        err.setStandardButtons(QMessageBox.Ok)
        retval = err.exec_()
        por.rem_sr.setText("")
        cp.cursor.execute("Select stockname from portfolio where username='"+unam+"'")
        resa = cp.cursor.fetchall()
        por.tableWidget.setColumnCount(1)
        por.tableWidget.setHorizontalHeaderLabels([""])
        por.tableWidget.setColumnWidth(0,1011)
        por.tableWidget.setRowCount(len(resa))
        i = 0
        for row in resa:
            por.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            i = i+1

class Mainprediction(QDialog):
    
    def __init__(self):
        
        super(Mainprediction,self).__init__()
        loadUi("Nextpage.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        self.backbutto.clicked.connect(self.backing)
        self.wishlist.clicked.connect(self.wish)
        self.portfoli.clicked.connect(self.porty)
        self.predict.clicked.connect(self.aop)
    
    def closeEvent(self, event):
            event.accept()
            global started
            started = False
            global intche
            intche = False 

    def porty(self):
        stockname = self.stock_name.text()
        un = self.username_ug.text()
        tc= self.sharenamemp.text()
        sql = """INSERT INTO portfolio (stockname, username, ticker ) Values(%s,%s,%s)"""
        val = (stockname,un,tc)
        cp.cursor.execute(sql,val)
        cp.connection.commit()
        err = QMessageBox()
        err.setIcon(QMessageBox.Information)
        err.setText("Added to Portfolio")
        err.setWindowTitle("Success")
        err.setStandardButtons(QMessageBox.Ok)
        retval = err.exec_()

    def seninmp(self):
        while started:
          
            page ='https://finance.yahoo.com/quote/%5Ebsesn/'
            HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                    'Accept-Language': 'en-US, en;q=0.5'})
            webpage = requests.get(page, headers=HEADERS)
            soup = BeautifulSoup(webpage.content, "lxml")
            try:
                sensex = soup.find("fin-streamer", attrs={'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).string.strip()

            except:
                sensex= ""
                print("err")
            if len(sensex)==0:
                mp.serverdown.setStyleSheet("background-color: rgb(255, 255, 255);border:1px ridge;")
                mp.serverdown.setText("We are facing a temporary issue!! We will be right back..\n Sorry for the inconvinience caused")
            else:
                mp.serverdown.setStyleSheet("")
                mp.serverdown.setText("")
                mp.sensexlabel_test.setText(sensex)

            if started == False:
                    print("thread1 end")
                    break   

    def niftyinmp(self):
        while started: 
                     
                page ='https://finance.yahoo.com/quote/%5ENSEI/'
                HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                        'Accept-Language': 'en-US, en;q=0.5'})
                webpage = requests.get(page, headers=HEADERS)
                soup = BeautifulSoup(webpage.content, "lxml")
                try:
                    nifty = soup.find("fin-streamer", attrs={'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).string.strip()
                except:
                    nifty = ""
                    print("err")
                if len(nifty)==0:
                    mp.serverdown.setStyleSheet("background-color: rgb(255, 255, 255);border:1px ridge;")
                    mp.serverdown.setText("We are facing a temporary issue!! We will be right back..\n Sorry for the inconvinience caused")
                else:
                    mp.serverdown.setStyleSheet("")
                    mp.serverdown.setText("")
                    mp.niftylabel_test.setText(nifty)

                if started == False:
                    print("thread2 end")
                    break
    
    def backing(self):
        ug.show()
        mp.close()
        global started
        started = True
        t1 = threading.Thread(target= ug.sen, args=())
        t1.start()
        t2 = threading.Thread(target=ug.nifty, args= ())
        t2.start()
        t3 = threading.Thread(target=ug.sensex_ch_rs, args=())
        t3.start()
        t4 = threading.Thread(target=ug.nifty_ch_rs,args=())
        t4.start()
        t5 = threading.Thread(target=ug.timeeee,args=())
        t5.start()
        t6 = threading.Thread(target=ug.timeeeenif,args=())
        t6.start()
        t7 = threading.Thread(target=ug.sensex_ch_per,args=())
        t7.start()
        t8 = threading.Thread(target=ug.nifty_ch_per,args=())
        t8.start()

    def wish(self):
        stockname = self.stock_name.text()
        un = self.username_ug.text()
        ti = self.sharenamemp.text()
        sql = """INSERT INTO wishlist (stockname, username ,ticker) Values(%s,%s,%s)"""
        val = (stockname,un,ti)
        cp.cursor.execute(sql,val)
        cp.connection.commit()
        err = QMessageBox()
        err.setIcon(QMessageBox.Information)
        err.setText("Added to wishlist")
        err.setWindowTitle("Success")
        err.setStandardButtons(QMessageBox.Ok)
        retval = err.exec_()

    def aop(self):
        self.actualfn()
            
    def actualfn(self):
        # print("abc")
        # mp.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        # mp.label_5.setText("Predictions Loading .... \nIt may take 5 6 minutes")
        
        start = '2015-01-01'
        today = date.today()
        end = today.strftime("%Y-%m-%d")

        stock_symbol = mp.sharenamemp.text()

        df = data.DataReader( stock_symbol , 'yahoo', start, end)

        df = df.reset_index()
        close = df[['Close']]
        
        #Splitting Data into Training and Testing
        data_train = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
        data_test = pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])

        scaler = MinMaxScaler(feature_range=(0,1))
        data_train_array = scaler.fit_transform(data_train)

        x_train = []
        y_train = []
        
        for i in range(100, data_train_array.shape[0]):
            x_train.append(data_train_array[i-100: i])
            y_train.append(data_train_array[i,0])

        x_train,y_train = np.array(x_train), np.array(y_train)

        #ML MODEL
        model = Sequential()
        model.add(LSTM(units = 50, activation= 'relu' , return_sequences= True, input_shape = (x_train.shape[1], 1)))
        model.add(Dropout(0.2))

        model.add(LSTM(units = 60, activation= 'relu' , return_sequences= True))
        model.add(Dropout(0.3))

        model.add(LSTM(units = 80, activation= 'relu' , return_sequences= True))
        model.add(Dropout(0.4))

        model.add(LSTM(units = 120, activation= 'relu'))
        model.add(Dropout(0.5))

        model.add(Dense(units=1))
        model.summary()

        model.compile(optimizer='adam', loss='mean_squared_error')
        model.fit(x_train, y_train, epochs = 40)

        past_100_days = data_train.tail(100)
        final_df = past_100_days.append(data_test, ignore_index=True)
        input_data = scaler.fit_transform(final_df)
        

        x_test = []
        y_test = []

        for i in range(100, input_data.shape[0]):
            x_test.append(input_data[i-100: i])
            y_test.append(input_data[i, 0])

        #Predicitng on train and test data
        train_predict = model.predict(x_train)

        #Inverse transform to get actual value
        train_predict = scaler.inverse_transform(train_predict)

        x_test, y_test =np.array(x_test), np.array(y_test)
        
        #making predictions
        y_predicted= model.predict(x_test)
        # print(scaler.scale_)

        scale_factor = 1/scaler.scale_
        y_predicted = y_predicted * scale_factor
        y_test = y_test * scale_factor

        ds_new = data_train_array.tolist()
        

        #Creating final data for plotting
        final_graph = scaler.inverse_transform(ds_new).tolist()
        
        #Plotting final results with predicted value after 30 Days
        plt.plot(final_graph,)
        plt.ylabel("Price")
        plt.xlabel("Time")
        plt.title("{0} prediction of next month open".format(stock_symbol))
        plt.axhline(y=final_graph[len(final_graph)-1], color = 'red', linestyle = ':', label = 'NEXT 30D: {0}'.format(round(float(*final_graph[len(final_graph)-1]),2)))
        plt.legend()
        plt.show()
    
class splash(QDialog):

    def __init__(self):
        super(splash,self).__init__()
        loadUi("SplashScreen.ui",self)
        self.setWindowTitle('AMJH_SPP')
        self.setWindowIcon(QIcon('120.jpeg'))
        
    def doAction(self):
        for i in range(101):
            time.sleep(3)
            sp.pbar.setValue(i)
        sp.close()         

# main
app = QApplication(sys.argv)

#objects
welcome = WelcomeScreen()
login = LoginScreen()
signup = SignupScreen()
frgot = Forgetpassword()
frgpasss = Changepassfor()
ug = UserPage()
f= Favourite()
his = History()
por = Portfolio()
se = Profileset()
m = mypr()
sup = Support()
mp = Mainprediction()
sp = splash()

#mainscreen
welcome.setFixedHeight(750)
welcome.setFixedWidth(1280)
login.setFixedHeight(750)
login.setFixedWidth(1280)
signup.setFixedHeight(750)
signup.setFixedWidth(1280)
frgot.setFixedHeight(750)
frgot.setFixedWidth(1280)
frgpasss.setFixedHeight(750)
frgpasss.setFixedWidth(1280)
ug.setFixedHeight(750)
ug.setFixedWidth(1280)
f.setFixedHeight(750)
f.setFixedWidth(1280)
his.setFixedHeight(750)
his.setFixedWidth(1280)
por.setFixedHeight(750)
por.setFixedWidth(1280)
se.setFixedHeight(750)
se.setFixedWidth(1280)
sup.setFixedHeight(750)
sup.setFixedWidth(1280)
mp.setFixedHeight(750)
mp.setFixedWidth(1280)
welcome.show()
app.exec()