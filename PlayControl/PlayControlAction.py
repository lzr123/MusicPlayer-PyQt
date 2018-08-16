from PlayControl import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QTimer, QtDebugMsg
from PyQt5.QtWidgets import QFileDialog, QSlider
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import pyqtSlot

class PlayControlAction(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(PlayControlAction, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        self.show()

    def initUi(self):
        self.is_playing = False
        self.song_len_time = '0:0'

        self.player = QMediaPlayer()
        self.play_list = QMediaPlaylist()

        self.timer = QTimer()
        self.timer.setInterval(1000)

        self.playPosSlider.setEnabled(False)

        self.playModePanel.setVisible(False)
        self.playModePanel.setEnabled(False)

        self.openFileButton.clicked.connect(self.openFile)

        self.playCtrlButton.clicked.connect(self.playAndPause)

        self.nextSongButton.clicked.connect(self.nextSong)

        self.prevSongButton.clicked.connect(self.prevSong)

        self.player.durationChanged.connect(self.calcTotalTime)

        self.playPosSlider.sliderMoved.connect(self.dragSlider)

        self.playPosSlider.sliderReleased.connect(self.sliderRelease)

        self.timer.timeout.connect(self.showTime)

        self.playModeChangeButton.clicked.connect(self.showPlayModePanel)

        self.seqPlay.clicked.connect(self.setPlayMode)

        self.itemOncePlay.clicked.connect(self.setPlayMode)

        self.randomPlay.clicked.connect(self.setPlayMode)



    def openFile(self):
        self.filename_list = QFileDialog.getOpenFileNames(self, 'Open File', './',
                               filter='(*.mp3);;(*.aac);;(*.flan);;(*.wav)')[0]

        if len(self.filename_list) != 0:
            self.play_list.clear()
            self.player.stop()

            self.playPosSlider.setEnabled(False)
            self.playPosSlider.setValue(0)

            for file in self.filename_list:
                self.play_list.addMedia(QMediaContent(QUrl.fromLocalFile(file)))

            self.play_list.setCurrentIndex(0)
            self.play_list.setPlaybackMode(QMediaPlaylist.Random)

            self.loadPlayList()
            self.playSong()

    def loadPlayList(self):
        self.player.setPlaylist(self.play_list)

    def playSong(self):
        current_song_name = self.filename_list[self.play_list.currentIndex()]
        current_song_name = current_song_name.split('/')[-1].split('.')[-2]
        self.songInfoLabel.setText(current_song_name)

        self.playPosSlider.setEnabled(True)

        self.player.setMedia(self.play_list.currentMedia())
        self.player.play()

        self.playCtrlButton.setText('Pause')
        self.is_playing = True
        self.timer.start()



    def playAndPause(self):
        if self.is_playing == True:
            self.player.pause()
            self.is_playing = False
            self.playCtrlButton.setText('Play')
            self.timer.stop()
        elif self.is_playing == False:
            self.player.play()
            self.is_playing = True
            self.playCtrlButton.setText('Pause')
            self.timer.start()

    def nextSong(self):
        self.play_list.next()
        self.playSong()
        # song_count = self.play_list.mediaCount()
        # current_song_index = self.play_list.currentIndex()
        # if current_song_index + 1 < song_count:
        #     self.play_list.setCurrentIndex(current_song_index + 1)
        #     self.playSong()
        # else:
        #     self.play_list.setCurrentIndex(0)
        #     self.playSong()

    def prevSong(self):
        self.play_list.previous()
        self.playSong()
        # song_count = self.play_list.mediaCount()
        # current_song_index = self.play_list.currentIndex()
        # if current_song_index - 1 >= 0:
        #     self.play_list.setCurrentIndex(current_song_index - 1)
        #     self.playSong()
        # else:
        #     self.play_list.setCurrentIndex(song_count - 1)
        #     self.playSong()

    def showTime(self):
        if (self.player.mediaStatus() != self.player.NoMedia) and (self.song_len_time != '0:0'):
            current_time = self.player.position()
            current_time = f'{(current_time//1000) // 60}:{(current_time//1000)%60}/{self.song_len_time}'
            self.timeLabel.setText(current_time)

            self.playPosSlider.setValue(self.player.position() * 1000 // self.player.duration())

    def calcTotalTime(self):
        if self.player.mediaStatus() != self.player.NoMedia:
            song_len = self.player.duration()
            self.song_len_time = f'{(song_len//1000)//60}:{(song_len//1000)%60}'
            self.playPosSlider.setEnabled(True)

            self.playPosSlider.setRange(0, 1000)

    def changeSlider(self):
        self.playPosSlider.setTickPosition(self.player.position()*1000//self.player.duration())

    def dragSlider(self):
        self.timer.stop()


    def sliderRelease(self):
        self.player.pause()
        self.player.setPosition(self.playPosSlider.value() * self.player.duration() // 1000)
        self.player.play()
        self.timer.start()
        self.is_playing = True
        self.playCtrlButton.setText('Pause')

    def showPlayModePanel(self):

        self.playModePanel.setEnabled(True)
        self.playModePanel.setVisible(True)

    def setPlayMode(self):
        sender = self.sender()

        if sender.text() == 'Seq':
            self.play_list.setPlaybackMode(self.play_list.Loop)
            self.playModeChangeButton.setText('Seq')
        elif sender.text() == 'Once':
            self.play_list.setPlaybackMode(self.play_list.CurrentItemInLoop)
            self.playModeChangeButton.setText('Once')
        elif sender.text() == 'Random':
            self.play_list.setPlaybackMode(self.play_list.Random)
            self.playModeChangeButton.setText('Random')

        self.playModePanel.setVisible(False)
        self.playModePanel.setEnabled(False)