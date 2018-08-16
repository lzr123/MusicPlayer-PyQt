# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlayControl.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 818)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 640, 1031, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.playCtrlButton = QtWidgets.QPushButton(self.frame)
        self.playCtrlButton.setGeometry(QtCore.QRect(80, 80, 61, 34))
        self.playCtrlButton.setObjectName("playCtrlButton")
        self.nextSongButton = QtWidgets.QPushButton(self.frame)
        self.nextSongButton.setGeometry(QtCore.QRect(150, 80, 61, 34))
        self.nextSongButton.setObjectName("nextSongButton")
        self.prevSongButton = QtWidgets.QPushButton(self.frame)
        self.prevSongButton.setGeometry(QtCore.QRect(10, 80, 61, 34))
        self.prevSongButton.setObjectName("prevSongButton")
        self.timeLabel = QtWidgets.QLabel(self.frame)
        self.timeLabel.setGeometry(QtCore.QRect(240, 47, 151, 31))
        self.timeLabel.setObjectName("timeLabel")
        self.playPosSlider = QtWidgets.QSlider(self.frame)
        self.playPosSlider.setGeometry(QtCore.QRect(240, 90, 551, 22))
        self.playPosSlider.setOrientation(QtCore.Qt.Horizontal)
        self.playPosSlider.setObjectName("playPosSlider")
        self.songInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.songInfoLabel.setGeometry(QtCore.QRect(590, 60, 421, 20))
        self.songInfoLabel.setObjectName("songInfoLabel")
        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(980, 10, 61, 34))
        self.openFileButton.setObjectName("openFileButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 170, 81, 18))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playCtrlButton.setText(_translate("MainWindow", "Play"))
        self.nextSongButton.setText(_translate("MainWindow", "Next"))
        self.prevSongButton.setText(_translate("MainWindow", "Prev"))
        self.timeLabel.setText(_translate("MainWindow", "0:0/0:0"))
        self.songInfoLabel.setText(_translate("MainWindow", "No music"))
        self.openFileButton.setText(_translate("MainWindow", "Open"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

