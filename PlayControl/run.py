import sys
from PlayControlAction import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    action = PlayControlAction()
    sys.exit(app.exec_())