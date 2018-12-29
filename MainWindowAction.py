from PyQt5.QtWidgets import *
from MainWindow import *
from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QUrl, Qt
from PyQt5.QtGui import QColor, QPixmap, QIcon, QPalette
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from Player import Player
import time

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

class MainWindowAction(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowAction, self).__init__(parent)

        self.player = QMediaPlayer()

        self.setupUi(self)
        self.init()
        self.show()


    def init(self):
        self.setWindowFlags(Qt.FramelessWindowHint)

        exit_normal_icon_path = QUrl.fromLocalFile(EXIT_ICON_PATH)
        self.exit_normal_icon = QIcon(EXIT_ICON_PATH)

        self.exitButton.setStyleSheet(EXIT_BUTTON_STYLE)

        self.exitButton.clicked.connect(self.close)
        self.minButton.clicked.connect(self.showMinimized)