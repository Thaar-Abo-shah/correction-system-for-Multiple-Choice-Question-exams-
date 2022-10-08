import glob
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QThreadPool, QObject, pyqtSignal, QRunnable, pyqtSlot, QThread
from PyQt5.QtGui import QColor, QDoubleValidator, QValidator, QMovie
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QApplication, QFileDialog, QMessageBox

import Main_Screen
from untitled import Ui_MainWindow
# from correction import Ui_MainWindow2
from ui import Ui_AQC
from ladder_mark import Ui_ladder_m
from insert_ladder import Ui_insert_ladder
from correction_complete import Ui_Correction
from ladder_paper import Ui_insert_lader
from dialog import Ui_Dialog
from print import Ui_print
import test
import cv2
# import pandas as pd
import xlrd
import numpy as np

counter = 0
global res,check,model_num,in_model_num
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main = Ui_AQC()
        self.main.setupUi(self)
        self.main.layouts.setCurrentWidget(self.main.home)
        self.main.home_btn.clicked.connect(self.home)
        self.main.correction_btn.clicked.connect(self.correction)
        self.main.archive_btn.clicked.connect(self.archive)
        self.main.setting_btn.clicked.connect(self.setting)
        self.main.dir_btn1.clicked.connect(self.dir1)
        self.main.dir_btn2.clicked.connect(self.dir2)
        self.main.dir_btn3.clicked.connect(self.dir3)
        self.main.dir_btn4.clicked.connect(self.dir4)
        self.main.correct_btn.clicked.connect(self.correct)
        self.main.ladder_btn1.clicked.connect(self.ladder1)
        self.main.ladder_btn2.clicked.connect(self.ladder2)
        self.main.ladder_btn3.clicked.connect(self.ladder3)
        self.main.ladder_btn4.clicked.connect(self.ladder4)
        self.main.subject_name.editingFinished.connect(self.validate_sub)
        self.main.num_students.editingFinished.connect(self.validate_std)
        self.main.num_ladders.editingFinished.connect(self.validate_ldr)
        self.main.total_mark_2.editingFinished.connect(self.validate_q)
        self.main.total_mark.editingFinished.connect(self.validate_mark)
        self.main.ladder_mark1.clicked.connect(self.ladder_mark1)
        self.main.ladder_mark2.clicked.connect(self.ladder_mark2)
        self.main.ladder_mark3.clicked.connect(self.ladder_mark3)
        self.main.ladder_mark4.clicked.connect(self.ladder_mark4)
        self.main.insert_ladder_btn1.clicked.connect(self.insert_ladder1)
        self.main.insert_ladder_btn2.clicked.connect(self.insert_ladder2)
        self.main.insert_ladder_btn3.clicked.connect(self.insert_ladder3)
        self.main.insert_ladder_btn4.clicked.connect(self.insert_ladder4)
        self.main.print.clicked.connect(self.print)


        self.mark = None



        self.movie = QMovie("Icons/1.gif")
        self.main.label.setMovie(self.movie)
        self.movie.start()



    def correction(self):
        self.main.layouts.setCurrentWidget(self.main.correction)
    def home(self):
        self.main.layouts.setCurrentWidget(self.main.home)
    def archive(self):
        self.main.layouts.setCurrentWidget(self.main.archive)
        wb = xlrd.open_workbook("arch.xlsx")
        sheet = wb.sheet_by_index(0)
        print(sheet.cell_value(0, 0))
        ss = []
        s = []
        for i in range(sheet.nrows):
            for j in range(9):
                s.append(sheet.cell_value(i, j))
            ss.append(s)
            s = []
        # for i in range(len(test.std)):
        #     x=ss[:].index(std[i][0])
        #     print(x)
        for i in range(sheet.nrows):
            self.main.arc.insertRow(i)
            self.main.arc.setItem(i, 0, QtWidgets.QTableWidgetItem(str(ss[i][0])))
            self.main.arc.setItem(i, 1, QtWidgets.QTableWidgetItem(str(ss[i][1])))
            self.main.arc.setItem(i, 2, QtWidgets.QTableWidgetItem(str(ss[i][2])))
            self.main.arc.setItem(i, 3, QtWidgets.QTableWidgetItem(str(ss[i][3])))
            self.main.arc.setItem(i, 4, QtWidgets.QTableWidgetItem(str(ss[i][4])))
            self.main.arc.setItem(i, 5, QtWidgets.QTableWidgetItem(str(ss[i][5])))
            self.main.arc.setItem(i, 6, QtWidgets.QTableWidgetItem(str(ss[i][6])))
            self.main.arc.setItem(i, 7, QtWidgets.QTableWidgetItem(str(ss[i][7])))
            self.main.arc.setItem(i, 8, QtWidgets.QTableWidgetItem(str(ss[i][8])))

    def setting(self):
        self.main.layouts.setCurrentWidget(self.main.setting)
    def restore_or_max_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    def dir1(self):
        res=QFileDialog.getExistingDirectory(self,caption='Select a folder..')
        test.path1=res+"/*.jpg"
        if len(res) > 0:
          self.main.dir_label1.setText("Done...")
    def dir2(self):
        res=QFileDialog.getExistingDirectory(self,caption='Select a folder..')
        # print(res)
        test.pat2=res+"/*.jpg"
        if len(res) > 0:
           self.main.dir_label2.setText("Done...")
    def dir3(self):
        res=QFileDialog.getExistingDirectory(self,caption='Select a folder..')
        # print(res)
        test.pat3=res+"/*.jpg"
        if len(res) > 0:
           self.main.dir_label3.setText("Done...")
    def dir4(self):
        res=QFileDialog.getExistingDirectory(self,caption='Select a folder..')
        # print(res)
        test.pat4=res+"/*.jpg"
        if len(res) > 0:
           self.main.dir_label4.setText("Done...")
    def correct(self):
        # if test.select_ladder1:
            # test.correct(test.ladder1)
        self.check_input()
        if self.check :
            self.correct_win = QtWidgets.QMainWindow()
            self.ui_correct = Ui_Correction()
            self.ui_correct.setupUi(self.correct_win)
            self.ui_correct.final_correct_btn.clicked.connect(self.final_correct)

            self.ui_correct.complete_btn.clicked.connect(self.complete)
            self.ui_correct.practical_mark_btn.clicked.connect(self.practical)
            self.ui_correct.analysis.clicked.connect(self.analysis)
            self.ui_correct.correct_progressBar.setValue(0)
            self.correct_win.show()
    def print(self):
        self.print_win = QtWidgets.QMainWindow()
        self.ui_print = Ui_print()
        self.ui_print.setupUi(self.print_win)
        self.ui_print.image.setStyleSheet("background-image : url(tem/temp.jpg);")
        self.print_win.show()
    def ladder1(self):
        self.check_input()
        if self.check:
            self.model_num = "1"

            fname,_ = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.jpg )")

            if len(fname) > 0:
                image=cv2.imread(fname)
                image2 = cv2.resize(image, (620,720))
                cv2.imwrite("temp.jpg",image2)
                self.insert_l = QtWidgets.QMainWindow()
                self.ui_insert_ladder = Ui_insert_lader()
                self.ui_insert_ladder.setupUi(self.insert_l)
                self.ui_insert_ladder.save_ladder_btn.clicked.connect(self.save_ladder_paper)
                self.ui_insert_ladder.cancel_ladder_btn.clicked.connect(self.cancel_ladder_paper)
                self.ui_insert_ladder.ladder_img.setStyleSheet("background-image : url(temp.jpg);")

                ret,aa= test.img_processing2(image,150)
                cv2.imshow("img processing",aa)
                cv2.waitKey()
                f1,aaa=test.crop(aa,image2)
                cv2.imshow("croped Img",f1)
                cv2.waitKey()
                test.ladder1 = test.get_q(f1)
                test.select_ladder1 = True

                if len(test.ladder1)== int(test.num_q):

                    for i in range(int(test.num_q)):
                        test.ladder1_mark.append(str(float(test.mark) / float(test.num_q)))
                        self.ui_insert_ladder.answers.insertRow(i)
                        self.ui_insert_ladder.answers.setItem(i, 0, QtWidgets.QTableWidgetItem(str(test.ladder1[i])))
                    self.insert_l.show()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)

                    msg.setText("error at Num quistions")
                    msg.setInformativeText("for more information")
                    msg.setWindowTitle("Details Missing")
                    msg.setDetailedText("The details are as follows:\n" + "Num Quistions you Entered :" + test.num_q + "\n Num Quistions in Ladder :" + str(len(test.ladder1)))
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    retval = msg.exec_()
                    self.main.corr_ladder1.setText("Not Selected..!")


    def ladder2(self):
        self.check_input()
        if self.check:
            self.model_num = "2"

            fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg )")

            if len(fname) > 0:
                image = cv2.imread(fname)
                image2 = cv2.resize(image, (620, 720))
                cv2.imwrite("temp.jpg", image2)
                self.insert_l = QtWidgets.QMainWindow()
                self.ui_insert_ladder = Ui_insert_lader()
                self.ui_insert_ladder.setupUi(self.insert_l)
                self.ui_insert_ladder.save_ladder_btn.clicked.connect(self.save_ladder_paper)
                self.ui_insert_ladder.cancel_ladder_btn.clicked.connect(self.cancel_ladder_paper)
                self.ui_insert_ladder.ladder_img.setStyleSheet("background-image : url(temp.jpg);")

                ret, aa = test.img_processing(image)
                test.ladder2 = test.get_q(aa)
                test.select_ladder2 = True

                if len(test.ladder2) == int(test.num_q):

                    for i in range(int(test.num_q)):
                        test.ladder2_mark.append(str(float(test.mark) / float(test.num_q)))
                        self.ui_insert_ladder.answers.insertRow(i)
                        self.ui_insert_ladder.answers.setItem(i, 0, QtWidgets.QTableWidgetItem(str(test.ladder2[i])))
                    self.insert_l.show()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)

                    msg.setText("error at Num quistions")
                    msg.setInformativeText("for more information")
                    msg.setWindowTitle("Details Missing")
                    msg.setDetailedText(
                        "The details are as follows:\n" + "Num Quistions you Entered :" + test.num_q + "\n Num Quistions in Ladder :" + str(
                            len(test.ladder2)))
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    retval = msg.exec_()
                    self.main.corr_ladder2.setText("Not Selected..!")
    def ladder3(self):
        self.check_input()
        if self.check:
            self.model_num = "3"

            fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg )")

            if len(fname) > 0:
                image = cv2.imread(fname)
                image2 = cv2.resize(image, (620, 720))
                cv2.imwrite("temp.jpg", image2)
                self.insert_l = QtWidgets.QMainWindow()
                self.ui_insert_ladder = Ui_insert_lader()
                self.ui_insert_ladder.setupUi(self.insert_l)
                self.ui_insert_ladder.save_ladder_btn.clicked.connect(self.save_ladder_paper)
                self.ui_insert_ladder.cancel_ladder_btn.clicked.connect(self.cancel_ladder_paper)
                self.ui_insert_ladder.ladder_img.setStyleSheet("background-image : url(temp.jpg);")

                ret, aa = test.img_processing(image)
                test.ladder3 = test.get_q(aa)
                test.select_ladder3 = True

                if len(test.ladder3) == int(test.num_q):

                    for i in range(int(test.num_q)):
                        test.ladder3_mark.append(str(float(test.mark) / float(test.num_q)))
                        self.ui_insert_ladder.answers.insertRow(i)
                        self.ui_insert_ladder.answers.setItem(i, 0, QtWidgets.QTableWidgetItem(str(test.ladder3[i])))
                    self.insert_l.show()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)

                    msg.setText("error at Num quistions")
                    msg.setInformativeText("for more information")
                    msg.setWindowTitle("Details Missing")
                    msg.setDetailedText(
                        "The details are as follows:\n" + "Num Quistions you Entered :" + test.num_q + "\n Num Quistions in Ladder :" + str(
                            len(test.ladder3)))
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    retval = msg.exec_()
                    self.main.corr_ladder3.setText("Not Selected..!")

    def ladder4(self):
        self.check_input()
        if self.check:
            self.model_num = "4"

            fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg )")

            if len(fname) > 0:
                image = cv2.imread(fname)
                image2 = cv2.resize(image, (620, 720))
                cv2.imwrite("temp.jpg", image2)
                self.insert_l = QtWidgets.QMainWindow()
                self.ui_insert_ladder = Ui_insert_lader()
                self.ui_insert_ladder.setupUi(self.insert_l)
                self.ui_insert_ladder.save_ladder_btn.clicked.connect(self.save_ladder_paper)
                self.ui_insert_ladder.cancel_ladder_btn.clicked.connect(self.cancel_ladder_paper)
                self.ui_insert_ladder.ladder_img.setStyleSheet("background-image : url(temp.jpg);")

                ret, aa = test.img_processing(image)
                test.ladder4 = test.get_q(aa)
                test.select_ladder4 = True

                if len(test.ladder2) == int(test.num_q):

                    for i in range(int(test.num_q)):
                        test.ladder4_mark.append(str(float(test.mark) / float(test.num_q)))
                        self.ui_insert_ladder.answers.insertRow(i)
                        self.ui_insert_ladder.answers.setItem(i, 0, QtWidgets.QTableWidgetItem(str(test.ladder4[i])))
                    self.insert_l.show()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)

                    msg.setText("error at Num quistions")
                    msg.setInformativeText("for more information")
                    msg.setWindowTitle("Details Missing")
                    msg.setDetailedText(
                        "The details are as follows:\n" + "Num Quistions you Entered :" + test.num_q + "\n Num Quistions in Ladder :" + str(
                            len(test.ladder4)))
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    retval = msg.exec_()
                    self.main.corr_ladder4.setText("Not Selected..!")
    def save_ladder_paper(self):

        if self.model_num == "1":
            self.insert_l.close()
            self.main.corr_ladder1.setText("Done..")
        elif self.model_num == "2":
            self.insert_l.close()
            self.main.corr_ladder2.setText("Done..")
        elif self.model_num == "3":
            self.insert_l.close()
            self.main.corr_ladder3.setText("Done..")
        elif self.model_num == "4":
            self.insert_l.close()
            self.main.corr_ladder3.setText("Done..")
    def cancel_ladder_paper(self):
        if self.model_num == "1":
            self.insert_l.close()
            self.main.corr_ladder1.setText("Not Selected..")
        elif self.model_num == "2":
            self.insert_l.close()
            self.main.corr_ladder2.setText("Not Selected..")
        elif self.model_num == "3":
            self.insert_l.close()
            self.main.corr_ladder3.setText("Not Selected..")
        elif self.model_num == "4":
            self.insert_l.close()
            self.main.corr_ladder3.setText("Not Selected..")
    def validate_sub(self):
        test.supject_name=self.main.subject_name.text()
        self.check = True
    def validate_std(self):
        validation_rule=QDoubleValidator(1,10000,0)
        if validation_rule.validate(self.main.num_students.text(),14)[0] == QValidator.State.Acceptable:
            self.main.num_students.hasAcceptableInput()
        else:
            self.main.num_students.setText('')
        test.num_std = self.main.num_students.text()
        self.check = True
    def validate_q(self):
        validation_rule=QDoubleValidator(1,200,0)
        if validation_rule.validate(self.main.total_mark_2.text(),14)[0] == QValidator.State.Acceptable:
            self.main.total_mark_2.hasAcceptableInput()
        else:
            self.main.total_mark_2.setText('')
        test.num_q = self.main.total_mark_2.text()
        self.check = True
    def validate_mark(self):
        validation_rule=QDoubleValidator(1,200,0)
        if validation_rule.validate(self.main.total_mark.text(),14)[0] == QValidator.State.Acceptable:
            self.main.total_mark.hasAcceptableInput()
        else:
            self.main.total_mark.setText('')
        test.mark= self.main.total_mark.text()
        self.check = True
    def validate_ldr(self):
        validation_rule=QDoubleValidator(1,4,0)
        # print(validation_rule.validate(self.main.num_students.text(),14))
        if validation_rule.validate(self.main.num_ladders.text(),14)[0] == QValidator.State.Acceptable:
            self.main.num_ladders.hasAcceptableInput()
        else:
            self.main.num_ladders.setText('')
        self.check = True
        test.laders= self.main.num_ladders.text()
        self.main.model1.setEnabled(False)
        self.main.model2.setEnabled(False)
        self.main.model3.setEnabled(False)
        self.main.model4.setEnabled(False)
        if self.main.num_ladders.text()== '1':
            self.main.model1.setEnabled(True)
        elif self.main.num_ladders.text()== '2':
             self.main.model1.setEnabled(True)
             self.main.model2.setEnabled(True)
        elif self.main.num_ladders.text() == '3':
             self.main.model1.setEnabled(True)
             self.main.model2.setEnabled(True)
             self.main.model3.setEnabled(True)
        elif self.main.num_ladders.text() == '4':
             self.main.model1.setEnabled(True)
             self.main.model2.setEnabled(True)
             self.main.model3.setEnabled(True)
             self.main.model4.setEnabled(True)


    def ladder_mark1(self):

        self.check_input()
        if self.check and len(test.ladder1_mark)>0:
            self.mark_1=QtWidgets.QMainWindow()
            self.ui_1 =Ui_ladder_m()

            self.ui_1.setupUi(self.mark_1)
            # row=0
            # self.ui.marks.setRowCount(25)
            for i in range (int(test.num_q)):
                self.ui_1.marks.insertRow(i)
                self.ui_1.marks.setItem(i,0,QtWidgets.QTableWidgetItem(str(test.ladder1_mark[i])))
            self.model_num="1"
            self.ui_1.ladder_ok.clicked.connect(self.test)
            self.ui_1.ladder_cancel.clicked.connect(self.cancel)
            self.mark_1.show()
    def ladder_mark2(self):

        self.check_input()
        if self.check and len(test.ladder2_mark)>0:
            self.mark_2=QtWidgets.QMainWindow()
            self.ui_2 =Ui_ladder_m()
            self.ui_2.setupUi(self.mark_2)
            # row=0
            # self.ui.marks.setRowCount(25)
            for i in range (int(test.num_q)):
                self.ui_2.marks.insertRow(i)
                self.ui_2.marks.setItem(i,0,QtWidgets.QTableWidgetItem(str(test.ladder2_mark[i])))
            self.model_num = "2"
            self.ui_2.ladder_ok.clicked.connect(self.test)
            self.ui_2.ladder_cancel.clicked.connect(self.cancel)
            self.mark_2.show()
    def ladder_mark3(self):

        self.check_input()
        if self.check and len(test.ladder2_mark)>0:
            self.mark_3=QtWidgets.QMainWindow()
            self.ui_3 =Ui_ladder_m()
            self.ui_3.setupUi(self.mark_3)
            # row=0
            # self.ui.marks.setRowCount(25)
            for i in range (int(test.num_q)):
                self.ui_3.marks.insertRow(i)
                self.ui_3.marks.setItem(i,0,QtWidgets.QTableWidgetItem(str(test.ladder3_mark[i])))
            self.model_num = "3"
            self.ui_3.ladder_ok.clicked.connect(self.test)
            self.ui_3.ladder_cancel.clicked.connect(self.cancel)
            self.mark_3.show()
    def ladder_mark4(self):
        self.check_input()
        if self.check and len(test.ladder2_mark)>0:
            self.mark_4 = QtWidgets.QMainWindow()
            self.ui_4 = Ui_ladder_m()
            self.ui_4.setupUi(self.mark_4)
            # row=
            # self.ui.marks.setRowCount(25)
            for i in range(int(test.num_q)):
                self.ui_4.marks.insertRow(i)
                self.ui_4.marks.setItem(i, 0, QtWidgets.QTableWidgetItem(str(test.ladder4_mark[i])))
            self.model_num = "4"
            self.ui_4.ladder_ok.clicked.connect(self.test)
            self.ui_4.ladder_cancel.clicked.connect(self.cancel)
            self.mark_4.show()
    def insert_ladder1(self):
        self.check_input()
        if self.check:
            self.ladder_1 = QtWidgets.QMainWindow()
            self.ui_1 = Ui_insert_ladder()

            self.ui_1.setupUi(self.ladder_1)

            # row=0
            # self.ui.marks.setRowCount(25)
            for i in range(int(test.num_q)):
                self.ui_1.marks.insertRow(i)
                self.ui_1.marks.setItem(i, 1, QtWidgets.QTableWidgetItem(str(float(test.mark) / float(test.num_q))))
                if len(test.ladder1)>0:
                    self.ui_1.marks.setItem(i, 0, QtWidgets.QTableWidgetItem(test.ladder1[i].upper()))
            self.in_model_num = "1"
            self.ui_1.ladder_ok.clicked.connect(self.save_ladder)
            self.ui_1.ladder_cancel.clicked.connect(self.cancel2)
            self.ladder_1.show()
    def insert_ladder2(self):
        self.check_input()
        if self.check:
            self.ladder_2 = QtWidgets.QMainWindow()
            self.ui_2 = Ui_insert_ladder()

            self.ui_2.setupUi(self.ladder_2)

            # row=0
            # self.ui.marks.setRowCount(25)
            for i in range(int(test.num_q)):
                self.ui_2.marks.insertRow(i)
                self.ui_2.marks.setItem(i, 1, QtWidgets.QTableWidgetItem(str(float(test.mark) / float(test.num_q))))
                if len(test.ladder2) > 0:
                    self.ui_2.marks.setItem(i, 0, QtWidgets.QTableWidgetItem(test.ladder2[i].upper()))
            self.in_model_num = "2"
            self.ui_2.ladder_ok.clicked.connect(self.save_ladder)
            self.ui_2.ladder_cancel.clicked.connect(self.cancel2)
            self.ladder_2.show()
    def insert_ladder3(self):
        self.check_input()
        if self.check:
            self.ladder_3 = QtWidgets.QMainWindow()
            self.ui_3 = Ui_insert_ladder()

            self.ui_3.setupUi(self.ladder_3)

            # row=0
            # self.ui.marks.setRowCount(25)
            for i in range(int(test.num_q)):
                self.ui_3.marks.insertRow(i)
                self.ui_3.marks.setItem(i, 1, QtWidgets.QTableWidgetItem(str(float(test.mark) / float(test.num_q))))
                if len(test.ladder3) > 0:
                    self.ui_3.marks.setItem(i, 0, QtWidgets.QTableWidgetItem(test.ladder3[i].upper()))
            self.in_model_num = "3"
            self.ui_3.ladder_ok.clicked.connect(self.save_ladder)
            self.ui_3.ladder_cancel.clicked.connect(self.cancel2)
            self.ladder_3.show()
    def insert_ladder4(self):
        self.check_input()
        if self.check:
            self.ladder_4= QtWidgets.QMainWindow()
            self.ui_4 = Ui_insert_ladder()

            self.ui_4.setupUi(self.ladder_4)

            # row=0
            # self.ui.marks.setRowCount(25)
            for i in range(int(test.num_q)):
                self.ui_4.marks.insertRow(i)
                self.ui_4.marks.setItem(i, 1, QtWidgets.QTableWidgetItem(str(float(test.mark) / float(test.num_q))))
                if len(test.ladder4) > 0:
                    self.ui_4.marks.setItem(i, 0, QtWidgets.QTableWidgetItem(test.ladder4[i].upper()))
            self.in_model_num = "4"
            self.ui_4.ladder_ok.clicked.connect(self.save_ladder)
            self.ui_4.ladder_cancel.clicked.connect(self.cancel2)
            self.ladder_4.show()
    def test(self):
        print("aaaaaaaaaa")
        mark=0
        if self.model_num == "1":
            for i in range(int(test.num_q)):
                mark += float(self.ui_1.marks.item(i, 0).text())
        elif self.model_num == "2":
            for i in range(int(test.num_q)):
                mark += float(self.ui_2.marks.item(i, 0).text())
        elif self.model_num == "3":
            for i in range(int(test.num_q)):
                mark += float(self.ui_3.marks.item(i, 0).text())
        elif self.model_num == "4":
            for i in range(int(test.num_q)):
                mark += float(self.ui_4.marks.item(i, 0).text())
        if round(mark)== float(test.mark):
            # print(round(mark))
            # print(float(test.mark))
            if self.model_num=="1":
                for i in range(int(test.num_q)):
                    test.ladder1_mark[i]=self.ui_1.marks.item(i,0).text()
                    print(test.ladder1_mark[i])
                self.mark_1.close()
            elif self.model_num=="2":
                for i in range(int(test.num_q)):
                    test.ladder2_mark[i]=self.ui_2.marks.item(i,0).text()
                self.mark_2.close()
            elif self.model_num=="3":
                for i in range(int(test.num_q)):
                    test.ladder3_mark[i]=self.ui_3.marks.item(i,0).text()
                self.mark_3.close()
            elif self.model_num=="4":
                for i in range(int(test.num_q)):
                    test.ladder4_mark[i]=self.ui_4.marks.item(i,0).text()
                self.mark_4.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("error at gathering mark")
            msg.setInformativeText("for more information")
            msg.setWindowTitle("Details Missing")
            msg.setDetailedText(
                "The details are as follows:\n" + "Supject Mark :" + test.mark + "\n gathering mark :" + str(mark) )
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # msg.buttonClicked.connect(self.msgbtn())

            retval = msg.exec_()
    def save_ladder(self):
        mark = 0
        if self.in_model_num == "1":
            for i in range(int(test.num_q)):
                mark += float(self.ui_1.marks.item(i, 1).text())
        elif self.in_model_num == "2":
            for i in range(int(test.num_q)):
                mark += float(self.ui_2.marks.item(i, 1).text())
        elif self.in_model_num == "3":
            for i in range(int(test.num_q)):
                mark += float(self.ui_3.marks.item(i, 1).text())
        elif self.in_model_num == "4":
            for i in range(int(test.num_q)):
                mark += float(self.ui_4.marks.item(i, 1).text())
        if round(mark) == float(test.mark):
            # print(round(mark))
            # print(float(test.mark))
            if self.in_model_num == "1":
                for i in range(int(test.num_q)):
                    if self.ui_1.marks.item(i, 0) is None :
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("error at answers")
                        msg.setInformativeText("for more information")
                        msg.setWindowTitle("Answers Missing")
                        msg.setDetailedText(
                            "The details are as follows:\n" + "Q :" + str(i+1) + "\n Answer :")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        retval = msg.exec_()
                        return
                    elif self.ui_1.marks.item(i, 0).text().upper() not in {"a","A","b","B","c","C","d","D","e","E"}:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("error at answers")
                        msg.setInformativeText("for more information")
                        msg.setWindowTitle("Answers Missing")
                        msg.setDetailedText(
                            "The details are as follows:\n" + "Q :" + str(i+1) + "\n Answer :" + self.ui_1.marks.item(i,0).text())
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        retval = msg.exec_()
                        return
                for i in range(int(test.num_q)):
                    test.ladder1_mark[i] = self.ui_1.marks.item(i, 1).text()
                    test.ladder1.append(self.ui_1.marks.item(i, 0).text())
                self.ladder_1.close()
            elif self.in_model_num == "2":
                for i in range(int(test.num_q)):
                    if self.ui_2.marks.item(i, 0) is None:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("error at answers")
                        msg.setInformativeText("for more information")
                        msg.setWindowTitle("Answers Missing")
                        msg.setDetailedText(
                            "The details are as follows:\n" + "Q :" + str(i + 1) + "\n Answer :")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        retval = msg.exec_()
                        return
                    elif self.ui_2.marks.item(i, 0).text().upper() not in {"a", "A", "b", "B", "c", "C", "d", "D", "e",
                                                                           "E"}:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("error at answers")
                        msg.setInformativeText("for more information")
                        msg.setWindowTitle("Answers Missing")
                        msg.setDetailedText(
                            "The details are as follows:\n" + "Q :" + str(i + 1) + "\n Answer :" + self.ui_2.marks.item(
                                i, 0).text())
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        retval = msg.exec_()
                        return
                for i in range(int(test.num_q)):
                    test.ladder2_mark[i] = self.ui_2.marks.item(i, 1).text()
                    test.ladder2.append(self.ui_2.marks.item(i, 0).text())

                self.ladder_2.close()
            elif self.in_model_num == "3":
                for i in range(int(test.num_q)):
                    if self.ui_3.marks.item(i, 0) is None:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("error at answers")
                        msg.setInformativeText("for more information")
                        msg.setWindowTitle("Answers Missing")
                        msg.setDetailedText(
                            "The details are as follows:\n" + "Q :" + str(i + 1) + "\n Answer :")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        retval = msg.exec_()
                        return
                    elif self.ui_3.marks.item(i, 0).text().upper() not in {"a", "A", "b", "B", "c", "C", "d", "D", "e",
                                                                           "E"}:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("error at answers")
                        msg.setInformativeText("for more information")
                        msg.setWindowTitle("Answers Missing")
                        msg.setDetailedText(
                            "The details are as follows:\n" + "Q :" + str(i + 1) + "\n Answer :" + self.ui_3.marks.item(
                                i, 0).text())
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        retval = msg.exec_()
                        return
                for i in range(int(test.num_q)):
                    test.ladder3_mark[i] = self.ui_3.marks.item(i, 1).text()
                    test.ladder3.append(self.ui_3.marks.item(i, 0).text())

                self.ladder_3.close()
            elif self.in_model_num == "4":
                for i in range(int(test.num_q)):
                    if self.ui_4.marks.item(i, 0) is None:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("error at answers")
                        msg.setInformativeText("for more information")
                        msg.setWindowTitle("Answers Missing")
                        msg.setDetailedText(
                            "The details are as follows:\n" + "Q :" + str(i + 1) + "\n Answer :")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        retval = msg.exec_()
                        return
                    elif self.ui_4.marks.item(i, 0).text().upper() not in {"a", "A", "b", "B", "c", "C", "d", "D", "e",
                                                                           "E"}:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("error at answers")
                        msg.setInformativeText("for more information")
                        msg.setWindowTitle("Answers Missing")
                        msg.setDetailedText(
                            "The details are as follows:\n" + "Q :" + str(i + 1) + "\n Answer :" + self.ui_4.marks.item(i, 0).text())
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        retval = msg.exec_()
                        return
                for i in range(int(test.num_q)):
                    test.ladder4_mark[i] = self.ui_4.marks.item(i, 1).text()
                    test.ladder4.append(self.ui_4.marks.item(i, 0).text())

                self.ladder_4.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("error at gathering mark")
            msg.setInformativeText("for more information")
            msg.setWindowTitle("Details Missing")
            msg.setDetailedText(
                "The details are as follows:\n" + "Supject Mark :" + test.mark + "\n gathering mark :" + str(mark))
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # msg.buttonClicked.connect(self.msgbtn())

            retval = msg.exec_()
    def cancel(self):
        if self.model_num == "1":
            self.mark_1.close()
        elif self.model_num == "2":
            self.mark_2.close()
        elif self.model_num == "3":
            self.mark_3.close()
        elif self.model_num == "4":
            self.mark_4.close()

    def cancel2(self):
        if self.in_model_num == "1":
            self.ladder_1.close()
        elif self.in_model_num == "2":
            self.ladder_2.close()
        elif self.in_model_num == "3":
            self.ladder_3.close()
        elif self.in_model_num == "4":
            self.ladder_4.close()


    def check_input(self):
        if (test.supject_name == "" or test.num_q == "" or test.mark== "" or test.num_std=="" or test.laders==""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Please fill all Supject Details...!")
            msg.setInformativeText("for more information")
            msg.setWindowTitle("Details Missing")
            msg.setDetailedText("The details are as follows:\n"+"Supject Name :"+test.supject_name+"\n Num OF Student :"+test.num_std+
                                "\n Num OF Qustions :" + test.num_q+"\n Num OF Ladders :"+test.laders+"\n Mark :"+test.mark)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # msg.buttonClicked.connect(self.msgbtn())
            self.check = False

            retval = msg.exec_()

    def final_correct(self):



        if test.select_ladder1:

            images = glob.glob(test.path1)
            j=0
            for image in images:
                print(image)
                img = cv2.imread(image, 1)
                image = img.copy()
                ret, aa = test.img_processing2(image,150)
                # cv2.imshow("aab", a)
                # cv2.imshow("aa", aa)
                f1,org = test.crop(aa,image)
                id = test.get_id(f1)
                print("id :"+str(id))
                if id==0:
                    test.no_ids+=1

                test.answers1 = test.get_q_stu(f1)
                #
                self.sum = 0
                self.q_error=True

                for i in range(int(test.num_q)):
                    self.th=150
                    if (test.ladder1[i] == test.answers1[i]):
                        self.sum += float(test.ladder1_mark[i])
                    # elif ("*" in test.answers1[i]) :
                    #     self.i = i
                    #     while self.q_error:
                    #
                    #       self.fix_error = QtWidgets.QDialog()
                    #       self.ui_fix = Ui_Dialog()
                    #       self.ui_fix.setupUi(self.fix_error)
                    #       self.fix_error.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                    #       self.ui_fix.ignor_btn.clicked.connect(self.ignor)
                    #       self.fix_error.setStyleSheet("QDialog{border:1px solid black;background-color:rgb(255,255,255)};")
                    #       self.ui_fix.horizontalSlider.valueChanged.connect(self.change_th)
                    #       self.ui_fix.complete_btn.clicked.connect(self.complete)
                    #
                    #       q, org_q = test.split_Q(f1, i, org)
                    #       org_q1 = cv2.resize(org_q, (475, 70))
                    #       q = test.Q_processing(org_q1, self.th)
                    #       q1 = test.Q_processing(org_q, self.th)
                    #
                    #       self.corrected_ans=test.get_one_q_answer(q1)
                    #       print(self.corrected_ans)
                    #       cv2.imwrite("org1.jpg", org_q1)
                    #       cv2.imwrite("error2.jpg", q)
                    #       self.ui_fix.id_txt.setText(str(id))
                    #       self.ui_fix.qnum.setText(str(i + 1))
                    #       self.ui_fix.error1.setStyleSheet("background-image : url(org1.jpg);")
                    #       self.ui_fix.error2.setStyleSheet("background-image : url(error2.jpg);")
                    #
                    #       self.fix_error.exec()
                    #

                                ## DROP SHADOW EFFECT


                            #
                            #
                            #
                            #
                            #
                            # cv2.imwrite("error2.jpg",q)
                            #


                test.std.append([id,self.sum])
                self.ui_correct.marks.insertRow(j)
                self.ui_correct.marks.setItem(j, 0, QtWidgets.QTableWidgetItem(str(id)))
                self.ui_correct.marks.setItem(j, 5, QtWidgets.QTableWidgetItem(str(round(self.sum))))
                j += 1
                self.ui_correct.correct_progressBar.setValue(int((j*100)/int(test.num_std)))
            if test.no_ids > 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)

                msg.setText("Exciptions..")
                msg.setInformativeText("for more information")
                msg.setWindowTitle("Details Missing")
                msg.setDetailedText(
                    "The details are as follows:\n" + "You Have  :" + str(test.no_ids) + "\n Papers without ID numper")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                # msg.buttonClicked.connect(self.msgbtn())

                retval = msg.exec_()

        if test.select_ladder2:
            std=test.correct(test.ladder2,test.ladder2_mark,test.path2)
            for i in range (len(std)):
                self.ui_correct.marks.insertRow(i)
                self.ui_correct.marks.setItem(i, 0, QtWidgets.QTableWidgetItem(str(std[i][0])))
                self.ui_correct.marks.setItem(i, 5, QtWidgets.QTableWidgetItem(str(round(std[i][1]))))
        if test.select_ladder3:
            std=test.correct(test.ladder3,test.ladder3_mark,test.path3)
            for i in range (len(std)):
                self.ui_correct.marks.insertRow(i)
                self.ui_correct.marks.setItem(i, 0, QtWidgets.QTableWidgetItem(str(std[i][0])))
                self.ui_correct.marks.setItem(i, 5, QtWidgets.QTableWidgetItem(str(round(std[i][1]))))
        if test.select_ladder4:
            std=test.correct(test.ladder4,test.ladder4_mark,test.path4)
            for i in range (len(std)):
                self.ui_correct.marks.insertRow(i)
                self.ui_correct.marks.setItem(i, 0, QtWidgets.QTableWidgetItem(str(std[i][0])))
                self.ui_correct.marks.setItem(i, 5, QtWidgets.QTableWidgetItem(str(round(std[i][1]))))


    def q_test(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))

        self.fix_error = QtWidgets.QDialog()
        self.ui_fix = Ui_Dialog()
        self.ui_fix.setupUi(self.fix_error)

        # self.fix_error.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.ui_fix.ignor_btn.clicked.connect(self.ignor)
        # self.fix_error.setGraphicsEffect(self.shadow)
        self.fix_error.resize(500,500)
        self.fix_error.exec()

    def ignor(self):
        self.q_error=False

        self.fix_error.close()
    # def change_th1(self):

    def change_th(self):
        self.th = self.ui_fix.horizontalSlider.value()
        self.ui_fix.complete_btn.setEnabled(True)
        #
        org1 = cv2.imread("org1.jpg")
        q = test.Q_processing(org1, self.th)
        cv2.imwrite("error2.jpg", q)
        self.ui_fix.error2.setStyleSheet("background-image : url(error2.jpg);")
    def complete(self):
        if  "*" not in self.corrected_ans:
            if test.ladder1[self.i]==self.corrected_ans:
                test.answers1[self.i]=self.corrected_ans
                self.sum+=float(test.ladder1_mark[self.i])
                self.q_error=False
                self.fix_error.close()
            else:
                self.q_error = False
                test.answers1[self.i] = self.corrected_ans
                self.fix_error.close()
    def analysis(self):
        self.ui_correct.tabWidget.setEnabled(True)
        self.ui_correct.avg_txt.setText("  40  ")
        self.ui_correct.sdev_txt.setText("  60.26  ")
        self.ui_correct.rate_txt_.setText("  30  ")
        self.ui_correct.max_txt.setText("  56  ")


    def practical(self):
        std=[]
        self.ui_correct.analysis.setEnabled(True)
        path, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Excil File (*.xlsx )")
        print(path)

        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_index(0)
        print(sheet.cell_value(0, 0))
        ss=[]
        s=[]
        for i in range(sheet.nrows):
             for j in range(7):
                 s.append(sheet.cell_value(i, j))
             ss.append(s)
             s=[]
        # for i in range(len(test.std)):
        #     x=ss[:].index(std[i][0])
        #     print(x)
        for i in range(1, sheet.nrows):
            self.ui_correct.marks.insertRow(i-1)
            self.ui_correct.marks.setItem(i-1, 0, QtWidgets.QTableWidgetItem(str(ss[i][0])))
            self.ui_correct.marks.setItem(i-1, 1, QtWidgets.QTableWidgetItem(str(ss[i][1])))
            self.ui_correct.marks.setItem(i-1, 2, QtWidgets.QTableWidgetItem(str(ss[i][2])))
            self.ui_correct.marks.setItem(i-1, 3, QtWidgets.QTableWidgetItem(str(ss[i][3])))
            self.ui_correct.marks.setItem(i-1, 4, QtWidgets.QTableWidgetItem(str(ss[i][4])))
            self.ui_correct.marks.setItem(i-1, 5, QtWidgets.QTableWidgetItem(str(ss[i][5])))
            self.ui_correct.marks.setItem(i-1, 6, QtWidgets.QTableWidgetItem(str(ss[i][6])))


        # self.n=False
        # while not self.n:

    def msgbtn(self):
        if self.zz==2:
            self.n=True
        self.zz+=1

class First_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.StartScreen.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(20)
        # CHANGE DESCRIPTION
        # Initial Text
        self.ui.label.setText("LOADING")
        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("LOADING DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label.setText("LOADING..."))
        QtCore.QTimer.singleShot(6000, lambda: self.ui.label.setText("LOADING.."))
        QtCore.QTimer.singleShot(7000, lambda: self.ui.label.setText("LOADING..."))
        QtCore.QTimer.singleShot(8000, lambda: self.ui.label.setText("LOADING."))
        QtCore.QTimer.singleShot(9000, lambda: self.ui.label.setText("LOADING.."))
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################


    def progress(self):
        global counter
        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)
        # CLOSE SPLASH SCREE AND OPEN APP
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()
            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()
            # CLOSE SPLASH SCREEN
            self.close()
        # INCREASE COUNTER
        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = First_Window()
    sys.exit(app.exec_())
