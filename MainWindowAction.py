from PyQt5.QtWidgets import *
from MainWindow import *
from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QUrl, Qt
from PyQt5.QtGui import QColor, QPixmap, QIcon, QPalette
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist, QMediaResource
from Player import Player
import time
import json
import os
import cgitb

cgitb.enable(format='text')

MUSIC_PATH = r'.\Music\排骨教主 - 牵丝戏.mp3'

EXIT_ICON_PATH = r'./Resources/Icon/exit_normal_icon.png'

EXIT_BUTTON_STYLE = '''
                        QPushButton{
                                background-image:url(./Resources/Icon/exit_normal_icon.bmp);
                                background-color:rgba(0, 0, 0, 0);
                                border: none;}
                        QPushButton:hover{
                                background-image:url(:/Resources/Icon/exit_normal_icon.bmp)
                                }
                        QPushButton:pressed{
                                background-image:url(:/Resources/Icon/exit_normal_icon.bmp);}
                    '''

CONFIG_PATH = './config/config.json'

class MainWindowAction(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowAction, self).__init__(parent)

        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()

        self.local_music_path = []


        self.setupUi(self)
        self.init()
        self.show()


    def init(self):
        # self.setWindowFlags(Qt.FramelessWindowHint)

        self.loadParams()

        self.playlist.setPlaybackMode(self.playlist.Loop)

        self.player.setPlaylist(self.playlist)
        self.player.play()

        exit_normal_icon_path = QUrl.fromLocalFile(EXIT_ICON_PATH)
        self.exit_normal_icon = QIcon(EXIT_ICON_PATH)

        self.exitButton.setStyleSheet(EXIT_BUTTON_STYLE)

        self.exitButton.clicked.connect(self.close)
        self.minButton.clicked.connect(self.showMinimized)
        # self.playButton.clicked.connect(self.playControl)

        self.nextButton.clicked.connect(self.playlist.next)
        self.prevButton.clicked.connect(self.playlist.previous)
        self.playButton.clicked.connect(self.controlPlay)

        self.player.currentMediaChanged.connect(self.initProgressBar)
        self.player.stateChanged.connect(self.changePlayState)
        self.player.positionChanged.connect(self.changeBar)

        self.playProgressBar.sliderReleased.connect(self.changePlayPosition)

    def loadParams(self):
        with open(CONFIG_PATH, 'r') as file:
            params = json.load(file)

            self.local_music_dirs = params['initParams']['LocalMusicDirs']
            last_playlist = params['lastPlayParams']['Playlist']

            self.initPlayList(last_playlist)

    def initPlayList(self, playlist_name):
        playlist_path = './PlayList/' + playlist_name + '.json'
        with open(playlist_path, 'r', encoding='UTF-8') as file:
            music_list = json.load(file)
            music_path_list = music_list['Songs']

        for music_path in music_path_list:
            path = QUrl.fromLocalFile(music_path)
            music = QMediaContent(path)
            self.playlist.addMedia(music)


    def controlPlay(self):
        if self.player.state() == self.player.PlayingState:
            self.player.pause()
            # self.playButton.setText("Play")
        elif self.player.state() == self.player.PausedState:
            self.player.play()
        elif self.player.state() == self.player.StoppedState:
            if self.player.mediaStatus() in [self.player.LoadingMedia, self.player.LoadedMedia,
                                             self.player.BufferedMedia, self.player.BufferingMedia]:
                self.player.play()

    def changePlayState(self):
        if self.player.state() == self.player.PlayingState:
            self.playButton.setText("Pause")
        else:
            self.playButton.setText("Play")

    def initProgressBar(self):
        print(self.playlist.currentMedia().resources()[0].url().fileName())
        self.playProgressBar.setValue(0)



    def changeBar(self):

        if self.player.state() == self.player.PlayingState:
            duration = self.player.duration()
            if duration > 0:
                value = self.player.position() * 100 // duration
                self.playProgressBar.setValue(value)

    def changePlayPosition(self):
        self.player.pause()

        duration = self.player.duration()
        value = self.playProgressBar.value() * duration // 100

        self.player.setPosition(value)

        self.player.play()