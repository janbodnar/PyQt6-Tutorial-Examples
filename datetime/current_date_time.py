#!/usr/bin/python

from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.DateFormat.ISODate))
print(now.toString(Qt.DateFormat.RFC2822Date))

datetime = QDateTime.currentDateTime()

print(datetime.toString())

time = QTime.currentTime()
print(time.toString(Qt.DateFormat.ISODate))
