#!/usr/bin/python

from PyQt6.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

unix_time = now.toSecsSinceEpoch() 
print(unix_time)

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(d.toString(Qt.DateFormat.ISODate))
