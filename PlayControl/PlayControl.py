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
        self.playControlPanel = QtWidgets.QFrame(self.centralwidget)
        self.playControlPanel.setGeometry(QtCore.QRect(10, 680, 1011, 89))
        self.playControlPanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playControlPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playControlPanel.setObjectName("playControlPanel")
        self.gridLayout = QtWidgets.QGridLayout(self.playControlPanel)
        self.gridLayout.setObjectName("gridLayout")
        self.timeLabel = QtWidgets.QLabel(self.playControlPanel)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout.addWidget(self.timeLabel, 0, 3, 1, 1)
        self.nextSongButton = QtWidgets.QPushButton(self.playControlPanel)
        self.nextSongButton.setObjectName("nextSongButton")
        self.gridLayout.addWidget(self.nextSongButton, 1, 2, 1, 1)
        self.playPosSlider = QtWidgets.QSlider(self.playControlPanel)
        self.playPosSlider.setOrientation(QtCore.Qt.Horizontal)
        self.playPosSlider.setObjectName("playPosSlider")
        self.gridLayout.addWidget(self.playPosSlider, 1, 3, 1, 1)
        self.prevSongButton = QtWidgets.QPushButton(self.playControlPanel)
        self.prevSongButton.setObjectName("prevSongButton")
        self.gridLayout.addWidget(self.prevSongButton, 1, 0, 1, 1)
        self.playModeChangeButton = QtWidgets.QPushButton(self.playControlPanel)
        self.playModeChangeButton.setObjectName("playModeChangeButton")
        self.gridLayout.addWidget(self.playModeChangeButton, 1, 4, 1, 1)
        self.playCtrlButton = QtWidgets.QPushButton(self.playControlPanel)
        self.playCtrlButton.setObjectName("playCtrlButton")
        self.gridLayout.addWidget(self.playCtrlButton, 1, 1, 1, 1)
        self.songInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.songInfoLabel.setGeometry(QtCore.QRect(590, 60, 421, 20))
        self.songInfoLabel.setObjectName("songInfoLabel")
        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(980, 10, 61, 34))
        self.openFileButton.setObjectName("openFileButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 170, 81, 18))
        self.label.setObjectName("label")
        self.playModePanel = QtWidgets.QFrame(self.centralwidget)
        self.playModePanel.setGeometry(QtCore.QRect(900, 560, 111, 148))
        self.playModePanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playModePanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playModePanel.setObjectName("playModePanel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.playModePanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.seqPlay = QtWidgets.QPushButton(self.playModePanel)
        self.seqPlay.setObjectName("seqPlay")
        self.verticalLayout.addWidget(self.seqPlay)
        self.itemOncePlay = QtWidgets.QPushButton(self.playModePanel)
        self.itemOncePlay.setObjectName("itemOncePlay")
        self.verticalLayout.addWidget(self.itemOncePlay)
        self.randomPlay = QtWidgets.QPushButton(self.playModePanel)
        self.randomPlay.setObjectName("randomPlay")
        self.verticalLayout.addWidget(self.randomPlay)
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
        self.timeLabel.setText(_translate("MainWindow", "0:0/0:0"))
        self.nextSongButton.setText(_translate("MainWindow", "Next"))
        self.prevSongButton.setText(_translate("MainWindow", "Prev"))
        self.playModeChangeButton.setText(_translate("MainWindow", "Random"))
        self.playCtrlButton.setText(_translate("MainWindow", "Play"))
        self.songInfoLabel.setText(_translate("MainWindow", "No music"))
        self.openFileButton.setText(_translate("MainWindow", "Open"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.seqPlay.setText(_translate("MainWindow", "Seq"))
        self.itemOncePlay.setText(_translate("MainWindow", "Once"))
        self.randomPlay.setText(_translate("MainWindow", "Random"))

