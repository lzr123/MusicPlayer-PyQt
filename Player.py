from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import time
from StatusCode import *

MUSIC_PATH = r'H:\Projects\PyCharmProjects\MusicPlayer\Music\排骨教主 - 牵丝戏.mp3'

# PLAYER_STATE_STOP = 0
# PLAYER_STATE_PLAY = 1
# PLAYER_STATE_PAUSE = 2


class Player():
    def __init__(self):
        self.player = QMediaPlayer()
        self.state = PLAYER_STATE_STOP

    def setMedia(self, music):
        self.player.setMedia(music)


    def play(self):
        print(self.player.mediaStatus())
        if self.state == PLAYER_STATE_PAUSE:
            self.state = PLAYER_STATE_PLAY
            self.player.play()
        elif self.state == PLAYER_STATE_STOP:
            if self.player.mediaStatus() == LOADED_MEDIA:
                self.state = PLAYER_STATE_PLAY
                self.state.play()

    def pause(self):
        if self.state == PLAYER_STATE_PLAY:
            self.state = PLAYER_STATE_PAUSE

        self.player.pause()

    def stop(self):
        self.player.state = PLAYER_STATE_STOP


if __name__ == '__main__':
    path = QUrl.fromLocalFile(MUSIC_PATH)
    music = QMediaContent(path)
    player = Player()
    player.setMedia(music)
    player.play()



