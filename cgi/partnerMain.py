#!/usr/bin/env python3
from os import environ
import cgi, cgitb
import EventCalendar, Student, UserInterface
stud = []

def main():
    print('<html><body><iframe src="/cgi-bin/partnerMatch.py?studNum=0"></iframe><iframe src="/cgi-bin/partnerMatch.py?studNum=1"></iframe><iframe src="/cgi-bin/partnerMatch.py?studNum=2"></iframe></body></html>')

print("Content-Type: text/html")
print()
print("<!DOCTYPE html>")
print("<html>")
main()
print('</html>')
