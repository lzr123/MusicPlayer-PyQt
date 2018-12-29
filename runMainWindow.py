import sys
from MainWindowAction import *
from MainWindowAction import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    action = MainWindowAction()
    sys.exit(app.exec_())