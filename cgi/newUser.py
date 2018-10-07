#!/usr/bin/env python3
import cgi, cgitb
import EventCalendar, Student, UserInterface

varNames = ['University', 'FirstName', 'LastName', '.edu Address', 'Password', 'ProblemSolver', 'Focus', 'Social', 'Noise']

def main():
    form = cgi.FieldStorage()
    for x in varNames:
        if x not in form:
            print('Content-Type: text/html')
            print()
            print('You missed a setting: {}'.format(x))
            return
    if '@' not in form['.edu Address'].value or '.edu' != form['.edu Address'].value[-4:]:
        print('Content-Type: text/html')
        print()
        print('Invalid email')
        return
    stud = Student.Student(form['.edu Address'].value.split('@')[0], form['Password'].value, form['FirstName'].value+' '+form['LastName'].value, int(form['ProblemSolver'].value), int(form['Focus'].value), int(form['Social'].value), int(form['Noise'].value))
    print('Set-Cookie:unityId = {}'.format(stud.unity_id))
    print('Set-Cookie:password = {}'.format(stud.password))
    print('Set-Cookie:prob = {}'.format(stud.avg_problemSolver))
    print('Set-Cookie:noise = {}'.format(stud.avg_noise))
    print('Set-Cookie:foc = {}'.format(stud.avg_focus))
    print('Set-Cookie:soc = {}'.format(stud.avg_social))
    print('Set-Cookie:name = {}'.format(stud.name))
    print("Content-Type: text/html")
    print()
    print('<!DOCTYPE html>')
    print('<html><head>')
    print('<meta http-equiv="Refresh" content="0; url=/study.html">')
    print('</head></html>')
    return

cgitb.enable(display=0, logdir="/home/jacob/Code/HackNC2018/logs/")

main()
