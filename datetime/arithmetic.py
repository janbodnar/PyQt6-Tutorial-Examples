#!/usr/bin/python

from PyQt6.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print(f'Today: {now.toString(Qt.DateFormat.ISODate)}')
print(f'Adding 12 days: {now.addDays(12).toString(Qt.DateFormat.ISODate)}')
print(f'Subtracting 22 days: {now.addDays(-22).toString(Qt.DateFormat.ISODate)}')

print(f'Adding 50 seconds: {now.addSecs(50).toString(Qt.DateFormat.ISODate)}')
print(f'Adding 3 months: {now.addMonths(3).toString(Qt.DateFormat.ISODate)}')
print(f'Adding 12 years: {now.addYears(12).toString(Qt.DateFormat.ISODate)}')
