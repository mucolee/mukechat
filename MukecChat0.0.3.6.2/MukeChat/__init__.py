import sys

from PyQt5.QtWidgets import QApplication
# from MukeChat.mukechat00362 import MainWindow     #打包时
from mukechat00362 import MainWindow

if __name__ == '__main__':
    # read_file()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
