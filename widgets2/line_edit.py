#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

This example shows text which
is entered in a QLineEdit
in a QLabel widget.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt6.QtWidgets import (QWidget, QLabel,
        QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QLineEdit')
        self.show()


    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    
