from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_main import Ui_MainWindow
import sys
from service import SendUrlsThread

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.progressBar.setVisible(False)
        self.progressBar.reset()
        self.progressBar.setValue(0)

        self.logstr = ''

        self.go_pushButton.clicked.connect(self.go_clicked)


    def go_clicked(self):

        self.go_pushButton.setDisabled(True)
        domain = self.domain_lineEdit.text()
        print(domain)
        self.progressBar.setVisible(True)
        sendService = SendUrlsThread(domain)
        sendService.progress_signal.connect(self.change_progressbar_value)
        sendService.start()
        sendService.exec()


    def change_progressbar_value(self,value, num, url):
        # print(value)
        self.progressBar.setValue(value)
        self.show_label.setText(url)
        if value == 100:
            self.go_pushButton.setDisabled(False)
            self.textBrowser.append(url)
        else:
            log = '[{}] {}'.format(num, url)
            self.textBrowser.append(log)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()

    sys.exit(app.exec_())