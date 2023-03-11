import sys
from qtpy import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
import webbrowser


class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Web Browser")
        self.resize(1000, 800)

        # Create URL bar
        self.url_bar = QtWidgets.QLineEdit(self)
        self.url_bar.setGeometry(QtCore.QRect(5, 5, 800, 32))
        self.url_bar.returnPressed.connect(self.open_url)

        # Create Go button
        self.go_button = QtWidgets.QPushButton("Go", self)
        self.go_button.setGeometry(QtCore.QRect(810, 5, 70, 32))
        self.go_button.clicked.connect(self.open_url)

        # Create Back button
        self.back_button = QtWidgets.QPushButton("Back", self)
        self.back_button.setGeometry(QtCore.QRect(5, 40, 70, 32))
        self.back_button.clicked.connect(self.back)

        # Create Forward button
        self.forward_button = QtWidgets.QPushButton("Forward", self)
        self.forward_button.setGeometry(QtCore.QRect(80, 40, 70, 32))
        self.forward_button.clicked.connect(self.forward)

        # Create WebEngineView
        self.view = QtWebEngineWidgets.QWebEngineView(self)
        self.view.setGeometry(QtCore.QRect(5, 75, 970, 720))
        self.view.loadFinished.connect(self.update_url_bar)

    def open_url(self):
        # Get URL from URL bar
        url = self.url_bar.text()

        # Load URL in WebEngineView
        self.view.load(QtCore.QUrl(url))

    def back(self):
        self.view.back()

    def forward(self):
        self.view.forward()

    def update_url_bar(self, success):
        if success:
            self.url_bar.setText(self.view.url().toString())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
