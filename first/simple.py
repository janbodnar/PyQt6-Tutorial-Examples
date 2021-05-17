#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

In this example, we create a simple
window in PyQt6.

Author: Jan Bodnar
Website: zetcode.com
"""


import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 200)
    w.move(300, 300)

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    
