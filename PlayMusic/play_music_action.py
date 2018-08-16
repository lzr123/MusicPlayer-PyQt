from PyQt5 import QtCore, QtWidgets, QtGui
from play_music import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QUrl

class PlayMusicAction(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(PlayMusicAction, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showDialog)
        self.player = QMediaPlayer()
        self.play_list = QMediaPlaylist()
        self.show()


    def showDialog(self):
        filename = QFileDialog.getOpenFileNames(self, 'Open File', './',
                                                filter="(*.mp3);;(*.aac);;(*.flan);;(*.wav)")[0]
        # self.play_list.addMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        # self.play_list.setPlaybackMode(QMediaPlaylist.Loop)
        # self.player.setPlaylist(self.play_list)
        # self.player.play()
        if len(filename) != 0:
            print(filename[0])
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(filename[0])))
            self.player.play()



