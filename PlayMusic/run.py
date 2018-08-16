import sys
from play_music_action import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    action = PlayMusicAction()
    sys.exit(app.exec_())