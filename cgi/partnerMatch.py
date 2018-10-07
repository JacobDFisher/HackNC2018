#!/usr/bin/env python3
from os import environ
import cgi, cgitb
import EventCalendar, Student, UserInterface
stud = []
stud.append(Student.Student("jacobdf", "noot", "Jacob Fisher", -1, 0, 1, 0))
stud.append(Student.Student("yicheng", "hack", "Yicheng Wang", 1, 1, 1, 1))
stud.append(Student.Student("porter", "OS", "Don Porter", -1, 1, 1, -1))

cal = EventCalendar.EventCalendar()
cal.add_session('jacobdf', 'Comp 530', 'Hill')
cal.add_session('yicheng', 'Comp 533', 'Talley')
cal.add_session('porter', 'Open', 'Open')

varNames = ['unityId', 'password', 'name', 'prob', 'foc', 'soc', 'noise']

def main():
    form = cgi.FieldStorage()
    if 'studNum' not in form:
        studNum = 0
    else:
        studNum = int(form['studNum'].value)
    a = {}
    for cookie in [x.strip() for x in environ.get('HTTP_COOKIE','').split(';')]:
        (key, value) = cookie.split('=')
        if key in {'prob', 'foc', 'soc', 'noise'}:
            a[key] = int(value)
        else:
            a[key] = value
    me = Student.Student(*[a[x] for x in varNames])
    print('<p>You have a {}% compatibility with this student.</p>'.format(me.compare(stud[studNum])))

print("Content-Type: text/html")
print()
print("<!DOCTYPE html>")
print("<html>")
main()
print('</html>')
